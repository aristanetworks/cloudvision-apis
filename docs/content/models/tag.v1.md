---
title: tag.v1
---



- [arista/tag.v1/tag.proto](#arista/tag.v1/tag.proto)
    - [DeviceTag](#devicetag)
    - [DeviceTagAssignmentConfig](#devicetagassignmentconfig)
    - [DeviceTagAssignmentKey](#devicetagassignmentkey)
    - [DeviceTagConfig](#devicetagconfig)
    - [InterfaceTag](#interfacetag)
    - [InterfaceTagAssignmentConfig](#interfacetagassignmentconfig)
    - [InterfaceTagAssignmentKey](#interfacetagassignmentkey)
    - [InterfaceTagConfig](#interfacetagconfig)
    - [TagKey](#tagkey)
  
    - [CreatorType](#arista.tag.v1.CreatorType)
  
- [arista/tag.v1/services.gen.proto](#arista/tag.v1/services.gen.proto)
    - [DeviceTagAssignmentConfigDeleteRequest](#devicetagassignmentconfigdeleterequest)
    - [DeviceTagAssignmentConfigDeleteResponse](#devicetagassignmentconfigdeleteresponse)
    - [DeviceTagAssignmentConfigRequest](#devicetagassignmentconfigrequest)
    - [DeviceTagAssignmentConfigResponse](#devicetagassignmentconfigresponse)
    - [DeviceTagAssignmentConfigSetRequest](#devicetagassignmentconfigsetrequest)
    - [DeviceTagAssignmentConfigSetResponse](#devicetagassignmentconfigsetresponse)
    - [DeviceTagAssignmentConfigStreamRequest](#devicetagassignmentconfigstreamrequest)
    - [DeviceTagAssignmentConfigStreamResponse](#devicetagassignmentconfigstreamresponse)
    - [DeviceTagConfigDeleteRequest](#devicetagconfigdeleterequest)
    - [DeviceTagConfigDeleteResponse](#devicetagconfigdeleteresponse)
    - [DeviceTagConfigRequest](#devicetagconfigrequest)
    - [DeviceTagConfigResponse](#devicetagconfigresponse)
    - [DeviceTagConfigSetRequest](#devicetagconfigsetrequest)
    - [DeviceTagConfigSetResponse](#devicetagconfigsetresponse)
    - [DeviceTagConfigStreamRequest](#devicetagconfigstreamrequest)
    - [DeviceTagConfigStreamResponse](#devicetagconfigstreamresponse)
    - [DeviceTagRequest](#devicetagrequest)
    - [DeviceTagResponse](#devicetagresponse)
    - [DeviceTagStreamRequest](#devicetagstreamrequest)
    - [DeviceTagStreamResponse](#devicetagstreamresponse)
    - [InterfaceTagAssignmentConfigDeleteRequest](#interfacetagassignmentconfigdeleterequest)
    - [InterfaceTagAssignmentConfigDeleteResponse](#interfacetagassignmentconfigdeleteresponse)
    - [InterfaceTagAssignmentConfigRequest](#interfacetagassignmentconfigrequest)
    - [InterfaceTagAssignmentConfigResponse](#interfacetagassignmentconfigresponse)
    - [InterfaceTagAssignmentConfigSetRequest](#interfacetagassignmentconfigsetrequest)
    - [InterfaceTagAssignmentConfigSetResponse](#interfacetagassignmentconfigsetresponse)
    - [InterfaceTagAssignmentConfigStreamRequest](#interfacetagassignmentconfigstreamrequest)
    - [InterfaceTagAssignmentConfigStreamResponse](#interfacetagassignmentconfigstreamresponse)
    - [InterfaceTagConfigDeleteRequest](#interfacetagconfigdeleterequest)
    - [InterfaceTagConfigDeleteResponse](#interfacetagconfigdeleteresponse)
    - [InterfaceTagConfigRequest](#interfacetagconfigrequest)
    - [InterfaceTagConfigResponse](#interfacetagconfigresponse)
    - [InterfaceTagConfigSetRequest](#interfacetagconfigsetrequest)
    - [InterfaceTagConfigSetResponse](#interfacetagconfigsetresponse)
    - [InterfaceTagConfigStreamRequest](#interfacetagconfigstreamrequest)
    - [InterfaceTagConfigStreamResponse](#interfacetagconfigstreamresponse)
    - [InterfaceTagRequest](#interfacetagrequest)
    - [InterfaceTagResponse](#interfacetagresponse)
    - [InterfaceTagStreamRequest](#interfacetagstreamrequest)
    - [InterfaceTagStreamResponse](#interfacetagstreamresponse)
  
    - [DeviceTagAssignmentConfigService](#arista.tag.v1.DeviceTagAssignmentConfigService)
    - [DeviceTagConfigService](#arista.tag.v1.DeviceTagConfigService)
    - [DeviceTagService](#arista.tag.v1.DeviceTagService)
    - [InterfaceTagAssignmentConfigService](#arista.tag.v1.InterfaceTagAssignmentConfigService)
    - [InterfaceTagConfigService](#arista.tag.v1.InterfaceTagConfigService)
    - [InterfaceTagService](#arista.tag.v1.InterfaceTagService)
  




<a name="arista/tag.v1/tag.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## arista/tag.v1/tag.proto



<a name="arista.tag.v1.DeviceTag"></a>

### DeviceTag
DeviceTag is a label-value pair that may or may not
be assigned to a device.


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [TagKey](#tagkey) | <p>Key uniquely identifies the device tag.</p> |
| **creator_type** | [CreatorType](#creatortype) | <p>CreatorType is the creator type of the tag.</p> |







<a name="arista.tag.v1.DeviceTagAssignmentConfig"></a>

### DeviceTagAssignmentConfig
DeviceTagAssignmentConfig is the assignment of a device tag to a
specific device.


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [DeviceTagAssignmentKey](#devicetagassignmentkey) | <p>Key uniquely identifies the device tag assignment.</p> |







<a name="arista.tag.v1.DeviceTagAssignmentKey"></a>

### DeviceTagAssignmentKey
DeviceTagAssignmentKey uniquely identifies a device tag
assignment.


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **label** | google.protobuf.StringValue | <p>Label is the label of the tag.</p> |
| **value** | google.protobuf.StringValue | <p>Value is the value of the tag.</p> |
| **device_id** | google.protobuf.StringValue | <p>DeviceId is the ID of the device.</p> |







<a name="arista.tag.v1.DeviceTagConfig"></a>

### DeviceTagConfig
DeviceTagConfig is a label-value pair that may or may not
be assigned to a device.


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [TagKey](#tagkey) | <p>Key uniquely identifies the device tag.</p> |







<a name="arista.tag.v1.InterfaceTag"></a>

### InterfaceTag
InterfaceTag is a label-value pair that may or may
not be assigned to an interface.


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [TagKey](#tagkey) | <p>Key uniquely identifies the interface tag.</p> |
| **creator_type** | [CreatorType](#creatortype) | <p>CreatorType is the creator type of the tag.</p> |







<a name="arista.tag.v1.InterfaceTagAssignmentConfig"></a>

### InterfaceTagAssignmentConfig
InterfaceTagAssignmentConfig is the assignment of an interface tag
to a specific interface.


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [InterfaceTagAssignmentKey](#interfacetagassignmentkey) | <p>Key uniquely identifies the interface tag assignment.</p> |







<a name="arista.tag.v1.InterfaceTagAssignmentKey"></a>

### InterfaceTagAssignmentKey
InterfaceTagAssignmentKey uniquely identifies an interface
tag assignment.


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **label** | google.protobuf.StringValue | <p>Label is the label of the tag.</p> |
| **value** | google.protobuf.StringValue | <p>Value is the value of the tag.</p> |
| **device_id** | google.protobuf.StringValue | <p>DeviceId is the ID of the interface's device.</p> |
| **interface_id** | google.protobuf.StringValue | <p>InterfaceId is the ID of the interface.</p> |







<a name="arista.tag.v1.InterfaceTagConfig"></a>

### InterfaceTagConfig
InterfaceTagConfig is a label-value pair that may or may
not be assigned to an interface.


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [TagKey](#tagkey) | <p>Key uniquely identifies the interface tag.</p> |







<a name="arista.tag.v1.TagKey"></a>

### TagKey
TagKey uniquely identifies a tag for a network element.


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **label** | google.protobuf.StringValue | <p>Label is the label of the tag.</p> |
| **value** | google.protobuf.StringValue | <p>Value is the value of the tag.</p> |






 <!-- end messages -->


<a name="arista.tag.v1.CreatorType"></a>

### CreatorType
CreatorType specifies an entity that creates something.

| Name | Number | Description |
| ---- | ------ | ----------- |
| CREATOR_TYPE_UNSPECIFIED | 0 | <p></p> |
| CREATOR_TYPE_SYSTEM | 1 | <p>CREATOR_TYPE_SYSTEM is the type for something created by the system.</p> |
| CREATOR_TYPE_USER | 2 | <p>CREATOR_TYPE_USER is the type for something created by a user.</p> |


 <!-- end enums -->

 <!-- end HasExtensions -->

 <!-- end services -->




<a name="arista/tag.v1/services.gen.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## arista/tag.v1/services.gen.proto



<a name="arista.tag.v1.DeviceTagAssignmentConfigDeleteRequest"></a>

### DeviceTagAssignmentConfigDeleteRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [DeviceTagAssignmentKey](#devicetagassignmentkey) | <p>Key indicates which DeviceTagAssignmentConfig instance to remove.</p><p>This field (and all keys, unless otherwise specified) must always be set.</p> |







<a name="arista.tag.v1.DeviceTagAssignmentConfigDeleteResponse"></a>

### DeviceTagAssignmentConfigDeleteResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [DeviceTagAssignmentKey](#devicetagassignmentkey) | <p>Key echoes back the key of the deleted DeviceTagAssignmentConfig instance.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the (UTC) timestamp at which the system recognizes the</p><p>deletion. The only guarantees made about this timestamp are:</p><p>- it is after the time the request was received</p><p>- a time-ranged query with StartTime==DeletedAt will not include this instance.</p> |







<a name="arista.tag.v1.DeviceTagAssignmentConfigRequest"></a>

### DeviceTagAssignmentConfigRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [DeviceTagAssignmentKey](#devicetagassignmentkey) | <p>Key uniquely identifies a DeviceTagAssignmentConfig instance to retrieve.</p><p>This value (and all fields, unless otherwise specified) must be populated.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the time for which you are interested in the data.</p><p>If no time is given, the server will use the time at twhich it makes the request.</p> |







<a name="arista.tag.v1.DeviceTagAssignmentConfigResponse"></a>

### DeviceTagAssignmentConfigResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [DeviceTagAssignmentConfig](#devicetagassignmentconfig) | <p>Value is the value requested.</p><p>This structure will be fully-populated as it exists in the datastore. If</p><p>optional fields were not given at creation, these fields will be empty or</p><p>set to default values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time carries the (UTC) timestamp of the last-modification of the</p><p>DeviceTagAssignmentConfig instance in this response.</p> |







<a name="arista.tag.v1.DeviceTagAssignmentConfigSetRequest"></a>

### DeviceTagAssignmentConfigSetRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [DeviceTagAssignmentConfig](#devicetagassignmentconfig) | <p>DeviceTagAssignmentConfig carries the value to set into the datastore.</p><p>See the documentation on the DeviceTagAssignmentConfig struct for which fields are required.</p> |







<a name="arista.tag.v1.DeviceTagAssignmentConfigSetResponse"></a>

### DeviceTagAssignmentConfigSetResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [DeviceTagAssignmentConfig](#devicetagassignmentconfig) | <p>Value carries all the values given in the DeviceTagAssignmentConfigSetRequest as well</p><p>as any server-generated values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the (UTC) timestamp at which the system recognizes the</p><p>creation. The only guarantees made about this timestamp are:</p><p>- it is after the time the request was received</p><p>- a time-ranged query with StartTime==CreatedAt will include this instance.</p> |







<a name="arista.tag.v1.DeviceTagAssignmentConfigStreamRequest"></a>

### DeviceTagAssignmentConfigStreamRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **partial_eq_filter** | [DeviceTagAssignmentConfig](#devicetagassignmentconfig)[...] | <p>PartialEqFilter provides a way to server-side filter a GetAll/Subscribe.</p><p>This requires all provided fields to be equal to the response.</p><p>While transparent to users, this field also allows services to optimize internal</p><p>subscriptions if filter(s) are sufficiently specific.</p> |
| **time** | arista.time.TimeBounds | <p>TimeRange allows limiting response data to within a specified time window.</p><p>If this field is populated, at least one of the two time fields are required.</p><p>This field is not allowed in the Subscribe RPC.</p> |







<a name="arista.tag.v1.DeviceTagAssignmentConfigStreamResponse"></a>

### DeviceTagAssignmentConfigStreamResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [DeviceTagAssignmentConfig](#devicetagassignmentconfig) | <p>Value is a value deemed relevant to the initiating request.</p><p>This structure will always have its key-field populated. Which other fields are</p><p>populated, and why, depends on the value of Operation and what triggered this notification.</p> |
| **time** | google.protobuf.Timestamp | <p>Time holds the timestamp of this DeviceTagAssignmentConfig's last modification.</p> |
| **type** | arista.subscriptions.Operation | <p>Operation indicates how the DeviceTagAssignmentConfig value in this response should be considered.</p><p>Under non-subscribe requests, this value should always be INITIAL. In a subscription,</p><p>once all initial data is streamed and the client begins to receive modification updates,</p><p>you should not see INITIAL again.</p> |







<a name="arista.tag.v1.DeviceTagConfigDeleteRequest"></a>

### DeviceTagConfigDeleteRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [TagKey](#tagkey) | <p>Key indicates which DeviceTagConfig instance to remove.</p><p>This field (and all keys, unless otherwise specified) must always be set.</p> |







<a name="arista.tag.v1.DeviceTagConfigDeleteResponse"></a>

### DeviceTagConfigDeleteResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [TagKey](#tagkey) | <p>Key echoes back the key of the deleted DeviceTagConfig instance.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the (UTC) timestamp at which the system recognizes the</p><p>deletion. The only guarantees made about this timestamp are:</p><p>- it is after the time the request was received</p><p>- a time-ranged query with StartTime==DeletedAt will not include this instance.</p> |







<a name="arista.tag.v1.DeviceTagConfigRequest"></a>

### DeviceTagConfigRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [TagKey](#tagkey) | <p>Key uniquely identifies a DeviceTagConfig instance to retrieve.</p><p>This value (and all fields, unless otherwise specified) must be populated.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the time for which you are interested in the data.</p><p>If no time is given, the server will use the time at twhich it makes the request.</p> |







<a name="arista.tag.v1.DeviceTagConfigResponse"></a>

### DeviceTagConfigResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [DeviceTagConfig](#devicetagconfig) | <p>Value is the value requested.</p><p>This structure will be fully-populated as it exists in the datastore. If</p><p>optional fields were not given at creation, these fields will be empty or</p><p>set to default values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time carries the (UTC) timestamp of the last-modification of the</p><p>DeviceTagConfig instance in this response.</p> |







<a name="arista.tag.v1.DeviceTagConfigSetRequest"></a>

### DeviceTagConfigSetRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [DeviceTagConfig](#devicetagconfig) | <p>DeviceTagConfig carries the value to set into the datastore.</p><p>See the documentation on the DeviceTagConfig struct for which fields are required.</p> |







<a name="arista.tag.v1.DeviceTagConfigSetResponse"></a>

### DeviceTagConfigSetResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [DeviceTagConfig](#devicetagconfig) | <p>Value carries all the values given in the DeviceTagConfigSetRequest as well</p><p>as any server-generated values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the (UTC) timestamp at which the system recognizes the</p><p>creation. The only guarantees made about this timestamp are:</p><p>- it is after the time the request was received</p><p>- a time-ranged query with StartTime==CreatedAt will include this instance.</p> |







<a name="arista.tag.v1.DeviceTagConfigStreamRequest"></a>

### DeviceTagConfigStreamRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **partial_eq_filter** | [DeviceTagConfig](#devicetagconfig)[...] | <p>PartialEqFilter provides a way to server-side filter a GetAll/Subscribe.</p><p>This requires all provided fields to be equal to the response.</p><p>While transparent to users, this field also allows services to optimize internal</p><p>subscriptions if filter(s) are sufficiently specific.</p> |
| **time** | arista.time.TimeBounds | <p>TimeRange allows limiting response data to within a specified time window.</p><p>If this field is populated, at least one of the two time fields are required.</p><p>This field is not allowed in the Subscribe RPC.</p> |







<a name="arista.tag.v1.DeviceTagConfigStreamResponse"></a>

### DeviceTagConfigStreamResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [DeviceTagConfig](#devicetagconfig) | <p>Value is a value deemed relevant to the initiating request.</p><p>This structure will always have its key-field populated. Which other fields are</p><p>populated, and why, depends on the value of Operation and what triggered this notification.</p> |
| **time** | google.protobuf.Timestamp | <p>Time holds the timestamp of this DeviceTagConfig's last modification.</p> |
| **type** | arista.subscriptions.Operation | <p>Operation indicates how the DeviceTagConfig value in this response should be considered.</p><p>Under non-subscribe requests, this value should always be INITIAL. In a subscription,</p><p>once all initial data is streamed and the client begins to receive modification updates,</p><p>you should not see INITIAL again.</p> |







<a name="arista.tag.v1.DeviceTagRequest"></a>

### DeviceTagRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [TagKey](#tagkey) | <p>Key uniquely identifies a DeviceTag instance to retrieve.</p><p>This value (and all fields, unless otherwise specified) must be populated.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the time for which you are interested in the data.</p><p>If no time is given, the server will use the time at twhich it makes the request.</p> |







<a name="arista.tag.v1.DeviceTagResponse"></a>

### DeviceTagResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [DeviceTag](#devicetag) | <p>Value is the value requested.</p><p>This structure will be fully-populated as it exists in the datastore. If</p><p>optional fields were not given at creation, these fields will be empty or</p><p>set to default values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time carries the (UTC) timestamp of the last-modification of the</p><p>DeviceTag instance in this response.</p> |







<a name="arista.tag.v1.DeviceTagStreamRequest"></a>

### DeviceTagStreamRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **partial_eq_filter** | [DeviceTag](#devicetag)[...] | <p>PartialEqFilter provides a way to server-side filter a GetAll/Subscribe.</p><p>This requires all provided fields to be equal to the response.</p><p>While transparent to users, this field also allows services to optimize internal</p><p>subscriptions if filter(s) are sufficiently specific.</p> |
| **time** | arista.time.TimeBounds | <p>TimeRange allows limiting response data to within a specified time window.</p><p>If this field is populated, at least one of the two time fields are required.</p><p>This field is not allowed in the Subscribe RPC.</p> |







<a name="arista.tag.v1.DeviceTagStreamResponse"></a>

### DeviceTagStreamResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [DeviceTag](#devicetag) | <p>Value is a value deemed relevant to the initiating request.</p><p>This structure will always have its key-field populated. Which other fields are</p><p>populated, and why, depends on the value of Operation and what triggered this notification.</p> |
| **time** | google.protobuf.Timestamp | <p>Time holds the timestamp of this DeviceTag's last modification.</p> |
| **type** | arista.subscriptions.Operation | <p>Operation indicates how the DeviceTag value in this response should be considered.</p><p>Under non-subscribe requests, this value should always be INITIAL. In a subscription,</p><p>once all initial data is streamed and the client begins to receive modification updates,</p><p>you should not see INITIAL again.</p> |







<a name="arista.tag.v1.InterfaceTagAssignmentConfigDeleteRequest"></a>

### InterfaceTagAssignmentConfigDeleteRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [InterfaceTagAssignmentKey](#interfacetagassignmentkey) | <p>Key indicates which InterfaceTagAssignmentConfig instance to remove.</p><p>This field (and all keys, unless otherwise specified) must always be set.</p> |







<a name="arista.tag.v1.InterfaceTagAssignmentConfigDeleteResponse"></a>

### InterfaceTagAssignmentConfigDeleteResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [InterfaceTagAssignmentKey](#interfacetagassignmentkey) | <p>Key echoes back the key of the deleted InterfaceTagAssignmentConfig instance.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the (UTC) timestamp at which the system recognizes the</p><p>deletion. The only guarantees made about this timestamp are:</p><p>- it is after the time the request was received</p><p>- a time-ranged query with StartTime==DeletedAt will not include this instance.</p> |







<a name="arista.tag.v1.InterfaceTagAssignmentConfigRequest"></a>

### InterfaceTagAssignmentConfigRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [InterfaceTagAssignmentKey](#interfacetagassignmentkey) | <p>Key uniquely identifies a InterfaceTagAssignmentConfig instance to retrieve.</p><p>This value (and all fields, unless otherwise specified) must be populated.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the time for which you are interested in the data.</p><p>If no time is given, the server will use the time at twhich it makes the request.</p> |







<a name="arista.tag.v1.InterfaceTagAssignmentConfigResponse"></a>

### InterfaceTagAssignmentConfigResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [InterfaceTagAssignmentConfig](#interfacetagassignmentconfig) | <p>Value is the value requested.</p><p>This structure will be fully-populated as it exists in the datastore. If</p><p>optional fields were not given at creation, these fields will be empty or</p><p>set to default values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time carries the (UTC) timestamp of the last-modification of the</p><p>InterfaceTagAssignmentConfig instance in this response.</p> |







<a name="arista.tag.v1.InterfaceTagAssignmentConfigSetRequest"></a>

### InterfaceTagAssignmentConfigSetRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [InterfaceTagAssignmentConfig](#interfacetagassignmentconfig) | <p>InterfaceTagAssignmentConfig carries the value to set into the datastore.</p><p>See the documentation on the InterfaceTagAssignmentConfig struct for which fields are required.</p> |







<a name="arista.tag.v1.InterfaceTagAssignmentConfigSetResponse"></a>

### InterfaceTagAssignmentConfigSetResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [InterfaceTagAssignmentConfig](#interfacetagassignmentconfig) | <p>Value carries all the values given in the InterfaceTagAssignmentConfigSetRequest as well</p><p>as any server-generated values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the (UTC) timestamp at which the system recognizes the</p><p>creation. The only guarantees made about this timestamp are:</p><p>- it is after the time the request was received</p><p>- a time-ranged query with StartTime==CreatedAt will include this instance.</p> |







<a name="arista.tag.v1.InterfaceTagAssignmentConfigStreamRequest"></a>

### InterfaceTagAssignmentConfigStreamRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **partial_eq_filter** | [InterfaceTagAssignmentConfig](#interfacetagassignmentconfig)[...] | <p>PartialEqFilter provides a way to server-side filter a GetAll/Subscribe.</p><p>This requires all provided fields to be equal to the response.</p><p>While transparent to users, this field also allows services to optimize internal</p><p>subscriptions if filter(s) are sufficiently specific.</p> |
| **time** | arista.time.TimeBounds | <p>TimeRange allows limiting response data to within a specified time window.</p><p>If this field is populated, at least one of the two time fields are required.</p><p>This field is not allowed in the Subscribe RPC.</p> |







<a name="arista.tag.v1.InterfaceTagAssignmentConfigStreamResponse"></a>

### InterfaceTagAssignmentConfigStreamResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [InterfaceTagAssignmentConfig](#interfacetagassignmentconfig) | <p>Value is a value deemed relevant to the initiating request.</p><p>This structure will always have its key-field populated. Which other fields are</p><p>populated, and why, depends on the value of Operation and what triggered this notification.</p> |
| **time** | google.protobuf.Timestamp | <p>Time holds the timestamp of this InterfaceTagAssignmentConfig's last modification.</p> |
| **type** | arista.subscriptions.Operation | <p>Operation indicates how the InterfaceTagAssignmentConfig value in this response should be considered.</p><p>Under non-subscribe requests, this value should always be INITIAL. In a subscription,</p><p>once all initial data is streamed and the client begins to receive modification updates,</p><p>you should not see INITIAL again.</p> |







<a name="arista.tag.v1.InterfaceTagConfigDeleteRequest"></a>

### InterfaceTagConfigDeleteRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [TagKey](#tagkey) | <p>Key indicates which InterfaceTagConfig instance to remove.</p><p>This field (and all keys, unless otherwise specified) must always be set.</p> |







<a name="arista.tag.v1.InterfaceTagConfigDeleteResponse"></a>

### InterfaceTagConfigDeleteResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [TagKey](#tagkey) | <p>Key echoes back the key of the deleted InterfaceTagConfig instance.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the (UTC) timestamp at which the system recognizes the</p><p>deletion. The only guarantees made about this timestamp are:</p><p>- it is after the time the request was received</p><p>- a time-ranged query with StartTime==DeletedAt will not include this instance.</p> |







<a name="arista.tag.v1.InterfaceTagConfigRequest"></a>

### InterfaceTagConfigRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [TagKey](#tagkey) | <p>Key uniquely identifies a InterfaceTagConfig instance to retrieve.</p><p>This value (and all fields, unless otherwise specified) must be populated.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the time for which you are interested in the data.</p><p>If no time is given, the server will use the time at twhich it makes the request.</p> |







<a name="arista.tag.v1.InterfaceTagConfigResponse"></a>

### InterfaceTagConfigResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [InterfaceTagConfig](#interfacetagconfig) | <p>Value is the value requested.</p><p>This structure will be fully-populated as it exists in the datastore. If</p><p>optional fields were not given at creation, these fields will be empty or</p><p>set to default values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time carries the (UTC) timestamp of the last-modification of the</p><p>InterfaceTagConfig instance in this response.</p> |







<a name="arista.tag.v1.InterfaceTagConfigSetRequest"></a>

### InterfaceTagConfigSetRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [InterfaceTagConfig](#interfacetagconfig) | <p>InterfaceTagConfig carries the value to set into the datastore.</p><p>See the documentation on the InterfaceTagConfig struct for which fields are required.</p> |







<a name="arista.tag.v1.InterfaceTagConfigSetResponse"></a>

### InterfaceTagConfigSetResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [InterfaceTagConfig](#interfacetagconfig) | <p>Value carries all the values given in the InterfaceTagConfigSetRequest as well</p><p>as any server-generated values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the (UTC) timestamp at which the system recognizes the</p><p>creation. The only guarantees made about this timestamp are:</p><p>- it is after the time the request was received</p><p>- a time-ranged query with StartTime==CreatedAt will include this instance.</p> |







<a name="arista.tag.v1.InterfaceTagConfigStreamRequest"></a>

### InterfaceTagConfigStreamRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **partial_eq_filter** | [InterfaceTagConfig](#interfacetagconfig)[...] | <p>PartialEqFilter provides a way to server-side filter a GetAll/Subscribe.</p><p>This requires all provided fields to be equal to the response.</p><p>While transparent to users, this field also allows services to optimize internal</p><p>subscriptions if filter(s) are sufficiently specific.</p> |
| **time** | arista.time.TimeBounds | <p>TimeRange allows limiting response data to within a specified time window.</p><p>If this field is populated, at least one of the two time fields are required.</p><p>This field is not allowed in the Subscribe RPC.</p> |







<a name="arista.tag.v1.InterfaceTagConfigStreamResponse"></a>

### InterfaceTagConfigStreamResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [InterfaceTagConfig](#interfacetagconfig) | <p>Value is a value deemed relevant to the initiating request.</p><p>This structure will always have its key-field populated. Which other fields are</p><p>populated, and why, depends on the value of Operation and what triggered this notification.</p> |
| **time** | google.protobuf.Timestamp | <p>Time holds the timestamp of this InterfaceTagConfig's last modification.</p> |
| **type** | arista.subscriptions.Operation | <p>Operation indicates how the InterfaceTagConfig value in this response should be considered.</p><p>Under non-subscribe requests, this value should always be INITIAL. In a subscription,</p><p>once all initial data is streamed and the client begins to receive modification updates,</p><p>you should not see INITIAL again.</p> |







<a name="arista.tag.v1.InterfaceTagRequest"></a>

### InterfaceTagRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [TagKey](#tagkey) | <p>Key uniquely identifies a InterfaceTag instance to retrieve.</p><p>This value (and all fields, unless otherwise specified) must be populated.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the time for which you are interested in the data.</p><p>If no time is given, the server will use the time at twhich it makes the request.</p> |







<a name="arista.tag.v1.InterfaceTagResponse"></a>

### InterfaceTagResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [InterfaceTag](#interfacetag) | <p>Value is the value requested.</p><p>This structure will be fully-populated as it exists in the datastore. If</p><p>optional fields were not given at creation, these fields will be empty or</p><p>set to default values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time carries the (UTC) timestamp of the last-modification of the</p><p>InterfaceTag instance in this response.</p> |







<a name="arista.tag.v1.InterfaceTagStreamRequest"></a>

### InterfaceTagStreamRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **partial_eq_filter** | [InterfaceTag](#interfacetag)[...] | <p>PartialEqFilter provides a way to server-side filter a GetAll/Subscribe.</p><p>This requires all provided fields to be equal to the response.</p><p>While transparent to users, this field also allows services to optimize internal</p><p>subscriptions if filter(s) are sufficiently specific.</p> |
| **time** | arista.time.TimeBounds | <p>TimeRange allows limiting response data to within a specified time window.</p><p>If this field is populated, at least one of the two time fields are required.</p><p>This field is not allowed in the Subscribe RPC.</p> |







<a name="arista.tag.v1.InterfaceTagStreamResponse"></a>

### InterfaceTagStreamResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [InterfaceTag](#interfacetag) | <p>Value is a value deemed relevant to the initiating request.</p><p>This structure will always have its key-field populated. Which other fields are</p><p>populated, and why, depends on the value of Operation and what triggered this notification.</p> |
| **time** | google.protobuf.Timestamp | <p>Time holds the timestamp of this InterfaceTag's last modification.</p> |
| **type** | arista.subscriptions.Operation | <p>Operation indicates how the InterfaceTag value in this response should be considered.</p><p>Under non-subscribe requests, this value should always be INITIAL. In a subscription,</p><p>once all initial data is streamed and the client begins to receive modification updates,</p><p>you should not see INITIAL again.</p> |






 <!-- end messages -->

 <!-- end enums -->

 <!-- end HasExtensions -->


<a name="arista.tag.v1.DeviceTagAssignmentConfigService"></a>

### DeviceTagAssignmentConfigService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetOne | [DeviceTagAssignmentConfigRequest](#arista.tag.v1.DeviceTagAssignmentConfigRequest) | [DeviceTagAssignmentConfigResponse](#arista.tag.v1.DeviceTagAssignmentConfigResponse) | <p>GetOne returns a unary model as specified by the key in the request.</p><p>The key must be provided and all fields populated (unless otherwise specified).</p> |
| GetAll | [DeviceTagAssignmentConfigStreamRequest](#arista.tag.v1.DeviceTagAssignmentConfigStreamRequest) | [DeviceTagAssignmentConfigStreamResponse](#arista.tag.v1.DeviceTagAssignmentConfigStreamResponse) stream | <p>GetAll returns all entities for this model, with optional filtering.</p> |
| Subscribe | [DeviceTagAssignmentConfigStreamRequest](#arista.tag.v1.DeviceTagAssignmentConfigStreamRequest) | [DeviceTagAssignmentConfigStreamResponse](#arista.tag.v1.DeviceTagAssignmentConfigStreamResponse) stream | <p>Subscribe first returns all initial state known to the system,</p><p>then will send deltas as entities are changed.</p> |
| Set | [DeviceTagAssignmentConfigSetRequest](#arista.tag.v1.DeviceTagAssignmentConfigSetRequest) | [DeviceTagAssignmentConfigSetResponse](#arista.tag.v1.DeviceTagAssignmentConfigSetResponse) | <p>Set allows setting values for the entity specified by the key in the request.</p><p>The key must be provided and all fields set (unless otherwise specified).</p> |
| Delete | [DeviceTagAssignmentConfigDeleteRequest](#arista.tag.v1.DeviceTagAssignmentConfigDeleteRequest) | [DeviceTagAssignmentConfigDeleteResponse](#arista.tag.v1.DeviceTagAssignmentConfigDeleteResponse) | <p>Delete will remove the entity specified by the key within the request.</p><p>The key must be provided and all fields populated (unless otherwise specified).</p> |


<a name="arista.tag.v1.DeviceTagConfigService"></a>

### DeviceTagConfigService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetOne | [DeviceTagConfigRequest](#arista.tag.v1.DeviceTagConfigRequest) | [DeviceTagConfigResponse](#arista.tag.v1.DeviceTagConfigResponse) | <p>GetOne returns a unary model as specified by the key in the request.</p><p>The key must be provided and all fields populated (unless otherwise specified).</p> |
| GetAll | [DeviceTagConfigStreamRequest](#arista.tag.v1.DeviceTagConfigStreamRequest) | [DeviceTagConfigStreamResponse](#arista.tag.v1.DeviceTagConfigStreamResponse) stream | <p>GetAll returns all entities for this model, with optional filtering.</p> |
| Subscribe | [DeviceTagConfigStreamRequest](#arista.tag.v1.DeviceTagConfigStreamRequest) | [DeviceTagConfigStreamResponse](#arista.tag.v1.DeviceTagConfigStreamResponse) stream | <p>Subscribe first returns all initial state known to the system,</p><p>then will send deltas as entities are changed.</p> |
| Set | [DeviceTagConfigSetRequest](#arista.tag.v1.DeviceTagConfigSetRequest) | [DeviceTagConfigSetResponse](#arista.tag.v1.DeviceTagConfigSetResponse) | <p>Set allows setting values for the entity specified by the key in the request.</p><p>The key must be provided and all fields set (unless otherwise specified).</p> |
| Delete | [DeviceTagConfigDeleteRequest](#arista.tag.v1.DeviceTagConfigDeleteRequest) | [DeviceTagConfigDeleteResponse](#arista.tag.v1.DeviceTagConfigDeleteResponse) | <p>Delete will remove the entity specified by the key within the request.</p><p>The key must be provided and all fields populated (unless otherwise specified).</p> |


<a name="arista.tag.v1.DeviceTagService"></a>

### DeviceTagService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetOne | [DeviceTagRequest](#arista.tag.v1.DeviceTagRequest) | [DeviceTagResponse](#arista.tag.v1.DeviceTagResponse) | <p>GetOne returns a unary model as specified by the key in the request.</p><p>The key must be provided and all fields populated (unless otherwise specified).</p> |
| GetAll | [DeviceTagStreamRequest](#arista.tag.v1.DeviceTagStreamRequest) | [DeviceTagStreamResponse](#arista.tag.v1.DeviceTagStreamResponse) stream | <p>GetAll returns all entities for this model, with optional filtering.</p> |
| Subscribe | [DeviceTagStreamRequest](#arista.tag.v1.DeviceTagStreamRequest) | [DeviceTagStreamResponse](#arista.tag.v1.DeviceTagStreamResponse) stream | <p>Subscribe first returns all initial state known to the system,</p><p>then will send deltas as entities are changed.</p> |


<a name="arista.tag.v1.InterfaceTagAssignmentConfigService"></a>

### InterfaceTagAssignmentConfigService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetOne | [InterfaceTagAssignmentConfigRequest](#arista.tag.v1.InterfaceTagAssignmentConfigRequest) | [InterfaceTagAssignmentConfigResponse](#arista.tag.v1.InterfaceTagAssignmentConfigResponse) | <p>GetOne returns a unary model as specified by the key in the request.</p><p>The key must be provided and all fields populated (unless otherwise specified).</p> |
| GetAll | [InterfaceTagAssignmentConfigStreamRequest](#arista.tag.v1.InterfaceTagAssignmentConfigStreamRequest) | [InterfaceTagAssignmentConfigStreamResponse](#arista.tag.v1.InterfaceTagAssignmentConfigStreamResponse) stream | <p>GetAll returns all entities for this model, with optional filtering.</p> |
| Subscribe | [InterfaceTagAssignmentConfigStreamRequest](#arista.tag.v1.InterfaceTagAssignmentConfigStreamRequest) | [InterfaceTagAssignmentConfigStreamResponse](#arista.tag.v1.InterfaceTagAssignmentConfigStreamResponse) stream | <p>Subscribe first returns all initial state known to the system,</p><p>then will send deltas as entities are changed.</p> |
| Set | [InterfaceTagAssignmentConfigSetRequest](#arista.tag.v1.InterfaceTagAssignmentConfigSetRequest) | [InterfaceTagAssignmentConfigSetResponse](#arista.tag.v1.InterfaceTagAssignmentConfigSetResponse) | <p>Set allows setting values for the entity specified by the key in the request.</p><p>The key must be provided and all fields set (unless otherwise specified).</p> |
| Delete | [InterfaceTagAssignmentConfigDeleteRequest](#arista.tag.v1.InterfaceTagAssignmentConfigDeleteRequest) | [InterfaceTagAssignmentConfigDeleteResponse](#arista.tag.v1.InterfaceTagAssignmentConfigDeleteResponse) | <p>Delete will remove the entity specified by the key within the request.</p><p>The key must be provided and all fields populated (unless otherwise specified).</p> |


<a name="arista.tag.v1.InterfaceTagConfigService"></a>

### InterfaceTagConfigService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetOne | [InterfaceTagConfigRequest](#arista.tag.v1.InterfaceTagConfigRequest) | [InterfaceTagConfigResponse](#arista.tag.v1.InterfaceTagConfigResponse) | <p>GetOne returns a unary model as specified by the key in the request.</p><p>The key must be provided and all fields populated (unless otherwise specified).</p> |
| GetAll | [InterfaceTagConfigStreamRequest](#arista.tag.v1.InterfaceTagConfigStreamRequest) | [InterfaceTagConfigStreamResponse](#arista.tag.v1.InterfaceTagConfigStreamResponse) stream | <p>GetAll returns all entities for this model, with optional filtering.</p> |
| Subscribe | [InterfaceTagConfigStreamRequest](#arista.tag.v1.InterfaceTagConfigStreamRequest) | [InterfaceTagConfigStreamResponse](#arista.tag.v1.InterfaceTagConfigStreamResponse) stream | <p>Subscribe first returns all initial state known to the system,</p><p>then will send deltas as entities are changed.</p> |
| Set | [InterfaceTagConfigSetRequest](#arista.tag.v1.InterfaceTagConfigSetRequest) | [InterfaceTagConfigSetResponse](#arista.tag.v1.InterfaceTagConfigSetResponse) | <p>Set allows setting values for the entity specified by the key in the request.</p><p>The key must be provided and all fields set (unless otherwise specified).</p> |
| Delete | [InterfaceTagConfigDeleteRequest](#arista.tag.v1.InterfaceTagConfigDeleteRequest) | [InterfaceTagConfigDeleteResponse](#arista.tag.v1.InterfaceTagConfigDeleteResponse) | <p>Delete will remove the entity specified by the key within the request.</p><p>The key must be provided and all fields populated (unless otherwise specified).</p> |


<a name="arista.tag.v1.InterfaceTagService"></a>

### InterfaceTagService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetOne | [InterfaceTagRequest](#arista.tag.v1.InterfaceTagRequest) | [InterfaceTagResponse](#arista.tag.v1.InterfaceTagResponse) | <p>GetOne returns a unary model as specified by the key in the request.</p><p>The key must be provided and all fields populated (unless otherwise specified).</p> |
| GetAll | [InterfaceTagStreamRequest](#arista.tag.v1.InterfaceTagStreamRequest) | [InterfaceTagStreamResponse](#arista.tag.v1.InterfaceTagStreamResponse) stream | <p>GetAll returns all entities for this model, with optional filtering.</p> |
| Subscribe | [InterfaceTagStreamRequest](#arista.tag.v1.InterfaceTagStreamRequest) | [InterfaceTagStreamResponse](#arista.tag.v1.InterfaceTagStreamResponse) stream | <p>Subscribe first returns all initial state known to the system,</p><p>then will send deltas as entities are changed.</p> |

 <!-- end services -->



