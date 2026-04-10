# playwright-automation

QA automation workspace built with Python, Playwright, Pytest, and a reusable core framework.

## Structure

```text
core/
|-- config/
|-- driver/
|-- pages/
|-- reporting/
`-- testing/

automation/
|-- conftest.py
|-- run_testng.py
|-- testng.xml
|-- functionalities/
|   |-- cart_func.py
|   |-- checkout_func.py
|   `-- login_func.py
|-- pages/
|   |-- cart_page.py
|   |-- checkout_complete_page.py
|   |-- checkout_information_page.py
|   |-- checkout_overview_page.py
|   |-- home_page.py
|   `-- login_page.py
`-- tasks/
    |-- task_0001_login.py
    |-- task_0002_invalid_login.py
    |-- task_0003_add_product_to_cart.py
    `-- task_0004_complete_checkout.py
```

## Architecture

- `pages`: map locators and page actions on top of the shared `BasePage`
- `functionalities`: orchestrate business journeys using one or more pages
- `tasks`: define the final test scenarios
- `testng.xml`: selects which task files should run

## Execution

The main entry point for IDE execution is:

- `automation/run_testng.py`

The XML runner reads:

- `automation/testng.xml`

Example:

```xml
<execution headed="false" slow_mo="0" />
<class path="automation/tasks/task_0001_login.py" enabled="true" />
```

To visually follow execution:

```xml
<execution headed="true" slow_mo="700" />
```

## How To Run

Windows PowerShell:

```powershell
.\tools\runners\run_tests_windows.ps1
.\tools\runners\run_tests_windows.ps1 -Target "automation\tasks\task_0001_login.py"
```

Windows batch:

```bat
tools\runners\run_tests_windows.bat
tools\runners\run_tests_windows.bat automation\tasks\task_0001_login.py
```

macOS/Linux:

```bash
chmod +x ./tools/runners/run_tests_unix.sh
./tools/runners/run_tests_unix.sh
./tools/runners/run_tests_unix.sh automation/tasks/task_0001_login.py
```

## Evidence

Execution artifacts are generated under `test-results/`.

- one PDF evidence report per executed task
- procedural naming to avoid overwriting previous runs

Screenshots are captured by page methods and used as temporary assets to compose the PDF report.

## Current Practice Scenarios

- successful login
- invalid login with locked user
- add product to cart
- complete checkout with a single product
