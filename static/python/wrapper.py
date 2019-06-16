import json
import sys

from pytutor import generate_trace

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("data")
args = parser.parse_args()

data = json.loads(args.data)

code = data["code"]
setup_code = data["setup_code"]
modules = data["modules"]
working_directory = data["working_directory"]

sys.path.insert(0, working_directory)

trace = generate_trace.run_logger(code, setup_code, modules)

print(trace)
