---
title: Dashboard
weight: 100
chapter: false
---

{{% toc %}}

{{% notice tip %}}
To generate a service account token please refer to the [authentication](../../../connecting/#token-based-authentication) chapter.
{{% /notice %}}

{{% notice info %}}
Dashboard Resource APIs are supported from CVP 2021.3.0 (gRPC only) or newer and in CloudVision-as-a-Service.
The REST endpoint for on-prem is available from 2022.3.0.
{{% /notice %}}

{{% notice tip %}}
[jq](https://stedolan.github.io/jq/) can be used to easily format and parse the outputs.
{{% /notice %}}

dashboard.v1
============

## Get the status of a specific dashboard

### curl

```bash
curl -sS -kX GET --header 'Accept: application/json' -b access_token=`cat token.tok` \
  'https://192.0.2.79/api/resources/dashboard/v1/Dashboard?key.dashboardId=125125'
```

{{% notice tip %}}
You cannot use the result of this output to create a dashboard without removing the status-only related fields.
{{% /notice %}}

## Get the configuration of a specific dashboard

### curl

```bash
curl -sS -kX GET --header 'Accept: application/json' -b access_token=`cat token.tok` \
  'https://192.0.2.79/api/resources/dashboard/v1/DashboardConfig?key.dashboardId=125125'
```

Result:

```json
{
  "value": {
    "key": {
      "dashboardId": "a6ad9e70-66aa-4faa-a0ca-9e7deee29ac4"
    },
    "name": "RAM",
    "description": "",
    "widgets": {
      "values": [
        {
          "id": "8327188b-a8c5-420e-a6ff-9209e700ab58",
          "name": "",
          "position": {
            "x": 0,
            "y": 0
          },
          "dimensions": {
            "width": 8,
            "height": 10
          },
          "type": "aql-query-widget",
          "inputs": "{\"expression\":\"let info = `*:Kernel/proc/meminfo` | map(merge(_value))\\n\\nmerge(`analytics:DatasetInfo/Devices`) | \\\\\\nwhere(dictHasKey(info, _key)) | \\\\\\nmap(info[_key]) | \\\\\\nmap(dictHasKey(_value, \\\"memTotal\\\") ? (_value[\\\"memTotal\\\"] - _value[\\\"memAvailable\\\"]) / _value[\\\"memTotal\\\"] * 100 : 0)\",\"graphConfig\":{\"mapToHostname\":true},\"visualization\":\"barGraph\"}",
          "location": "main",
          "parent": ""
        }
      ]
    }
  },
  "time": "2022-11-08T02:07:05.218Z"
}
```

The `value` key of the result of the DashboardConfig call can then be used to create a dashboard on another CloudVision instance.

## Get all dashboard configurations

### curl

```bash
curl -sS -kX GET --header 'Accept: application/json' -b access_token=`cat token.tok` \
  'https://www.arista.io/api/resources/dashboard/v1/Dashboard/all'
```

## Create a dashboard

### curl

```bash
curl -sS -kX POST --header 'Accept: application/json' -b access_token=`cat token.tok` \
  'https://www.arista.io/api/resources/dashboard/v1/DashboardConfig' -d @bgp-peering.json
```

Input file:

```json
{
  "key": {
    "dashboard_id": "dd328b0c-279f-4d75-841c-c7489cd6f7fe"
  },
  "name": "bgp peering info",
  "description": "",
  "widgets": {
    "values": [
      {
        "id": "c2e45460-b76c-4007-8963-1ca87f6f3322",
        "name": "",
        "position": {
          "x": 0,
          "y": 0
        },
        "dimensions": {
          "width": 19,
          "height": 17
        },
        "type": "aql-query-widget",
        "inputs": "{\"expression\":\"let data = merge(`<device>:/Smash/routing/bgp/bgpPeerInfoStatus/default/bgpPeerStatusEntry`)\\nlet data3 = merge(`<device>:/Smash/routing/bgp/bgpPeerInfoStatus/default/bgpPeerStatisticsEntry`)\\nlet data2 = `analytics:/Devices/<device>/versioned-data/routing/bgp/status/vrf/default/bgpPeerInfoStatusEntry/*` | map(merge(_value))\\nlet y_data = newDict()\\n\\n\\n\\nfor key, val in data {  \\n    if val[\\\"bgpAfiSafiState\\\"][3][\\\"Name\\\"] != \\\"Unknown\\\" {\\n        y_data[key] = val[\\\"bgpAfiSafiState\\\"][3]\\n        y_data[key][\\\"AFI/SAFI State\\\"] = \\\"L2VPN EVPN\\\"\\n    }\\n    if val[\\\"bgpAfiSafiState\\\"][1][\\\"Name\\\"] != \\\"Unknown\\\" {\\n        y_data[key] = val[\\\"bgpAfiSafiState\\\"][1]\\n        y_data[key][\\\"AFI/SAFI State\\\"] = \\\"IPv4 Unicast\\\"\\n    }\\n    y_data[key][\\\"AS\\\"] = data2[key][\\\"bgpPeerAs\\\"][\\\"value\\\"]\\n    \\n    \\n}\\n\\n\\nfor key, val in data3 {\\n    y_data[key][\\\"MsgRcvd\\\"] = val[\\\"bgpPeerInTotalMessages\\\"]\\n    y_data[key][\\\"MsgSent\\\"] = val[\\\"bgpPeerOutTotalMessages\\\"]\\n}\\ny_data\",\"visualization\":\"table\"}",
        "location": "main"
      },
      {
        "id": "5d707fe5-6995-4485-809b-b2a50840b655",
        "name": "",
        "position": {
          "x": 0,
          "y": 0
        },
        "dimensions": {
          "width": 4,
          "height": 2
        },
        "type": "input-widget",
        "inputs": "{\"defaultValue\":\"0123F2E4462997EB155B7C50EC148767\",\"inputName\":\"device\",\"inputSource\":\"devices\",\"inputWidgetId\":\"5d707fe5-6995-4485-809b-b2a50840b655\",\"tagLabel\":\"device\"}",
        "location": "inputs"
      }
    ]
  }
}
```

### Quick Import/Export example with cURL

Export from instance 1:

```shell
curl -sS -kX GET --header 'Accept: application/json' -b access_token=`cat token.tok` \
  'https://192.0.2.79/api/resources/dashboard/v1/DashboardConfig?key.dashboardId=125125' | jq .value > networkmonitoring.json
```

Import to instance 2:

```bash
curl -sS -kX POST --header 'Accept: application/json' -b access_token=`cat token.tok` \
  'https://www.arista.io/api/resources/dashboard/v1/DashboardConfig' -d @networkmonitoring.json
```

### Quick Import/Export example with python

The following example will download a dashboard from an on-prem instance and upload it to a CVaaS tenant:

```python
import requests

# Read bearer token for 192.0.2.79
with open('token1.tok', 'r') as file:
    bearer_token1 = file.read().strip()

# Connect to the first API and retrieve the dashboard
dashboard_id = "CHANGEME"
api_url = f"http://192.0.2.79/api/resources/dashboard/v1/DashboardConfig?key.dashboardId={dashboard_id}"

headers1 = {
    'Authorization': f'Bearer {bearer_token1}'
}

response1 = requests.get(api_url, headers=headers1, verify=False)
dashboard_data = response1.json()

# Read bearer token for www.arista.io
with open('token2.tok', 'r') as file:
    bearer_token2 = file.read().strip()

# Connect to www.arista.io and upload the dashboard
# Note that the correct regional CVaaS URL should be used if your tenant is not on us-central1-a
upload_url = 'https://www.arista.io/api/resources/dashboard/v1/DashboardConfig'

headers2 = {
    'Authorization': f'Bearer {bearer_token2}'
}

response2 = requests.post(upload_url, headers=headers2, json=dashboard_data["value"])

if response2.status_code == 200:
    print('Dashboard uploaded successfully!')
else:
    print('Failed to upload the dashboard.')
```

## Delete a dashboard

### curl

```bash
curl -sS -kX DELETE --header 'Accept: application/json' -b access_token=`cat token.tok` \
  'https://www.arista.io/api/resources/dashboard/v1/DashboardConfig?key.dashboardId=dd328b0c-279f-4d75-841c-c7489cd6f7fe'
```

Output:

```json
{"key":{"dashboardId":"dd328b0c-279f-4d75-841c-c7489cd6f7fe"},"time":"2022-08-12T19:12:15.855946857Z"}
```

## Delete all dashboards (except the built-ins)

### curl

```bash
curl -sS -kX DELETE --header 'Accept: application/json' -b access_token=`cat token.tok` \
 'https://www.arista.io/api/resources/dashboard/v1/DashboardConfig/all'
```
