from .hybrid_solver_api import QQVM_CMD

from quantagonia.runner import Runner
from quantagonia.runner_factory import HybridSolverConnectionType, RunnerFactory
from quantagonia.enums import HybridSolverServers

class QPuLPAdapter:
  """
  This class provides an adapter for solving MILPs modeled with PuLP.
  """

  @classmethod
  def getSolver(cls,
                connection : HybridSolverConnectionType = HybridSolverConnectionType.CLOUD,
                api_key : str = None,
                server : HybridSolverServers = HybridSolverServers.PROD,
                spec_dict : dict = None,
                keep_files : bool = False):
    """
    Returns a solver object for MILP problem instances created with PuLP.

    The solver solves these MILPs with Quantagonias cloud-based HybridSolver.

    Args:
        connection (optional): Connection type. Defaults to `HybridSolverConnectionType.CLOUD`.
        api_key (optional): The Quantagonia API key used for the connection. Defaults to None.
        server (optional): The server used for the connection. It is recommended to use the default value: `HybridSolverServers.PROD`.
        spec_dict (optional): A solver specifications dictionary. Defaults to None.
        keep_files (optional): Whether to keep the generated input and output files. Defaults to False.

    Returns:
        A solver instance.
    """
    runner : Runner = RunnerFactory.getRunner(connection, api_key, server)
    solver = QQVM_CMD(runner=runner, spec_dict=spec_dict, keepFiles=keep_files)

    return solver
