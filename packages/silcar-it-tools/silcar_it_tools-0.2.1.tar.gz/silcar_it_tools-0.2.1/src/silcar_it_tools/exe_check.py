# When testing, use:
# (env) $ python3 -c 'import exe_check.cli; exe_check.cli.main()' [ARGS]
# This makes it run the same way as installed version, which makes imports work
# correctly.

import argparse
import pefile

from . import config
from . import packing
from . import utils


def check_file(f):
    status = 'Good'
    reasons = []
    # Check for zero size.
    if utils.get_valid_size_status(f) is False:
        status = 'Bad'
        reasons.append('File has zero length.')
    # Check for packing.
    res = packing.get_packed_status_and_reasons(f)
    if res[0] is None and status == 'Good':
        status = 'Unknown'
        if res[1] is not None:
            reasons.extend(res[1])
    elif res[0] is True:
        status = 'Bad'
        if res[1] is not None:
            reasons.extend(res[1])
    return status, reasons


def evaluate_file(file_path):
    status, reasons = check_file(file_path)
    utils.show_file_status(file_path, status, reasons)
    if config.REMOVE_FILES is True and status == 'Bad':
        print(f"  > Removing: {file_path}")
        file_path.unlink()


def evaluate_dir_path(base_dir, exts):
    """ Scan folder and all subfolders for packed EXE, etc. files. """
    # Putting the glob generator directly in the for-loop allows real-time file
    # checking. Otherwise, all the files have to be found first, then they can
    # be checked.
    for f in (p for p in base_dir.rglob('*') if p.suffix.lower() in exts):
        if f.is_file():
            evaluate_file(f)


def show_file_info(f):
    # Dump all PE info to stdout.
    try:
        pe = pefile.PE(f, fast_load=True)
        print(pe.dump_info())
        # # TODO: Testing.
        # packing.packed_mismatched_data_sizes(pe)
    except pefile.PEFormatError as e:
        utils.error(e)


def exe_check():
    description = (
        "Quickly determine if EXE or other similar file has been \"packed\""
        "with extra data; i.e. it has been corrupted by a virus."
    )
    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        )
    parser.add_argument(
        '-c', '--clean',
        action='store_true',
        help="delete bad file(s)",
    )
    parser.add_argument(
        '-d', '--directory',
        action='store_true',
        help=(
            "arg is a directory; recursively check all EXE and similar files"
            "within"
        ),
    )
    parser.add_argument(
        '-i', '--info',
        action='store_true',
        help="show all Portable Executable-related info for the given file",
    )
    parser.add_argument(
        '-V', '--version',
        action='store_true',
        help="show all Portable Executable-related info for the given file",
    )
    parser.add_argument(
        'file',
        nargs='?',
        help="check the given EXE (or similar) file for evidence of packing",
    )
    args = parser.parse_args()
    exts = ['.dll', '.exe']

    if args.version is True:
        print(config.VERSION)
        exit()

    if args.file is None:
        parser.print_help()
        exit(1)

    full_path = utils.get_full_path(args.file)

    if args.clean:
        config.REMOVE_FILES = True

    if args.directory:
        # Scan folder and all subfolders for packed EXE files.
        base_dir = full_path
        if not base_dir.is_dir():
            utils.error(f"Not a folder: {base_dir}")
        evaluate_dir_path(base_dir, exts)
        exit()

    elif args.info:
        target_file = full_path
        if not target_file.is_file():
            utils.error(f"File not found: {target_file}")
        show_file_info(target_file)
        exit()

    elif args.file:
        target_file = full_path
        if not target_file.is_file():
            utils.error(f"File not found: {target_file}")
        if not target_file.suffix.lower() in exts:
            utils.error(f"Invalid file type: {target_file}")
        evaluate_file(target_file)
        exit()


def cli_exe_check():
    utils.run_cli_cmd(exe_check)
