# playwright-automation

Consumer automation project built on top of the external [`playwright-core`](https://github.com/tenorio0/playwright-core) framework.

## Purpose

This repository is focused only on:

- page models specific to the application under test
- business functionalities and journeys
- final scenario construction through task classes
- XML-based execution selection

## Structure

```text
automation/
|-- runners/
|   |-- run_test_01.py
|   `-- set_test_01.xml
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

config/
|-- conftest.py
|-- pytest.ini
`-- requirements.txt
```

## Framework Dependency

The reusable framework now lives in:

- [`playwright-core`](https://github.com/tenorio0/playwright-core)

Installed through:

```bash
pip install -r config/requirements.txt
```

## Execution

Run the XML selector:

```bash
python -B automation/runners/run_test_01.py
```

Or call the framework runner directly:

```bash
python -B -m playwright_core.testing.testng_runner automation/runners/set_test_01.xml
```

## Current Practice Scenarios

- successful login
- invalid login with locked user
- add product to cart
- complete checkout with a single product
