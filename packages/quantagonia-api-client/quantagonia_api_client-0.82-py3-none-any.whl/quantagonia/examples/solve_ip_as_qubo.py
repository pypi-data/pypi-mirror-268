import os, math

from quantagonia.enums import *
from quantagonia.runner_factory import RunnerFactory
from quantagonia.spec_builder import MIPSpecBuilder

input_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "ip_as_qubo.lp")

api_key = os.environ["QUANTAGONIA_API_KEY"]

runner = RunnerFactory.getRunner(HybridSolverConnectionType.CLOUD,
                                 api_key=api_key,
                                 server = HybridSolverServers.PROD,
                                 suppress_output=False)
spec = MIPSpecBuilder()
spec.set_time_limit(120)
spec.set_option("as_qubo_only", True)

res_dict, _ = runner.solve(input_file_path, spec.getd())

# print some results
print("Runtime:", res_dict["timing"])
print("Objective:", res_dict["objective"])
print("Bound:", res_dict["bound"])
print("Solution:")
for idx, val in res_dict["solution"].items():
    print(f"\t{idx}: {val}")

# in order to use these as test
if math.fabs(res_dict["objective"] - 4.0) > 1e-4:
    raise Exception("Objective value is not correct")
