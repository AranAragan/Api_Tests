import os
import shutil
import pathlib
import subprocess

os.chdir(pathlib.Path(__file__).parent)
shutil.rmtree("results", True)
subprocess.Popen(
    "python3 -m pytest -s tests/negative/test.py --alluredir results/negative", shell=True).wait()
subprocess.Popen("allure serve results/negative",
                 shell=True)
subprocess.Popen(
    "python3 -m pytest -s tests/regress/test.py --alluredir results/regress", shell=True).wait()
subprocess.Popen("allure serve results/regress",
                 shell=True)
