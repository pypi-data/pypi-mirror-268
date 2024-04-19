from ligo.lw import utils, lsctables, ligolw
import os


def get_margll_from_result_file(result_file):
    xmldoc = utils.load_filename(
        result_file, contenthandler=ligolw.LIGOLWContentHandler
    )
    new_tbl = lsctables.SnglInspiralTable.get_table(xmldoc)
    row = new_tbl[0]
    margll = row.snr
    return margll


def check_result_ready(result_f_name_full):
    run_complete = os.path.exists(result_f_name_full)
    status = "Ready" if run_complete else "Not Ready"
    return status
