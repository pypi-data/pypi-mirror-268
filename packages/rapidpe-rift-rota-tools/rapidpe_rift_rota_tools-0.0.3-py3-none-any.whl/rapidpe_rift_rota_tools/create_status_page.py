#!/usr/bin/env python3

"""
Creates status page from RapidPE-RIFT runs
"""

__author__ = "Vinaya Valsan"

import os
import json
import shutil
import time

from argparse import ArgumentParser
from jinja2 import Environment, FileSystemLoader
from rapidpe_rift_pipe.config import Config
from . import status_summary as statutils

DEFAUL_DIR = os.path.dirname(__file__)
DEFAULT_TEMPLATE_DIR = os.path.join(DEFAUL_DIR, "template_files")

optp = ArgumentParser()

run_dir_group = optp.add_mutually_exclusive_group()
run_dir_group.add_argument("--run-dir", help="path to event run dir")
gracedb_group = run_dir_group.add_argument_group("GraceDB options")
gracedb_group.add_argument("--superevent-id", help="superevent id")
gracedb_group.add_argument(
    "--gracedb",
    default="production",
    help="type of gracedb instance. Options are"
    "production, playground, dev, test",
)

optp.add_argument("--web-dir", default=None, help="path to web dir")
optp.add_argument("--output-dir", default="./", help="directory to save files")
optp.add_argument(
    "--overwrite-output-dir",
    action="store_true",
    help="replaced existing output-dir",
)
optp.add_argument(
    "--sleep",
    default=5,
    help="sleep for this many seconds before updating the status page",
)
opts = optp.parse_args()
if opts.run_dir:
    run_dir = os.path.abspath(opts.run_dir)
    config = Config.load(os.path.join(run_dir, "Config.ini"))

    is_event = config.event.mode in {"sid", "gid"}
    if is_event:
        if config.event.mode == "sid":
            event_id = config.event.superevent_id
        else:
            event_id = config.event.gracedb_id

else:
    with open(os.path.join(DEFAUL_DIR, "static/gracedb_dir.json"), "r") as f:
        gracedb_dirs = json.load(f)
    emfollow_dir = gracedb_dirs[opts.gracedb]
    event_id = opts.superevent_id
    run_dir = f"{emfollow_dir}/{event_id}"

if opts.web_dir:
    web_dir = os.path.abspath(opts.web_dir)
else:
    web_dir = os.path.join(
        os.getenv("HOME"),
        f"public_html/RapidPE/O4_run_status/{opts.gracedb}/{event_id}",
    )


output_dir = os.path.abspath(opts.output_dir)
if opts.overwrite_output_dir:
    if os.path.exists(output_dir):
        print(f"Output dir ({output_dir}) exists. Removing output dir.")
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)
else:
    try:
        os.makedirs(output_dir)
    except FileExistsError:
        print(f"Output dir ({output_dir}) already exists. Exiting the run.")
        exit(1)

os.makedirs(web_dir, exist_ok=True)

status_file = os.path.join(output_dir, "status.json")
status_html = os.path.join(output_dir, "index.html")


start_time = time.time()

all_status = ["RUN", "IDLE", "HOLD", "SUCCESS", "FAIL"]


def main():

    end_time = start_time + 30 * 60

    job_complete = False
    pastro_ready = False
    status_complete = job_complete*pastro_ready

    number_of_status_check = 0

    while time.time() < end_time and not status_complete:
        job_complete = os.path.exists(os.path.join(run_dir, "JOB_COMPLETE"))
        pastro_ready = os.path.exists(
            os.path.join(run_dir, "summary", "p_astro.json")
        )
        if os.path.exists(status_file):
            with open(status_file, "r") as f:
                status_dict = json.load(f)
        else:
            status_dict = {}
        number_of_status_check += 1
        print(f"Updating status page: {number_of_status_check}", end="\r")
        status_dict = statutils.get_results_status(
            run_dir, data_dict=status_dict
        )
        with open(status_file, "w") as f:
            json.dump(status_dict, fp=f)

        status_summary = {k: {} for k in all_status}
        status_summary["TOTAL"] = {}

        for k, d in sorted(status_dict.items()):
            iteration = str(d["iteration_level"])
            node_status = d["node_status"]
            if node_status != "":
                if iteration not in status_summary[node_status]:
                    status_summary[node_status][iteration] = 1
                else:
                    status_summary[node_status][iteration] += 1

            if iteration not in status_summary["TOTAL"]:
                status_summary["TOTAL"][iteration] = 1
            else:
                status_summary["TOTAL"][iteration] += 1

        status_complete = job_complete*pastro_ready
        if status_complete:
            print("\nstatus COMPLETE")
            with open(
                os.path.join(output_dir, "status_complete.txt"), "w"
            ) as f:
                f.write("COMPLETE")

        additional_data = {
            "run_dir": run_dir,
            "event_id": event_id,
            "status_complete": status_complete,
            "pastro_ready": (
                "p_astro ready" if pastro_ready else "p_astro not ready"
            ),
            "job_complete": (
                "Job Complete" if job_complete else "Job Not Complete"
            ),
        }

        # Load the template from the file
        file_loader = FileSystemLoader(DEFAULT_TEMPLATE_DIR)
        env = Environment(loader=file_loader)
        template = env.get_template("status.jinja2")
        template_vars = {
            "status": status_dict,
            "status_summary": status_summary,
            "additional_data": additional_data,
        }
        with open(status_html, "w") as output:
            output.write(template.render(**template_vars))
        try:
            shutil.copy(status_html, web_dir)
        except shutil.SameFileError:
            pass
        shutil.copy(
            os.path.join(DEFAULT_TEMPLATE_DIR, "status_style.css"), web_dir
        )
        shutil.copy(
            os.path.join(DEFAULT_TEMPLATE_DIR, "status_style.js"), web_dir
        )

        time.sleep(opts.sleep)


if __name__ == "__main__":
    main()
