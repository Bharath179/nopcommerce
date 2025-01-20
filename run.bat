@echo off
call venv\scripts\active
pytest -s -v -m "smoke" --html .\reports\test_report.html --browser chrome
pause