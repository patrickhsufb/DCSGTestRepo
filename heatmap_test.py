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

import datetime
import logging
import os
import sys
import uuid

sys.path.append("../../../")
from ctf.common import constants as common_constants
from ctf.ctf_client.lib.helper_functions import (
    create_test_run_result,
    save_test_action_result,
    save_test_run_outcome,
    set_test_setup_and_devices_free,
    tg_add_test_action_heatmap,
)

TEAM_ID = 1
TEST_SETUP_ID = os.environ.get(common_constants.CTF_CLIENT_TEST_SETUP_ID, 1)
DEV_ID = 1


log = logging.getLogger(__name__)
out_hdlr = logging.StreamHandler(sys.stdout)
out_hdlr.setFormatter(logging.Formatter("%(message)s"))
out_hdlr.setLevel(logging.INFO)
log.addHandler(out_hdlr)
log.setLevel(logging.INFO)


result = create_test_run_result(
    name="Sample Heatmap Test",
    identifier=str(uuid.uuid4),
    description="Get date",
    team_id=TEAM_ID,
    test_setup=TEST_SETUP_ID,
)
test_exe_details = result["data"]
test_exe_id = test_exe_details["id"]

save_test_action_result(
    test_run_id=test_exe_id,
    description="Some Generic Action with no heatmap",
    outcome=0,
    logs="This action is to demonstrate a generic action where heatmap is not saved",
    start_time=datetime.datetime.now(),
    end_time=datetime.datetime.now(),
)

heatmap_action_res = save_test_action_result(
    test_run_id=test_exe_id,
    description="Heatmap Action",
    outcome=0,
    logs="This action is to demonstrate the association of heatmap data files with an action",
    start_time=datetime.datetime.now(),
    end_time=datetime.datetime.now(),
)

tg_add_test_action_heatmap(
    test_exe_id=test_exe_id,
    test_action_result_id=heatmap_action_res["data"]["test_action_result_id"],
    initiator_file_path="/Users/patrickhsu/Downloads/DUT-2_2_full_fw_stat.txt",
    responder_file_path="/Users/patrickhsu/Downloads/DUT-1_1_full_fw_stat.txt",
    description="Association from DUT1 to DUT2",
)

tg_add_test_action_heatmap(
    test_exe_id=test_exe_id,
    test_action_result_id=heatmap_action_res["data"]["test_action_result_id"],
    initiator_file_path="/Users/patrickhsu/Downloads/DUT-3_3_full_fw_stat.txt",
    responder_file_path="/Users/patrickhsu/Downloads/DUT-1_1_full_fw_stat.txt",
    description="Association from DUT1 to DUT3",
)

test_outcome = save_test_run_outcome(test_exe_id)

set_test_setup_and_devices_free(TEST_SETUP_ID)
