---
title: workspace.v1
---



- [arista/workspace.v1/workspace.proto](#arista/workspace.v1/workspace.proto)
    - [BuildResult](#buildresult)
    - [BuildResults](#buildresults)
    - [BuildResults.ValuesEntry](#valuesentry)
    - [ConfigValidationResult](#configvalidationresult)
    - [ConfigletBuildResult](#configletbuildresult)
    - [ConfigletBuildResults](#configletbuildresults)
    - [ConfigletBuildResults.ValuesEntry](#valuesentry)
    - [InputError](#inputerror)
    - [InputErrors](#inputerrors)
    - [InputValidationResult](#inputvalidationresult)
    - [InputValidationResults](#inputvalidationresults)
    - [InputValidationResults.ValuesEntry](#valuesentry)
    - [RequestParams](#requestparams)
    - [Response](#response)
    - [Responses](#responses)
    - [Responses.ValuesEntry](#valuesentry)
    - [TemplateError](#templateerror)
    - [TemplateErrors](#templateerrors)
    - [Workspace](#workspace)
    - [WorkspaceBuild](#workspacebuild)
    - [WorkspaceBuildKey](#workspacebuildkey)
    - [WorkspaceConfig](#workspaceconfig)
    - [WorkspaceKey](#workspacekey)
  
    - [BuildStage](#arista.workspace.v1.BuildStage)
    - [BuildState](#arista.workspace.v1.BuildState)
    - [Request](#arista.workspace.v1.Request)
    - [ResponseStatus](#arista.workspace.v1.ResponseStatus)
    - [WorkspaceState](#arista.workspace.v1.WorkspaceState)
  
- [arista/workspace.v1/services.gen.proto](#arista/workspace.v1/services.gen.proto)
    - [WorkspaceBuildRequest](#workspacebuildrequest)
    - [WorkspaceBuildResponse](#workspacebuildresponse)
    - [WorkspaceBuildStreamRequest](#workspacebuildstreamrequest)
    - [WorkspaceBuildStreamResponse](#workspacebuildstreamresponse)
    - [WorkspaceConfigDeleteRequest](#workspaceconfigdeleterequest)
    - [WorkspaceConfigDeleteResponse](#workspaceconfigdeleteresponse)
    - [WorkspaceConfigRequest](#workspaceconfigrequest)
    - [WorkspaceConfigResponse](#workspaceconfigresponse)
    - [WorkspaceConfigSetRequest](#workspaceconfigsetrequest)
    - [WorkspaceConfigSetResponse](#workspaceconfigsetresponse)
    - [WorkspaceConfigStreamRequest](#workspaceconfigstreamrequest)
    - [WorkspaceConfigStreamResponse](#workspaceconfigstreamresponse)
    - [WorkspaceRequest](#workspacerequest)
    - [WorkspaceResponse](#workspaceresponse)
    - [WorkspaceStreamRequest](#workspacestreamrequest)
    - [WorkspaceStreamResponse](#workspacestreamresponse)
  
    - [WorkspaceBuildService](#arista.workspace.v1.WorkspaceBuildService)
    - [WorkspaceConfigService](#arista.workspace.v1.WorkspaceConfigService)
    - [WorkspaceService](#arista.workspace.v1.WorkspaceService)
  




<a name="arista/workspace.v1/workspace.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## arista/workspace.v1/workspace.proto



<a name="arista.workspace.v1.BuildResult"></a>

### BuildResult
BuildResult is the per-device build output


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **state** | [BuildState](#buildstate) | <p></p> |
| **stage** | [BuildStage](#buildstage) | <p></p> |
| **input_validation_results** | [InputValidationResults](#inputvalidationresults) | <p></p> |
| **configlet_build_results** | [ConfigletBuildResults](#configletbuildresults) | <p></p> |
| **config_validation_result** | [ConfigValidationResult](#configvalidationresult) | <p></p> |







<a name="arista.workspace.v1.BuildResults"></a>

### BuildResults
BuildResults is the build output for all devices, indexed by device ID


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **values** | [BuildResults.ValuesEntry](#buildresults.valuesentry)[...] | <p></p> |







<a name="arista.workspace.v1.BuildResults.ValuesEntry"></a>

### BuildResults.ValuesEntry



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | string | <p></p> |
| **value** | [BuildResult](#buildresult) | <p></p> |







<a name="arista.workspace.v1.ConfigValidationResult"></a>

### ConfigValidationResult
ConfigValidationResult is the result of validating config with an EOS device


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **summary** | arista.configstatus.v1.ConfigSummary | <p></p> |
| **errors** | arista.configstatus.v1.ConfigErrors | <p></p> |
| **warnings** | arista.configstatus.v1.ConfigErrors | <p></p> |







<a name="arista.workspace.v1.ConfigletBuildResult"></a>

### ConfigletBuildResult
ConfigletBuildResult is the output of configlet (template) build


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **template_errors** | [TemplateErrors](#templateerrors) | <p></p> |
| **generated_config** | google.protobuf.StringValue | <p></p> |







<a name="arista.workspace.v1.ConfigletBuildResults"></a>

### ConfigletBuildResults
ConfigletBuildResults is the output of configlet build, one per studio


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **values** | [ConfigletBuildResults.ValuesEntry](#configletbuildresults.valuesentry)[...] | <p></p> |







<a name="arista.workspace.v1.ConfigletBuildResults.ValuesEntry"></a>

### ConfigletBuildResults.ValuesEntry



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | string | <p></p> |
| **value** | [ConfigletBuildResult](#configletbuildresult) | <p></p> |







<a name="arista.workspace.v1.InputError"></a>

### InputError
InputError represents an error in an input field, with either schema or value


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **field_id** | google.protobuf.StringValue | <p>ID of the field</p> |
| **path** | fmp.RepeatedString | <p>Path leading up to the field</p> |
| **members** | fmp.RepeatedString | <p>Members of the field</p> |
| **message** | google.protobuf.StringValue | <p>The error message</p> |







<a name="arista.workspace.v1.InputErrors"></a>

### InputErrors
InputErrors is the nullable list of InputError


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **values** | [InputError](#inputerror)[...] | <p></p> |







<a name="arista.workspace.v1.InputValidationResult"></a>

### InputValidationResult
InputValidationResult is the result of input validation of a studio


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **input_schema_errors** | [InputErrors](#inputerrors) | <p></p> |
| **input_value_errors** | [InputErrors](#inputerrors) | <p></p> |
| **other_errors** | fmp.RepeatedString | <p></p> |







<a name="arista.workspace.v1.InputValidationResults"></a>

### InputValidationResults
InputValidationResults is the result of input validation, one per studio


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **values** | [InputValidationResults.ValuesEntry](#inputvalidationresults.valuesentry)[...] | <p></p> |







<a name="arista.workspace.v1.InputValidationResults.ValuesEntry"></a>

### InputValidationResults.ValuesEntry



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | string | <p></p> |
| **value** | [InputValidationResult](#inputvalidationresult) | <p></p> |







<a name="arista.workspace.v1.RequestParams"></a>

### RequestParams
RequestParams is the parameters associated with a WorkspaceRequest


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **request_id** | google.protobuf.StringValue | <p></p> |







<a name="arista.workspace.v1.Response"></a>

### Response
Response is the response to the last Request, typically errors in processing


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **status** | [ResponseStatus](#responsestatus) | <p></p> |
| **message** | google.protobuf.StringValue | <p></p> |







<a name="arista.workspace.v1.Responses"></a>

### Responses
Responses is the map of all request ID to response that are processed so far


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **values** | [Responses.ValuesEntry](#responses.valuesentry)[...] | <p></p> |







<a name="arista.workspace.v1.Responses.ValuesEntry"></a>

### Responses.ValuesEntry



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | string | <p></p> |
| **value** | [Response](#response) | <p></p> |







<a name="arista.workspace.v1.TemplateError"></a>

### TemplateError
TemplateError represents a single error generated by a template evaluation


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **line_num** | google.protobuf.UInt32Value | <p>Line on which the error occurred</p> |
| **exception** | google.protobuf.StringValue | <p>The exception type</p> |
| **detail** | google.protobuf.StringValue | <p>Backtrace, etc.</p> |







<a name="arista.workspace.v1.TemplateErrors"></a>

### TemplateErrors
TemplateErrors is the nullable list of TemplateError


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **values** | [TemplateError](#templateerror)[...] | <p></p> |







<a name="arista.workspace.v1.Workspace"></a>

### Workspace
Workspace is the status of a workspace


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [WorkspaceKey](#workspacekey) | <p></p> |
| **created_at** | google.protobuf.Timestamp | <p></p> |
| **created_by** | google.protobuf.StringValue | <p></p> |
| **last_modified_at** | google.protobuf.Timestamp | <p></p> |
| **last_modified_by** | google.protobuf.StringValue | <p></p> |
| **state** | [WorkspaceState](#workspacestate) | <p></p> |
| **last_build_id** | google.protobuf.StringValue | <p></p> |
| **responses** | [Responses](#responses) | <p></p> |
| **cc_ids** | fmp.RepeatedString | <p>Change Controls created by submitting this workspace</p> |







<a name="arista.workspace.v1.WorkspaceBuild"></a>

### WorkspaceBuild
WorkspaceBuild is the result, or output of a workspace build
This includes results for all devices across all studios in the workspace


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [WorkspaceBuildKey](#workspacebuildkey) | <p></p> |
| **state** | [BuildState](#buildstate) | <p></p> |
| **build_results** | [BuildResults](#buildresults) | <p></p> |







<a name="arista.workspace.v1.WorkspaceBuildKey"></a>

### WorkspaceBuildKey
WorkspaceBuildKey is the key to get the build result for a workspace


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **workspace_id** | google.protobuf.StringValue | <p>workspace_id is a required field which represents workspace ID</p> |
| **build_id** | google.protobuf.StringValue | <p>build_id is a required field which represents build ID</p> |







<a name="arista.workspace.v1.WorkspaceConfig"></a>

### WorkspaceConfig
WorkspaceConfig represents the configurable parameters of a workspace


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [WorkspaceKey](#workspacekey) | <p></p> |
| **display_name** | google.protobuf.StringValue | <p></p> |
| **description** | google.protobuf.StringValue | <p></p> |
| **request** | [Request](#request) | <p></p> |
| **request_params** | [RequestParams](#requestparams) | <p></p> |







<a name="arista.workspace.v1.WorkspaceKey"></a>

### WorkspaceKey
WorkspaceKey is the key to get a workspace's status


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **workspace_id** | google.protobuf.StringValue | <p></p> |






 <!-- end messages -->


<a name="arista.workspace.v1.BuildStage"></a>

### BuildStage
BuildStage is the stage of a workspace build

| Name | Number | Description |
| ---- | ------ | ----------- |
| BUILD_STAGE_UNSPECIFIED | 0 | <p></p> |
| BUILD_STAGE_INPUT_VALIDATION | 1 | <p></p> |
| BUILD_STAGE_CONFIGLET_BUILD | 2 | <p></p> |
| BUILD_STAGE_CONFIG_VALIDATION | 3 | <p></p> |



<a name="arista.workspace.v1.BuildState"></a>

### BuildState


| Name | Number | Description |
| ---- | ------ | ----------- |
| BUILD_STATE_UNSPECIFIED | 0 | <p></p> |
| BUILD_STATE_IN_PROGRESS | 1 | <p></p> |
| BUILD_STATE_CANCELED | 2 | <p></p> |
| BUILD_STATE_SUCCESS | 3 | <p></p> |
| BUILD_STATE_FAIL | 4 | <p></p> |



<a name="arista.workspace.v1.Request"></a>

### Request
Operations on a workspace that can be requested by a client.
These are workspace-specific operations. The standard operations Add, Delete, etc.
are performed via the standard ("core") APIs.
This is an asynchronous request that returns immediately if the request is valid.
The result of the operation will be available in WorkspaceStatus when it is generated.

| Name | Number | Description |
| ---- | ------ | ----------- |
| REQUEST_UNSPECIFIED | 0 | <p></p> |
| REQUEST_START_BUILD | 1 | <p>Start a new build</p> |
| REQUEST_CANCEL_BUILD | 2 | <p>Cancel any pending build</p> |
| REQUEST_SUBMIT | 3 | <p>Submit the workspace (merge into mainline)</p> |
| REQUEST_ABANDON | 4 | <p>Abandon the workspace. Not delete</p> |
| REQUEST_ROLLBACK | 5 | <p>Rollback an already submitted workspace</p> |



<a name="arista.workspace.v1.ResponseStatus"></a>

### ResponseStatus


| Name | Number | Description |
| ---- | ------ | ----------- |
| RESPONSE_STATUS_UNSPECIFIED | 0 | <p></p> |
| RESPONSE_STATUS_SUCCESS | 1 | <p></p> |
| RESPONSE_STATUS_FAIL | 2 | <p></p> |



<a name="arista.workspace.v1.WorkspaceState"></a>

### WorkspaceState


| Name | Number | Description |
| ---- | ------ | ----------- |
| WORKSPACE_STATE_UNSPECIFIED | 0 | <p></p> |
| WORKSPACE_STATE_PENDING | 1 | <p></p> |
| WORKSPACE_STATE_SUBMITTED | 2 | <p></p> |
| WORKSPACE_STATE_ABANDONED | 3 | <p></p> |
| WORKSPACE_STATE_CONFLICTS | 4 | <p></p> |
| WORKSPACE_STATE_ROLLED_BACK | 5 | <p></p> |


 <!-- end enums -->

 <!-- end HasExtensions -->

 <!-- end services -->




<a name="arista/workspace.v1/services.gen.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## arista/workspace.v1/services.gen.proto



<a name="arista.workspace.v1.WorkspaceBuildRequest"></a>

### WorkspaceBuildRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [WorkspaceBuildKey](#workspacebuildkey) | <p>Key uniquely identifies a WorkspaceBuild instance to retrieve.</p><p>This value must be populated.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the time for which you are interested in the data.</p><p>If no time is given, the server will use the time at which it makes the request.</p> |







<a name="arista.workspace.v1.WorkspaceBuildResponse"></a>

### WorkspaceBuildResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [WorkspaceBuild](#workspacebuild) | <p>Value is the value requested.</p><p>This structure will be fully-populated as it exists in the datastore. If</p><p>optional fields were not given at creation, these fields will be empty or</p><p>set to default values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time carries the (UTC) timestamp of the last-modification of the</p><p>WorkspaceBuild instance in this response.</p> |







<a name="arista.workspace.v1.WorkspaceBuildStreamRequest"></a>

### WorkspaceBuildStreamRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **partial_eq_filter** | [WorkspaceBuild](#workspacebuild)[...] | <p>PartialEqFilter provides a way to server-side filter a GetAll/Subscribe.</p><p>This requires all provided fields to be equal to the response.</p><p>While transparent to users, this field also allows services to optimize internal</p><p>subscriptions if filter(s) are sufficiently specific.</p> |
| **time** | arista.time.TimeBounds | <p>TimeRange allows limiting response data to within a specified time window.</p><p>If this field is populated, at least one of the two time fields are required.</p><p>This field is not allowed in the Subscribe RPC.</p> |







<a name="arista.workspace.v1.WorkspaceBuildStreamResponse"></a>

### WorkspaceBuildStreamResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [WorkspaceBuild](#workspacebuild) | <p>Value is a value deemed relevant to the initiating request.</p><p>This structure will always have its key-field populated. Which other fields are</p><p>populated, and why, depends on the value of Operation and what triggered this notification.</p> |
| **time** | google.protobuf.Timestamp | <p>Time holds the timestamp of this WorkspaceBuild's last modification.</p> |
| **type** | arista.subscriptions.Operation | <p>Operation indicates how the WorkspaceBuild value in this response should be considered.</p><p>Under non-subscribe requests, this value should always be INITIAL. In a subscription,</p><p>once all initial data is streamed and the client begins to receive modification updates,</p><p>you should not see INITIAL again.</p> |







<a name="arista.workspace.v1.WorkspaceConfigDeleteRequest"></a>

### WorkspaceConfigDeleteRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [WorkspaceKey](#workspacekey) | <p>Key indicates which WorkspaceConfig instance to remove.</p><p>This field must always be set.</p> |







<a name="arista.workspace.v1.WorkspaceConfigDeleteResponse"></a>

### WorkspaceConfigDeleteResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [WorkspaceKey](#workspacekey) | <p>Key echoes back the key of the deleted WorkspaceConfig instance.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the (UTC) timestamp at which the system recognizes the</p><p>deletion. The only guarantees made about this timestamp are:</p><p>- it is after the time the request was received</p><p>- a time-ranged query with StartTime==DeletedAt will not include this instance.</p> |







<a name="arista.workspace.v1.WorkspaceConfigRequest"></a>

### WorkspaceConfigRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [WorkspaceKey](#workspacekey) | <p>Key uniquely identifies a WorkspaceConfig instance to retrieve.</p><p>This value must be populated.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the time for which you are interested in the data.</p><p>If no time is given, the server will use the time at which it makes the request.</p> |







<a name="arista.workspace.v1.WorkspaceConfigResponse"></a>

### WorkspaceConfigResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [WorkspaceConfig](#workspaceconfig) | <p>Value is the value requested.</p><p>This structure will be fully-populated as it exists in the datastore. If</p><p>optional fields were not given at creation, these fields will be empty or</p><p>set to default values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time carries the (UTC) timestamp of the last-modification of the</p><p>WorkspaceConfig instance in this response.</p> |







<a name="arista.workspace.v1.WorkspaceConfigSetRequest"></a>

### WorkspaceConfigSetRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [WorkspaceConfig](#workspaceconfig) | <p>WorkspaceConfig carries the value to set into the datastore.</p><p>See the documentation on the WorkspaceConfig struct for which fields are required.</p> |







<a name="arista.workspace.v1.WorkspaceConfigSetResponse"></a>

### WorkspaceConfigSetResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [WorkspaceConfig](#workspaceconfig) | <p>Value carries all the values given in the WorkspaceConfigSetRequest as well</p><p>as any server-generated values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the (UTC) timestamp at which the system recognizes the</p><p>creation. The only guarantees made about this timestamp are:</p><p>- it is after the time the request was received</p><p>- a time-ranged query with StartTime==CreatedAt will include this instance.</p> |







<a name="arista.workspace.v1.WorkspaceConfigStreamRequest"></a>

### WorkspaceConfigStreamRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **partial_eq_filter** | [WorkspaceConfig](#workspaceconfig)[...] | <p>PartialEqFilter provides a way to server-side filter a GetAll/Subscribe.</p><p>This requires all provided fields to be equal to the response.</p><p>While transparent to users, this field also allows services to optimize internal</p><p>subscriptions if filter(s) are sufficiently specific.</p> |
| **time** | arista.time.TimeBounds | <p>TimeRange allows limiting response data to within a specified time window.</p><p>If this field is populated, at least one of the two time fields are required.</p><p>This field is not allowed in the Subscribe RPC.</p> |







<a name="arista.workspace.v1.WorkspaceConfigStreamResponse"></a>

### WorkspaceConfigStreamResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [WorkspaceConfig](#workspaceconfig) | <p>Value is a value deemed relevant to the initiating request.</p><p>This structure will always have its key-field populated. Which other fields are</p><p>populated, and why, depends on the value of Operation and what triggered this notification.</p> |
| **time** | google.protobuf.Timestamp | <p>Time holds the timestamp of this WorkspaceConfig's last modification.</p> |
| **type** | arista.subscriptions.Operation | <p>Operation indicates how the WorkspaceConfig value in this response should be considered.</p><p>Under non-subscribe requests, this value should always be INITIAL. In a subscription,</p><p>once all initial data is streamed and the client begins to receive modification updates,</p><p>you should not see INITIAL again.</p> |







<a name="arista.workspace.v1.WorkspaceRequest"></a>

### WorkspaceRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [WorkspaceKey](#workspacekey) | <p>Key uniquely identifies a Workspace instance to retrieve.</p><p>This value must be populated.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the time for which you are interested in the data.</p><p>If no time is given, the server will use the time at which it makes the request.</p> |







<a name="arista.workspace.v1.WorkspaceResponse"></a>

### WorkspaceResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [Workspace](#workspace) | <p>Value is the value requested.</p><p>This structure will be fully-populated as it exists in the datastore. If</p><p>optional fields were not given at creation, these fields will be empty or</p><p>set to default values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time carries the (UTC) timestamp of the last-modification of the</p><p>Workspace instance in this response.</p> |







<a name="arista.workspace.v1.WorkspaceStreamRequest"></a>

### WorkspaceStreamRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **partial_eq_filter** | [Workspace](#workspace)[...] | <p>PartialEqFilter provides a way to server-side filter a GetAll/Subscribe.</p><p>This requires all provided fields to be equal to the response.</p><p>While transparent to users, this field also allows services to optimize internal</p><p>subscriptions if filter(s) are sufficiently specific.</p> |
| **time** | arista.time.TimeBounds | <p>TimeRange allows limiting response data to within a specified time window.</p><p>If this field is populated, at least one of the two time fields are required.</p><p>This field is not allowed in the Subscribe RPC.</p> |







<a name="arista.workspace.v1.WorkspaceStreamResponse"></a>

### WorkspaceStreamResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [Workspace](#workspace) | <p>Value is a value deemed relevant to the initiating request.</p><p>This structure will always have its key-field populated. Which other fields are</p><p>populated, and why, depends on the value of Operation and what triggered this notification.</p> |
| **time** | google.protobuf.Timestamp | <p>Time holds the timestamp of this Workspace's last modification.</p> |
| **type** | arista.subscriptions.Operation | <p>Operation indicates how the Workspace value in this response should be considered.</p><p>Under non-subscribe requests, this value should always be INITIAL. In a subscription,</p><p>once all initial data is streamed and the client begins to receive modification updates,</p><p>you should not see INITIAL again.</p> |






 <!-- end messages -->

 <!-- end enums -->

 <!-- end HasExtensions -->


<a name="arista.workspace.v1.WorkspaceBuildService"></a>

### WorkspaceBuildService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetOne | [WorkspaceBuildRequest](#arista.workspace.v1.WorkspaceBuildRequest) | [WorkspaceBuildResponse](#arista.workspace.v1.WorkspaceBuildResponse) | <p></p> |
| GetAll | [WorkspaceBuildStreamRequest](#arista.workspace.v1.WorkspaceBuildStreamRequest) | [WorkspaceBuildStreamResponse](#arista.workspace.v1.WorkspaceBuildStreamResponse) stream | <p></p> |
| Subscribe | [WorkspaceBuildStreamRequest](#arista.workspace.v1.WorkspaceBuildStreamRequest) | [WorkspaceBuildStreamResponse](#arista.workspace.v1.WorkspaceBuildStreamResponse) stream | <p></p> |


<a name="arista.workspace.v1.WorkspaceConfigService"></a>

### WorkspaceConfigService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetOne | [WorkspaceConfigRequest](#arista.workspace.v1.WorkspaceConfigRequest) | [WorkspaceConfigResponse](#arista.workspace.v1.WorkspaceConfigResponse) | <p></p> |
| GetAll | [WorkspaceConfigStreamRequest](#arista.workspace.v1.WorkspaceConfigStreamRequest) | [WorkspaceConfigStreamResponse](#arista.workspace.v1.WorkspaceConfigStreamResponse) stream | <p></p> |
| Subscribe | [WorkspaceConfigStreamRequest](#arista.workspace.v1.WorkspaceConfigStreamRequest) | [WorkspaceConfigStreamResponse](#arista.workspace.v1.WorkspaceConfigStreamResponse) stream | <p></p> |
| Set | [WorkspaceConfigSetRequest](#arista.workspace.v1.WorkspaceConfigSetRequest) | [WorkspaceConfigSetResponse](#arista.workspace.v1.WorkspaceConfigSetResponse) | <p></p> |
| Delete | [WorkspaceConfigDeleteRequest](#arista.workspace.v1.WorkspaceConfigDeleteRequest) | [WorkspaceConfigDeleteResponse](#arista.workspace.v1.WorkspaceConfigDeleteResponse) | <p></p> |


<a name="arista.workspace.v1.WorkspaceService"></a>

### WorkspaceService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetOne | [WorkspaceRequest](#arista.workspace.v1.WorkspaceRequest) | [WorkspaceResponse](#arista.workspace.v1.WorkspaceResponse) | <p></p> |
| GetAll | [WorkspaceStreamRequest](#arista.workspace.v1.WorkspaceStreamRequest) | [WorkspaceStreamResponse](#arista.workspace.v1.WorkspaceStreamResponse) stream | <p></p> |
| Subscribe | [WorkspaceStreamRequest](#arista.workspace.v1.WorkspaceStreamRequest) | [WorkspaceStreamResponse](#arista.workspace.v1.WorkspaceStreamResponse) stream | <p></p> |

 <!-- end services -->



