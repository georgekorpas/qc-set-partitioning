# main.py

import numpy as np
from scipy.optimize import linprog

def run(input_data, solver_params, extra_arguments):
    costs = np.array(input_data['costs'])
    constraints = np.array(input_data['constraints'])

    # Solve the Set Partitioning Problem
    return solve_set_partitioning(costs, constraints)

def solve_set_partitioning(costs, constraints):
    num_vars = len(costs)
    num_constraints = len(constraints)

    A_ub = np.vstack([-np.eye(num_vars), np.eye(num_vars)])
    b_ub = np.hstack([np.zeros(num_vars), np.ones(num_vars)])

    A_eq = constraints
    b_eq = np.ones(num_constraints)

    x_bounds = [(0, 1) for _ in range(num_vars)]

    result = linprog(c=costs, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=x_bounds, method='highs')

    return {"Optimum Objective Function Value": result.fun}
