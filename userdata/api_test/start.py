import os
import shutil
import pathlib
import subprocess

os.chdir(pathlib.Path(__file__).parent)
shutil.rmtree("results", True)
subprocess.Popen(
    "python -m pytest -s /api_test/tests/negative/test.py --alluredir /api_test/results/negative", shell=True).wait()
subprocess.Popen("allure serve results/negative",
                 shell=True)
subprocess.Popen(
    "python -m pytest -s /api_test/tests/regress/test.py --alluredir /api_test/results/regress", shell=True).wait()
subprocess.Popen("allure serve results/regress",
                 shell=True)
