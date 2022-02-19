#!/bin/bash
#
# Testing the package building :
# python3 -m venv tmp_env && source tmp_env/bin/activate
# ./build.sh
# ls dist
# pip list
# pip show -v my_minipack
# ./tests/logger_test.py
# ./tests/loading_test.py
# deactivate
# rm -rf tmp_env dist machine.log src/my_minipack.egg-info
#
python -m pip install --upgrade build
pip install --upgrade pip
pip install --upgrade setuptools
pip install --upgrade wheel
python -m build
pip install dist/my-minipack-1.0.0.tar.gz