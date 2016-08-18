#!/bin/sh

# --time_format, --earliest_time, and --latest_time are added by search2.py
# search_interval.py calls search.py with the extra above params
# search.py has been modified to remove the csv header, and the extra newline at the end of each interval

python splunk2csv.py "search sourcetype=snort | convert timeformat=\"%b %d %H:%M:%S\" ctime(_time) AS c_time | table c_time, sourcetype, generator_id, signature, signature_rev, name, classification, priority, proto, src_ip, src_port, dest_ip, dest_port | sort time" --output_mode="csv" > /var/log/splunk2csv.log

