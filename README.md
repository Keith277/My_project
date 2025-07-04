# MCP Playwright Test Suite

This project contains automated tests for the login functionality using Playwright and pytest.

## Project Structure
```
mcp-playwright-cx/
|-- requirements.txt
|-- page/
|   |-- __init__.py
|   |-- login_page.py
|-- tests/
|   |-- pytest.ini
|   |-- test_Login/
|       |-- Login_successfully.py
|       |-- Invalid_email.py
|       |-- Invalid_pass.py
|       |-- blank_email.py
|       |-- blank_pass.py
|-- README.md
```

## Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Install Playwright browsers:
```bash
playwright install
```

## Running Tests

To run all tests:
```bash
pytest
```

To run a specific test:
```bash
pytest tests/test_Login/Login_successfully.py
```

## Test Cases

1. Login Successfully (TC_01)
2. Login with Invalid Email (TC_02)
3. Login with Invalid Password (TC_03)
4. Login with Blank Email (TC_04)
5. Login with Blank Password (TC_05) 