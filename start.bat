rd /s /q .\results
python -m pytest -s test.py --alluredir results\1
allure serve .\results\1