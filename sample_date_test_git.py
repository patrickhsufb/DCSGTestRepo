#!/usr/bin/env python3
from __future__ import absolute_import, division, print_function, unicode_literals

"""
Copyright (c) Facebook, Inc. and its affiliates.
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.
"""

"""
    isort:skip_file
"""

import atexit
import datetime
import json
import logging
import os
import sys
import uuid

sys.path.append("../../../")
from ctf.common import constants as common_constants
from ctf.ctf_client.lib.helper_functions import (
    check_if_test_setup_is_free,
    create_test_run_result,
    get_test_setup_devices_and_connections,
    save_test_action_result,
    save_test_action_result_json_data,
    save_test_run_outcome,
    set_test_setup_and_devices_busy,
    set_test_setup_and_devices_free,
)

# In order to run this test on your local machine
# create a python virtual environment: python3 -m venv ctf_client_env
# activate virtual env:  source ./ctf_client_env/bin/activate
# install required packages (run this command within the common and ctf_client dir): pip install -r requirements.txt
# run test: python sample_date_test.py


# Please changes these to match the team, test setup
# and device id for your setup
TEAM_ID = 1
TEST_SETUP_ID = 3
DEV_ID = 1

log = logging.getLogger(__name__)
out_hdlr = logging.StreamHandler(sys.stdout)
out_hdlr.setFormatter(logging.Formatter("%(message)s"))
out_hdlr.setLevel(logging.INFO)
log.addHandler(out_hdlr)
log.setLevel(logging.INFO)


def free_test_setup_clean_up() -> None:
    log.info("\n------------free_test_setup_clean_up-------------")
    set_test_setup_and_devices_free(TEST_SETUP_ID)


def sample_test() -> None:
    log.info("\n------------sample_test-------------")
    if check_if_test_setup_is_free(TEST_SETUP_ID) and set_test_setup_and_devices_busy(
        TEST_SETUP_ID
    ):
        atexit.register(free_test_setup_clean_up)
        device_info = get_test_setup_devices_and_connections(TEST_SETUP_ID)
        if device_info:
            result = create_test_run_result(
                name="Sample Date Test",
                identifier=str(uuid.uuid4),
                description="Get date",
                team_id=TEAM_ID,
                test_setup=TEST_SETUP_ID,
            )
            if result["data"]:
                test_exe_details = result["data"]
                test_exe_id = test_exe_details["id"]

                date_action_outcome = 1
                start = datetime.datetime.now()
                output = device_info[DEV_ID].connection.send_command(
                    cmd="date +%F", timeout=60
                )

                if str(datetime.date.today()) in output["message"]:
                    date_action_outcome = 0
                else:
                    log.error(
                        f"date action failed, date on device: {output['message']} date on system: {str(datetime.date.today())}"
                    )

                date_test_action_result = save_test_action_result(
                    test_run_id=test_exe_id,
                    description="Date",
                    outcome=date_action_outcome,
                    logs=" ".join(map(str, output["message"])),
                    start_time=start,
                    end_time=datetime.datetime.now(),
                )

                log.info(date_test_action_result["message"])

                data_list1 = [
                    {
                        "Interval": 0,
                        "Transfer Mbytes": 121,
                        "Bandwidth Mbits/sec": 1014,
                        "Jitter ms": 0.059,
                    },
                    {
                        "Interval": 1,
                        "Transfer Mbytes": 121,
                        "Bandwidth Mbits/sec": 1013,
                        "Jitter ms": 0.058,
                    },
                ]
                data_source1_name = "iperf data 1"

                data_list2 = [
                    {
                        "Interval": 0,
                        "Transfer Mbytes": 108,
                        "Bandwidth Mbits/sec": 909,
                        "Jitter ms": 0.061,
                    },
                    {
                        "Interval": 1,
                        "Transfer Mbytes": 103,
                        "Bandwidth Mbits/sec": 861,
                        "Jitter ms": 0.070,
                    },
                ]
                data_source2_name = "iperf data 2"

                json_data1 = {
                    "data_source": data_source1_name,
                    "data_list": data_list1,
                }
                json_data2 = {
                    "data_source": data_source2_name,
                    "data_list": data_list2,
                }

                json_table1 = {
                    "title": "Demo Iperf Table Small",
                    "table_type": "static",
                    "columns": "Interval,Bandwidth Mbits/sec",
                    "data_source_list": data_source1_name + "," + data_source2_name,
                }

                json_table2 = {
                    "title": "Demo Iperf Table Full",
                    "data_source_list": data_source1_name + "," + data_source2_name,
                }

                x_axis1 = {
                    "key": "Interval",
                    "options": {
                        "label": "Interval ms",
                        "type": "linear",
                        "position": "bottom",
                    },
                }
                y_axis1 = {
                    "series_list": [
                        {
                            "data_source": data_source1_name,
                            "key": "Bandwidth Mbits/sec",
                            "label": "TestData_iperflink1",
                        },
                        {
                            "data_source": data_source2_name,
                            "key": "Bandwidth Mbits/sec",
                            "label": "TestData_iperflink2",
                        },
                    ],
                    "options": {"label": "Bandwidth Mbits/sec", "fill": "false"},
                }
                chart_options = {"display_type": "line", "tension": "true"}
                json_chart = {
                    "title": "Iperf Chart",
                    "axes": {
                        "x_axis1": x_axis1,
                        "y_axis1": y_axis1,
                    },
                    "chart_type": "static",
                    "options": chart_options,
                }

                ctf_json_data_all = {
                    "ctf_data": [json_data1, json_data2],
                    "ctf_tables": [json_table1, json_table2],
                    "ctf_charts": [json_chart],
                }

                save_test_action_result_json_data(
                    test_action_result_id=date_test_action_result["data"][
                        "test_action_result_id"
                    ],
                    ctf_json_data_all=json.dumps(ctf_json_data_all),
                )

                test_outcome = save_test_run_outcome(test_exe_id)
                log.info(test_outcome["message"])
            else:
                log.error("Unable to create test run result")
        else:
            log.error("Unable to find device")
    else:
        log.error("Unable to reserve test setup")
    set_test_setup_and_devices_free(TEST_SETUP_ID)


if __name__ == "__main__":
    sample_test()
