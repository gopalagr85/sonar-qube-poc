@echo off
echo Running Ruff...
ruff check src --output-format=json > ruff-report.json

echo Running Pylint...
pylint src --reports=n > pylint-report.txt

echo Running Tests with Coverage...
coverage run --source=src -m pytest
coverage xml

REM --------------------------------------------
REM Get Git Commit Hash as Sonar Project Version
REM --------------------------------------------
for /f %%i in ('git rev-parse --short HEAD') do set VERSION=%%i

echo Sonar Project Version: %VERSION%

echo Running Sonar Scanner...
sonar-scanner.bat -X -Dsonar.projectVersion=%VERSION% -Dsonar.qualitygate.wait=true -Dsonar.login=sqp_9cad84b2f3fcb8333b94d08bd28fb1daac14764f

REM using REM we can add the comments in .bat file
REM sonar-scanner.bat -X

echo Done.
pause
