# Copyright (c) 2021 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the COPYING file.

from cvprac.cvp_client import CvpClient
from pprint import pprint as pp
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

# Reading the service account token from a file
with open("token.tok") as f:
    token = f.read().strip('\n')

clnt = CvpClient()
clnt.connect(nodes=['192.0.2.100'], username='',password='',api_token=token)

def get_events_all(client):
    ''' Get All events '''
    event_url = '/api/resources/event/v1/Event/all'
    response = client.get(event_url)
    return response['data']

def get_event(client, key, ts):
    event_url = '/api/resources/event/v1/Event?'
    url = event_url + 'key.key=' + key + "&key.timestamp=" + ts
    response = client.get(url)
    return response

def get_events_t1_t2(client, t1, t2):
    event_url = '/api/resources/event/v1/Event/all?'
    url = event_url + 'time.start=' + t1 + "&time.end=" + t2
    response = client.get(url)
    return response['data']

def get_events_by_severity(client, severity):
    payload = {"partialEqFilter": [{"severity": severity }]}
    event_url = '/api/resources/event/v1/Event/all'
    response = client.post(event_url, data=payload)
    if 'data' in response.keys():
        return response['data']
    else:
        return response

def get_events_by_type(client, etype):
    payload = {"partialEqFilter": [{"eventType": etype }]}
    event_url = '/api/resources/event/v1/Event/all'
    response = client.post(event_url, data=payload)
    if 'data' in response.keys():
        return response['data']
    else:
        return response

def get_active_devices(client):
    ''' Get active devices '''
    dev_url = '/api/resources/inventory/v1/Device/all'
    devices_data = client.get(dev_url)
    devices = []
    for device in devices_data['data']:
        try:
            if device['result']['value']['streamingStatus'] == "STREAMING_STATUS_ACTIVE":
                devices.append(device['result']['value']['hostname'])
        # pass on archived datasets
        except KeyError as e:
            continue
    return devices

### Uncomment the below functions/print statement to test

# ### Get all active events
# print ('=== All active events ===')
# cvpevents = get_events_all(clnt)
# for event in cvpevents:
#     print(event)

# ### Get a specific event
# key = "6098ae39e4c8a9d7"
# ts ="2021-04-06T21:53:00Z"
# get_event(clnt, key, ts)

# ### Get events between two dates
# t1 = "2021-04-06T09:00:00Z"
# t2 = "2021-04-06T14:00:00Z"
# events = get_events_t1_t2(clnt, t1, t2)
# print(f"=== Events between {t1} and {t2} ===")
# pp(events)

# ### Get all INFO severity events ###
# # EVENT_SEVERITY_UNSPECIFIED = 0
# # EVENT_SEVERITY_INFO =	1
# # EVENT_SEVERITY_WARNING = 2
# # EVENT_SEVERITY_ERROR = 3
# # EVENT_SEVERITY_CRITICAL =	4
# ####################################

# severity = 1 ## Severity INFO
# info = get_events_by_severity(clnt, severity)
# print('=== Get all INFO severity events ===')
# pp(info)

# ### Get specific event types

# etype = "LOW_DEVICE_DISK_SPACE"
# event = get_events_by_type(clnt, etype)
# print('=== Get all Low Disk Space events ===')
# pp(event)

# ### Get the inventory
# print ('=== Inventory ===')
# print(get_active_devices(clnt))
