import pyqubo as pq

from quantagonia.enums import HybridSolverConnectionType
from quantagonia.qubo import *
from quantagonia.runner_factory import RunnerFactory
from quantagonia.spec_builder import QUBOSpecBuilder

API_KEY = os.environ["QUANTAGONIA_API_KEY"]

x0, x1, x2, x3, x4 = pq.Binary("x0"), pq.Binary("x1"), pq.Binary("x2"), pq.Binary("x3"), pq.Binary("x4")
pyqubo_qubo = (2 * x0 + 2 * x2 + 2 * x4 - x0 * x2 - x2 * x0 - x0 * x4 - x4 * x0 - x2 * x4 - x4 * x2 + 3).compile()

# setup model
qubo = QuboModel.fromPyqubo(pyqubo_qubo)

# solve with Quantagonia
runner = RunnerFactory.getRunner(HybridSolverConnectionType.CLOUD, api_key=API_KEY)
specs = QUBOSpecBuilder()
qubo.solve(specs.getd(), runner=runner)

# to be used in tests
if qubo.eval() != 3.0:
  raise Exception("Objective value is not correct")
