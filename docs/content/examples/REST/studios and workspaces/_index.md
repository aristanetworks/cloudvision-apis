---
title: Studios and Workspaces
weight: 100
chapter: false
---

{{% toc %}}

{{% notice tip %}}
To generate a service account token please refer to the [authentication](../../../connecting/_index.md#authentication) chapter.
{{% /notice %}}

{{% notice tip %}}
[jq](https://stedolan.github.io/jq/) can be used to easily format and parse the outputs.
{{% /notice %}}

Introduction
============

This document describes how to use Studio APIs to interact with Cloudvision Studios. They follow the Resource API semantics that are documented at [https://aristanetworks.github.io/cloudvision-apis/](https://aristanetworks.github.io/cloudvision-apis/). In this document, we illustrate the APIs using HTTP endpoints with JSON requests and responses. Using protobuf bindings, these operations can be done in a supported programming language (Go and Python) as well. See the above link for further details on how to use those bindings.

All changes that impact device configuration must be made in a workspace and submitted. The typical sequence of operations is
    1.Create a workspace
    2.Add objects that you want to modify into the workspace (either brand new objects, or copies of existing objects from mainline, or content that’s already submitted via a previous workspace);
    3.Build the workspace
    4.Submit.

Below are example APIs to use an existing studio, and also to create a brand new studio that generates timezone configuration. Given are the HTTP URL for each API and the body to POST to that URL.

You can use the below curl command to POST the body. “$token” is obtained from the access_token cookie returned by authenticating to CVP.

```shell
curl -sS -k -X POST $URL --cookie "access_token=$token" -d “$BODY”
```

e.g.

```shell
curl -sS -k -X POST "https://192.0.2.100/api/resources/workspace/v1/WorkspaceConfig" --cookie "access_token=$token" -d '{"key":{"workspace_id":"ws-change-timezone"}, "display_name": "Set timezone to EST"}'
```

> Note that for the field names in the POST body, both snake case (such as `studio_id`) and camel case (such as `studioId`) are accepted. Responses are always in camel case.

Get Studio and Workspace info
=============================

Get all workspace configs
-------------------------

```shell
curl -sS -k -X GET https://$CVP/api/resources/workspace/v1/WorkspaceConfig/all -b access_token=`cat token.tok`
```

Get a single workspace config
-----------------------------

```shell
curl -sS -k -X GET https://$CVP/api/resources/workspace/v1/WorkspaceConfig?key.workspaceId=ws-timezone  -b access_token=`cat token.tok`
```

Get all workspaces’ state
-------------------------

```shell
curl -sS -k -X GET https://$CVP/api/resources/workspace/v1/Workspace/all  -b access_token=`cat token.tok`
```

Get a single workspace state
----------------------------

```shell
curl -sS -k -X GET https://$CVP/api/resources/workspace/v1/Workspace?key.workspaceId=ws-timezone -b access_token=`cat token.tok`
```

Get a workspace build status and output
---------------------------------------

```shell
curl -sS -k -X GET https://$CVP/api/resources/workspace/v1/WorkspaceBuild?key.workspaceId=ws-timezone&key.buildId=b1 -b access_token=`cat token.tok`
```

Get all studio configs
----------------------

```shell
curl -sS -k -X GET  https://$CVP/api/resources/studio/v1/StudioConfig/all -b access_token=`cat token.tok`
```

```shell
grpcurl  -H "Authorization: Bearer `cat token.tok`" -import-path $GOPATH/src/arista/resources -proto $GOPATH/src/arista/resources/arista/studio.v1/services.gen.proto  -cacert cvp.crt  192.0.2.100:8443 arista.studio.v1.StudioConfigService/GetAll
```

Get all studios’ state
----------------------

```shell
curl -sS -k -X GET https://$CVP/api/resources/studio/v1/Studio/all -b access_token=`cat token.tok`
```

Get a single studio config in a workspace
-----------------------------------------

```shell
curl -sS -k -X GET https://$CVP/api/resources/studio/v1/StudioConfig?key.studioId=studio-timezone&key.workspaceId=ws-timezone -b access_token=`cat token.tok`
```

Get a single studio config in mainline
--------------------------------------

```shell
curl -sS -k -X GET https://$CVP/api/resources/studio/v1/StudioConfig?key.studioId=studio-timezone&key.workspaceId= -b access_token=`cat token.tok`
```

Get a single studio state in a workspace
----------------------------------------

```shell
curl -sS -k -X GET https://$CVP/api/resources/studio/v1/Studio?key.studioId=studio-timezone&key.workspaceId=ws-timezone -b access_token=`cat token.tok`
```

Get a single studio state in mainline
-------------------------------------

```shell
curl -sS -k -X GET https://$CVP/api/resources/studio/v1/Studio?key.studioId=studio-timezone&key.workspaceId= -b access_token=`cat token.tok`
```

Output:

```javascript
{
  "value": {
    "key": {
      "studioId": "studio-timezone",
      "workspaceId": ""
    },
    "displayName": "Set timezone",
    "description": "This studio generates timezone configuration",
    "template": {
      "type": "TEMPLATE_TYPE_MAKO",
      "body": "%if timezoneAssignment[\"timezone\"]:\nclock timezone ${timezoneAssignment[\"timezone\"]}\n%endif\n"
    },
    "inputSchema": {
...
...
    }
}
```

Use an existing studio
======================

Create a workspace
------------------

URL: `https://$CVP_INSTANCE/api/resources/workspace/v1/WorkspaceConfig `

POST BODY (`workspace.json`):

```json
{
    "key":{
        "workspace_id":"ws-change-timezone"
    },
    "display_name":"Configure timezone",
    "description":"Configure timezone on all devices",
}
```

### curl

```bash
curl -sS -kX POST --header 'Accept: application/json' \
  -b access_token=`cat token.tok` \
  'https://192.0.2.79/api/resources/workspace/v1/WorkspaceConfig' \
  -d "`cat workspace.json`"
```

Set inputs for the studio
-------------------------

URL: `https://$CVP/api/resources/studio/v1/InputsConfig `

POST BODY (`studio-payload.json`):

> Note the embedded JSON string.

```json
{
  "key": {
    "studio_id": "studio-date-time",
    "workspace_id": "ws-change-timezone",
    "path": {"values": []}
  },
  "inputs": "{\"ntpServerResolver\": [{\"inputs\": {\"ntpServers\": [{\"iburst\": false, \"ntpServer\": \"time.google.com\", \"preferred\": false, \"vrf\": \"MGMT\"}, {\"iburst\": false, \"ntpServer\": \"pool.ntp.org\", \"preferred\": false, \"vrf\": \"MGMT\"}]}, \"tags\": {\"query\": \"datacenter:NY\"}}], \"timezoneResolver\": [{\"inputs\": {\"timezoneGroup\": {\"otherTimezone\": \"\", \"timezone\": \"GMT\"}}, \"tags\": {\"query\": \"datacenter:NY\"}}]}"
}
```

### curl

```bash
curl -sS -kX POST --header 'Accept: application/json' \
  -b access_token=`cat token.tok` \
  'https://192.0.2.79/api/resources/studio/v1/InputsConfig' \
  -d "`cat studio-payload.json`"
```

Assign the studio to devices
----------------------------

URL: `https://$CVP/api/resources/studio/v1/AssignedTagsConfig `

POST BODY (`assigntags.json`):

```javascript
{
  "key": {
    "studio_id": "studio-date-time",
    "workspace_id": "ws-change-timezone"
  },
  "query": "datacenter:NY"
}
```

### curl

```bash
curl -sS -kX POST --header 'Accept: application/json' \
  -b access_token=`cat token.tok` \
  'https://192.0.2.79/api/resources/studio/v1/AssignedTagsConfig' \
  -d "`cat assigntags.json`"
```

Build the workspace
-------------------

URL: `https://$CVP/api/resources/workspace/v1/WorkspaceConfig `

POST BODY (`ws-build.json`):

```javascript
{
      "key":{
         "workspace_id":"ws-change-timezone"
      },
      "request":"REQUEST_START_BUILD",
      "request_params":{
         "request_id":"b1"
      }
}
```

### curl

```bash
curl -sS -kX POST --header 'Accept: application/json' \
  -b access_token=`cat token.tok` \
  'https://192.0.2.79/api/resources/workspace/v1/WorkspaceConfig' \
  -d "`cat workspace.json`"
```

Submit the workspace
--------------------

URL: `https://$CVP/api/resources/workspace/v1/WorkspaceConfig `

POST BODY:

```javascript
{
      "key":{
         "workspace_id":"ws-change-timezone"
      },
      "request":"REQUEST_SUBMIT",
      "request_params":{
         "request_id":"s1"
      }
}
```

### curl

```bash
curl -sS -kX POST --header 'Accept: application/json' \
  -b access_token=`cat token.tok` \
  'https://192.0.2.79/api/resources/workspace/v1/WorkspaceConfig' \
  -d "`cat ws-submit.json`"
```

Create a new Studio
===================

Create a workspace
------------------

URL:  `https://$CVP_INSTANCE/api/resources/workspace/v1/WorkspaceConfig`

POST BODY:

```javascript
{
      "key":{
         "workspace_id":"ws-timezone"
      }
      "display_name":"Configure timezone",
      "description":"Configure timezone on all devices",
}
```

### curl

```bash
curl -sS -kX POST --header 'Accept: application/json' \
  -b access_token=`cat token.tok` \
  'https://192.0.2.79/api/resources/workspace/v1/WorkspaceConfig' \
  -d "`cat workspace.json`"
```

Create a studio
---------------

URL: `https://$CVP_INSTANCE/api/resources/studio/v1/StudioConfig`

POST BODY (`newstudio.json`):

```javascript
{
    "key": {
        "studio_id": "studio-timezone",
        "workspace_id": "ws-timezone"
    },
    "display_name": "Set timezone",
    "description": "This configlet generates timezone configuration",
    "template": {
        "type": "TEMPLATE_TYPE_MAKO",
        "body": "% if timezone:\n  clock timezone ${timezone}\n% endif\n"
    },
    "input_schema": {
        "fields": {
            "values": {
                "root": {
                    "id": "root",
                    "type": "INPUT_FIELD_TYPE_GROUP",
                    "name": "",
                    "label": "",
                    "group_props": {
                        "members": {
                            "values": [
                                "inputfield_timezoneAssignment"
                            ]
                        }
                    }
                },
                "inputfield_timezoneAssignment": {
                    "id": "inputfield_timezoneAssignment",
                    "type": "INPUT_FIELD_TYPE_RESOLVER",
                    "name": "timezoneAssignment",
                    "label": "Timezone Assignment",
                    "description": "Timezone resolver input",
                    "required": false,
                    "resolver_props": {
                        "base_field_id": "inputfield_timezone",
                        "display_mode": "RESOLVER_FIELD_DISPLAY_MODE_SPARSE",
                        "input_mode": "RESOLVER_FIELD_INPUT_MODE_MULTI_DEVICE_TAG"
                    }
                },
                "inputfield_timezone": {
                    "id": "inputfield_timezone",
                    "type": "INPUT_FIELD_TYPE_STRING",
                    "name": "timezone",
                    "label": "Timezone",
                    "description": "Timezone value configured on the device",
                    "string_props": {
                        "default_value": "GMT",
                        "static_options": {
                            "values": [
                                "CST",
                                "EST",
                                "GMT",
                                "PST"
                            ]
                        }
                    }
                }
            }
        }
    }
}
```

### curl

```bash
curl -sS -kX POST --header 'Accept: application/json' \
  -b access_token=`cat token.tok` \
  'https://192.0.2.79/api/resources/studio/v1/StudioConfig' \
  -d "`cat newstudio.json`"
```

Build the workspace
-------------------

URL: `https://$CVP/api/resources/workspace/v1/WorkspaceConfig`

POST BODY (`ws-build.json`):

```javascript
{
      "key":{
         "workspace_id":"ws-timezone"
      },
      "request":"REQUEST_START_BUILD",
      "request_params":{
         "request_id":"b1"
      }
}
```

### curl

```bash
curl -sS -kX POST --header 'Accept: application/json' \
  -b access_token=`cat token.tok` \
  'https://192.0.2.79/api/resources/workspace/v1/WorkspaceConfig' \
  -d "`cat ws-build.json`"
```

Submit the workspace
--------------------------------

URL: `https://$CVP/api/resources/workspace/v1/WorkspaceConfig `

POST BODY (`ws-submit.json`):

```javascript
{
      "key":{
         "workspace_id":"ws-timezone"
      },
      "request":"REQUEST_SUBMIT",
      "request_params":{
         "request_id":"s1"
      }
}
```

### curl

```bash
curl -sS -kX POST --header 'Accept: application/json' \
  -b access_token=`cat token.tok` \
  'https://192.0.2.79/api/resources/workspace/v1/WorkspaceConfig' \
  -d "`cat ws-submit.json`"
```

Delete a Studio
===============

Create workspace
----------------

POST BODY (`workspace.json`):

```json
{
      "key":{
            "workspace_id":"del-studio"
      },
      "display_name":"Delete timezone studio",
      "description":"Remove timezone on all devices"
}
```

### curl

```bash
curl -sS -kX POST --header 'Accept: application/json' \
  -b access_token=`cat token.tok` \
  'https://192.0.2.79/api/resources/workspace/v1/WorkspaceConfig' \
  -d "`cat workspace.json`"
```

Output:

```json
{
    "value": {
        "key": {
            "workspaceId": "del-studio"
        },
        "displayName": "Delete timezone studio",
        "description": "Remove timezone on all devices"
    },
    "time": "2022-08-16T23:59:35.551Z"
}
```

Unassign the tags
-----------------

POST BODY (`unassigntags.json`):

```json
{
    "key": {
      "studio_id": "studio-timezone",
      "workspace_id": "del-studio"
    },
    "query": ""
}
```

### curl

```bash
curl -sS -kX POST --header 'Accept: application/json' \
  -b access_token=`cat token.tok` \
  'https://192.0.2.79/api/resources/studio/v1/AssignedTagsConfig' \
  -d "`cat unassigntags.json`"
```

Output:

```json
{
    "value": {
        "key": {
            "studioId": "studio-timezone",
            "workspaceId": "ws-timezone-delete"
        },
        "query": ""
    },
    "time": "2022-08-16T23:24:30.397673655Z"
}
```

Delete the studio
-----------------

POST BODY (`deletestudio.json`):

```json
{
    "key": {
        "studio_id": "studio-timezone",
        "workspace_id": "del-studio"
    },
    "remove": true
}
```

### curl

```bash
curl -sS -kX POST --header 'Accept: application/json' \
  -b access_token=`cat token.tok` \
  'https://192.0.2.79/api/resources/studio/v1/StudioConfig' \
  -d "`cat deletestudio.json`"
```

```json
{
    "value": {
        "key": {
            "studioId": "studio-timezone",
            "workspaceId": "del-studio"
        },
        "remove": true
    },
    "time": "2022-08-17T00:00:45.225196219Z"
}
```

Build the workspace
-----------------------

POST BODY (`ws-build.json`):

```json
{
    "key":{
       "workspace_id":"del-studio"
    },
    "request":"REQUEST_START_BUILD",
    "request_params":{
       "request_id":"b1"
    }
}
```

### curl

```bash
curl -sS -kX POST --header 'Accept: application/json' \
  -b access_token=`cat token.tok` \
  'https://192.0.2.79/api/resources/workspace/v1/WorkspaceConfig' \
  -d "`cat ws-build.json`"
```

Output:

```json
{
    "value": {
        "key": {
            "workspaceId": "del-studio"
        },
        "request": "REQUEST_START_BUILD",
        "requestParams": {
            "requestId": "b1"
        }
    },
    "time": "2022-08-17T00:00:54.195Z"
}
```

Submit the workspace
--------------------

POST BODY (`ws-submit.json`):

```json
{
    "key":{
       "workspace_id": "del-studio"
    },
    "request": "REQUEST_SUBMIT",
    "request_params":{
       "request_id":"s1"
    }
}
```

### curl

```bash
curl -sS -kX POST --header 'Accept: application/json' \
  -b access_token=`cat token.tok` \
  'https://192.0.2.79/api/resources/workspace/v1/WorkspaceConfig' \
  -d "`cat ws-submit.json`"
```

Output:

```json
{
    "value": {
        "key": {
            "workspaceId": "del-studio"
        },
        "request": "REQUEST_SUBMIT",
        "requestParams": {
            "requestId": "s1"
        }
    },
    "time": "2022-08-17T00:00:57.894Z"
}
```

Delete a workspace
==================

URL: `https://$CVP_INSTANCE/api/resources/workspace/v1/WorkspaceConfig`

POST BODY:

```javascript
{
      "key":{
         "workspace_id":"ws-timezone"
      }
}
```

## grpcurl

```shell
grpcurl  -H "Authorization: Bearer `cat token.tok`" -import-path $GOPATH/src/arista/resources -proto $GOPATH/src/arista/resources/arista/workspace.v1/services.gen.proto  -cacert cvp.crt -d '{"key":{"workspaceId": "builtin-studios-V0-l3ls"}}' 192.0.2.100:8443 arista.workspace.v1.WorkspaceConfigService/Delete
```

Result:

```javascript
{
  "key": {
    "workspaceId": "builtin-studios-V0-l3ls"
  },
  "time": "2021-07-22T17:09:51.788962287Z"
}
```

## curl

```shell
curl -sS -kX DELETE --header 'Accept: application/json' -H "Authorization: Bearer `cat token.tok`" 'https://192.0.2.100/api/resources/workspace/v1/WorkspaceConfig?key.workspaceId=builtin-studios-V0-l3ls'
```

Result:

```json
{
    "key": {
        "workspaceId": "builtin-studios-V0-l3ls"
    },
    "time": "2021-07-22T17:39:28.789768498Z"
}
```
