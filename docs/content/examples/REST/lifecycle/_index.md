---
title: Lifecycle
weight: 100
chapter: false
---

{{% toc %}}

{{% notice info %}}
Lifecycle Resource APIs are supported from CVP 2022.1.1 or newer and in CloudVision-as-a-Service.
{{% /notice %}}

{{% notice tip %}}
[jq](https://stedolan.github.io/jq/) can be used to easily format and parse the outputs.
{{% /notice %}}

Lifecycle.v1
================================

Get device lifecycle summary for all devices
--------------------------------------------

### curl

```bash
curl -sS -kX GET --header 'Accept: application/json' -b access_token=`cat token.tok` \
  'https://www.arista.io/api/resources/lifecycle/v1/DeviceLifecycleSummary/all'
```

Output:

```json
{
  "result": {
    "value": {
      "key": {
        "deviceId": "ZZZ9999999"
      },
      "softwareEol": {
        "version": "4.28.1F",
        "endOfSupport": "2025-04-18T00:00:00Z"
      }
    },
    "time": "2022-08-11T06:37:43.841719913Z",
    "type": "INITIAL"
  }
}
{
  "result": {
    "value": {
      "key": {
        "deviceId": "ZZZ9999999"
      },
      "softwareEol": {
        "version": "4.27.3.1F",
        "endOfSupport": "2024-09-27T00:00:00Z"
      },
      "hardwareLifecycleSummary": {
        "endOfLife": {
          "date": "2025-03-20T00:00:00Z",
          "models": {
            "values": {
              "DCS-7050SX-64": 1
            }
          }
        },
        "endOfSale": {
          "date": "2022-03-20T00:00:00Z",
          "models": {
            "values": {
              "DCS-7050SX-64": 1
            }
          }
        },
        "endOfTacSupport": {
          "date": "2024-03-20T00:00:00Z",
          "models": {
            "values": {
              "DCS-7050SX-64": 1
            }
          }
        },
        "endOfHardwareRmaRequests": {
          "date": "2025-03-20T00:00:00Z",
          "models": {
            "values": {
              "DCS-7050SX-64": 1
            }
          }
        }
      }
    },
    "time": "2022-08-04T03:44:29.409669418Z",
    "type": "INITIAL"
  }
}
```

Get device lifecycle summary for a device
-----------------------------------------

### curl

```bash
curl -sS -kX GET --header 'Accept: application/json' -b access_token=`cat token.tok` \
  'https://192.0.2.79/api/resources/lifecycle/v1/DeviceLifecycleSummary?key.deviceId=ZZZ9999999'
```

Output:

```json
{
  "value": {
    "key": {
      "deviceId": "ZZZ9999999"
    },
    "softwareEol": {
      "version": "4.23.10M",
      "endOfSupport": "2022-09-27T00:00:00Z"
    },
    "hardwareLifecycleSummary": {
      "endOfLife": {
        "date": "2024-12-20T00:00:00Z",
        "models": {
          "values": {
            "DCS-7150S-52-CL": 1
          }
        }
      },
      "endOfSale": {
        "date": "2021-12-20T00:00:00Z",
        "models": {
          "values": {
            "DCS-7150S-52-CL": 1
          }
        }
      },
      "endOfTacSupport": {
        "date": "2024-12-20T00:00:00Z",
        "models": {
          "values": {
            "DCS-7150S-52-CL": 1
          }
        }
      },
      "endOfHardwareRmaRequests": {
        "date": "2024-12-20T00:00:00Z",
        "models": {
          "values": {
            "DCS-7150S-52-CL": 1
          }
        }
      }
    }
  },
  "time": "2022-07-26T06:56:05.385727340Z"
}
```
