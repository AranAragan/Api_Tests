import os
import shutil
import pathlib
import subprocess

os.chdir(pathlib.Path(__file__).parent)
shutil.rmtree("/result/", True)
subprocess.Popen(
    "python -m pytest -s /api_test/tests/negative/test.py --alluredir /result/negative", shell=True).wait()
subprocess.Popen("allure serve /result/negative",
                 shell=True)
subprocess.Popen(
    "python -m pytest -s /api_test/tests/regress/test.py --alluredir /result/regress", shell=True).wait()
subprocess.Popen("allure serve /result/regress",
                 shell=True)
