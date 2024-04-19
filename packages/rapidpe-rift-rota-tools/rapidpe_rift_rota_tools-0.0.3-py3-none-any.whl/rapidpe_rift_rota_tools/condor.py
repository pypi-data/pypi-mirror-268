import re


def parse_log_file_name(log_file):
    pattern = r"(integrate-)(\d+)(-MASS_SET_)(\d+)(-)(\d+)(-\d+\.log)"
    match = re.search(pattern, log_file)
    iteration = match.group(2)
    mass_point_id = match.group(4)
    process_id = match.group(6)
    return iteration, mass_point_id, process_id


status_dict = {
    "000": "Job submitted",
    "001": "Job executing",
    "005": "Job terminated",
    "009": "Job aborted",
    "010": "Job was suspended",
    "012": "Job was held",
    "013": "Job was released",
}


def get_latest_status(condor_status_id, condor_line_id):
    status_found = False
    status_keys = status_dict.keys()
    latest_status = None
    status_line = None
    i = len(condor_status_id) - 1
    while status_found is False and i >= 0:
        if condor_status_id[i] in status_keys:
            status_found = True
            latest_status = condor_status_id[i]
            status_line = condor_line_id[i]
        if status_found:
            break
        else:
            i -= 1
    return latest_status, status_line


def get_condor_status(log_file):
    _, _, process_id = parse_log_file_name(log_file)
    with open(log_file, "r") as f:
        lines = f.readlines()
    pattern = "(^\d{3})(.\(" + process_id + ".\d{3}.\d{3}\).)"
    condor_status_id = []
    condor_line_id = []
    for i, line in enumerate(lines):
        match = re.match(pattern, line)
        if match:
            condor_status_id.append(match.group(1))
            condor_line_id.append(i)
    latest_status, status_line = get_latest_status(
        condor_status_id, condor_line_id
    )
    if latest_status in ["005","009", "010", "012"]:
        detailed_condor_message = lines[status_line + 1].strip()
        if latest_status == "005":
            for l_i in range(status_line, len(lines)):
                if "Job terminated of its own accord" in lines[l_i]:
                    detailed_condor_message += f": {lines[l_i]}"
    else:
        detailed_condor_message = ""
    if latest_status is not None:
        condor_status_message = status_dict[latest_status]
    else:
        condor_status_message = ""
    return latest_status, detailed_condor_message, condor_status_message
