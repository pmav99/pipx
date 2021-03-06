import argparse
import subprocess
import sys


def run(cmd):
    print(f"Running {' '.join(cmd)!r}")
    rc = subprocess.run(cmd).returncode
    if rc:
        print(f"test failed; exiting with code {rc}")
        exit(rc)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--only-static", action="store_true")
    args = parser.parse_args()

    files = ["get-pipx.py", "pipx", "tests"]

    run(["black", "--check"] + files)
    run(["flake8"] + files)
    run(["mypy"] + files)

    if not args.only_static:
        run([sys.executable, "-m", "tests"])


if __name__ == "__main__":
    main()
