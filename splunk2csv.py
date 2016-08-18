#!/usr/bin/env python
#
# Copyright 2016 Savvius, Inc.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""A command line utility for executing Splunk searches for an interval of time."""

import sys, os, time
import search
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from time import sleep

from splunklib.binding import HTTPError
import splunklib.client as client

interval = 10
current_time = time.time() 
earliest_time = current_time - interval

while True:
    earliest_time_arg = "--earliest_time=\"" + time.strftime("%m/%d/%Y:%H:%M:%S", time.localtime(earliest_time )) + "\""
    latest_time_arg = "--latest_time=\"" + time.strftime("%m/%d/%Y:%H:%M:%S", time.localtime(current_time )) + "\""
    time_format_arg = "--time_format=\"" + "%m/%d/%Y:%H:%M:%S\"" 
    argv2 = sys.argv
    argv2.append(time_format_arg)
    argv2.append(earliest_time_arg)
    argv2.append(latest_time_arg)
    
    # call search
    search.main(argv2[1:])

    new_time = time.time()
    run_time = new_time - current_time
    this_interval = 0
    if (run_time < interval):
        this_interval = interval - run_time
    time.sleep( this_interval )
    earliest_time = current_time + 1 
    current_time = time.time()

