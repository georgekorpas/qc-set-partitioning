import json
import numpy as np
from scipy.optimize import linprog

# Load data from the JSON file
with open('spp_input.json', 'r') as file:
    data = json.load(file)

costs = np.array(data['costs'])
constraints = np.array(data['constraints'])

# Construct the linear programming problem
num_vars = len(costs)
num_constraints = len(constraints)

# Coefficients for the inequality constraints
A_ub = np.vstack([-np.eye(num_vars), np.eye(num_vars)])
b_ub = np.hstack([np.zeros(num_vars), np.ones(num_vars)])

# Coefficients for the equality constraints
A_eq = constraints
b_eq = np.ones(num_constraints)

# Bounds for each variable (0 to 1, since we are interpreting them as binary)
x_bounds = [(0, 1) for _ in range(num_vars)]

# Solve the linear program
result = linprog(c=costs, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=x_bounds, method='highs')

# Print the value of the objective function
print("Optimum Objective Function Value:", result.fun)
