# app.py

input_file_name = "input.json"

import json
import main

with open(input_file_name) as f:
    input_data = json.load(f)

data = input_data["data"]

# Optional extra parameters
extra_arguments = input_data.get('extra_arguments', {})
solver_params = input_data.get('solver_params', {})

result = main.run(data, solver_params, extra_arguments)

print(result)
