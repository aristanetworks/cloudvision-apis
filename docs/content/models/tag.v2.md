---
title: tag.v2
---



- [arista/tag.v2/tag.proto](#arista/tag.v2/tag.proto)
    - [Tag](#tag)
    - [TagAssignment](#tagassignment)
    - [TagAssignmentConfig](#tagassignmentconfig)
    - [TagAssignmentKey](#tagassignmentkey)
    - [TagConfig](#tagconfig)
    - [TagKey](#tagkey)
  
    - [CreatorType](#arista.tag.v2.CreatorType)
    - [ElementType](#arista.tag.v2.ElementType)
  
- [arista/tag.v2/services.gen.proto](#arista/tag.v2/services.gen.proto)
    - [TagAssignmentConfigDeleteRequest](#tagassignmentconfigdeleterequest)
    - [TagAssignmentConfigDeleteResponse](#tagassignmentconfigdeleteresponse)
    - [TagAssignmentConfigRequest](#tagassignmentconfigrequest)
    - [TagAssignmentConfigResponse](#tagassignmentconfigresponse)
    - [TagAssignmentConfigSetRequest](#tagassignmentconfigsetrequest)
    - [TagAssignmentConfigSetResponse](#tagassignmentconfigsetresponse)
    - [TagAssignmentConfigStreamRequest](#tagassignmentconfigstreamrequest)
    - [TagAssignmentConfigStreamResponse](#tagassignmentconfigstreamresponse)
    - [TagAssignmentRequest](#tagassignmentrequest)
    - [TagAssignmentResponse](#tagassignmentresponse)
    - [TagAssignmentStreamRequest](#tagassignmentstreamrequest)
    - [TagAssignmentStreamResponse](#tagassignmentstreamresponse)
    - [TagConfigDeleteRequest](#tagconfigdeleterequest)
    - [TagConfigDeleteResponse](#tagconfigdeleteresponse)
    - [TagConfigRequest](#tagconfigrequest)
    - [TagConfigResponse](#tagconfigresponse)
    - [TagConfigSetRequest](#tagconfigsetrequest)
    - [TagConfigSetResponse](#tagconfigsetresponse)
    - [TagConfigStreamRequest](#tagconfigstreamrequest)
    - [TagConfigStreamResponse](#tagconfigstreamresponse)
    - [TagRequest](#tagrequest)
    - [TagResponse](#tagresponse)
    - [TagStreamRequest](#tagstreamrequest)
    - [TagStreamResponse](#tagstreamresponse)
  
    - [TagAssignmentConfigService](#arista.tag.v2.TagAssignmentConfigService)
    - [TagAssignmentService](#arista.tag.v2.TagAssignmentService)
    - [TagConfigService](#arista.tag.v2.TagConfigService)
    - [TagService](#arista.tag.v2.TagService)
  




<a name="arista/tag.v2/tag.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## arista/tag.v2/tag.proto



<a name="arista.tag.v2.Tag"></a>

### Tag
Tag holds a merge-preview or the existing merged state (if the
workspace ID is "") of a tag.


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [TagKey](#tagkey) | <p>key identifies a tag.</p> |
| **creator_type** | [CreatorType](#creatortype) | <p>creator_type is the creator type of the tag.</p> |







<a name="arista.tag.v2.TagAssignment"></a>

### TagAssignment
TagAssignment holds a merge-preview or the existing merged
state (if the workspace ID is "") of an assignment between
a tag and a network element.


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [TagAssignmentKey](#tagassignmentkey) | <p>key identifies an assignment.</p> |







<a name="arista.tag.v2.TagAssignmentConfig"></a>

### TagAssignmentConfig
TagAssignmentConfig holds a configuration for an assignment
between a tag and a network element.


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [TagAssignmentKey](#tagassignmentkey) | <p>key identifies an assignment. The special workspace ID ""</p><p>for merged assignments should not be set here.</p> |
| **remove** | google.protobuf.BoolValue | <p>remove indicates whether to remove (true) or add (false,</p><p>unset) the assignment identified by the key if the</p><p>encompassing workspace merges.</p> |







<a name="arista.tag.v2.TagAssignmentKey"></a>

### TagAssignmentKey
TagAssignmentKey uniquely identifies an assignment between
a tag and a network element.


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **workspace_id** | google.protobuf.StringValue | <p>workspace_id is the ID of a workspace. The special ID ""</p><p>identifies the location where merged assignments reside.</p> |
| **element_type** | [ElementType](#elementtype) | <p>element_type is the element type of a tag. What should</p><p>be set per element type:</p><p>ELEMENT_TYPE_DEVICE: device_id</p><p>ELEMENT_TYPE_INTERFACE: device_id, interface_id</p> |
| **label** | google.protobuf.StringValue | <p>label is the label of a tag.</p> |
| **value** | google.protobuf.StringValue | <p>value is the value of a tag.</p> |
| **device_id** | google.protobuf.StringValue | <p>device_id identifies a device.</p> |
| **interface_id** | google.protobuf.StringValue | <p>interface_id identifies an interface on a device.</p> |







<a name="arista.tag.v2.TagConfig"></a>

### TagConfig
TagConfig holds a configuration for a user tag.


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [TagKey](#tagkey) | <p>key identifies a tag. The special workspace ID "" for</p><p>merged tags should not be set here.</p> |
| **remove** | google.protobuf.BoolValue | <p>remove indicates whether to remove (true) or add (false,</p><p>unset) the tag identified by the key if the encompassing</p><p>workspace merges.</p> |







<a name="arista.tag.v2.TagKey"></a>

### TagKey
TagKey uniquely identifies a tag.


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **workspace_id** | google.protobuf.StringValue | <p>workspace_id is the ID of a workspace. The special ID ""</p><p>identifies the location where merged tags reside.</p> |
| **element_type** | [ElementType](#elementtype) | <p>element_type is the category of network element to which</p><p>this tag can be assigned.</p> |
| **label** | google.protobuf.StringValue | <p>label is an arbitrary label.</p> |
| **value** | google.protobuf.StringValue | <p>value is an arbitrary value.</p> |






 <!-- end messages -->


<a name="arista.tag.v2.CreatorType"></a>

### CreatorType
CreatorType enumerates the types of entities that can create
a tag.

| Name | Number | Description |
| ---- | ------ | ----------- |
| CREATOR_TYPE_UNSPECIFIED | 0 | <p></p> |
| CREATOR_TYPE_SYSTEM | 1 | <p>CREATOR_TYPE_SYSTEM is used for system tags.</p> |
| CREATOR_TYPE_USER | 2 | <p>CREATOR_TYPE_USER is used for user tags.</p> |



<a name="arista.tag.v2.ElementType"></a>

### ElementType
ElementType enumerates the types of network elements that can
be associated with tags.

| Name | Number | Description |
| ---- | ------ | ----------- |
| ELEMENT_TYPE_UNSPECIFIED | 0 | <p></p> |
| ELEMENT_TYPE_DEVICE | 1 | <p>ELEMENT_TYPE_DEVICE is used for device tags.</p> |
| ELEMENT_TYPE_INTERFACE | 2 | <p>ELEMENT_TYPE_INTERFACE is used for interface tags.</p> |


 <!-- end enums -->

 <!-- end HasExtensions -->

 <!-- end services -->




<a name="arista/tag.v2/services.gen.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## arista/tag.v2/services.gen.proto



<a name="arista.tag.v2.TagAssignmentConfigDeleteRequest"></a>

### TagAssignmentConfigDeleteRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [TagAssignmentKey](#tagassignmentkey) | <p>Key indicates which TagAssignmentConfig instance to remove.</p><p>This field must always be set.</p> |







<a name="arista.tag.v2.TagAssignmentConfigDeleteResponse"></a>

### TagAssignmentConfigDeleteResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [TagAssignmentKey](#tagassignmentkey) | <p>Key echoes back the key of the deleted TagAssignmentConfig instance.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the (UTC) timestamp at which the system recognizes the</p><p>deletion. The only guarantees made about this timestamp are:</p><p>- it is after the time the request was received</p><p>- a time-ranged query with StartTime==DeletedAt will not include this instance.</p> |







<a name="arista.tag.v2.TagAssignmentConfigRequest"></a>

### TagAssignmentConfigRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [TagAssignmentKey](#tagassignmentkey) | <p>Key uniquely identifies a TagAssignmentConfig instance to retrieve.</p><p>This value must be populated.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the time for which you are interested in the data.</p><p>If no time is given, the server will use the time at which it makes the request.</p> |







<a name="arista.tag.v2.TagAssignmentConfigResponse"></a>

### TagAssignmentConfigResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [TagAssignmentConfig](#tagassignmentconfig) | <p>Value is the value requested.</p><p>This structure will be fully-populated as it exists in the datastore. If</p><p>optional fields were not given at creation, these fields will be empty or</p><p>set to default values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time carries the (UTC) timestamp of the last-modification of the</p><p>TagAssignmentConfig instance in this response.</p> |







<a name="arista.tag.v2.TagAssignmentConfigSetRequest"></a>

### TagAssignmentConfigSetRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [TagAssignmentConfig](#tagassignmentconfig) | <p>TagAssignmentConfig carries the value to set into the datastore.</p><p>See the documentation on the TagAssignmentConfig struct for which fields are required.</p> |







<a name="arista.tag.v2.TagAssignmentConfigSetResponse"></a>

### TagAssignmentConfigSetResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [TagAssignmentConfig](#tagassignmentconfig) | <p>Value carries all the values given in the TagAssignmentConfigSetRequest as well</p><p>as any server-generated values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the (UTC) timestamp at which the system recognizes the</p><p>creation. The only guarantees made about this timestamp are:</p><p>- it is after the time the request was received</p><p>- a time-ranged query with StartTime==CreatedAt will include this instance.</p> |







<a name="arista.tag.v2.TagAssignmentConfigStreamRequest"></a>

### TagAssignmentConfigStreamRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **partial_eq_filter** | [TagAssignmentConfig](#tagassignmentconfig)[...] | <p>PartialEqFilter provides a way to server-side filter a GetAll/Subscribe.</p><p>This requires all provided fields to be equal to the response.</p><p>While transparent to users, this field also allows services to optimize internal</p><p>subscriptions if filter(s) are sufficiently specific.</p> |
| **time** | arista.time.TimeBounds | <p>TimeRange allows limiting response data to within a specified time window.</p><p>If this field is populated, at least one of the two time fields are required.</p><p>This field is not allowed in the Subscribe RPC.</p> |







<a name="arista.tag.v2.TagAssignmentConfigStreamResponse"></a>

### TagAssignmentConfigStreamResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [TagAssignmentConfig](#tagassignmentconfig) | <p>Value is a value deemed relevant to the initiating request.</p><p>This structure will always have its key-field populated. Which other fields are</p><p>populated, and why, depends on the value of Operation and what triggered this notification.</p> |
| **time** | google.protobuf.Timestamp | <p>Time holds the timestamp of this TagAssignmentConfig's last modification.</p> |
| **type** | arista.subscriptions.Operation | <p>Operation indicates how the TagAssignmentConfig value in this response should be considered.</p><p>Under non-subscribe requests, this value should always be INITIAL. In a subscription,</p><p>once all initial data is streamed and the client begins to receive modification updates,</p><p>you should not see INITIAL again.</p> |







<a name="arista.tag.v2.TagAssignmentRequest"></a>

### TagAssignmentRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [TagAssignmentKey](#tagassignmentkey) | <p>Key uniquely identifies a TagAssignment instance to retrieve.</p><p>This value must be populated.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the time for which you are interested in the data.</p><p>If no time is given, the server will use the time at which it makes the request.</p> |







<a name="arista.tag.v2.TagAssignmentResponse"></a>

### TagAssignmentResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [TagAssignment](#tagassignment) | <p>Value is the value requested.</p><p>This structure will be fully-populated as it exists in the datastore. If</p><p>optional fields were not given at creation, these fields will be empty or</p><p>set to default values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time carries the (UTC) timestamp of the last-modification of the</p><p>TagAssignment instance in this response.</p> |







<a name="arista.tag.v2.TagAssignmentStreamRequest"></a>

### TagAssignmentStreamRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **partial_eq_filter** | [TagAssignment](#tagassignment)[...] | <p>PartialEqFilter provides a way to server-side filter a GetAll/Subscribe.</p><p>This requires all provided fields to be equal to the response.</p><p>While transparent to users, this field also allows services to optimize internal</p><p>subscriptions if filter(s) are sufficiently specific.</p> |
| **time** | arista.time.TimeBounds | <p>TimeRange allows limiting response data to within a specified time window.</p><p>If this field is populated, at least one of the two time fields are required.</p><p>This field is not allowed in the Subscribe RPC.</p> |







<a name="arista.tag.v2.TagAssignmentStreamResponse"></a>

### TagAssignmentStreamResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [TagAssignment](#tagassignment) | <p>Value is a value deemed relevant to the initiating request.</p><p>This structure will always have its key-field populated. Which other fields are</p><p>populated, and why, depends on the value of Operation and what triggered this notification.</p> |
| **time** | google.protobuf.Timestamp | <p>Time holds the timestamp of this TagAssignment's last modification.</p> |
| **type** | arista.subscriptions.Operation | <p>Operation indicates how the TagAssignment value in this response should be considered.</p><p>Under non-subscribe requests, this value should always be INITIAL. In a subscription,</p><p>once all initial data is streamed and the client begins to receive modification updates,</p><p>you should not see INITIAL again.</p> |







<a name="arista.tag.v2.TagConfigDeleteRequest"></a>

### TagConfigDeleteRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [TagKey](#tagkey) | <p>Key indicates which TagConfig instance to remove.</p><p>This field must always be set.</p> |







<a name="arista.tag.v2.TagConfigDeleteResponse"></a>

### TagConfigDeleteResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [TagKey](#tagkey) | <p>Key echoes back the key of the deleted TagConfig instance.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the (UTC) timestamp at which the system recognizes the</p><p>deletion. The only guarantees made about this timestamp are:</p><p>- it is after the time the request was received</p><p>- a time-ranged query with StartTime==DeletedAt will not include this instance.</p> |







<a name="arista.tag.v2.TagConfigRequest"></a>

### TagConfigRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [TagKey](#tagkey) | <p>Key uniquely identifies a TagConfig instance to retrieve.</p><p>This value must be populated.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the time for which you are interested in the data.</p><p>If no time is given, the server will use the time at which it makes the request.</p> |







<a name="arista.tag.v2.TagConfigResponse"></a>

### TagConfigResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [TagConfig](#tagconfig) | <p>Value is the value requested.</p><p>This structure will be fully-populated as it exists in the datastore. If</p><p>optional fields were not given at creation, these fields will be empty or</p><p>set to default values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time carries the (UTC) timestamp of the last-modification of the</p><p>TagConfig instance in this response.</p> |







<a name="arista.tag.v2.TagConfigSetRequest"></a>

### TagConfigSetRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [TagConfig](#tagconfig) | <p>TagConfig carries the value to set into the datastore.</p><p>See the documentation on the TagConfig struct for which fields are required.</p> |







<a name="arista.tag.v2.TagConfigSetResponse"></a>

### TagConfigSetResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [TagConfig](#tagconfig) | <p>Value carries all the values given in the TagConfigSetRequest as well</p><p>as any server-generated values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the (UTC) timestamp at which the system recognizes the</p><p>creation. The only guarantees made about this timestamp are:</p><p>- it is after the time the request was received</p><p>- a time-ranged query with StartTime==CreatedAt will include this instance.</p> |







<a name="arista.tag.v2.TagConfigStreamRequest"></a>

### TagConfigStreamRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **partial_eq_filter** | [TagConfig](#tagconfig)[...] | <p>PartialEqFilter provides a way to server-side filter a GetAll/Subscribe.</p><p>This requires all provided fields to be equal to the response.</p><p>While transparent to users, this field also allows services to optimize internal</p><p>subscriptions if filter(s) are sufficiently specific.</p> |
| **time** | arista.time.TimeBounds | <p>TimeRange allows limiting response data to within a specified time window.</p><p>If this field is populated, at least one of the two time fields are required.</p><p>This field is not allowed in the Subscribe RPC.</p> |







<a name="arista.tag.v2.TagConfigStreamResponse"></a>

### TagConfigStreamResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [TagConfig](#tagconfig) | <p>Value is a value deemed relevant to the initiating request.</p><p>This structure will always have its key-field populated. Which other fields are</p><p>populated, and why, depends on the value of Operation and what triggered this notification.</p> |
| **time** | google.protobuf.Timestamp | <p>Time holds the timestamp of this TagConfig's last modification.</p> |
| **type** | arista.subscriptions.Operation | <p>Operation indicates how the TagConfig value in this response should be considered.</p><p>Under non-subscribe requests, this value should always be INITIAL. In a subscription,</p><p>once all initial data is streamed and the client begins to receive modification updates,</p><p>you should not see INITIAL again.</p> |







<a name="arista.tag.v2.TagRequest"></a>

### TagRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [TagKey](#tagkey) | <p>Key uniquely identifies a Tag instance to retrieve.</p><p>This value must be populated.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the time for which you are interested in the data.</p><p>If no time is given, the server will use the time at which it makes the request.</p> |







<a name="arista.tag.v2.TagResponse"></a>

### TagResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [Tag](#tag) | <p>Value is the value requested.</p><p>This structure will be fully-populated as it exists in the datastore. If</p><p>optional fields were not given at creation, these fields will be empty or</p><p>set to default values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time carries the (UTC) timestamp of the last-modification of the</p><p>Tag instance in this response.</p> |







<a name="arista.tag.v2.TagStreamRequest"></a>

### TagStreamRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **partial_eq_filter** | [Tag](#tag)[...] | <p>PartialEqFilter provides a way to server-side filter a GetAll/Subscribe.</p><p>This requires all provided fields to be equal to the response.</p><p>While transparent to users, this field also allows services to optimize internal</p><p>subscriptions if filter(s) are sufficiently specific.</p> |
| **time** | arista.time.TimeBounds | <p>TimeRange allows limiting response data to within a specified time window.</p><p>If this field is populated, at least one of the two time fields are required.</p><p>This field is not allowed in the Subscribe RPC.</p> |







<a name="arista.tag.v2.TagStreamResponse"></a>

### TagStreamResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [Tag](#tag) | <p>Value is a value deemed relevant to the initiating request.</p><p>This structure will always have its key-field populated. Which other fields are</p><p>populated, and why, depends on the value of Operation and what triggered this notification.</p> |
| **time** | google.protobuf.Timestamp | <p>Time holds the timestamp of this Tag's last modification.</p> |
| **type** | arista.subscriptions.Operation | <p>Operation indicates how the Tag value in this response should be considered.</p><p>Under non-subscribe requests, this value should always be INITIAL. In a subscription,</p><p>once all initial data is streamed and the client begins to receive modification updates,</p><p>you should not see INITIAL again.</p> |






 <!-- end messages -->

 <!-- end enums -->

 <!-- end HasExtensions -->


<a name="arista.tag.v2.TagAssignmentConfigService"></a>

### TagAssignmentConfigService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetOne | [TagAssignmentConfigRequest](#arista.tag.v2.TagAssignmentConfigRequest) | [TagAssignmentConfigResponse](#arista.tag.v2.TagAssignmentConfigResponse) | <p></p> |
| GetAll | [TagAssignmentConfigStreamRequest](#arista.tag.v2.TagAssignmentConfigStreamRequest) | [TagAssignmentConfigStreamResponse](#arista.tag.v2.TagAssignmentConfigStreamResponse) stream | <p></p> |
| Subscribe | [TagAssignmentConfigStreamRequest](#arista.tag.v2.TagAssignmentConfigStreamRequest) | [TagAssignmentConfigStreamResponse](#arista.tag.v2.TagAssignmentConfigStreamResponse) stream | <p></p> |
| Set | [TagAssignmentConfigSetRequest](#arista.tag.v2.TagAssignmentConfigSetRequest) | [TagAssignmentConfigSetResponse](#arista.tag.v2.TagAssignmentConfigSetResponse) | <p></p> |
| Delete | [TagAssignmentConfigDeleteRequest](#arista.tag.v2.TagAssignmentConfigDeleteRequest) | [TagAssignmentConfigDeleteResponse](#arista.tag.v2.TagAssignmentConfigDeleteResponse) | <p></p> |


<a name="arista.tag.v2.TagAssignmentService"></a>

### TagAssignmentService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetOne | [TagAssignmentRequest](#arista.tag.v2.TagAssignmentRequest) | [TagAssignmentResponse](#arista.tag.v2.TagAssignmentResponse) | <p></p> |
| GetAll | [TagAssignmentStreamRequest](#arista.tag.v2.TagAssignmentStreamRequest) | [TagAssignmentStreamResponse](#arista.tag.v2.TagAssignmentStreamResponse) stream | <p></p> |
| Subscribe | [TagAssignmentStreamRequest](#arista.tag.v2.TagAssignmentStreamRequest) | [TagAssignmentStreamResponse](#arista.tag.v2.TagAssignmentStreamResponse) stream | <p></p> |


<a name="arista.tag.v2.TagConfigService"></a>

### TagConfigService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetOne | [TagConfigRequest](#arista.tag.v2.TagConfigRequest) | [TagConfigResponse](#arista.tag.v2.TagConfigResponse) | <p></p> |
| GetAll | [TagConfigStreamRequest](#arista.tag.v2.TagConfigStreamRequest) | [TagConfigStreamResponse](#arista.tag.v2.TagConfigStreamResponse) stream | <p></p> |
| Subscribe | [TagConfigStreamRequest](#arista.tag.v2.TagConfigStreamRequest) | [TagConfigStreamResponse](#arista.tag.v2.TagConfigStreamResponse) stream | <p></p> |
| Set | [TagConfigSetRequest](#arista.tag.v2.TagConfigSetRequest) | [TagConfigSetResponse](#arista.tag.v2.TagConfigSetResponse) | <p></p> |
| Delete | [TagConfigDeleteRequest](#arista.tag.v2.TagConfigDeleteRequest) | [TagConfigDeleteResponse](#arista.tag.v2.TagConfigDeleteResponse) | <p></p> |


<a name="arista.tag.v2.TagService"></a>

### TagService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetOne | [TagRequest](#arista.tag.v2.TagRequest) | [TagResponse](#arista.tag.v2.TagResponse) | <p></p> |
| GetAll | [TagStreamRequest](#arista.tag.v2.TagStreamRequest) | [TagStreamResponse](#arista.tag.v2.TagStreamResponse) stream | <p></p> |
| Subscribe | [TagStreamRequest](#arista.tag.v2.TagStreamRequest) | [TagStreamResponse](#arista.tag.v2.TagStreamResponse) stream | <p></p> |

 <!-- end services -->



