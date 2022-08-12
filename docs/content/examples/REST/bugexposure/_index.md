---
title: Bugexposure
weight: 100
chapter: false
---

{{% toc %}}

{{% notice info %}}
BugExposure Resource APIs are supported from CVP 2022.1.0 or newer and in CloudVision-as-a-Service.
{{% /notice %}}

{{% notice tip %}}
[jq](https://stedolan.github.io/jq/) can be used to easily format and parse the outputs.
{{% /notice %}}

Bugexposure.v1
================================

Get device bug exposure for one device
--------------------------------------------

### curl

```bash
curl -sS -kX GET --header 'Accept: application/json' -b access_token=`cat token.tok` \
  'https://192.0.2.79/api/resources/bugexposure/v1/BugExposure?key.deviceId=0123F2E4462997EB155B7C50EC148767' | jq
```

Output:

```json
{
  "value": {
    "key": {
      "deviceId": "0123F2E4462997EB155B7C50EC148767"
    },
    "bugIds": {
      "values": [
        578084,
        638303,
        647110,
        653156,
        662431,
        664223,
        672067,
        686581
      ]
    },
    "cveIds": {
      "values": [
        674519
      ]
    },
    "bugCount": 8,
    "cveCount": 1,
    "highestBugExposure": "HIGHEST_EXPOSURE_HIGH",
    "highestCveExposure": "HIGHEST_EXPOSURE_HIGH"
  },
  "time": "2022-08-11T06:56:09.228269719Z"
}
```

Get device bug exposure for all devices
--------------------------------------------

### curl

```bash
curl -sS -kX GET --header 'Accept: application/json' -b access_token=`cat token.tok` \
  'https://192.0.2.79/api/resources/bugexposure/v1/BugExposure/all' | jq
```

```json
{
  "result": {
    "value": {
      "key": {
        "deviceId": "HSH15201149"
      },
      "bugIds": {
        "values": [
          578084,
          653156,
          662431,
          671983,
          686096
        ]
      },
      "cveIds": {},
      "bugCount": 5,
      "cveCount": 0,
      "highestBugExposure": "HIGHEST_EXPOSURE_HIGH",
      "highestCveExposure": "HIGHEST_EXPOSURE_NONE"
    },
    "time": "2022-07-26T06:56:05.385727340Z",
    "type": "INITIAL"
  }
}
{
  "result": {
    "value": {
      "key": {
        "deviceId": "JPE20270454"
      },
      "bugIds": {
        "values": [
          578084
        ]
      },
      "cveIds": {},
      "bugCount": 1,
      "cveCount": 0,
      "highestBugExposure": "HIGHEST_EXPOSURE_LOW",
      "highestCveExposure": "HIGHEST_EXPOSURE_NONE"
    },
    "time": "2022-08-11T06:56:09.228269719Z",
    "type": "INITIAL"
  }
}
{
  "result": {
    "value": {
      "key": {
        "deviceId": "CD0EADBEEA126915EA78E0FB4DC776CA"
      },
      "bugIds": {
        "values": [
          578084,
          647110,
          653156,
          662431,
          664223,
          672067,
          686581
        ]
      },
      "cveIds": {
        "values": [
          674519
        ]
      },
      "bugCount": 7,
      "cveCount": 1,
      "highestBugExposure": "HIGHEST_EXPOSURE_HIGH",
      "highestCveExposure": "HIGHEST_EXPOSURE_HIGH"
    },
    "time": "2022-08-11T06:56:09.228269719Z",
    "type": "INITIAL"
  }
}
```

Get the acknowledged bugs for a device
--------------------------------------------

### curl

```bash
curl -sS -kX POST --header 'Accept: application/json' -b access_token=`cat token.tok` \
  'https://192.0.2.79/api/v3/services/arista.bugexposure.v1.BugExposureService/GetOne' \
  -d '{"key":{"deviceId":"BAD032986065E8DC14CBB6472EC314A6", "acknowledgement": "ACKNOWLEDGEMENT_ACKNOWLEDGED"}}'
```

Output:


```
[
  {
    "value": {
      "key": {
        "device_id": "BAD032986065E8DC14CBB6472EC314A6",
        "acknowledgement": "ACKNOWLEDGEMENT_ACKNOWLEDGED"
      },
      "bug_ids": {
        "values": [
          672067,
          686581
        ]
      },
      "cve_ids": {
        "values": []
      },
      "bug_count": 2,
      "cve_count": 0,
      "highest_bug_exposure": "HIGHEST_EXPOSURE_HIGH",
      "highest_cve_exposure": "HIGHEST_EXPOSURE_NONE"
    },
    "time": "2022-08-11T17:08:31.477858091Z"
  }
]
```
