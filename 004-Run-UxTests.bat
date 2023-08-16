@echo off
poetry run pytest uxtest\uxtest.py --html=ux-test-report.html --self-contained-html

