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
"sample_date_test.py" 218L, 7568C                                                                                                                                                                                                           47,17         Top
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