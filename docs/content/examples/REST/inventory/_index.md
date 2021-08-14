---
title: Inventory
weight: 100
chapter: false
---

{{% toc %}}

{{% notice tip %}}
[jq](https://stedolan.github.io/jq/) can be used to easily format and parse the outputs.
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
