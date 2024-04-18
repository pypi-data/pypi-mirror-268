"""
Class to parse solution from file.
"""

class SolutionParser:

    def __init__(self):
        """Constructor."""
        pass

    @staticmethod
    def parse(solution_file):
        """
        Parse solution from file.
        """

        if not len(solution_file):  # if file is empty
            return None

        sol_file_as_list = solution_file.splitlines()

        solution = {}
        # on platform 2 and for MIPs on platform 1, we have parse the solution from a file
        # that has keys like 'Model status', 'Primal solution values', etc.
        if "Model status" in sol_file_as_list[0]:

            # find index of 'Primal solution values' keyword
            try:
                key_idx = sol_file_as_list.index("Primal solution values:")
            except ValueError:
                # no solution
                return solution
            # get only the primal solution part
            sol_as_list = sol_file_as_list[key_idx + 1 :]

            # split entries to have var name and value
            for l in sol_as_list:
                var_name, var_val = l.split()
                solution[str(var_name)] = float(var_val)

        else:
            # For QUBOs on platform 1, the solution file consists only of the variable values
            solution = {str(idx): float(val) for idx, val in enumerate(sol_file_as_list)}

        return solution
