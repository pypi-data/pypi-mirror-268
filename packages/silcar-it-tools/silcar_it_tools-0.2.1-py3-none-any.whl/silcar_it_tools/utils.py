import sys
from pathlib import Path


def get_full_path(input_str):
    return Path(input_str).expanduser().resolve()


def warn(text):
    print(f"Warning: {text}", file=sys.stderr)


def error(text):
    print(f"Error: {text}", file=sys.stderr)
    exit(1)


def get_valid_size_status(file_path):
    return len(file_path.read_bytes()) > 0


def show_file_status(file_path, status, reasons):
    if status is None:
        status = '???'
    if reasons is None:
        reasons = ['unknown']

    print(f"{status}\t{file_path}")
    if status != 'Good':
        for r in reasons:
            print(f"  > {r}")


def run_cli_cmd(func):
    try:
        func()
    except KeyboardInterrupt:
        print("Cancelled with Ctrl+C")
        exit(1)
