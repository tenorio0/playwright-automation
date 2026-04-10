from pathlib import Path
import sys

sys.dont_write_bytecode = True

from playwright_core.testing.testng_runner import run_from_xml


def main() -> int:
    return run_from_xml(Path(__file__).with_name("testng.xml"))


if __name__ == "__main__":
    raise SystemExit(main())
