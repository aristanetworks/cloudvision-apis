# Copyright (c) 2021 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the COPYING file.

import json
import requests
from json import JSONDecoder, JSONDecodeError
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from pprint import pprint as pp

with open("token.tok") as f:
    token = f.read().strip('\n')

cvp_url = "https://10.83.13.33"

def json_decoder(data):
    decoder = JSONDecoder()
    pos = 0
    result = []
    while True:
        try:
            o, pos = decoder.raw_decode(data, pos)
            result.append(o)
            pos +=1
        except JSONDecodeError:
            break
    return result

def get_events_all():
    event_url = '/api/resources/event/v1/Event/all'
    url = cvp_url + event_url
    head = {'Authorization': 'Bearer {}'.format(token)}
    response = requests.get(url, headers=head, verify=False)
    print(response.text)

def get_event(key, ts):
    event_url = '/api/resources/event/v1/Event?'
    url = cvp_url + event_url + 'key.key=' + key + "&key.timestamp=" + ts
    head = {'Authorization': 'Bearer {}'.format(token)}
    response = requests.get(url, headers=head, verify=False)
    print(response.text)

def get_events_t1_t2(t1, t2):
    event_url = '/api/resources/event/v1/Event/all?'
    url = cvp_url + event_url + 'time.start=' + t1 + "&time.end=" + t2
    head = {'Authorization': 'Bearer {}'.format(token)}
    response = requests.get(url, headers=head, verify=False)
    print(response.text)

def get_events_by_severity(severity):
    payload = {"partialEqFilter": [{"severity": severity }]}
    event_url = '/api/resources/event/v1/Event/all'
    url = cvp_url + event_url
    head = {'Authorization': 'Bearer {}'.format(token)}
    response = requests.post(url, headers=head, data=json.dumps(payload), verify=False)
    print(response.text)

def get_events_by_type(etype):
    payload = {"partialEqFilter": [{"eventType": etype }]}
    event_url = '/api/resources/event/v1/Event/all'
    url = cvp_url + event_url
    head = {'Authorization': 'Bearer {}'.format(token)}
    response = requests.post(url, headers=head, data=json.dumps(payload), verify=False)
    print(response.text)

def get_active_devices():
    dev_url = '/api/resources/inventory/v1/Device/all'
    url = cvp_url + dev_url
    head = {'Authorization': 'Bearer {}'.format(token)}
    response = requests.get(url, headers=head, verify=False)
    devices_data = json_decoder(response.text)
    devices = []
    for device in devices_data:
        try:
            if device['result']['value']['streamingStatus'] == "STREAMING_STATUS_ACTIVE":
                devices.append(device['result']['value']['hostname'])
        # pass on archived datasets
        except KeyError as e:
            continue
    return devices

### Uncomment the below functions/print statement to test

# ### Get all active events
# get_events_all()

# ### Get a specific event
# get_event("bf931ff01f5c5a2","2021-04-01T18:14:53Z")

# ### Get events between two dates
# get_events_t1_t2("2021-03-24T09:00:00Z", "2021-03-24T10:00:00Z")

# ### Get all INFO severity events ###
# get_events_by_severity("EVENT_SEVERITY_INFO")

# ### Get all WARNING severity events ###
# get_events_by_severity(2)

# ### Get all Low Disk Space events
# get_events_by_type("LOW_DEVICE_DISK_SPACE")
# print(get_active_devices())
