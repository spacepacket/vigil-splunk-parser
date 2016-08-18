# Vigil Splunk Parser
A Logstash based solution to pull and convert Splunk events into Savvius Vigil events 

These are the splunk listener files.


Logstash Universal Parser for Splunk (on Vigil machine)
--------------------------------------------------------

- csv2vigil.conf

These are logstash configuration files the Universal Vigil Parser. They go in /etc/logstash/conf.d

Logstash can be run on the command line against one or all of the .conf files in the directory

/opt/logstash/bin/logstash -f /etc/logstash/conf.d


Splunk Listener Files (on Vigil machine)
-----------------------------------------

- splunk2csv.sh
- splunk2csv.py
- search.py

The Splunk listener, which is really a puller, depends on the splunk python SDK being installed. The files listed go in the examples folder of the SDK.

Actually, search.py is one of the samples.

They also depend on a file called ~/.splunkrc which looks like this:

# Splunk host (default: localhost)
host=10.4.2.159
# Splunk admin port (default: 8089)
port=8089
# Splunk username
username=admin
# Splunk password
password=changeme
# Access scheme (default: https)
scheme=https
# Your version of Splunk (default: 5.0)
version=5.0

Also, allowremotelogin has to be enabled on the Splunk server in /opt/splunk/etc/system/defaults/server.conf

splunk2csv.sh -> splunk2csv.py -> search.py -> other python files from the SDK 

Splunk Server Files
-------------------

- splunk-for-snort_05.tgz

In order to get events from Splunk, the listener depends on having snort events going into Splunk in the Common Information Model (CIM) for IDS.  This is accomplished by having the splunk for snort app installed in the Splunk server.  The splunk for snort app takes the raw events coming from Splunk and extracts the fields into the Splunk Common Information Model (CIM) for IDS.

To install the snort app into the SplunkServer, put the app into /opt and run the followng command:

/opt/splunk/bin/splunk install app /opt/splunk-for-snort_05.tgz


Snort Server Files
------------------

- Splunk forwarder
- TA-snort.tar.gz

In order to get raw snort events into Splunk, there has to be a Splunk forwarder on the snort box, with the TA-snort app to monitor the alert file, and send new alerts to the Splunk Server.

To install the TA into the Splunk forwarder, put the TA into /opt and run the followng command:

/opt/splunkforwarder/bin/splunk install app /opt/TA-snort.tar.gz

To run snort, the following command is used with the "-A alert" option to create the /var/log/snort/alert file.

/usr/sbin/snort -m 027 -D -d -l /var/log/snort -u snort -g snort -c /etc/snort/snort.conf -S HOME_NET=[10.4.0.0/16] -i eth1 -A alert

Of course, HOME_NET and interface have to be set accordingly.



