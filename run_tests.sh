#!/bin/bash

# you may activate the env if you are running locally
# pyenv activate inpe_cdsr_cdsr_pack

# just run the test cases
# python -m unittest discover tests "test_*.py" -v

# run test cases and coverage it
coverage run -m unittest discover tests "test_*.py" -v &&
    coverage report -m &&
    coverage html
