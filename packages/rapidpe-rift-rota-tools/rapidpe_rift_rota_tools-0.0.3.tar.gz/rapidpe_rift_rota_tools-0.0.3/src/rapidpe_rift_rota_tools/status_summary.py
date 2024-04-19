import os
import pathlib
from glob import glob

from rapidpe_rift_rota_tools import condor
from rapidpe_rift_rota_tools import results


def get_node_status(result_status, condor_status_id):
    node_status = ""
    if result_status == "Ready":
        node_status = "SUCCESS"
    else:
        if condor_status_id == "000":
            node_status = "IDLE"
        elif condor_status_id in ["001", "013"]:
            node_status = "RUN"
        elif condor_status_id in ["005", "009", "010"]:
            node_status = "FAIL"
        elif condor_status_id == "012":
            node_status = "HOLD"
    return node_status


def get_results_status(run_dir, data_dict={}):
    list_of_log_files = glob(os.path.join(run_dir, "logs", "integrate*.log"))
    for f in list_of_log_files:
        iteration_level, mass_point_id, process_id = (
            condor.parse_log_file_name(f)
        )
        unique_id = f"{iteration_level}-{mass_point_id}"
        new_file = unique_id not in data_dict
        if new_file:
            data_dict[unique_id] = {}
            data_dict[unique_id]["iteration_level"] = iteration_level
            data_dict[unique_id]["mass_point_id"] = mass_point_id
            data_dict[unique_id]["process_id"] = process_id
            result_f_name = (
                f"ILE_iteration_{iteration_level}-"
                f"MASS_SET_{mass_point_id}-{process_id}-0..xml.gz_0_.xml.gz"
            )
            result_f_name_full = os.path.join(
                run_dir, f"results/{result_f_name}"
            )
            data_dict[unique_id]["result_file"] = result_f_name
            result_status = results.check_result_ready(result_f_name_full)
            data_dict[unique_id]["result_status"] = result_status
        else:
            result_f_name = data_dict[unique_id]["result_file"]
            result_f_name_full = os.path.join(
                run_dir, f"results/{result_f_name}"
            )
            if data_dict[unique_id]["result_status"] == "Not Ready":
                result_status = results.check_result_ready(result_f_name_full)
                data_dict[unique_id]["result_status"] = result_status
        is_complete = data_dict[unique_id]["result_status"] == "Ready"
        if is_complete and "margll" not in data_dict[unique_id]:
            margll = results.get_margll_from_result_file(result_f_name_full)
            data_dict[unique_id]["margll"] = margll
        condor_status_id, detailed_condor_message, condor_status = (
            condor.get_condor_status(f)
        )
        data_dict[unique_id]["condor_status"] = condor_status
        data_dict[unique_id]["condor_status_id"] = condor_status_id
        data_dict[unique_id]["note"] = detailed_condor_message

        data_dict[unique_id]["node_status"] = get_node_status(
            data_dict[unique_id]["result_status"], condor_status_id
        )

    return data_dict
