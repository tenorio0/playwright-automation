from pathlib import Path
import os
import sys

sys.dont_write_bytecode = True

from playwright_core.testing.testng_runner import run_from_xml

ROOT = Path(__file__).resolve().parents[2]
PYTEST_CONFIG = ROOT / "config" / "pytest.ini"
XML_CONFIG = ROOT / "config" / "set_test_01.xml"


def main() -> int:
    extra_addopts = f'-c "{PYTEST_CONFIG}" -p config.conftest'
    existing_addopts = os.environ.get("PYTEST_ADDOPTS", "").strip()
    os.environ["PYTEST_ADDOPTS"] = f"{existing_addopts} {extra_addopts}".strip()
    return run_from_xml(XML_CONFIG)


if __name__ == "__main__":
    raise SystemExit(main())
