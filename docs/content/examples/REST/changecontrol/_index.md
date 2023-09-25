---
title: Change Control
weight: 100
chapter: false
---

{{% toc %}}

{{% notice info %}}
Change Control Resource APIs are supported from CVP 2021.2.0 or newer and in CloudVision-as-a-Service.
{{% /notice %}}

{{% notice tip %}}
[jq](https://stedolan.github.io/jq/) can be used to easily format and parse the outputs.
{{% /notice %}}

# changeControl.v1

{{% notice note %}}
A change can be only be in unapproved state if it was approved initially. Change Controls which have never been approved will have the status of `Pending Approval`
{{% /notice %}}

## Get the approval state for a specific change control

### curl

```shell
curl -sS -kX GET --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.0.2.100/api/resources/changecontrol/v1/ApproveConfig?key.id=-WIh3Xnwu'
```

Output:

```json
{"value":{"key":{"id":"-WIh3Xnwu"}, "approve":{"value":true}, "version":"2021-12-03T10:41:40.810064204Z"}, "time":"2021-12-03T10:41:44.109088624Z"}
```

Changes that were never approved will have a nil state and the following result will be returned:

```json
{"code":5, "message":"resource not found"}
```

The state of a change that was unapproved will result in the following:

```json
{"value":{"key":{"id":"gKCZL1eNG"}, "approve":{"value":false, "notes":"Unapproved explicitly by user"}, "version":"2021-12-08T13:18:16.436235494Z"}, "time":"2021-12-13T18:05:08.243031760Z"}
```

## Get the approval state for all approved/unapproved changes

### curl

```shell
curl -sS -kX GET --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.0.2.100/api/resources/changecontrol/v1/ApproveConfig/all'
```

Output:

```json
{"result":{"value":{"key":{"id":"-WIh3Xnwu"},"approve":{"value":true},"version":"2021-12-03T10:41:40.810064204Z"},"time":"2021-12-03T10:41:44.109088624Z","type":"INITIAL"}}
{"result":{"value":{"key":{"id":"-5UxLHCBk"},"approve":{"value":true},"version":"2021-12-03T10:53:58.819000425Z"},"time":"2021-12-03T10:54:05.099957401Z","type":"INITIAL"}}
{"result":{"value":{"key":{"id":"-gKtnAX0s"},"approve":{"value":true},"version":"2021-08-19T18:27:25.312165529Z"},"time":"2021-08-19T18:27:28.961559476Z","type":"INITIAL"}}
{"result":{"value":{"key":{"id":"Dpum-Owhq"},"approve":{"value":true},"version":"2021-08-02T09:47:47.324298592Z"},"time":"2021-08-02T09:47:49.603355580Z","type":"INITIAL"}}
{"result":{"value":{"key":{"id":"1ZgkJ.Wed"},"approve":{"value":true},"version":"2021-11-29T20:42:25.298103662Z"},"time":"2021-11-29T20:42:41.187649168Z","type":"INITIAL"}}
```

## Approve a change

First we need to get the change control state for the specified key and extract the value of `time` from the `change` dictionary:

### curl

```shell
curl -sS -kX GET --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.0.2.100/api/resources/changecontrol/v1/ChangeControl?key.id=rxwA-N65u'
```

Output:

```json
{"value":{"key":{"id":"rxwA-N65u"}, "change":{"name":"Change 20211213_183228", "rootStageId":"c2uIKIkq0c", "stages":{"values":{"c2uIKIkq0c":{"name":"Change 20211213_183228 Root", "rows":{"values":[{"values":["gaKs4SdpMj"]}]}}, "gaKs4SdpMj":{"name":"Update Config", "action":{"name":"task", "timeout":3000, "args":{"values":{"TaskID":"542"}}}}}}, "notes":"", "time":"2021-12-13T18:32:31.830585136Z", "user":"cvpadmin"}}, "time":"2021-12-13T18:32:31.830585136Z"}
```

Then use the `time` value in the `version` value in the ApproveConfig POST message as below:

```shell
curl -sS -kX POST --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.0.2.100/api/resources/changecontrol/v1/ApproveConfig' -H 'Content-Type: application/json' \
-d '{"key":{"id":"rxwA-N65u"}, "approve": {"value": true, "notes": "REST API test"}, "version": "2021-12-13T18:32:31.830585136Z"}'
```

Output:

```json
{"value":{"key":{"id":"rxwA-N65u"}, "approve":{"value":true, "notes":"REST API test"}, "version":"2021-12-13T18:32:31.830585136Z"}, "time":"2021-12-13T19:00:11.500491001Z"}
```

## Get the state of all Change Controls

```shell
curl -L -X GET "https://192.0.2.100/api/resources/changecontrol/v1/ChangeControl/all" \
-H "Accept: application/json" \
-H "Authorization: Bearer `cat token.tok`"
```

Output:

```json
{"result":{"value":{"key":{"id":"CC_Task_f7d44737-485e-4002-bfe7-8c577ac51023"},"change":{"name":"Change Control CC_Task_f7d44737-485e-4002-bfe7-8c577ac51023","rootStageId":"root","stages":{"values":{"Task_2827":{"name":"Task stage 2827","action":{"name":"task","timeout":7200,"args":{"values":{"TaskID":"2827"}}},"rows":{},"status":"STAGE_STATUS_COMPLETED"},"root":{"name":"root","rows":{"values":[{"values":["Task_2827"]}]},"status":"STAGE_STATUS_COMPLETED"}}},"notes":"Auto Generated Request","time":"2023-08-25T02:13:17.292234597Z","user":"cvpadmin"},"approve":{"value":true,"notes":"","time":"2023-08-25T02:13:17.315590969Z","user":"cvpadmin"},"start":{"value":true,"notes":"Auto Start","time":"2023-08-25T02:13:17.327707307Z","user":"cvpadmin"},"status":"CHANGE_CONTROL_STATUS_COMPLETED","deviceIds":{"values":["BAD032986065E8DC14CBB6472EC314A6"]}},"time":"2023-08-25T02:13:17.991529440Z","type":"INITIAL"}}
...
```

## Create a change control

### curl

```shell
curl -sS -kX POST --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.0.2.100/api/resources/changecontrol/v1/ChangeControlConfig' -d "`cat task_data.json`"
```

where `task_data.json` looks like below:

`cat task_data.json | jq`

Output:

```json
{
  "key": {
    "id": "5821c7c1-e276-4387-b60a"
  },
  "change": {
    "name": "Change_20211222_191032",
    "rootStageId": "root",
    "stages": {
      "values": {
        "root": {
          "name": "root",
          "rows": {
            "values": [
              {
                "values": [
                  "stage0",
                  "stage1",
                  "stage2",
                  "stage3"
                ]
              }
            ]
          }
        },
        "stage0": {
          "name": "stage0",
          "action": {
            "name": "task",
            "timeout": 3000,
            "args": {
              "values": {
                "TaskID": "1245"
              }
            }
          }
        },
        "stage1": {
          "name": "stage1",
          "action": {
            "name": "task",
            "timeout": 3000,
            "args": {
              "values": {
                "TaskID": "1246"
              }
            }
          }
        },
        "stage2": {
          "name": "stage2",
          "action": {
            "name": "task",
            "timeout": 3000,
            "args": {
              "values": {
                "TaskID": "1247"
              }
            }
          }
        },
        "stage3": {
          "name": "stage3",
          "action": {
            "name": "task",
            "timeout": 3000,
            "args": {
              "values": {
                "TaskID": "1248"
              }
            }
          }
        }
      }
    },
    "notes": "curl_cc_test"
  }
}
```

or without `jq` formatting:

```json
{"key": {"id": "5821c7c1-e276-4387-b60a"}, "change": {"name": "Change_20211222_191032", "rootStageId": "root", "stages": {"values": {"root": {"name": "root", "rows": {"values": [{"values": ["stage0", "stage1", "stage2", "stage3"]}]}}, "stage0": {"name": "stage0", "action": {"name": "task", "timeout": 3000, "args": {"values": {"TaskID": "1245"}}}}, "stage1": {"name": "stage1", "action": {"name": "task", "timeout": 3000, "args": {"values": {"TaskID": "1246"}}}}, "stage2": {"name": "stage2", "action": {"name": "task", "timeout": 3000, "args": {"values": {"TaskID": "1247"}}}}, "stage3": {"name": "stage3", "action": {"name": "task", "timeout": 3000, "args": {"values": {"TaskID": "1248"}}}}}}, "notes": "curl_cc_test"}}
```

## Delete a change control

### curl

Pending Change controls can be deleted as below:

```shell
curl -sS -kX DELETE --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.0.2.100/api/resources/changecontrol/v1/ChangeControlConfig?key.id=wvisXUy5N'
```

Output:

```json
{"key":{"id":"wvisXUy5N"}, "time":"2021-12-14T20:01:42.058348061Z"}
```

## Start a change control

### curl

```shell
curl -sS -kX POST --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.0.2.100/api/resources/changecontrol/v1/ChangeControlConfig' -d '{"key":{"id":"VhkkzxK4U"},"start":{"value":true,"notes":"Starting change via REST call"}}'
```

Output:

```json
{"value":{"key":{"id":"VhkkzxK4U"}, "start":{"value":true, "notes":"starting change via curl"}}, "time":"2021-12-14T21:02:18.940285772Z"}
```

## Stop a change control

### curl

```shell
curl -sS -kX POST --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.0.2.100/api/resources/changecontrol/v1/ChangeControlConfig' -d '{"key":{"id":"VhkkzxK4U"},"start":{"value":false,"notes":"Stopping change via REST call"}}'
```

Output:

```json
{"value":{"key":{"id":"VhkkzxK4U"}, "start":{"value":false, "notes":"stopping change via curl"}}, "time":"2021-12-14T21:02:21.830306071Z"}
```

## Schedule a change control

### curl

{{% notice info %}}
Change control scheduling using Resource APIs is only supported in 2022.1.0 or newer.
{{% /notice %}}

The below example shows how to schedule a Change Control at 2:07 AM on 2021-12-23:

```shell
curl -sS -kX POST --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.0.2.100/api/resources/changecontrol/v1/ChangeControlConfig' -d '{"key":{"id":"5821c7c1-e276-4387-b60a"},"schedule":{"value":"2021-12-23T02:07:00.0Z","notes":"CC schedule via curl"}}'
```

Output:

```json
{"value":{"key":{"id":"5821c7c1-e276-4387-b60a"}, "schedule":{"value":"2021-12-23T01:49:00Z", "notes":"CC schedule via curl"}}, "time":"2021-12-23T01:47:32.521200888Z"}
```

{{% notice note %}}
A scheduled change will be only successfully executed if the change was approved.
{{% /notice %}}

Fetching the state of a scheduled change which wasn't approved before execution time will result in the following error:

`"error":"Reschedule required: not approved at schedule time"`

e.g.:

```shell
curl -sS -kX GET --header 'Accept: application/json' -b access_token=`cat token.tok` 'https://192.0.2.100/api/resources/changecontrol/v1/ChangeControl?key.id=5821c7c1-e276-4387-b60a'

{"value":{"key":{"id":"5821c7c1-e276-4387-b60a"}, "change":{"name":"Change_20211222_191032", "rootStageId":"root", "stages":{"values":{"root":{"name":"root", "rows":{"values":[{"values":["stage0", "stage1", "stage2", "stage3"]}]}}, "stage0":{"name":"stage0", "action":{"name":"task", "timeout":3000, "args":{"values":{"TaskID":"1245"}}}}, "stage1":{"name":"stage1", "action":{"name":"task", "timeout":3000, "args":{"values":{"TaskID":"1246"}}}}, "stage2":{"name":"stage2", "action":{"name":"task", "timeout":3000, "args":{"values":{"TaskID":"1247"}}}}, "stage3":{"name":"stage3", "action":{"name":"task", "timeout":3000, "args":{"values":{"TaskID":"1248"}}}}}}, "notes":"curl_cc_test", "time":"2021-12-22T19:10:35.472979755Z", "user":"resourceapis"}, "error":"Reschedule required: not approved at schedule time", "schedule":{"notes":"Reschedule required: not approved at schedule time", "time":"2021-12-23T01:49:00.004927172Z"}}, "time":"2021-12-23T01:49:00.004927172Z"}
```

## Change the name of a Change Control

### curl


```shell
curl -L -X POST "https://192.0.2.100/api/resources/changecontrol/v1/ChangeControlConfig" \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-H "Authorization: Bearer `cat token.tok`" \
-d '{"key": {"id": "FvDMjNx7aRbUPnCUVqLQ4"},"change": {"name": "MLAG ISSU in DC1" }}'
```

or

```shell
curl -L -X POST "https://192.0.2.100/api/resources/changecontrol/v1/ChangeControlConfig" \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-H "Authorization: Bearer `cat token.tok`" \
-d @cc_payload.json
```

where `cc_payload.json` has the following content:

```json
{
  "key": {
    "id": "FvDMjNx7aRbUPnCUVqLQ4"
  },
  "change": {
    "name": "MLAG ISSU in DC1"
  }
}
```
