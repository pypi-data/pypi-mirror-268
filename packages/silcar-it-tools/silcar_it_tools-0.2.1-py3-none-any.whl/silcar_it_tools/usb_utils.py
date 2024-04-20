import argparse
import os
import queue
import shutil
import threading
from pathlib import Path

from . import utils


def copy_filtered_files(srcdir, outdir, ignored, q):
    root = None
    outdir = Path(outdir)
    copy_ct = 0
    for dirpath, dirnames, filenames in os.walk(srcdir):
        dirpathobj = Path(dirpath)
        parent = dirpathobj.name
        if not root:
            root = dirpathobj
            parent = None
        if len(filenames) == 0:
            continue  # skip empty folder
        badnames = []
        for expr in ignored:
            badnames.extend([p.name for p in dirpathobj.glob(expr)])
        goodnames = [f for f in filenames if f not in badnames]
        for n in goodnames:
            if not parent or len(parent) < 2:
                destdir = outdir
            else:
                destdir = outdir / parent
            destdir.mkdir(parents=True, exist_ok=True)
            destfile = destdir / n
            srcfile = dirpathobj / n
            if not destfile.is_file():
                try:
                    shutil.copy2(srcfile, destfile)
                except OSError:
                    print(f"\nError: Could not copy {srcfile}")
                    continue
            copy_ct += 1
            q.put(copy_ct)


def write_progress(value, screen_width=80):
    print(f"\rfiles recovered: {value} ", end='')


def get_usb_files():
    parser = argparse.ArgumentParser(
        prog="get-usb-files",
        description="copy files found within the given folder's file tree",
    )
    parser.add_argument(
        'DIR', nargs=1,
        help="root folder of filesystem"
    )
    args = parser.parse_args()
    ignored = [
        '*.CHK',
        '*.dat',
        '*.dll',
        '*.exe',
        '*.EXE',
        '*.ini',
        '*.lnk',
        '*.rar',
        '.~lock.*',
        '~*',
        'FOUND.*',
        'IndexerVolumeGuid',
        'System Volume Information',
    ]
    srcdir = Path(args.dir[0])
    outdir = Path.home() / srcdir.name
    if outdir.exists() and next(outdir.iterdir(), None):
        print(f"Folder is not empty: {outdir}")
        ans = input("Continue? [y/N] ")
        if ans.lower() != 'y':
            exit(1)

    q = queue.Queue()
    outdir.mkdir(exist_ok=True)
    t = threading.Thread(
        target=copy_filtered_files,
        args=[srcdir, outdir, ignored, q],
        daemon=True,
    )
    t.start()
    while t.is_alive():
        if not q.empty():
            write_progress(q.get())
    print()


def cli_get_usb_files():
    utils.run_cli_cmd(get_usb_files)
