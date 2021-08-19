---
title: Tags
weight: 100
chapter: false
---

{{% toc %}}

{{% notice tip %}}
[jq](https://stedolan.github.io/jq/) can be used to easily format and parse the outputs.
{{% /notice %}}

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
