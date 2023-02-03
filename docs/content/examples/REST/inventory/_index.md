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

## Get device state by serial number

### curl

```shell
curl -sS -kX GET --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.0.2.100/api/resources/inventory/v1/Device?key.deviceId=BAD032986065E8DC14CBB6472EC314A6'
```

Output:

```json
{"value":{"key":{"deviceId":"BAD032986065E8DC14CBB6472EC314A6"}, "softwareVersion":"4.27.0F", "modelName":"vEOS-lab", "hardwareRevision":"", "fqdn":"tp-avd-leaf1", "hostname":"tp-avd-leaf1", "domainName":"", "systemMacAddress":"50:08:00:a7:ca:c3", "bootTime":"2021-12-01T20:06:18.607800006Z", "streamingStatus":"STREAMING_STATUS_ACTIVE", "extendedAttributes":{"featureEnabled":{"Danz":false, "Mlag":false}}}, "time":"2022-02-03T10:04:38.376359403Z"}%
```

## Get all devices from inventory

### curl

```shell
curl -sS -kX GET --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.0.2.100/api/resources/inventory/v1/Device/all' | jq '.result.value | with_entries(select(.[])) | select(.streamingStatus=="STREAMING_STATUS_ACTIVE") | .hostname'
"cd263"
"sn413"
"fm422"
"sn503"
"psp301"
"wl504"
"cloudEOS1"
```

We can use `POST` and `partialEqFilter` to get more specific data, e.g.: to get all actively streaming devices we can filter by `streamingStatus` by setting the `"STREAMING_STATUS_ACTIVE"` or `2`

```shell
curl -sS -kX POST --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.0.2.100/api/resources/inventory/v1/Device/all' -d '{"partialEqFilter": [{"streamingStatus":2}]}'
```

Get all actively streaming devices that are running on EOS 4.27.0F:

```shell
curl -sS -kX POST --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.0.2.100/api/resources/inventory/v1/Device/all' -d '{"partialEqFilter": [{"streamingStatus":2, "softwareVersion":"4.27.0F"}]}'
```

Output:

```json
{"result":{"value":{"key":{"deviceId":"6323DA7D2B542B5D09630F87351BEA41"},"softwareVersion":"4.27.0F","modelName":"vEOS-lab","hardwareRevision":"","fqdn":"tp-avd-leaf4","hostname":"tp-avd-leaf4","domainName":"","systemMacAddress":"50:08:00:25:9d:36","bootTime":"2021-10-20T17:44:35.621819972Z","streamingStatus":"STREAMING_STATUS_ACTIVE","extendedAttributes":{"featureEnabled":{"Danz":false,"Mlag":false}}},"time":"2022-01-27T22:33:58.745524517Z","type":"INITIAL"}}
{"result":{"value":{"key":{"deviceId":"BAD032986065E8DC14CBB6472EC314A6"},"softwareVersion":"4.27.0F","modelName":"vEOS-lab","hardwareRevision":"","fqdn":"tp-avd-leaf1","hostname":"tp-avd-leaf1","domainName":"","systemMacAddress":"50:08:00:a7:ca:c3","bootTime":"2021-12-01T20:06:18.607800006Z","streamingStatus":"STREAMING_STATUS_ACTIVE","extendedAttributes":{"featureEnabled":{"Danz":false,"Mlag":false}}},"time":"2022-02-03T10:04:38.376359403Z","type":"INITIAL"}}
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

## Decommission a device

### curl

```shell
curl -sS -kX POST --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.0.2.100/api/resources/inventory/v1/DeviceDecommissioningConfig' -d '{"key":{"request_id":"123456789"},"device_id": "0123F2E4462997EB155B7C50EC148767"}'
```

## Get the decommission state of a device

### curl

```shell
curl -sS -kX GET --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.0.2.100/api/resources/inventory/v1/DeviceDecommissioning?key.requestId=123456789'
```

Output:

```json
{"value":{"key":{"requestId":"123456789"}, "status":"DECOMMISSIONING_STATUS_IN_PROGRESS", "statusMessage":"Disabled TerminAttr, waiting for device to be marked inactive"}, "time":"2022-02-04T00:40:24.893100195Z"}
```

## Get the decommission state of all devices

### curl

```shell
curl -sS -kX GET --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.0.2.100/api/resources/inventory/v1/DeviceDecommissioning/all'
```

## Get the decommission state of all devices that failed to be decommissioned

### curl

```shell
curl -sS -kX POST --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.0.2.100/api/resources/inventory/v1/DeviceDecommissioning/all' -d '{"partialEqFilter": [ {"status":2}]}'
```

Output:

```json
{"result":{"value":{"key":{"requestId":"2337d655-b1e5-4003-9325-beff8c9e7f4a"},"status":"DECOMMISSIONING_STATUS_FAILURE","error":"Timed out waiting for device BAD032986065E8DC14CBB6472EC314A6 status to be inactive","statusMessage":""},"time":"2022-02-04T19:41:49.566294590Z","type":"INITIAL"}}
{"result":{"value":{"key":{"requestId":"7802d5a5-040d-4d86-805f-d63891256201"},"status":"DECOMMISSIONING_STATUS_FAILURE","error":"Pending/In-progress tasks exist for the device","statusMessage":""},"time":"2022-02-04T19:41:49.566299871Z","type":"INITIAL"}}
{"result":{"value":{"key":{"requestId":"d88b046f-3338-450f-bf47-a28f6ced700e"},"status":"DECOMMISSIONING_STATUS_FAILURE","error":"Pending/In-progress tasks exist for the device","statusMessage":""},"time":"2022-02-04T19:41:49.566304560Z","type":"INITIAL"}}
```

or get the state of decommissioning for devices for which the decommissioning is still in progress:

```shell
curl -sS -kX POST --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.0.2.100/api/resources/inventory/v1/DeviceDecommissioning/all' -d '{"partialEqFilter": [ {"status":1}]}'
```

Output:

```json

{"result":{"value":{"key":{"requestId":"123456789"},"status":"DECOMMISSIONING_STATUS_IN_PROGRESS","statusMessage":"Disabled TerminAttr, waiting for device to be marked inactive"},"time":"2022-02-04T19:41:46.376310308Z","type":"INITIAL"}}
```

## Onboard a device

{{% notice note %}}
The service account's name has to match the username logged in on the CVP UI and that same username has to be allowed on the device.
The user should be logged in on the UI when using the the DeviceOnboarding APIs.
{{% /notice %}}

### curl

```shell
curl -sS -kX POST --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.0.2.100/api/resources/inventory/v1/DeviceOnboardingConfig' -d '{"key":{"requestId":"133713371337"},"hostnameOrIp":"192.0.2.139","device_type":"eos"}'
```

## Get the onboarding state by request ID

### curl

```shell
curl -sS -kX GET --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.0.2.100/api/resources/inventory/v1/DeviceOnboarding?key.requestId=133713371337'
```

Output:

```json
{"value":{"key":{"requestId":"133713371337"}, "deviceId":"ZZZ9999999", "status":"ONBOARDING_STATUS_SUCCESS", "statusMessage":"Device onboarded successfully"}, "time":"2022-02-04T19:51:13.447185558Z"}
```

## Get the onboarding state for all devices

### curl

```shell
curl -sS -kX GET --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.0.2.100/api/resources/inventory/v1/DeviceOnboarding/all'
```

Output:

```json
{"result":{"value":{"key":{"requestId":"133713371337"},"deviceId":"ZZZ9999999","status":"ONBOARDING_STATUS_SUCCESS","statusMessage":"Device onboarded successfully"},"time":"2022-02-04T19:51:13.447185558Z","type":"INITIAL"}}
```

## Get the onboarding state for all devices and filter by status

### curl

```shell
curl -sS -kX GET --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.0.2.100/api/resources/inventory/v1/DeviceOnboarding/all' -d '{"partialEqFilter":[{"status":"ONBOARDING_STATUS_SUCCESS"}]}'
```

```json
{"result":{"value":{"key":{"requestId":"133713371337"},"deviceId":"ZZZ7654321","status":"ONBOARDING_STATUS_SUCCESS","statusMessage":"Device onboarded successfully"},"time":"2022-02-04T19:51:13.447185558Z","type":"INITIAL"}}
{"result":{"value":{"key":{"requestId":"1337133713381123"},"deviceId":"ZZZ1234567","status":"ONBOARDING_STATUS_SUCCESS","statusMessage":"Device onboarded successfully"},"time":"2022-02-04T22:46:33.709449980Z","type":"INITIAL"}}
{"result":{"value":{"key":{"requestId":"0342271e-19e0-4672-9d09-85acd7a427b5"},"deviceId":"6323DA7D2B542B5D09630F87351BEA41","status":"ONBOARDING_STATUS_SUCCESS","statusMessage":"Device onboarded successfully"},"time":"2022-07-11T15:19:22.293390239Z","type":"INITIAL"}}
```

## Get the provisioning state for devices in ZTP mode

### curl

```shell
curl -sS -kX POST --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.0.2.100/api/resources/inventory/v1/ProvisionedDevice/all' -d '{"partialEqFilter":[{"ztpMode":true}]}'
```

Output:

```json
{"result":{"value":{"key":{"deviceId":"JPE15214224"},"status":"PROVISIONING_STATUS_SUCCESS","ztpMode":true,"ipAddress":{"value":"192.0.2.240"},"provisioningGroupName":"undefined_container"},"time":"2022-01-31T13:16:09.885Z","type":"INITIAL"}}
{"result":{"value":{"key":{"deviceId":"JPE19050707"},"status":"PROVISIONING_STATUS_SUCCESS","ztpMode":true,"ipAddress":{"value":"192.0.2.121"},"provisioningGroupName":"undefined_container"},"time":"2022-01-30T19:06:00.070338261Z","type":"INITIAL"}}
{"result":{"value":{"key":{"deviceId":"JPE16401934"},"status":"PROVISIONING_STATUS_SUCCESS","ztpMode":true,"ipAddress":{"value":"192.0.2.254"},"provisioningGroupName":"undefined_container"},"time":"2022-02-04T19:48:14.187Z","type":"INITIAL"}}
{"result":{"value":{"key":{"deviceId":"JPE15064123"},"status":"PROVISIONING_STATUS_SUCCESS","ztpMode":true,"ipAddress":{"value":"192.0.2.250"},"provisioningGroupName":"undefined_container"},"time":"2022-02-04T19:53:13.016Z","type":"INITIAL"}}
```
