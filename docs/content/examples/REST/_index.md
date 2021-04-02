---
title: REST API Examples
weight: 100
chapter: false
---

{{% toc %}}

{{% attachments title="Related files" style="blue" pattern=".*" /%}}

{{% notice tip %}}
[jq](https://stedolan.github.io/jq/) can be used to easily format and parse the outputs.
{{% /notice %}}



Events
================================

Get all active events
--------------------------------

### curl

```bash
curl -sS -kX GET --header 'Accept: application/json' 'https://10.83.13.33/api/resources/event/v1/Event/all' -b access_token=`cat token.tok`
```

### cvprac

```python
event_url = '/api/resources/event/v1/Event/all'
response = client.get(event_url)
```

### python requests

```python
def get_events_all():
    event_url = '/api/resources/event/v1/Event/all'
    url = cvp_url + event_url
    head = {'Authorization': 'Bearer {}'.format(token)}
    response = requests.get(url, headers=head, verify=False)
    print(response.text)

get_events_all()
```

Get a specific event
--------------------------------

### curl

```bash
curl -sS -kX GET --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://10.83.13.33/api/resources/event/v1/Event?key.key=6152f6160fc38f55&key.timestamp=2021-03-23T13:38:59.295341290Z'
```

Result:

```python
{
   "value":{
      "key":{
         "key":"6152f6160fc38f55",
         "timestamp":"2021-03-23T13:38:59.295341290Z"
      },
      "severity":"EVENT_SEVERITY_ERROR",
      "title":"Low Disk Volume Space Available",
      "description":"Detected low disk space on volume /mnt/flash, 93.46756% of space used",
      "eventType":"LOW_DEVICE_DISK_SPACE",
      "data":{
         "data":{
            "deviceId":"JPE15233329",
            "threshold":"90",
            "value":"93.46756",
            "volume":"/mnt/flash"
         }
      },
      "components":{
         "components":[
            {
               "type":"COMPONENT_TYPE_DEVICE",
               "components":{
                  "deviceId":"JPE15233329"
               }
            }
         ]
      }
   },
   "time":"2021-03-25T14:37:00Z"
}
```

{{% notice note %}}
The `time` key here shows the state of the resource at a given time,
`key.timestmap` is part of the key for that an event.
{{% /notice %}}

### cvprac

```python
event_url = '/api/resources/event/v1/Event?'
url = event_url + 'key.key=' + key + "&key.timestamp=" + ts
response = client.get(url)
```

### python requests

```python
def get_event(key, ts):
    event_url = '/api/resources/event/v1/Event?'
    url = cvp_url + event_url + 'key.key=' + key + "&key.timestamp=" + ts
    head = {'Authorization': 'Bearer {}'.format(token)}
    response = requests.get(url, headers=head, verify=False)
    print(response.text)

get_event("bf931ff01f5c5a2","2021-04-01T18:14:53Z")
```

Get events between two dates
--------------------------------

### curl

```bash
curl -sS -kX GET --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://10.83.13.33/api/resources/event/v1/Event/all?time.start=2021-03-24T09:00:00Z&time.end=2021-03-24T10:00:00Z'
```

Result:

```python
{
  "result": {
    "value": {
      "key": {
        "key": "6a5eea29e5599b0",
        "timestamp": "2021-02-04T23:19:22.809962243Z"
      },
      "severity": "EVENT_SEVERITY_WARNING",
      "title": "Interface went down unexpectedly",
      "description": "Interface Ethernet1 on JPE19332824 is no longer operationally active",
      "eventType": "DEVICE_INTF_ERR_SMART",
      "data": {
        "data": {
          "deviceId": "JPE19332824",
          "interfaceId": "Ethernet1"
        }
      },
      "components": {
        "components": [
          {
            "type": "COMPONENT_TYPE_INTERFACE",
            "components": {
              "deviceId": "JPE19332824",
              "interfaceId": "Ethernet1"
            }
          }
        ]
      }
    },
    "time": "2021-02-04T23:19:22.809962243Z",
    "type": "INITIAL"
  }
}
{
  "result": {
    "value": {
      "key": {
        "key": "6acbaa29e5b6002",
        "timestamp": "2021-02-04T23:19:22.819264873Z"
      },
      "severity": "EVENT_SEVERITY_WARNING",
      "title": "Interface went down unexpectedly",
      "description": "Interface Ethernet3 on JPE19332824 is no longer operationally active",
      "eventType": "DEVICE_INTF_ERR_SMART",
      "data": {
        "data": {
          "deviceId": "JPE19332824",
          "interfaceId": "Ethernet3"
        }
      },
      "components": {
        "components": [
          {
            "type": "COMPONENT_TYPE_INTERFACE",
            "components": {
              "deviceId": "JPE19332824",
              "interfaceId": "Ethernet3"
            }
          }
        ]
      }
    }
```

### cvprac

```python
event_url = '/api/resources/event/v1/Event/all?'
url = event_url + 'time.start=' + t1 + "&time.end=" + t2
response = client.get(url)
```

### python requests

```python
def get_events_t1_t2(t1, t2):
    event_url = '/api/resources/event/v1/Event/all?'
    url = cvp_url + event_url + 'time.start=' + t1 + "&time.end=" + t2
    head = {'Authorization': 'Bearer {}'.format(token)}
    response = requests.get(url, headers=head, verify=False)
    print(response.text)

get_events_t1_t2("2021-03-24T09:00:00Z", "2021-03-24T10:00:00Z")
```

Get all INFO severity events
--------------------------------

{{% notice note %}}
To apply filters on events, the POST method has to be used.
{{% /notice %}}

### curl

```bash
curl -sS -kX POST --header 'Accept: application/json' -b access_token=`cat token.tok` -d '{"partialEqFilter": [{"severity": 1}]}' 'https://10.83.13.33/api/resources/event/v1/Event/all'
```

Result:

```python
{
  "result": {
    "value": {
      "key": {
        "key": "571d021ba26bbb96",
        "timestamp": "2020-12-11T10:35:00Z"
      },
      "severity": "EVENT_SEVERITY_INFO",
      "title": "High PTP skew",
      "description": "Detected high PTP skew (0)",
      "eventType": "HIGH_PTP_SKEW",
      "data": {
        "data": {
          "deviceId": "JPE15233329",
          "discovered": "true",
          "threshold": "0.9",
          "value": "0"
        }
      },
      "components": {
        "components": [
          {
            "components": {
              "deviceId": "JPE15233329"
            }
          }
        ]
      }
    },
    "time": "2020-12-11T10:35:00Z",
    "type": "INITIAL"
  }
}
```

```bash
curl -sS -kX POST --header 'Accept: application/json' -b access_token=`cat token.tok` -d '{"partialEqFilter": [{"severity": "EVENT_SEVERITY_INFO"}]}' 'https://10.83.13.33/api/resources/event/v1/Event/all'
```

```bash
curl -sS -kX POST --header 'Accept: application/json' -b access_token=`cat token.tok` -d '{"partial_eq_filter": [{"severity": 1}]}' 'https://10.83.13.33/api/resources/event/v1/Event/all'
```

### cvprac

```python
severity = 1 ## Severity INFO
payload = {"partialEqFilter": [{"severity": severity }]}
event_url = '/api/resources/event/v1/Event/all'
response = client.post(event_url, data=payload)
```

### python requests

```python
def get_events_by_severity(severity):
    payload = {"partialEqFilter": [{"severity": severity }]}
    event_url = '/api/resources/event/v1/Event/all'
    url = cvp_url + event_url
    head = {'Authorization': 'Bearer {}'.format(token)}
    response = requests.post(url, headers=head, data=json.dumps(payload), verify=False)
    print(response.text)

# Get with string value
get_events_by_severity("EVENT_SEVERITY_INFO")

# Get with enum value
get_events_by_severity(1)
```

Get specific event types
--------------------------------

### curl

```bash
curl -sS -kX POST --header 'Accept: application/json' -b access_token=`cat token.tok` -d '{"partialEqFilter": [{"eventType":"LOW_DEVICE_DISK_SPACE"}]}' 'https://10.83.13.33/api/resources/event/v1/Event/all'
```

Result:

```python
{
  "result": {
    "value": {
      "key": {
        "key": "6152f6160fc38f55",
        "timestamp": "2021-03-23T13:38:59.295341290Z"
      },
      "severity": "EVENT_SEVERITY_ERROR",
      "title": "Low Disk Volume Space Available",
      "description": "Detected low disk space on volume /mnt/flash, 93.46756% of space used",
      "eventType": "LOW_DEVICE_DISK_SPACE",
      "data": {
        "data": {
          "deviceId": "JPE15233329",
          "threshold": "90",
          "value": "93.46756",
          "volume": "/mnt/flash"
        }
      },
      "components": {
        "components": [
          {
            "type": "COMPONENT_TYPE_DEVICE",
            "components": {
              "deviceId": "JPE15233329"
            }
          }
        ]
      }
    },
    "time": "2021-03-23T13:38:59.295341290Z",
    "type": "INITIAL"
  }
}
```

### cvprac

```python
etype = "LOW_DEVICE_DISK_SPACE"
payload = {"partialEqFilter": [{"eventType": etype }]}
get_events_by_type = clnt.post(event_url, data=payload)
print(get_events_by_type)
```

### python requests

```python
def get_events_by_type(etype):
    payload = {"partialEqFilter": [{"eventType": etype }]}
    event_url = '/api/resources/event/v1/Event/all'
    url = cvp_url + event_url
    head = {'Authorization': 'Bearer {}'.format(token)}
    response = requests.post(url, headers=head, data=json.dumps(payload), verify=False)
    print(response.text)

get_events_by_type("LOW_DEVICE_DISK_SPACE")
```

Get all Low device disk space events with ERROR severity
--------------------------------

The `Low Disk Volume Space Available` events have two default rules (custom rules can be added):
- generate a WARNING event if a partition on EOS goes above 80%
- generate an ERROR event if a partition on EOS goes above 90%

To get only the ERROR events we can add the `severity` key to our filter.

### curl

```bash
curl -sS -kX POST --header 'Accept: application/json' -b access_token=`cat token.tok` -d '{"partialEqFilter": [{"eventType":"LOW_DEVICE_DISK_SPACE","severity":"EVENT_SEVERITY_ERROR"}]}' 'https://10.83.13.33/api/resources/event/v1/Event/all'
```

Result:

```python
{
  "result": {
    "value": {
      "key": {
        "key": "6152f6160fc38f55",
        "timestamp": "2021-04-06T19:39:29.307757986Z"
      },
      "severity": "EVENT_SEVERITY_ERROR",
      "title": "Low Disk Volume Space Available",
      "description": "Detected low disk space on volume /mnt/flash, 93.46767% of space used",
      "eventType": "LOW_DEVICE_DISK_SPACE",
      "data": {
        "data": {
          "deviceId": "JPE15233329",
          "threshold": "90",
          "value": "93.46767",
          "volume": "/mnt/flash"
        }
      },
      "components": {
        "components": [
          {
            "type": "COMPONENT_TYPE_DEVICE",
            "components": {
              "deviceId": "JPE15233329"
            }
          }
        ]
      }
    },
    "time": "2021-04-06T19:39:29.307757986Z",
    "type": "INITIAL"
  }
}
```

{{% notice note %}}
If the `partialEqFilter` would've had two dictionaries inside the list, e.g.:
`[{"eventType":"LOW_DEVICE_DISK_SPACE"},{"severity":"EVENT_SEVERITY_ERROR"}]}'` the filtering
would've used an OR operation instead of AND, meaning that all events that have
`eventType`=`"LOW_DEVICE_DISK_SPACE"` and all events that have ERROR severity would've been printed.
{{% /notice %}}

Device
================================================

## Get all devices from inventory

### curl

```bash
curl -sS -kX GET --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://10.83.13.33/api/resources/inventory/v1/Device/all' | jq '.result.value | with_entries(select(.[])) | select(.streamingStatus=="STREAMING_STATUS_ACTIVE") | .hostname'
"cd263"
"sn413"
"fm422"
"sn503"
"psp301"
"wl504"
"cloudEOS1"
```

### cvprac

```python
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

print(get_active_devices(clnt))
```

### python requests

```python
from json import JSONDecoder, JSONDecodeError

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

print(get_active_devices())
```

##### Sample output

```bash
python3 resource_native.py
['cd263', 'sn413', 'fm422', 'sn503', 'psp301', 'wl504', 'cloudEOS1']
```

Tags
================================

Get all device tags
--------------------------------

### curl

```bash
curl -sS -kX GET --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://10.83.13.33/api/resources/tag/v1/DeviceTag/all' | jq '.result.value.key | .label + " " + .value'
```

Result:

```bash
<snippet>
topology_datacenter Shannon"
"topology_datacenter vDC1R"
"topology_hint_pod Vantage"
"topology_hint_pod vPod1R"
"topology_hint_pod vPod3R"
"topology_hint_pod tac-ire-pod1"
"topology_hint_pod tac-ire-pod3"
"topology_hint_pod tac-ire-pod2"
"topology_hint_rack Rack17"
"topology_hint_rack Rack15"
"topology_hint_rack Rack27"
"topology_hint_rack vRack2R"
"topology_hint_rack vRack1R"
"topology_hint_rack vRack4R"
"topology_hint_rack vRack3R"
"topology_hint_type edge"
"topology_hint_type leaf"
"topology_hint_type spine"
"topology_hint_type server"
"topology_hint_type endpoint"
"topology_hint_type management"
"topology_hint_datacenter vDC1R"
"topology_hint_datacenter Shannon"
<snippet>
```

### cvprac

```python
def get_all_device_tags(client):
    tag_url = '/api/resources/tag/v1/DeviceTag/all'
    tag_data = client.get(tag_url)
    tags = []
    for tag in tag_data['data']:
        tags.append({tag['result']['value']['key']['label']:tag['result']['value']['key']['value']})
    return tags

for tag in get_all_device_tags(clnt):
    print (tag)
```

### python requests

```python
def get_all_device_tags():
    tag_url = '/api/resources/tag/v1/DeviceTag/all'
    url = cvp_url + tag_url
    head = {'Authorization': 'Bearer {}'.format(token)}
    response = requests.get(url, headers=head, verify=False)
    tag_data = json_decoder(response.text)
    tags = []
    for tag in tag_data:
        tags.append({tag['result']['value']['key']['label']:tag['result']['value']['key']['value']})
    return tags

pp(get_all_device_tags())
```

Get all assigned interface tags
--------------------------------

### curl

```bash
 curl -sS -kX GET --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://10.83.13.33/api/resources/tag/v1/InterfaceTagAssignmentConfig/all'
 ```

### cvprac

```python
def get_all_interface_tags(client):
    tag_url = '/api/resources/tag/v1/InterfaceTagAssignmentConfig/all'
    tags = client.get(tag_url)
    return tags['data']

print(get_all_interface_tags(clnt))
```

### python requests

```python
def get_all_interface_tags():
    tag_url = '/api/resources/tag/v1/InterfaceTagAssignmentConfig/all'
    url = cvp_url + tag_url
    head = {'Authorization': 'Bearer {}'.format(token)}
    response = requests.get(url, headers=head, verify=False)
    tags = json_decoder(response.text)
    return tags

pp(get_all_interface_tags())
```

Get all tags for a device
--------------------------------

### curl

```bash
curl -sS -kX POST --header 'Accept: application/json' -b access_token=`cat token.tok` -d '{"partialEqFilter": [{"key":{"deviceId": "JPE14070534"}}]}' 'https://10.83.13.33/api/resources/tag/v1/InterfaceTagAssignmentConfig/all'
 ```

Result:

```python
{
   "result":{
      "value":{
         "key":{
            "label":"speed",
            "value":"speed1Gbps",
            "deviceId":"JPE14070534",
            "interfaceId":"Ethernet1"
         }
      },
      "time":"2021-03-30T18:33:18.639842067Z",
      "type":"INITIAL"
   }
}
{
   "result":{
      "value":{
         "key":{
            "label":"name",
            "value":"Ethernet1",
            "deviceId":"JPE14070534",
            "interfaceId":"Ethernet1"
         }
      },
      "time":"2021-03-27T00:38:41.945746826Z",
      "type":"INITIAL"
   }
}
{
   "result":{
      "value":{
         "key":{
            "label":"speed",
            "value":"speed10Gbps",
            "deviceId":"JPE14070534",
            "interfaceId":"Ethernet2"
         }
      },
      "time":"2021-03-27T00:38:41.906241108Z",
      "type":"INITIAL"
   }
}
{
   "result":{
      "value":{
         "key":{
            "label":"name",
            "value":"Ethernet2",
            "deviceId":"JPE14070534",
            "interfaceId":"Ethernet2"
         }
      },
      "time":"2021-03-27T00:38:41.906241108Z",
      "type":"INITIAL"
   }
}
```

Using `jq` to only print the list of 40Gbps interfaces:

```bash
curl -sS -kX POST --header 'Accept: application/json' -b access_token=`cat token.tok` -d '{"partialEqFilter": [{"key":{"deviceId": "JPE14070534", "value":"speed40Gbps" }}]}' 'https://10.83.13.33/api/resources/tag/v1/InterfaceTagAssignmentConfig/all' | jq '.result.value.key.interfaceId'
"Ethernet97"
"Ethernet98"
"Ethernet99"
"Ethernet100"
"Ethernet101"
"Ethernet102"
"Ethernet103"
"Ethernet104"
```

### cvprac

```python
def filter_interface_tag(client, dId=None, ifId=None, label=None, value=None):
    tag_url = '/api/resources/tag/v1/InterfaceTagAssignmentConfig/all'
    payload = {
                "partialEqFilter": [
                    {"key": {"deviceId": dId, "interfaceId": ifId, "label": label, "value": value}}
                ]
            }
    response = client.post(tag_url, data=payload)
    return response

print(filter_interface_tag(clnt, dId="JPE14070534", value="speed40Gbps"))
```

### python requests

```python
def filter_interface_tag(dId=None, ifId=None, label=None, value=None):
    tag_url = '/api/resources/tag/v1/InterfaceTagAssignmentConfig/all'
    payload = {
                "partialEqFilter": [
                    {"key": {"deviceId": dId, "interfaceId": ifId, "label": label, "value": value}}
                ]
            }
    url = cvp_url + tag_url
    head = {'Authorization': 'Bearer {}'.format(token)}
    response = requests.post(url, headers=head, data=json.dumps(payload), verify=False)
    return response.text

print(filter_interface_tag(dId="JPE14070534", value="speed40Gbps"))
```

Get all tags for an interface of a device
------------------------------------------

### curl

```bash
curl -sS -kX POST --header 'Accept: application/json' -b access_token=`cat token.tok` -d '{"partialEqFilter": [{"key":{"deviceId": "JPE14070534", "interfaceId": "Ethernet1"}}]}' 'https://10.83.13.33/api/resources/tag/v1/InterfaceTagAssignmentConfig/all'
```

Result:

```python
{
  "result": {
    "value": {
      "key": {
        "label": "name",
        "value": "Ethernet1",
        "deviceId": "JPE14070534",
        "interfaceId": "Ethernet1"
      }
    },
    "time": "2021-03-27T00:38:41.945746826Z",
    "type": "INITIAL"
  }
}
{
  "result": {
    "value": {
      "key": {
        "label": "speed",
        "value": "speed1Gbps",
        "deviceId": "JPE14070534",
        "interfaceId": "Ethernet1"
      }
    },
    "time": "2021-03-30T18:33:18.639842067Z",
    "type": "INITIAL"
  }
}
```

### cvprac

```python
print(filter_interface_tag(clnt, dId="JPE14070534", ifId="Ethernet1"))
```

### python requests

```python
print(filter_interface_tag(dId="JPE14070534", ifId="Ethernet1"))
```

Get all interfaces that have a specific tag assigned
-----------------------------------------------------

### curl

```bash
curl -sS -kX POST --header 'Accept: application/json' -b access_token=`cat token.tok` -d '{"partialEqFilter": [{"key":{"deviceId": "JPE14070534", "label":"lldp_hostname" }}]}' 'https://10.83.13.33/api/resources/tag/v1/InterfaceTagAssignmentConfig/all' | jq '.result.value.key.interfaceId'

"Ethernet2"
```

### cvprac

```python
print(filter_interface_tag(clnt, dId="JPE14070534", label="lldp_hostname"))
```

### python requests

```python
print(filter_interface_tag(dId="JPE14070534", label="lldp_hostname"))
```

Get all interfaces that have a tag with a specific value on a device
--------------------------------

### curl

```bash
curl -sS -kX POST --header 'Accept: application/json' -b access_token=`cat token.tok` -d '{"partialEqFilter": [{"key":{"deviceId": "JPE14070534", "value":"speed40Gbps" }}]}' 'https://10.83.13.33/api/resources/tag/v1/InterfaceTagAssignmentConfig/all'
```

Result:

```python
      "time":"2021-03-27T00:38:41.886763089Z",
      "type":"INITIAL"
   }
}{
   "result":{
      "value":{
         "key":{
            "label":"speed",
            "value":"speed40Gbps",
            "deviceId":"JPE14070534",
            "interfaceId":"Ethernet101"
         }
      },
      "time":"2021-03-27T00:38:41.901936362Z",
      "type":"INITIAL"
   }
}{
   "result":{
      "value":{
         "key":{
            "label":"speed",
            "value":"speed40Gbps",
            "deviceId":"JPE14070534",
            "interfaceId":"Ethernet102"
         }
      },
      "time":"2021-03-27T00:38:41.935420476Z",
      "type":"INITIAL"
   }
}{
   "result":{
      "value":{
         "key":{
            "label":"speed",
            "value":"speed40Gbps",
            "deviceId":"JPE14070534",
            "interfaceId":"Ethernet103"
         }
      },
      "time":"2021-03-27T00:38:41.970652360Z",
      "type":"INITIAL"
   }
}{
   "result":{
      "value":{
         "key":{
            "label":"speed",
            "value":"speed40Gbps",
            "deviceId":"JPE14070534",
            "interfaceId":"Ethernet104"
         }
      },
      "time":"2021-03-27T00:38:41.968041519Z",
      "type":"INITIAL"
   }
}
```

### cvprac

```python
print(filter_interface_tag(clnt, dId="JPE14070534", value="speed40Gbps"))
```

### python requests

```python
print(filter_interface_tag(dId="JPE14070534", value="speed40Gbps"))
```

Create interface tag
--------------------------------

### curl

```bash
curl -sS -kX POST --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://10.83.13.33/api/resources/tag/v1/InterfaceTagConfig' -d '{"key":{"label":"lldp_chassis","value":"50:08:00:0d:00:08"}}'
```

Result:

```python
{"value":{"key":{"label":"lldp_chassis", "value":"50:08:00:0d:00:08"}}, "time":"2021-04-02T21:58:29.100209908Z"}%
```


### cvprac

```python
def create_itag(client, label, value):
    tag_url = '/api/resources/tag/v1/InterfaceTagConfig'
    payload = {"key":{"label":label,"value":value}}
    response = client.post(tag_url, data=payload)
    return response

create_itag(clnt, "lldp_chassis", "50:08:00:0d:00:38")
```

### python requests

```python
def create_itag(label, value):
    tag_url = '/api/resources/tag/v1/InterfaceTagConfig'
    payload = {"key":{"label":label,"value":value}}
    url = cvp_url + tag_url
    head = {'Authorization': 'Bearer {}'.format(token)}
    response = requests.post(url, headers=head, data=json.dumps(payload), verify=False)
    return response

create_itag("lldp_chassis", "50:08:00:0d:00:18")
```

Assign interface tag
--------------------------------

### curl

```bash
curl -sS -kX POST --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://10.83.13.33/api/resources/tag/v1/InterfaceTagAssignmentConfig' -d '{"key":{"label":"lldp_chassis", "value":"50:08:00:0d:00:08", "deviceId":"JPE14070534", "interfaceId": "Ethernet2"}}'
```

Result:

```python
{"value":{"key":{"label":"lldp_chassis", "value":"50:08:00:0d:00:08", "deviceId":"JPE14070534", "interfaceId":"Ethernet2"}}, "time":"2021-04-02T22:00:29.492449919Z"}%
```

### cvprac

```python
def assign_itag(client, dId, ifId, label, value):
    tag_url = '/api/resources/tag/v1/InterfaceTagAssignmentConfig'
    payload = {"key":{"label":label, "value":value, "deviceId": dId, "interfaceId": ifId}}
    response = client.post(tag_url, data=payload)
    return response

assign_itag(clnt, "JPE14070534", "Ethernet4", "lldp_chassis", "50:08:00:0d:00:38")
```

### python requests

```python
def assign_itag(dId, ifId, label, value):
    tag_url = '/api/resources/tag/v1/InterfaceTagAssignmentConfig'
    payload = {"key":{"label":label, "value":value, "deviceId": dId, "interfaceId": ifId}}
    url = cvp_url + tag_url
    head = {'Authorization': 'Bearer {}'.format(token)}
    response = requests.post(url, headers=head, data=json.dumps(payload), verify=False)
    return response

assign_itag("JPE14070534", "Ethernet3", "lldp_chassis", "50:08:00:0d:00:48")
```

Create device tag
--------------------------------

### curl

```bash
curl -sS -kX POST --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://10.83.13.33/api/resources/tag/v1/DeviceTagConfig' -d '{"key":{"label":"topology_hint_pod", "value":"ire-pod10"}}'
```

Result:

```python
{"value":{"key":{"label":"topology_hint_pod", "value":"ire-pod10"}}, "time":"2021-04-02T21:55:03.147265316Z"}%
```

### cvprac

```python
def create_dtag(client, label, value):
    tag_url = '/api/resources/tag/v1/DeviceTagConfig'
    payload = {"key":{"label":label,"value":value}}
    response = client.post(tag_url, data=payload)
    return response

create_dtag(clnt, "topology_hint_pod", "ire-pod11")
```

### python requests

```python
def create_dtag(label, value):
    tag_url = '/api/resources/tag/v1/DeviceTagConfig'
    payload = {"key":{"label":label, "value":value}}
    url = cvp_url + tag_url
    head = {'Authorization': 'Bearer {}'.format(token)}
    response = requests.post(url, headers=head, data=json.dumps(payload), verify=False)
    return response

create_dtag("topology_hint_pod", "ire-pod11")
```

Assign device tag
--------------------------------

### curl

```bash
curl -sS -kX POST --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://10.83.13.33/api/resources/tag/v1/DeviceTagAssignmentConfig' -d '{"key":{"label":"topology_hint_pod", "value":"ire-pod10","deviceId":"JPE14070534"}}'
```

Result:

```python
{"value":{"key":{"label":"topology_hint_pod", "value":"ire-pod10", "deviceId":"JPE14070534"}}, "time":"2021-04-02T21:56:24.575813791Z"}%
```

### cvprac

```python
def assign_dtag(client, dId, label, value):
    tag_url = '/api/resources/tag/v1/DeviceTagAssignmentConfig'
    payload = {"key":{"label":label, "value":value, "deviceId": dId}}
    response = client.post(tag_url, data=payload)
    return response

assign_dtag(clnt, "JPE14070534", "topology_hint_pod", "ire-pod11" )
```

### python requests

```python
def assign_dtag(dId, label, value):
    tag_url = '/api/resources/tag/v1/DeviceTagAssignmentConfig'
    payload = {"key":{"label":label, "value":value, "deviceId": dId}}
    url = cvp_url + tag_url
    head = {'Authorization': 'Bearer {}'.format(token)}
    response = requests.post(url, headers=head, data=json.dumps(payload), verify=False)
    return response

assign_dtag("JPE14070534", "topology_hint_pod", "ire-pod11")
```
