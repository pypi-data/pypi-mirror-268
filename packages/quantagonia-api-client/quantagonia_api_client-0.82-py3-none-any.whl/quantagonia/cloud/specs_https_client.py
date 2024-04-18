import json
import os
import urllib
import uuid
import requests
import copy
from typing import Tuple

from requests.packages.urllib3.util import Retry
from requests.adapters import HTTPAdapter

from quantagonia.cloud.dto.encoder import DtoJSONEncoder
from quantagonia.cloud.dto.job import JobDto
from quantagonia.cloud.dto.presigned_s3 import PresignedS3
from quantagonia.cloud.specs_enums import *
from quantagonia.enums import HybridSolverServers
from quantagonia.errors import SolverError


class SpecsHTTPSClient():
    """ client class for qqvm server """
    def __init__(self, api_key: str, target_server: HybridSolverServers = HybridSolverServers.PROD,
        custom_headers = {}) -> None:
        """ """
        self.api_key = api_key
        self.server = target_server.value
        self.custom_headers = custom_headers

        self.retry = Retry(total=5, backoff_factor=1, allowed_methods=frozenset(['GET', 'POST', 'PUT', 'DELETE']))
        self.session = requests.Session()
        self.session.mount('http://', HTTPAdapter(max_retries=self.retry))
        self.session.mount('https://', HTTPAdapter(max_retries=self.retry))

    def _submitJob(self, problem_files: list, specs: list, tag : str = "", context : str = "") -> uuid:

        # build a single JSON array with specs
        spec_arr = {}
        for ix in range(0, len(specs)):
            spec_arr[str(ix)] = specs[ix]

        files = [("files", (os.path.basename(prob), open(prob, "rb"))) for prob in problem_files]

        job = JobDto()
        data = json.dumps(job, cls=DtoJSONEncoder)
        response = self.session.post(self.server + SpecsEndpoints.job,
            data=data,
            headers={"X-api-key": self.api_key, 'Content-type': "application/json",
            **self.custom_headers})
        if not response.ok:
            error_report = response.json()
            raise RuntimeError(error_report)
        jobId = response.json()['jobId']
        problems = []
        spec_files = []
        for ind, prob in enumerate(problem_files):
            try:
                filename = prob.parts[len(prob.parts)-1]
            except AttributeError as e:
                filename = prob.split("/")[len(prob.split("/")) - 1]

            file_key = jobId + "/" + str(ind) + "/" + filename
            problems.append(file_key)
            ps3_problem_file = PresignedS3(jobId=jobId, contentType="application/octet-stream",
                key=file_key)
            data_for_s3 = json.dumps(ps3_problem_file, cls=DtoJSONEncoder)
            response = self.session.post(self.server + SpecsEndpoints.s3, data=data_for_s3,
                headers={"X-api-key": self.api_key, 'Content-type': "application/json",
                **self.custom_headers})
            if not response.ok:
                raise RuntimeError("Unable to get an S3 presigned URL")
            presigned_url = response.json()['url']
            author = response.json()['metaAuthor']
            version = response.json()['metaVersion']

            # uploading files as binaries as they could be zipped
            with open(prob, 'rb') as problem_file:
                problem_bytes = problem_file.read()

            headers = {"X-amz-meta-author": author,
                       "X-amz-meta-version": version,
                       'Content-type': "application/octet-stream"}
            response = self.session.put(presigned_url, data=problem_bytes, headers=headers)
            if not response.ok:
                error_report = response.json()
                raise RuntimeError(error_report)
            spec = spec_arr[str(ind)]
            spec_key = jobId + "/" + str(ind) + "/spec.json"
            spec_files.append(spec_key)
            ps3_specs_file = PresignedS3(jobId=jobId, contentType="text/plain", key=spec_key)
            spec_for_s3 = json.dumps(ps3_specs_file, cls=DtoJSONEncoder)
            response = self.session.post(self.server + SpecsEndpoints.s3, data=spec_for_s3,
                headers={"X-api-key": self.api_key, 'Content-type': "application/json",
                **self.custom_headers})
            spec_str = json.dumps(spec)
            presigned_url = response.json()['url']
            author = response.json()['metaAuthor']
            version = response.json()['metaVersion']
            headers = {"X-amz-meta-author": author,
                        "X-amz-meta-version": version,
                        'Content-type': "text/plain"}
            response = self.session.put(presigned_url, data=spec_str, headers=headers)
            if not response.ok:
                error_report = response.json()
                raise RuntimeError(error_report)

        start_job = JobDto(jobId=jobId, problemFiles=problems, specFiles=spec_files, tag=tag, context=context)
        start_job_data = json.dumps(start_job, cls=DtoJSONEncoder)
        started_job = self.session.post(self.server + SpecsEndpoints.job, data=start_job_data,
            headers={"X-api-key": self.api_key, 'Content-type': "application/json",
            **self.custom_headers})
        if not started_job.ok:
            error_report = started_job.json()
            raise RuntimeError(error_report)
        returned_job_id = started_job.json()['jobId']
        return returned_job_id

    def _replaceFileContentFromUrl(self, e, key):
        e[key] = self._getFileContentFromUrl(e[key])
            
    def _getFileContentFromUrl(self, e):
        if type(e) is dict and "error" in e:
            return "Error: " + e["error"]
        elif type(e) is dict and "url" in e:
            if e["url"] == "":
                return ""
            response = self.session.get(e["url"])
            if response.status_code == 200:
                return response.text
            else:
                return ""
        else:
            return e

    def _checkJob(self, jobid: uuid) -> str:
        params = {'jobid': str(jobid)}
        response = self.session.get(self.server + SpecsEndpoints.checkjob, params=params,
            headers={"X-api-key": self.api_key, **self.custom_headers})
        if response.ok:
            return response.json()['status']
        elif response.status_code > 499:
            log = self._getCurrentLog(jobid)
            error_report = response.json()
            error_report["details"] = log[0]
            raise SolverError(error_report)
        elif response.status_code < 499:
            error_report = response.json()
            raise RuntimeError(error_report)

    def _getCurrentStatus(self, jobid: uuid) -> str:
        params = {'jobid': str(jobid)}
        response = self.session.get(self.server + SpecsEndpoints.getcurstatus, params=params,
            headers={"X-api-key" : self.api_key, **self.custom_headers})

        return json.loads(response.text)

    def _getCurrentSolution(self, jobid: uuid) -> str:
        params = {'jobid': str(jobid)}
        response = self.session.get(self.server + SpecsEndpoints.getcursolution, params=params,
            headers={"X-api-key" : self.api_key, **self.custom_headers})

        array = json.loads(response.text)
        for e in array:
            self._replaceFileContentFromUrl(e, "solution")
        return array

    def _getCurrentLog(self, jobid: uuid) -> str:
        params = {'jobid': str(jobid)}
        response = self.session.get(self.server + SpecsEndpoints.getcurlog, params=params,
            headers={"X-api-key" : self.api_key, **self.custom_headers})
        if not response.ok:
            error_report = response.json()
            raise RuntimeError(error_report)
        return [self._getFileContentFromUrl(e) for e in json.loads(response.text)]

    def _getResults(self, jobid: uuid) -> Tuple[dict, int]:
        params = {'jobid': str(jobid)}
        response = self.session.get(self.server + SpecsEndpoints.getresults, params=params,
            headers={"X-api-key" : self.api_key, **self.custom_headers})

        if not response.ok:
            error_report = response.json()
            raise RuntimeError(error_report)
    
        result = json.loads(response.text)
        array = copy.deepcopy(result["result"])

        for e in array:
            self._replaceFileContentFromUrl(e, "solution_file")
            self._replaceFileContentFromUrl(e, "solver_log")

        return array, int(result["time_billed"])
    
    def _getJobs(self, n : int) -> dict:
        params = {'n': str(n)}
        response = self.session.get(self.server + SpecsEndpoints.getjobs, params=params,
            headers={"X-api-key" : self.api_key, **self.custom_headers})

        if not response.ok:
            error_report = response.json()
            raise RuntimeError(error_report)

        return json.loads(response.text)

    def _interruptJob(self, jobid: uuid):
        response = self.session.delete(self.server + SpecsEndpoints.interruptjob + "/" + str(jobid),
            headers={"X-api-key": self.api_key, **self.custom_headers})
        
        if not response.ok:
            error_report = response.json()
            raise RuntimeError(error_report)

        return True

    ### blocking interface
    def submitJob(self, problem_files: list, specs: list, tag : str = "", context : str = "") -> uuid:
        return self._submitJob(problem_files, specs, tag = tag, context = context)

    def checkJob(self, jobid: uuid) -> str:
        return self._checkJob(jobid)

    def getCurrentStatus(self, jobid: uuid) -> str:
        return self._getCurrentStatus(jobid)

    def getCurrentSolution(self, jobid: uuid) -> str:
        return self._getCurrentSolution(jobid)

    def getCurrentLog(self, jobid: uuid) -> str:
        return self._getCurrentLog(jobid)

    def getResults(self, jobid: uuid) -> Tuple[dict, int]:
        return self._getResults(jobid)
    
    def getJobs(self, n : int) -> dict:
        return self._getJobs(n)

    def interruptJob(self, jobid: uuid) -> dict:
        return self._interruptJob(jobid)

    ### non-blocking interface
    async def submitJobAsync(self, problem_files: list, specs: list, tag : str = "", context : str = "") -> uuid:
        return self._submitJob(problem_files, specs, tag = tag, context = context)

    async def checkJobAsync(self, jobid: uuid) -> str:
        return self._checkJob(jobid)

    async def getCurrentStatusAsync(self, jobid: uuid) -> str:
        return self._getCurrentStatus(jobid)

    async def getCurrentSolutionAsync(self, jobid: uuid) -> str:
        return self._getCurrentSolution(jobid)

    async def getCurrentLogAsync(self, jobid: uuid) -> str:
        return self._getCurrentLog(jobid)

    async def getResultsAsync(self, jobid: uuid) -> Tuple[dict, int]:
        return self._getResults(jobid)
    
    async def getJobsAsync(self) -> dict:
        return self._getJobs()

    async def interruptJobAsync(self, jobid: uuid) -> dict:
        return self._interrupt_job(jobid)
