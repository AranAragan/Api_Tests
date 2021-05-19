import os
import shutil
import pathlib
import subprocess

os.chdir(pathlib.Path(__file__).parent)
shutil.rmtree("results", True)

subprocess.Popen(
    "python -m pytest -s tests/regress/test.py --alluredir results/regress", shell=True).wait()
subprocess.Popen("allure serve results/regress",
                 shell=True)
