---
title: configstatus.v1
---



- [arista/configstatus.v1/configstatus.proto](#arista/configstatus.v1/configstatus.proto)
    - [ConfigDiff](#configdiff)
    - [ConfigDiffKey](#configdiffkey)
    - [ConfigError](#configerror)
    - [ConfigErrors](#configerrors)
    - [ConfigKey](#configkey)
    - [ConfigSummary](#configsummary)
    - [Configuration](#configuration)
    - [DiffEntries](#diffentries)
    - [DiffEntry](#diffentry)
    - [Summary](#summary)
    - [SummaryKey](#summarykey)
  
    - [ConfigFilterCode](#arista.configstatus.v1.ConfigFilterCode)
    - [ConfigSyncCode](#arista.configstatus.v1.ConfigSyncCode)
    - [ConfigType](#arista.configstatus.v1.ConfigType)
    - [DiffOp](#arista.configstatus.v1.DiffOp)
    - [ErrorCode](#arista.configstatus.v1.ErrorCode)
  
- [arista/configstatus.v1/services.gen.proto](#arista/configstatus.v1/services.gen.proto)
    - [ConfigDiffRequest](#configdiffrequest)
    - [ConfigDiffResponse](#configdiffresponse)
    - [ConfigDiffStreamRequest](#configdiffstreamrequest)
    - [ConfigDiffStreamResponse](#configdiffstreamresponse)
    - [ConfigurationRequest](#configurationrequest)
    - [ConfigurationResponse](#configurationresponse)
    - [ConfigurationStreamRequest](#configurationstreamrequest)
    - [ConfigurationStreamResponse](#configurationstreamresponse)
    - [SummaryRequest](#summaryrequest)
    - [SummaryResponse](#summaryresponse)
    - [SummaryStreamRequest](#summarystreamrequest)
    - [SummaryStreamResponse](#summarystreamresponse)
  
    - [ConfigDiffService](#arista.configstatus.v1.ConfigDiffService)
    - [ConfigurationService](#arista.configstatus.v1.ConfigurationService)
    - [SummaryService](#arista.configstatus.v1.SummaryService)
  




<a name="arista/configstatus.v1/configstatus.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## arista/configstatus.v1/configstatus.proto



<a name="arista.configstatus.v1.ConfigDiff"></a>

### ConfigDiff



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [ConfigDiffKey](#configdiffkey) | <p>Key represents config diff key</p> |
| **uri** | google.protobuf.StringValue | <p>Uri represents the HTTP URI client can use to GET config diff and associated errors</p> |
| **error** | [ConfigError](#configerror) | <p></p> |







<a name="arista.configstatus.v1.ConfigDiffKey"></a>

### ConfigDiffKey
ConfigDiffKey uniquely identifies a configuration diff request


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **a_device_id** | google.protobuf.StringValue | <p>A_device_id is the serial number of the device on A side (left hand side)</p> |
| **a_type** | [ConfigType](#configtype) | <p>A_type is the config type on A side (left hand side)</p> |
| **a_time** | google.protobuf.Timestamp | <p>A_time is the time at which to fetch config on A side (left hand side)</p> |
| **b_device_id** | google.protobuf.StringValue | <p>B_device_id is the serial number of the device on B side (right hand side)</p> |
| **b_type** | [ConfigType](#configtype) | <p>B_type is the config type on B side (right hand side)</p> |
| **b_time** | google.protobuf.Timestamp | <p>B_time is the time at which to fetch config on B side (right hand side)</p> |







<a name="arista.configstatus.v1.ConfigError"></a>

### ConfigError
ConfigError represents errors reported by CVP when handling device configuration


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **error_code** | [ErrorCode](#errorcode) | <p></p> |
| **error_msg** | google.protobuf.StringValue | <p></p> |
| **line_num** | google.protobuf.Int32Value | <p>Line_num represents line number, if any</p> |
| **configlet_name** | google.protobuf.StringValue | <p>Configlet_name represents the originating configlet name. Configlet_name</p><p>and line_num point to the line where config warning or config error originate.</p> |







<a name="arista.configstatus.v1.ConfigErrors"></a>

### ConfigErrors



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **values** | [ConfigError](#configerror)[...] | <p></p> |







<a name="arista.configstatus.v1.ConfigKey"></a>

### ConfigKey
ConfigKey uniquely identifies a config request.


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **device_id** | google.protobuf.StringValue | <p>Device_id is the serial number of the device</p> |
| **type** | [ConfigType](#configtype) | <p>Type describes the config type</p> |







<a name="arista.configstatus.v1.ConfigSummary"></a>

### ConfigSummary
ConfigSummary represents device configuration summary.


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **sync** | [ConfigSyncCode](#configsynccode) | <p></p> |
| **nop_lines** | google.protobuf.Int32Value | <p>Number of lines with code no-operation</p> |
| **ignored_lines** | google.protobuf.Int32Value | <p>Number of lines with code IGNORE</p> |
| **added_lines** | google.protobuf.Int32Value | <p>Number of lines with code ADD</p> |
| **deleted_lines** | google.protobuf.Int32Value | <p>Number of lines with code DELETE</p> |
| **changed_lines** | google.protobuf.Int32Value | <p>Number of lines with code CHANGE</p> |
| **designed_config_errors** | google.protobuf.Int32Value | <p>Number of designed config errors</p> |
| **designed_config_warnings** | google.protobuf.Int32Value | <p>Number of designed config warnings</p> |
| **running_config_update_time** | google.protobuf.Timestamp | <p>Timestamp at which running config is updated</p> |
| **designed_config_update_time** | google.protobuf.Timestamp | <p>Timestamp at which designed config is updated</p> |
| **running_config_uri** | google.protobuf.StringValue | <p>The HTTP URI client can use to GET running config and associated errors</p> |
| **designed_config_uri** | google.protobuf.StringValue | <p>The HTTP URI client can use to GET designed config and associated errors</p> |
| **diff_uri** | google.protobuf.StringValue | <p>The HTTP URI client can use to GET config diff and associated errors</p> |
| **digest** | google.protobuf.StringValue | <p>Digest of the config diff. For example, it can be SHA-256 hash of the config diff</p> |







<a name="arista.configstatus.v1.Configuration"></a>

### Configuration
Configuration represents device's CLI configuration


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [ConfigKey](#configkey) | <p></p> |
| **uri** | google.protobuf.StringValue | <p>Uri represents the HTTP URI client can use to GET config body and associated errors</p> |
| **error** | [ConfigError](#configerror) | <p></p> |







<a name="arista.configstatus.v1.DiffEntries"></a>

### DiffEntries
DiffEntries indicates potential multiple lines of config diff


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **values** | [DiffEntry](#diffentry)[...] | <p></p> |







<a name="arista.configstatus.v1.DiffEntry"></a>

### DiffEntry
DiffEntry represents one entry in a Diff


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **op** | [DiffOp](#diffop) | <p></p> |
| **a_line_num** | google.protobuf.Int32Value | <p>line number in A this diff applies to</p> |
| **b_line_num** | google.protobuf.Int32Value | <p>line number in B this diff applies to</p> |
| **b_parent_line_num** | google.protobuf.Int32Value | <p>line number in B of the leading command of the containing block</p> |
| **a_line** | google.protobuf.StringValue | <p>content of config line in A</p> |
| **b_line** | google.protobuf.StringValue | <p>content of config line in B</p> |
| **a_filter_code** | [ConfigFilterCode](#configfiltercode) | <p>Config filter code of the line in A</p> |
| **b_filter_code** | [ConfigFilterCode](#configfiltercode) | <p>Config filter code of the line in B</p> |







<a name="arista.configstatus.v1.Summary"></a>

### Summary



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [SummaryKey](#summarykey) | <p></p> |
| **summary** | [ConfigSummary](#configsummary) | <p></p> |
| **error** | [ConfigError](#configerror) | <p></p> |







<a name="arista.configstatus.v1.SummaryKey"></a>

### SummaryKey
SummaryKey uniquely identifies a device summary request


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **device_id** | google.protobuf.StringValue | <p>Device_id is the serial number of the device</p> |






 <!-- end messages -->


<a name="arista.configstatus.v1.ConfigFilterCode"></a>

### ConfigFilterCode
ConfigFilterCode indicates if a config line matches PCM filter(s)

| Name | Number | Description |
| ---- | ------ | ----------- |
| CONFIG_FILTER_CODE_UNSPECIFIED | 0 | <p>UNSPECIFIED indicates config line did not match any partial config management (PCM) filter</p> |
| CONFIG_FILTER_CODE_MANAGED_LINE | 1 | <p>MANAGED_LINE indicates config line matches managed PCM filter hence is managed</p> |
| CONFIG_FILTER_CODE_UNMANAGED_LINE | 2 | <p>UNMANAGED_LINE indicates config line matches unmanaged PCM filter hence is not managed</p> |



<a name="arista.configstatus.v1.ConfigSyncCode"></a>

### ConfigSyncCode
ConfigSyncCode indicates config synchronization status

| Name | Number | Description |
| ---- | ------ | ----------- |
| CONFIG_SYNC_CODE_UNSPECIFIED | 0 | <p></p> |
| CONFIG_SYNC_CODE_IN_SYNC | 1 | <p>IN_SYNC indicates designed config and running config are identical</p> |
| CONFIG_SYNC_CODE_OUT_OF_SYNC | 2 | <p>OUT_OF_SYNC indicates designed config and running config are not identical</p> |



<a name="arista.configstatus.v1.ConfigType"></a>

### ConfigType


| Name | Number | Description |
| ---- | ------ | ----------- |
| CONFIG_TYPE_UNSPECIFIED | 0 | <p></p> |
| CONFIG_TYPE_RUNNING_CONFIG | 1 | <p></p> |
| CONFIG_TYPE_DESIGNED_CONFIG | 2 | <p></p> |



<a name="arista.configstatus.v1.DiffOp"></a>

### DiffOp
DiffOp is the operation to a line from one side of diff to get to another

| Name | Number | Description |
| ---- | ------ | ----------- |
| DIFF_OP_UNSPECIFIED | 0 | <p></p> |
| DIFF_OP_NOP | 1 | <p>NOP indicates no change. A and B are identical at this line</p> |
| DIFF_OP_IGNORE | 2 | <p>IGNORE indicates a line that's ignored in either A or B.</p><p>One of a_line_num or b_line_num will be -1</p> |
| DIFF_OP_ADD | 3 | <p>ADD is an addition of a line from A</p> |
| DIFF_OP_DELETE | 4 | <p>DELETE is deletion of a line from B</p> |
| DIFF_OP_CHANGE | 5 | <p>CHANGE is a modification to a line in A</p> |



<a name="arista.configstatus.v1.ErrorCode"></a>

### ErrorCode
ErrorCode indicates warnings and errors produced during computing config

| Name | Number | Description |
| ---- | ------ | ----------- |
| ERROR_CODE_UNSPECIFIED | 0 | <p></p> |
| ERROR_CODE_DEVICE_WARNING | 1 | <p>DEVICE_WARNING indicates device warning</p> |
| ERROR_CODE_DEVICE_ERROR | 2 | <p>DEVICE_ERROR indicates device error</p> |
| ERROR_CODE_UNREACHABLE_DEVICE | 3 | <p>UNREACHABLE_DEVICE indicates the device cannot be reached</p> |
| ERROR_CODE_CONFIG_FILTER_ERROR | 4 | <p>CONFIG_FILTER_ERROR indicates error from partial config management filters</p> |
| ERROR_CODE_INTERNAL | 5 | <p>INTERNAL indicates internal errors</p> |


 <!-- end enums -->

 <!-- end HasExtensions -->

 <!-- end services -->




<a name="arista/configstatus.v1/services.gen.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## arista/configstatus.v1/services.gen.proto



<a name="arista.configstatus.v1.ConfigDiffRequest"></a>

### ConfigDiffRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [ConfigDiffKey](#configdiffkey) | <p>Key uniquely identifies a ConfigDiff instance to retrieve.</p><p>This value must be populated.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the time for which you are interested in the data.</p><p>If no time is given, the server will use the time at which it makes the request.</p> |







<a name="arista.configstatus.v1.ConfigDiffResponse"></a>

### ConfigDiffResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [ConfigDiff](#configdiff) | <p>Value is the value requested.</p><p>This structure will be fully-populated as it exists in the datastore. If</p><p>optional fields were not given at creation, these fields will be empty or</p><p>set to default values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time carries the (UTC) timestamp of the last-modification of the</p><p>ConfigDiff instance in this response.</p> |







<a name="arista.configstatus.v1.ConfigDiffStreamRequest"></a>

### ConfigDiffStreamRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **partial_eq_filter** | [ConfigDiff](#configdiff)[...] | <p>PartialEqFilter provides a way to server-side filter a GetAll/Subscribe.</p><p>This requires all provided fields to be equal to the response.</p><p>While transparent to users, this field also allows services to optimize internal</p><p>subscriptions if filter(s) are sufficiently specific.</p> |
| **time** | arista.time.TimeBounds | <p>TimeRange allows limiting response data to within a specified time window.</p><p>If this field is populated, at least one of the two time fields are required.</p><p>This field is not allowed in the Subscribe RPC.</p> |







<a name="arista.configstatus.v1.ConfigDiffStreamResponse"></a>

### ConfigDiffStreamResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [ConfigDiff](#configdiff) | <p>Value is a value deemed relevant to the initiating request.</p><p>This structure will always have its key-field populated. Which other fields are</p><p>populated, and why, depends on the value of Operation and what triggered this notification.</p> |
| **time** | google.protobuf.Timestamp | <p>Time holds the timestamp of this ConfigDiff's last modification.</p> |
| **type** | arista.subscriptions.Operation | <p>Operation indicates how the ConfigDiff value in this response should be considered.</p><p>Under non-subscribe requests, this value should always be INITIAL. In a subscription,</p><p>once all initial data is streamed and the client begins to receive modification updates,</p><p>you should not see INITIAL again.</p> |







<a name="arista.configstatus.v1.ConfigurationRequest"></a>

### ConfigurationRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [ConfigKey](#configkey) | <p>Key uniquely identifies a Configuration instance to retrieve.</p><p>This value must be populated.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the time for which you are interested in the data.</p><p>If no time is given, the server will use the time at which it makes the request.</p> |







<a name="arista.configstatus.v1.ConfigurationResponse"></a>

### ConfigurationResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [Configuration](#configuration) | <p>Value is the value requested.</p><p>This structure will be fully-populated as it exists in the datastore. If</p><p>optional fields were not given at creation, these fields will be empty or</p><p>set to default values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time carries the (UTC) timestamp of the last-modification of the</p><p>Configuration instance in this response.</p> |







<a name="arista.configstatus.v1.ConfigurationStreamRequest"></a>

### ConfigurationStreamRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **partial_eq_filter** | [Configuration](#configuration)[...] | <p>PartialEqFilter provides a way to server-side filter a GetAll/Subscribe.</p><p>This requires all provided fields to be equal to the response.</p><p>While transparent to users, this field also allows services to optimize internal</p><p>subscriptions if filter(s) are sufficiently specific.</p> |
| **time** | arista.time.TimeBounds | <p>TimeRange allows limiting response data to within a specified time window.</p><p>If this field is populated, at least one of the two time fields are required.</p><p>This field is not allowed in the Subscribe RPC.</p> |







<a name="arista.configstatus.v1.ConfigurationStreamResponse"></a>

### ConfigurationStreamResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [Configuration](#configuration) | <p>Value is a value deemed relevant to the initiating request.</p><p>This structure will always have its key-field populated. Which other fields are</p><p>populated, and why, depends on the value of Operation and what triggered this notification.</p> |
| **time** | google.protobuf.Timestamp | <p>Time holds the timestamp of this Configuration's last modification.</p> |
| **type** | arista.subscriptions.Operation | <p>Operation indicates how the Configuration value in this response should be considered.</p><p>Under non-subscribe requests, this value should always be INITIAL. In a subscription,</p><p>once all initial data is streamed and the client begins to receive modification updates,</p><p>you should not see INITIAL again.</p> |







<a name="arista.configstatus.v1.SummaryRequest"></a>

### SummaryRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [SummaryKey](#summarykey) | <p>Key uniquely identifies a Summary instance to retrieve.</p><p>This value must be populated.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the time for which you are interested in the data.</p><p>If no time is given, the server will use the time at which it makes the request.</p> |







<a name="arista.configstatus.v1.SummaryResponse"></a>

### SummaryResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [Summary](#summary) | <p>Value is the value requested.</p><p>This structure will be fully-populated as it exists in the datastore. If</p><p>optional fields were not given at creation, these fields will be empty or</p><p>set to default values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time carries the (UTC) timestamp of the last-modification of the</p><p>Summary instance in this response.</p> |







<a name="arista.configstatus.v1.SummaryStreamRequest"></a>

### SummaryStreamRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **partial_eq_filter** | [Summary](#summary)[...] | <p>PartialEqFilter provides a way to server-side filter a GetAll/Subscribe.</p><p>This requires all provided fields to be equal to the response.</p><p>While transparent to users, this field also allows services to optimize internal</p><p>subscriptions if filter(s) are sufficiently specific.</p> |
| **time** | arista.time.TimeBounds | <p>TimeRange allows limiting response data to within a specified time window.</p><p>If this field is populated, at least one of the two time fields are required.</p><p>This field is not allowed in the Subscribe RPC.</p> |







<a name="arista.configstatus.v1.SummaryStreamResponse"></a>

### SummaryStreamResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [Summary](#summary) | <p>Value is a value deemed relevant to the initiating request.</p><p>This structure will always have its key-field populated. Which other fields are</p><p>populated, and why, depends on the value of Operation and what triggered this notification.</p> |
| **time** | google.protobuf.Timestamp | <p>Time holds the timestamp of this Summary's last modification.</p> |
| **type** | arista.subscriptions.Operation | <p>Operation indicates how the Summary value in this response should be considered.</p><p>Under non-subscribe requests, this value should always be INITIAL. In a subscription,</p><p>once all initial data is streamed and the client begins to receive modification updates,</p><p>you should not see INITIAL again.</p> |






 <!-- end messages -->

 <!-- end enums -->

 <!-- end HasExtensions -->


<a name="arista.configstatus.v1.ConfigDiffService"></a>

### ConfigDiffService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetOne | [ConfigDiffRequest](#arista.configstatus.v1.ConfigDiffRequest) | [ConfigDiffResponse](#arista.configstatus.v1.ConfigDiffResponse) | <p></p> |
| GetAll | [ConfigDiffStreamRequest](#arista.configstatus.v1.ConfigDiffStreamRequest) | [ConfigDiffStreamResponse](#arista.configstatus.v1.ConfigDiffStreamResponse) stream | <p></p> |
| Subscribe | [ConfigDiffStreamRequest](#arista.configstatus.v1.ConfigDiffStreamRequest) | [ConfigDiffStreamResponse](#arista.configstatus.v1.ConfigDiffStreamResponse) stream | <p></p> |


<a name="arista.configstatus.v1.ConfigurationService"></a>

### ConfigurationService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetOne | [ConfigurationRequest](#arista.configstatus.v1.ConfigurationRequest) | [ConfigurationResponse](#arista.configstatus.v1.ConfigurationResponse) | <p></p> |
| GetAll | [ConfigurationStreamRequest](#arista.configstatus.v1.ConfigurationStreamRequest) | [ConfigurationStreamResponse](#arista.configstatus.v1.ConfigurationStreamResponse) stream | <p></p> |
| Subscribe | [ConfigurationStreamRequest](#arista.configstatus.v1.ConfigurationStreamRequest) | [ConfigurationStreamResponse](#arista.configstatus.v1.ConfigurationStreamResponse) stream | <p></p> |


<a name="arista.configstatus.v1.SummaryService"></a>

### SummaryService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetOne | [SummaryRequest](#arista.configstatus.v1.SummaryRequest) | [SummaryResponse](#arista.configstatus.v1.SummaryResponse) | <p></p> |
| GetAll | [SummaryStreamRequest](#arista.configstatus.v1.SummaryStreamRequest) | [SummaryStreamResponse](#arista.configstatus.v1.SummaryStreamResponse) stream | <p></p> |
| Subscribe | [SummaryStreamRequest](#arista.configstatus.v1.SummaryStreamRequest) | [SummaryStreamResponse](#arista.configstatus.v1.SummaryStreamResponse) stream | <p></p> |

 <!-- end services -->



