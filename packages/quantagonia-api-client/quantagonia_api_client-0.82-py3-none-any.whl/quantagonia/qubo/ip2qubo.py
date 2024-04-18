import os, os.path
import pathlib
import pulp
import math
import copy
from enum import Enum
from abc import ABC, abstractmethod
from typing import List, Dict

from quantagonia.qubo import *
from quantagonia.enums import HybridSolverConnectionType, HybridSolverOptSenses


class MIPSourceFormat(Enum):
  """
  List of supported MIP formats.
  """
  MIP_PULP = 0
  MIP_INTERMEDIATE = 1

###
# These class represent an editeable intermediate format for MIPs. In the MIP-to-
# QUBO process, several conversion steps are executed while the problem is still
# a MIP - the QUBO conversion itself is only the last step.
# This class is mostly based on dictionaries and enables fast modifications,
# while making all the conversion steps indepenedent from the MIP data format
# in question (e.g. PuLP, CPLEX, ...).
###
class MIPObjective:

  def __init__(self, coefficients : Dict[str, float] = {}, constant : float = 0):
    self.coefficients = coefficients
    self.constant = constant

  def __str__(self):
    ss = ""
    for c_name, c_val in self.coefficients.items():
      ss += ("+ " if c_val >= 0 else "- ") + str(c_val) + " * " + c_name + " "

    if self.constant != 0:
      ss += ("+ " if self.constant >= 0 else "- ") + str(self.constant)

    return ss

class MIPConstraint:

  def __init__(self, name : str = "", coefficients : Dict[str, float] = {},
    sense = pulp.const.LpConstraintEQ, rhs : float = 0):
    self.name = name
    self.coefficients = coefficients
    self.sense = sense
    self.rhs = rhs

  def __str__(self):
    sense_char = " = "
    if self.sense == pulp.const.LpConstraintLE:
      sense_char = " <= "
    if self.sense == pulp.const.LpConstraintGE:
      sense_char = " >= "

    ss = ""
    for c_name, c_val in self.coefficients.items():
      ss += ("+ " if c_val >= 0 else "- ") + str(c_val) + " * " + c_name + " "

    ss += sense_char + str(self.rhs) + " (" + self.name + ") "

    return ss

class MIPIntermediate:

  def __init__(self, sense = HybridSolverOptSenses.MINIMIZE,
    mip_vars : Dict[str, pulp.LpVariable] = {},
    objective : MIPObjective = MIPObjective(),
    constraints : List[MIPConstraint] = []):

    self.sense = sense
    # current variables
    self.vars = {}
    # original variables from MIP
    self.mip_vars = mip_vars

    self.objective = objective
    self.constraints = constraints

  def __str__(self):
    sense_str = "MAXIMIZE" if self.sense == HybridSolverOptSenses.MAXIMIZE else "MINIMIZE"
    ss = sense_str + "  " + str(self.objective) + "\n"
    ss += "s.t.\n"

    for cons in self.constraints:
      ss += "\t" + str(cons) + "\n"

    ss += "\nVariables:\n"
    for var in self.vars:
      ss += "\t" + var + " (" + str(self.vars[var].lowBound) + ", " + \
        str(self.vars[var].upBound) + ")\n"

    return ss

###
# Finally, this class converts from community MIP formats (PuLP, CPLEX, ...)
# into our intermediate format to decouple the conversion codes from
# other MIP data formats.
###
class ConvPULPMIPToIntermediate:

  def conv(self, lp : pulp.LpProblem,
    sense = HybridSolverOptSenses.MINIMIZE) -> MIPIntermediate:

    mip = MIPIntermediate(
      sense,
      {},
      MIPObjective({}, 0),
      []
    )

    # copy variables
    for var in lp.variables():
      mip.mip_vars[var.name] = copy.deepcopy(var)

    mip.vars = copy.deepcopy(mip.mip_vars)

    # copy objective function
    for var, var_coeff in lp.objective.items():
      mip.objective.coefficients[var.name] = var_coeff

    # copy constraints
    for cons_name, cons in lp.constraints.items():
      coeffs = {}

      for var, var_coeff in cons.items():
        coeffs[var.name] = var_coeff

      mip.constraints.append(MIPConstraint(name=cons_name, coefficients=coeffs,
        sense=cons.sense, rhs=-cons.constant))

    return mip

###
# IP to QUBO conversion passes
###

class ScaleConstraints:

  def __init__(self, scaleEqualityConstraints : bool, scaleObjective : bool):
    self._scaleEqualityConstraints = scaleEqualityConstraints
    self._scaleObjective = scaleObjective

  def _scaleExpr(self, lp_expr, rhs = None):

    if len(lp_expr) == 0:
      return 1

    multiplier = 1
    coeffs = []

    # collect coefficients and RHS
    for lp_var, lp_coeff in lp_expr.items():
      coeffs.append(lp_coeff)
    if rhs is not None:
      coeffs.append(rhs)

    # find required multiplier
    for c in coeffs:
      new_c = multiplier * abs(float(c))

      while(new_c - int(new_c)) != 0:
        new_c *= 10
        multiplier *= 10

    # look for GCD to scale down coefficients
    gcd = math.gcd(*[int(c * multiplier) for c in coeffs])

    # apply coefficients
    for lp_var in lp_expr:
      lp_expr[lp_var] = int(multiplier * lp_expr[lp_var])
      lp_expr[lp_var] //= gcd

    if rhs is None:
      return None

    new_rhs = int(multiplier * rhs)
    new_rhs = new_rhs // gcd

    return new_rhs

  def conv(self, lp : MIPIntermediate):

    # scale constraints
    for cons in lp.constraints:
      if cons.sense == pulp.const.LpConstraintEQ and not self._scaleEqualityConstraints:
        continue
      cons.rhs = self._scaleExpr(cons.coefficients, rhs=cons.rhs)

    # scale objective
    if self._scaleObjective:
      lp.objective.constant = self._scaleExpr(lp.objective.coefficients, rhs=lp.objective.constant)

    return lp

  def interpret(self, x : Dict[str, int]):

    # nothing changes, since variables are not affected
    return x

class ShiftVars:

  def __init__(self):
    self._shifts = {}

  def conv(self, lp : MIPIntermediate):

    # determine shifts
    for var_name in lp.vars:
      if lp.vars[var_name].lowBound != 0:
        self._shifts[var_name] = lp.vars[var_name].lowBound
        lp.vars[var_name].lowBound -= self._shifts[var_name]
        lp.vars[var_name].upBound -= self._shifts[var_name]

    # apply shifts to all constraints
    for cons in lp.constraints:
      new_rhs = cons.rhs
      for var in cons.coefficients:
        if var in self._shifts:
          new_rhs -= self._shifts[var] * cons.coefficients[var]

      cons.rhs = new_rhs

    # apply shifts to objective (in order to maintain optimumn)
    for var in lp.objective.coefficients:
      if var in self._shifts:
        lp.objective.constant += self._shifts[var] * lp.objective.coefficients[var]

    return lp

  def interpret(self, x : Dict[str, int]):
    for var in self._shifts:
      x[var] += self._shifts[var]

    return x

class InequalityToEquality:

  def __init__(self):
    self.slacks = []

  def conv(self, lp : MIPIntermediate):

    for cons in lp.constraints:

      if cons.sense == pulp.const.LpConstraintEQ:
        continue

      # check integrality of contraints
      if not float(cons.rhs).is_integer():
          raise Exception(f"RHS {cons.rhs} of constraint ({cons}) is not integral.")
      for lp_var_name, lp_coeff in cons.coefficients.items():
        if not float(lp_coeff).is_integer():
          raise Exception(f"Coefficient {lp_coeff} for {lp_var_name} in constraint ({cons}) is not integral.")

      # compute lower and upper bound on LHS
      cons_up = 0
      cons_low = 0
      for lp_var_name, lp_coeff in cons.coefficients.items():
        lp_var = lp.vars[lp_var_name]

        combos = [lp_coeff * lp_var.upBound, lp_coeff * lp_var.lowBound]
        up_bnd = max(combos)
        low_bnd = min(combos)

        cons_up += up_bnd
        cons_low += low_bnd

      # compute the slack bounds
      if cons.sense == pulp.const.LpConstraintLE:
        min_slack = 0
        max_slack = cons.rhs - cons_low

      if cons.sense == pulp.const.LpConstraintGE:
        min_slack = 0
        max_slack = cons_up - cons.rhs

      # now add the slack as a new var to the LP
      slack_name = f"{cons.name}@slack"
      slack_var = pulp.LpVariable(slack_name, lowBound=min_slack, upBound=max_slack, cat=pulp.const.LpInteger)
      lp.vars[slack_name] = slack_var
      self.slacks.append(slack_name)

      if cons.sense == pulp.const.LpConstraintLE:
        cons.coefficients[slack_name] = +1
      else:
        cons.coefficients[slack_name] = -1

      # ... and change the sense
      cons.sense = pulp.const.LpConstraintEQ

    return lp

  def interpret(self, x : Dict[str, int]):
    for slack in self.slacks:
      del x[slack]

    return x

class IntegerToBinary:

  def __init__(self):
    self._old_to_new_var = {}

  def conv(self, lp : MIPIntermediate):

    # deduce integer's bounds and get a representation from that
    bit_vars = []
    for var_name in lp.vars:
      var = lp.vars[var_name]

      if var.cat == pulp.LpBinary:
        continue

      var_lo = var.lowBound
      var_up = var.upBound

      if var_lo == 0 and var_up == 1:
        continue

      var.cat = pulp.LpBinary

      if var_lo != 0:
        raise Exception(f"Variable {var_name} has not been shifted (lb = {var_lo}).")

      num_bits = int(math.ceil(math.log2(var_up)))

      # create binary variables and a map for replacement
      self._old_to_new_var[var_name] = []
      for bit in range(num_bits):
        bit_var_name = f"{var_name}@b{bit}"
        bit_var = pulp.LpVariable(bit_var_name, cat=pulp.const.LpBinary, lowBound = 0, upBound=1)
        self._old_to_new_var[var_name].append((bit_var, 2**bit))
        bit_vars.append((bit_var_name, bit_var))

    # add binary variables
    for t in bit_vars:
      lp.vars[t[0]] = t[1]

    # replace variables in constraints
    for cons in lp.constraints:

      # collect integer vars
      cons_integer_vars = []
      for var_name in cons.coefficients:
        if var_name in self._old_to_new_var:
          cons_integer_vars.append(var_name)

      # replace integer vars in equation
      for var_name in cons_integer_vars:
        old_coeff = cons.coefficients[var_name]
        del cons.coefficients[var_name]

        for tpl in self._old_to_new_var[var_name]:
          bit_var, bit_var_coeff = tpl
          cons.coefficients[bit_var.name] = old_coeff * bit_var_coeff

    # replace integer vars in objective
    obj_integer_vars = []
    for var_name in lp.objective.coefficients:
      if var_name in self._old_to_new_var:
        obj_integer_vars.append(var_name)

    for var_name in obj_integer_vars:
      old_coeff = lp.objective.coefficients[var_name]
      del lp.objective.coefficients[var_name]

      for tpl in self._old_to_new_var[var_name]:
        bit_var, bit_var_coeff = tpl
        lp.objective.coefficients[bit_var.name] = old_coeff * bit_var_coeff

    # completely remove integer variables
    for int_var_name in self._old_to_new_var:
      del lp.vars[int_var_name]

    return lp

  def interpret(self, x : Dict[str, int]):
    for old_var_name in self._old_to_new_var:
      old_var_val = 0

      for bit_tpl in self._old_to_new_var[old_var_name]:
        old_var_val += bit_tpl[1] * x[bit_tpl[0].name]
        del x[bit_tpl[0].name]

      x[old_var_name] = old_var_val

    return x

###
# IP to QUBO conversion controller
###
class IP2Qubo:
  """
  Converts an IP problem to a QUBO problem.
  Supported MIP formats: PulP MIP format, intermediate MIP format

  Args:
      sense (int): The optimization sense. Defaults to `HybridSolverOptSenses.MINIMIZE`.
      verbose (bool): Whether to print additional output during conversion. Defaults to `False`.
      scaleEqualityConstraints (bool): Whether to scale equality constraints during conversion. Defaults to `False`.
      scaleObjective (bool): Whether to scale the objective function during conversion. Defaults to `False`.

  Attributes:
      verbose (bool): Whether to print additional output during conversion.
      vars (Dict[str, QuboVariable]): A dictionary of QUBO variables in pairs of variable name and :class:`QuboVariable`.
      objective (QuboExpression): A QuboExpression for objective function.
      constraints (Dict[str, QuboExpression]): A dictionary of QUBO constraints, containing pairs of constraint names and :class:`QuboExpression`.
      sense (HybridSolverOptSenses): An enum representing the optimization sense of the QUBO. Default is :code:`HybridSolverOptSenses.MINIMIZE`.

  """
  def __init__(self,
               sense = HybridSolverOptSenses.MINIMIZE,
               verbose : bool = False,
               scaleEqualityConstraints : bool = False,
               scaleObjective : bool = False):
    super().__init__()
    self.verbose = verbose
    self._convs = [
      ScaleConstraints(scaleEqualityConstraints, scaleObjective),
      InequalityToEquality(),
      ShiftVars(),
      IntegerToBinary()
    ]

    self._var_order = []

    self.vars : Dict[str, QuboVariable] = {}
    self.objective : QuboExpression = None
    self.constraints : Dict[str, QuboExpression] = {}
    self.sense = sense

  def _checkMIPApplicability(self, prob : pulp.LpProblem) -> bool:
    vars = prob.variables()

    # check that there are no SOS constraints
    if len(prob.sos1) > 0:
      print("[MIP2QUBO] Unsuitable for QUBO conversion: There are SOS1 constraints.")
      return False

    if len(prob.sos2) > 0:
      print("[MIP2QUBO] Unsuitable for QUBO conversion: There are SOS2 constraints.")
      return False

    # check whether all variables are bounded and discrete
    for var in vars:

      if var.cat == pulp.const.LpContinuous:
        print("[MIP2QUBO] Unsuitable for QUBO conversion: " + var.name + " is continuous.")
        return False

      if var.lowBound is None or var.upBound is None:
        print("[MIP2QUBO] Unsuitable for QUBO conversion: " + var.name + " is unbounded.")
        return False

    return True

  def _IPtoQUBO(self, prob, mip_format):

    # store MIP to compute objective value
    self._mip = prob

    ### convert PuLP-MIP to intermediate format
    lp = None
    if mip_format == MIPSourceFormat.MIP_PULP:
      cvt = ConvPULPMIPToIntermediate()
      lp = cvt.conv(prob, self.sense)

      if not self._checkMIPApplicability(self._mip):
        raise Exception("IP not suited for QUBO conversion.")
    elif mip_format == MIPSourceFormat.MIP_INTERMEDIATE:
      lp = prob
    else:
      raise Exception("Unsupported MIP format.")

    ###
    # apply simplification steps on the (M)IP side
    ###
    if self.verbose:
      print("\n--- Input IP:")
      print(lp)
    for c in self._convs:
      lp = c.conv(lp)

      if self.verbose:
        print("\n--- After pass \"" + type(c).__name__ + "\" ---\n")
        print(lp)

    ###
    # create a set of QUBOs, where each QUBO represents either the objective
    # or a MIP constraint
    ###

    # convert variables
    ctr = 0
    self.vars = {}
    self._var_order = [""] * len(lp.vars)
    for var in lp.vars:
      self.vars[var] = QuboVariable(name=var, pos=ctr, initial=0)
      self._var_order[ctr] = var
      ctr += 1

    # create objective QUBO
    self.objective = QuboExpression()
    for var_name, var_coeff in lp.objective.coefficients.items():
      self.objective += var_coeff * self.vars[var_name]

    # create constraint QUBOs
    for cons in lp.constraints:
      qbo_cons = QuboExpression()
      for var_name, var_coeff in cons.coefficients.items():
        qbo_cons += var_coeff * self.vars[var_name]
      qbo_cons -= cons.rhs

      # square constraint
      self.constraints[cons.name] = qbo_cons * qbo_cons

  def _toWeightedQUBO(self, penalties : Dict[str, float]) -> QuboModel:
    qbo = QuboExpression()
    qbo += self.objective

    for cons in self.constraints:
      qbo += penalties[cons] * self.constraints[cons]

    mdl = QuboModel(sense=self.sense)
    mdl.objective = qbo
    mdl.vars = self.vars
    mdl._pos_ctr = len(mdl.vars)

    return mdl

  def fromIP(self, ip, mip_format : MIPSourceFormat):
    """
    Imports an IP problem into the class.

    Parameters:
        ip (dict): A dictionary containing an IP problem.
        mip_format (MIPSourceFormat): The format of the IP problem.
    """
    self._IPtoQUBO(ip, mip_format)

  def toQUBO(self, penalty : Union[float, Dict[str, float]] = 1.0):
    """
    Transforms the current QUBO instance to a weighted QUBO instance.

    Parameters:
        penalty (Union[float, Dict[str, float]]): Penalty factors as float that adjust the weight of each constraint.
            A single float is accepted to be applied to all constraints.
            Alternatively a dictionary of pairs of constraint name and respective penalty factor is accepted as well to apply individual penalty factors to constraints.

    Returns:
        QuboModel: A weighted QUBO.
    """
    penalty_vec = penalty

    if not isinstance(penalty, dict):
      penalty_vec = {}
      for cons in self.constraints:
        penalty_vec[cons] = penalty

    return self._toWeightedQUBO(penalty_vec)

  def liftQUBOSolution(self, x : Dict[str, int]):
    y = x

    for c in reversed(self._convs):
      y = c.interpret(y)

    return y

###
# Solvers for IPS via QUBO conversion
###

class IPviaQUBOSolver(ABC):
  """
  Abstract base class for solving IP problems using the QUBO solver.

  Parameters:
      verbose (bool): If True, prints additional information about the solver. Default is False.

  Attributes:
      ip2qubo (IP2Qubo): An instance of the :class:`IP2Qubo` class, which converts an IP problem to a QUBO problem.
      verbose (bool): If True, prints additional information about the solver. Default is False.
      iter (int): Integer stating the current number of iterations in the solver.
  """
  def __init__(self, verbose = False):
    self.ip2qubo = None
    self.verbose = verbose
    self.iter = 0

    # store the latest generated QUBO
    self._cur_qubo = None

  def _extractX(self):
    x = {}

    for _, var in self._cur_qubo.vars.items():
      x[var.name] = var.assignment

    return x

  def _getQUBOFeasibility(self):
    feas_vector = {}
    for cons_name, cons_qubo in self.ip2qubo.constraints.items():
      feas_vector[cons_name] = (cons_qubo.eval() == 0)

    return feas_vector

  def _checkQUBOFeasibility(self):
    feas_vector = self._getQUBOFeasibility()
    feas_vals = [feas_vector[t] for t in feas_vector]
    return all(feas_vals)

  def reportSolution(self):
    """
    Prints information about the current solution.
    """
    feas_vector = self._getQUBOFeasibility()

    print("")
    print(f"Solution #{self.iter}")
    print(f"\tObjective: {self.ip2qubo.objective.eval()}")
    print("\tConstraints:")
    for cons in self.ip2qubo.constraints:
      e_val = self.ip2qubo.constraints[cons].eval()
      print(f"\t\t({cons}) {'satisfied' if feas_vector[cons] else 'VIOLATED'}")
    print("")

  @abstractmethod
  def _solveIP(self, ip, mip_format : MIPSourceFormat):
    pass

  def solveIP(self, ip):
    """
    Solves an IP problem using the current solver.

    Parameters:
        ip (:class:`pulp.LpProblem`): A PulP LpProblem instance to solve.

    Returns:
        Solved IP or None.

    """
    if isinstance(ip, pulp.LpProblem):
      return self._solveIP(ip, MIPSourceFormat.MIP_PULP,
        HybridSolverOptSenses.MINIMIZE if
        ip.sense == pulp.const.LpMinimize else HybridSolverOptSenses.MAXIMIZE)

    raise Exception("Unsupported MIP format")

class OneShotIPviaQUBOSolver(IPviaQUBOSolver):
  """
  A class that solves an integer programming problem in one shot using a QUBO solver.

  Args:
      verbose (bool): Whether to print verbose output. Defaults to False.
      penalty (Union[float, Dict[str, float]]): Penalty factors as float that adjust the weight of each constraint.
            A single float is accepted to be applied to all constraints.
            Alternatively a dictionary of pairs of constraint name and respective penalty factor is accepted as well to apply individual penalty factors to constraints.

      hsolver_type (HybridSolverConnectionType): The type of Hybrid Solver to use for solving the QUBO. Defaults to
          HybridSolverConnectionType.CLOUD.
      api_key (str): The API key to use for connecting to the Hybrid Solver. Defaults to None.
  """

  def __init__(self, verbose = False, penalty : float = 1.0,
    hsolver_type = HybridSolverConnectionType.CLOUD, api_key = None):
    super().__init__(verbose)
    self.penalty = penalty
    self.hsolver_type = hsolver_type
    self.api_key = api_key

  def _solveIP(self, ip, mip_format : MIPSourceFormat, sense):
    self.ip2qubo = IP2Qubo(sense, self.verbose)

    # convert IP into partial QUBOs
    if self.verbose:
      print("Converting IP to QUBO...")
    self.ip2qubo.fromIP(ip, mip_format)

    # create a single QUBO
    penalty = (1.0 if self.ip2qubo.sense == HybridSolverOptSenses.MINIMIZE
      else -1.0) * abs(self.penalty)
    self._cur_qubo = self.ip2qubo.toQUBO(penalty)

    # solve QUBO
    if self.verbose:
      print("Solving QUBO...")
    spec = QUBOSpecBuilder()

    runner = RunnerFactory.getRunner(self.hsolver_type, api_key=self.api_key)
    self._cur_qubo.solve(spec.getd(), runner)

    x_qubo = {}
    for var_name, var in self._cur_qubo.vars.items():
      x_qubo[var_name] = var.assignment

    # print status
    if self.verbose:
      self.reportSolution()

    # lift solution back to MIP
    if self.verbose:
      print("Lifting solution back to MIP...")

    x_ip = self.ip2qubo.liftQUBOSolution(copy.deepcopy(x_qubo))
    for var in ip.variables():
      var.varValue = x_ip[var.name]

    # return IP with variables set to the lifted values
    return ip

class AutomaticPenaltyScalingIPviaQUBOSolver(IPviaQUBOSolver):
  """
  A subclass of :class:`IPviaQUBOSolver` that automatically scales penalty terms
  during the optimization process to find feasible solutions for IP problems.

  Args:
      verbose (bool): If True, prints additional information about the optimization process.
          Default is False.
      initial_penalty (Union[float, Dict[str, float]]): Penalty factors as float that adjust the weight of each constraint.
            A single float is accepted to be applied to all constraints.
            Alternatively a dictionary of pairs of constraint name and respective penalty factor is accepted as well to apply individual penalty factors to constraints.
            Default is 1.0.

      hsolver_type (HybridSolverConnectionType): The type of hybrid solver to use.
          Default and recommended is HybridSolverConnectionType.CLOUD.
      api_key (str): The API key for accessing the solver.
          Default is None.
      max_iters (int): The maximum number of iterations for the optimization process.
          Default is 100.

  Attributes:
      initial_penalty (Union[float, Dict[str, float]]): The initial value(s) for the penalty terms.
      hsolver_type (HybridSolverConnectionType): The type of hybrid solver to use.
      api_key (str): The API key for accessing the hybrid solver.
  """
  def __init__(self, verbose = False, initial_penalty : float = 1.0,
    hsolver_type = HybridSolverConnectionType.CLOUD, api_key = None,
    max_iters = 100):
    super().__init__(verbose)
    self.initial_penalty = initial_penalty
    self.hsolver_type = hsolver_type
    self.api_key = api_key

    self._cur_penalty = None
    self._iter = 0
    self._max_iters = max_iters

    self._inflation_factor = 10.0
    self._deflation_factor = 0.5

  def _solveIP(self, ip, mip_format : MIPSourceFormat, sense):
    self.ip2qubo = IP2Qubo(sense, self.verbose)

    # convert IP into partial QUBOs
    if self.verbose:
      print("Converting IP to QUBO...")
    self.ip2qubo.fromIP(ip, mip_format)

    # create the initial penalty vector
    self._cur_penalty = {}
    for cons in self.ip2qubo.constraints:
      self._cur_penalty[cons] = (1.0 if self.ip2qubo.sense == HybridSolverOptSenses.MINIMIZE
        else -1.0) * abs(self.initial_penalty)

    while self._iter < self._max_iters:
      self._cur_qubo = self.ip2qubo.toQUBO(self._cur_penalty)

      # solve QUBO
      if self.verbose:
        print("Solving QUBO with penalties:", self._cur_penalty)
      spec = QUBOSpecBuilder()

      runner = RunnerFactory.getRunner(self.hsolver_type, api_key=self.api_key)
      self._cur_qubo.solve(spec.getd(), runner)

      # check feasibility
      feas_vector = self._getQUBOFeasibility()

      # print status
      self.reportSolution()

      if all([feas_vector[t] for t in feas_vector]):
        break

      # reweight it
      for cons in feas_vector:
        if feas_vector[cons]:
          self._cur_penalty[cons] *= self._deflation_factor
        else:
          self._cur_penalty[cons] *= self._inflation_factor

      self._iter += 1

    x_qubo = {}
    for var_name, var in self._cur_qubo.vars.items():
      x_qubo[var_name] = var.assignment

    # lift solution back to MIP
    if self.verbose:
      print("Lifting solution back to MIP...")

    x_ip = self.ip2qubo.liftQUBOSolution(copy.deepcopy(x_qubo))
    for var in ip.variables():
      var.varValue = x_ip[var.name]

    # return IP with variables set to the lifted values
    return ip
