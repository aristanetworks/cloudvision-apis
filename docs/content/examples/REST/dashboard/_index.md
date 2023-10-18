---
title: Dashboard
weight: 100
chapter: false
---

{{% toc /%}}

{{% notice info %}}
Dashboard Resource APIs are supported from CVP 2021.3.0 (gRPC only) or newer and in CloudVision-as-a-Service.
The REST endpoint for on-prem is available from 2022.3.0.
{{% /notice %}}

{{% notice tip %}}
[jq](https://stedolan.github.io/jq/) can be used to easily format and parse the outputs.
{{% /notice %}}

dashboard.v1
============

## Get a specific dashboard

### curl

```bash
curl -sS -kX GET --header 'Accept: application/json' -b access_token=`cat token.tok` \
  'https://192.0.2.79/api/resources/dashboard/v1/Dashboard?key.dashboardId=125125'
```

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
  'https://www.arista.io/api/resources/dashboard/v1/DashboardConfig' -d "`cat bgp-peering.json`"
```

Input file:

```
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
