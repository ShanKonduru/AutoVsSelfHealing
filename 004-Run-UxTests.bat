@echo off
poetry run pytest apptest\uxtest\uxtest.py --html=ux-test-report.html --self-contained-html

