"""
Creates status page for online RapidPE-RIFT runs
"""

__author__ = "Vinaya Valsan"

import os
import shutil
import subprocess
import json
import logging

from argparse import ArgumentParser


logging.basicConfig(level=logging.INFO)
DEFAULT_DIR = os.path.dirname(__file__)

optp = ArgumentParser()
optp.add_argument(
    "--gracedb",
    default="production",
    help="type of gracedb instance. Options are"
    "production, playground, dev, test",
)
opts = optp.parse_args()
gracedb = opts.gracedb

with open(os.path.join(DEFAULT_DIR, "static/gracedb_dir.json"), "r") as f:
    gracedb_dirs = json.load(f)


def main():
    web_dir_base = os.path.join(
        os.getenv("HOME"), f"public_html/RapidPE/O4_run_status/{gracedb}"
    )

    os.makedirs(web_dir_base, exist_ok=True)

    processed_dir = os.listdir(web_dir_base)

    all_dir = os.listdir(gracedb_dirs[gracedb])

    new_dir = list(set(all_dir) - set(processed_dir))

    create_status_page_exe_path = shutil.which('rapidpe-rift-rota-tools')

    for sid in sorted(new_dir, reverse=True):
        web_dir = os.path.join(web_dir_base, sid)
        cmd = (
            f"{create_status_page_exe_path} --superevent-id {sid}"
            f" --gracedb {gracedb} --web-dir {web_dir}"
            f" --output-dir {web_dir}"
        )
        logging.info(cmd)
        try:
            subprocess.run(cmd, shell=True, check=True)
        except subprocess.CalledProcessError:
            continue


if __name__ == "__main__":
    main()
