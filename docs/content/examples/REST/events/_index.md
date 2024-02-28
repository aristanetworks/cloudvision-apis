---
title: Events
weight: 100
chapter: false
---

{{% toc %}}

{{% notice tip %}}
To generate a service account token please refer to the [authentication](../../../connecting/#token-based-authentication) chapter.
{{% /notice %}}

{{% notice tip %}}
[jq](https://stedolan.github.io/jq/) can be used to easily format and parse the outputs.
{{% /notice %}}

Events
================================

Get all active events
--------------------------------

### curl

```bash
curl -sS -kX GET --header 'Accept: application/json' 'https://192.0.2.33/api/resources/event/v1/Event/all' -b access_token=`cat token.tok`
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
curl -sS -kX GET --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.0.2.33/api/resources/event/v1/Event?key.key=6152f6160fc38f55&key.timestamp=2021-03-23T13:38:59.295341290Z'
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

{{% notice note %}}
When fetching a state from NetDB between two arbitrary dates, the result returned will contain data that existed between those two dates and not just data that was created between those dates. For instance if BGP events are queried between 2021-03-24 09:00 and 2021-03-24 10:00 the result will contain events that were active in the range of 9 AM to 10 AM. If there were events that started before 9 AM and were not resolved (still active) at that time, the result will contain those events too.
{{% /notice %}}

### curl

```bash
curl -sS -kX GET --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.0.2.33/api/resources/event/v1/Event/all?time.start=2021-03-24T09:00:00Z&time.end=2021-03-24T10:00:00Z'
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
curl -sS -kX POST --header 'Accept: application/json' -b access_token=`cat token.tok` -d '{"partialEqFilter": [{"severity": 1}]}' 'https://192.0.2.33/api/resources/event/v1/Event/all'
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
curl -sS -kX POST --header 'Accept: application/json' -b access_token=`cat token.tok` -d '{"partialEqFilter": [{"severity": "EVENT_SEVERITY_INFO"}]}' 'https://192.0.2.33/api/resources/event/v1/Event/all'
```

```bash
curl -sS -kX POST --header 'Accept: application/json' -b access_token=`cat token.tok` -d '{"partial_eq_filter": [{"severity": 1}]}' 'https://192.0.2.33/api/resources/event/v1/Event/all'
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
curl -sS -kX POST --header 'Accept: application/json' -b access_token=`cat token.tok` -d '{"partialEqFilter": [{"eventType":"LOW_DEVICE_DISK_SPACE"}]}' 'https://192.0.2.33/api/resources/event/v1/Event/all'
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
curl -sS -kX POST --header 'Accept: application/json' -b access_token=`cat token.tok` -d '{"partialEqFilter": [{"eventType":"LOW_DEVICE_DISK_SPACE","severity":"EVENT_SEVERITY_ERROR"}]}' 'https://192.0.2.33/api/resources/event/v1/Event/all'
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
