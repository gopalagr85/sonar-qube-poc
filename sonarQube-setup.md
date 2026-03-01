# SonarQube + Python Quality Setup (Complete POC Documentation)

This document explains how to configure SonarQube for a Python project using Docker on Windows, integrate quality tools, configure Quality Gates, and validate the setup using a sample “bad” project.

---

# 1. Why Run SonarQube via Docker on Windows

Running SonarQube on Windows via Docker is the industry standard for a clean, hassle-free Proof of Concept.

Benefits:
1. No manual Java 17 installation required
2. No PostgreSQL setup required
3. No environment conflicts
4. Fully isolated and clean setup
5. Easy to delete and restart

---

# 2. Prerequisites

1. Docker Desktop installed
2. Docker Desktop running
3. Python 3.x installed
4. pip available

---

# 3. Phase 1 – Start SonarQube Server (Docker)

Open Command Prompt or PowerShell and run:

```bash
# Production-safe: 
docker run -d --name sonarqube -p 9000:9000 sonarqube:lts-community

# for POC:
docker run -d --name sonarqube -p 9000:9000 -e SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true sonarqube:community
```


Note:
Bootstrap checks are disabled to prevent Elasticsearch errors on Windows/WSL in POC Command.


# Open browser:
```
http://localhost:9000
```

## Login:
   - Username: admin  
   - Password: admin  

   - Change password when prompted (example: admin123 for demo).

---

# 4. Phase 2 – Create Project and Generate Token

1. Click "Manually"
2. Project Display Name: My Python POC
3. Project Key: my-python-poc
4. Main Branch: main
5. Click Set Up

Select:
Analyze Locally

Generate Token:
Token Name: poc-token
Expiry: 30 days

Copy the token immediately (it will not be shown again).

Select:
Language: Other
OS: Windows

Download SonarScanner for Windows.
- https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-8.0.1.6346-windows-x64.zip

Unzip to:
C:\sonar-scanner

---
# Phase 3:
    run-quality.bat
---

# SonarQube + Python Quality Setup (POC Documentation)

This document explains how to configure SonarQube as a Quality Gate for a Python project with selected coding standards, coverage, duplication control, and IDE integration.

---

# 1. Pre-Requisites

1. Install Docker
2. Run SonarQube (Community Edition) in Docker
3. Install SonarScanner CLI
4. Install Python 3.x
5. Install required Python packages:

   pip install pytest coverage pylint ruff

---

# 2. Start Fresh SonarQube Setup

1. Start SonarQube container
2. Open http://localhost:9000
3. Login with admin/admin
4. Change default password
5. Create a new Project manually
6. Generate a User Token
7. Save the token securely (it is shown only once)

---

# 3. Configure sonar-project.properties

Create file in project root:

sonar.projectKey=your_project_key  
sonar.host.url=http://localhost:9000  
sonar.login=your_token  

sonar.sources=src  
sonar.inclusions=**/*.py  
sonar.sourceEncoding=UTF-8  

sonar.exclusions=**/venv/**, **/.ruff_cache/**  

sonar.python.ruff.reportPaths=ruff-report.json  
sonar.python.pylint.reportPaths=pylint-report.json  
sonar.python.coverage.reportPaths=coverage.xml  

sonar.scm.disabled=true  

---

# 4. Configure Quality Tools Execution Script (Windows Example)

Create run-quality.bat:

echo Running Ruff...
ruff check src --output-format=json > ruff-report.json

echo Running Pylint...
pylint src --output-format=json > pylint-report.json

echo Running Tests with Coverage...
coverage run --source=src -m pytest
coverage xml

echo Running Sonar Scanner...
sonar-scanner

pause

---

# 5. Configure New Code Definition

Go to:

Project Settings → New Code

Select one option:
1. Previous Version
2. Number of Days

Recommended for POC:
Use "Previous Version"

Increase version using:

sonar.projectVersion=1.0

Update version when releasing new changes.

---

# 6. Configure Coverage Properly

1. Run coverage only for src:

   coverage run --source=src -m pytest

2. Generate coverage.xml:

   coverage xml

3. In SonarQube:

   Project Settings → Quality Gate

Set threshold example:

New Code Coverage ≥ 80%

---

# 7. Ignore Tests for Duplication

To exclude test folder from duplication:

sonar.exclusions=tests/**

Or specifically:

sonar.cpd.exclusions=tests/**

---

# 8. Configure Professional Duplication Threshold

Go to:

Quality Gates → Edit Condition

Add:

Duplicated Lines on New Code < 3%

Note:
SonarQube detects duplication only above minimum block size.
Very small duplicate blocks may not be detected.

---

# 9. Control PEP8 Rules Flexibly

Instead of enforcing full PEP8:

1. Use Ruff
2. Enable only selected rules in pyproject.toml
3. Disable unwanted rules

Example:

[tool.ruff]
select = ["E", "F"]
ignore = ["E501"]

This gives flexibility instead of strict enforcement.

---

# 10. Token Configuration

Use only:

User Token

Add token inside:

sonar.login=your_token

If authentication fails:
Check token under:

My Account → Security → Tokens

---

# 11. GitHub Integration Clarification

There are two setups:

A) Local Scanner Only  
SonarScanner runs locally and pushes results to SonarQube server.

B) GitHub CI Integration  
Configure GitHub Actions to run sonar-scanner.

In this POC, analysis was done using Local Scanner.

---

# 12. IDE Integration

PyCharm:

1. Install plugin: SonarQube for IDE
2. Go to:
   File → Settings → Tools → SonarQube for IDE
3. Add server URL and token
4. Bind project

Note:
SonarLint is now renamed to SonarQube for IDE.

VSCode:

1. Install SonarLint extension
2. Bind to SonarQube server
3. Issues will appear inline

---

# 13. Understanding A–F Grades in SonarQube

SonarQube assigns grades based on:

A = Best  
B = Minor issues  
C = Moderate issues  
D = Major issues  
E = Critical issues  
F = Very Poor quality  

Grades are based on:
- Bugs
- Vulnerabilities
- Code Smells
- Coverage
- Duplication

These grades are visible in SonarQube dashboard.
They are not fully displayed inline inside IDE.

---

# 14. Coverage Failure Example

If you see:

"Coverage on New Code is less than 80%"

It means:
Your new changes do not meet Quality Gate threshold.

Solution:
1. Add more unit tests
2. Cover missing branches
3. Re-run coverage and sonar-scanner

---

# 15. Final Recommended Professional Setup

1. Use Ruff for style enforcement
2. Use Pylint for code quality rules
3. Use pytest + coverage
4. Enforce:
   - New Code Coverage ≥ 80%
   - Duplication < 3%
5. Define New Code as Previous Version
6. Integrate SonarQube for IDE for developer visibility
7. Keep rules flexible, not fully strict PEP8

---

End of Document