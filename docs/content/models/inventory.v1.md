---
title: inventory.v1
---



- [arista/inventory.v1/inventory.proto](#arista/inventory.v1/inventory.proto)
    - [Device](#device)
    - [DeviceKey](#devicekey)
    - [ExtendedAttributes](#extendedattributes)
    - [ExtendedAttributes.FeatureEnabledEntry](#featureenabledentry)
  
    - [StreamingStatus](#arista.inventory.v1.StreamingStatus)
  
- [arista/inventory.v1/services.gen.proto](#arista/inventory.v1/services.gen.proto)
    - [DeviceRequest](#devicerequest)
    - [DeviceResponse](#deviceresponse)
    - [DeviceStreamRequest](#devicestreamrequest)
    - [DeviceStreamResponse](#devicestreamresponse)
  
    - [DeviceService](#arista.inventory.v1.DeviceService)
  




<a name="arista/inventory.v1/inventory.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## arista/inventory.v1/inventory.proto



<a name="arista.inventory.v1.Device"></a>

### Device
Device is the primary model for this service.


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [DeviceKey](#devicekey) | <p>The key that uniquely identifies this device.</p> |
| **software_version** | google.protobuf.StringValue | <p>SoftwareVersion gives the currently running device software version.</p> |
| **model_name** | google.protobuf.StringValue | <p>ModelName describes the hardware model of this device.</p> |
| **hardware_revision** | google.protobuf.StringValue | <p>HardwareREvision describes any revisional data to the model name.</p> |
| **fqdn** | google.protobuf.StringValue | <p>FQDN gives the fully qualified hostname to reach the device.</p> |
| **hostname** | google.protobuf.StringValue | <p>Hostname is the hostname as reported on the device.</p> |
| **domain_name** | google.protobuf.StringValue | <p>DomainName provides the domain name the device is registered on.</p> |
| **system_mac_address** | google.protobuf.StringValue | <p>SystemMacAddress provides the MAC address of the management port.</p> |
| **boot_time** | google.protobuf.Timestamp | <p>BootTime indicates when the device was last booted.</p> |
| **streaming_status** | [StreamingStatus](#streamingstatus) | <p>StreamingStatus the status of streaming telemetry for this device.</p> |
| **extended_attributes** | [ExtendedAttributes](#extendedattributes) | <p>ExtendedAttributes wraps any additional, potentially non-standard, features</p><p>or attributes the device reports.</p> |







<a name="arista.inventory.v1.DeviceKey"></a>

### DeviceKey
DeviceKey uniquely identifies a single device.


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **device_id** | google.protobuf.StringValue | <p></p> |







<a name="arista.inventory.v1.ExtendedAttributes"></a>

### ExtendedAttributes
ExtendedAttributes wraps any additional, potentially non-standard, features
or attributes the device reports.


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **feature_enabled** | [ExtendedAttributes.FeatureEnabledEntry](#extendedattributes.featureenabledentry)[...] | <p>FeatureEnabled is a map of feature name to enabled status.</p><p>If a feature is missing from this map it can be assumed off.</p> |







<a name="arista.inventory.v1.ExtendedAttributes.FeatureEnabledEntry"></a>

### ExtendedAttributes.FeatureEnabledEntry



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | string | <p></p> |
| **value** | bool | <p></p> |






 <!-- end messages -->


<a name="arista.inventory.v1.StreamingStatus"></a>

### StreamingStatus
StreamingStatus the status of streaming telemetry for this device.

| Name | Number | Description |
| ---- | ------ | ----------- |
| STREAMING_STATUS_UNSPECIFIED | 0 | <p>Unspecified is the uninitialized state of this enum.</p> |
| STREAMING_STATUS_INACTIVE | 1 | <p>Inactive indicates the device is not streaming telemetry.</p> |
| STREAMING_STATUS_ACTIVE | 2 | <p>Active indicates the device is streaming telemetry.</p> |


 <!-- end enums -->

 <!-- end HasExtensions -->

 <!-- end services -->




<a name="arista/inventory.v1/services.gen.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## arista/inventory.v1/services.gen.proto



<a name="arista.inventory.v1.DeviceRequest"></a>

### DeviceRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [DeviceKey](#devicekey) | <p>Key uniquely identifies a Device instance to retrieve.</p><p>This value (and all fields, unless otherwise specified) must be populated.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the time for which you are interested in the data.</p><p>If no time is given, the server will use the time at twhich it makes the request.</p> |







<a name="arista.inventory.v1.DeviceResponse"></a>

### DeviceResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [Device](#device) | <p>Value is the value requested.</p><p>This structure will be fully-populated as it exists in the datastore. If</p><p>optional fields were not given at creation, these fields will be empty or</p><p>set to default values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time carries the (UTC) timestamp of the last-modification of the</p><p>Device instance in this response.</p> |







<a name="arista.inventory.v1.DeviceStreamRequest"></a>

### DeviceStreamRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **partial_eq_filter** | [Device](#device)[...] | <p>PartialEqFilter provides a way to server-side filter a GetAll/Subscribe.</p><p>This requires all provided fields to be equal to the response.</p><p>While transparent to users, this field also allows services to optimize internal</p><p>subscriptions if filter(s) are sufficiently specific.</p> |
| **time** | arista.time.TimeBounds | <p>TimeRange allows limiting response data to within a specified time window.</p><p>If this field is populated, at least one of the two time fields are required.</p><p>This field is not allowed in the Subscribe RPC.</p> |







<a name="arista.inventory.v1.DeviceStreamResponse"></a>

### DeviceStreamResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [Device](#device) | <p>Value is a value deemed relevant to the initiating request.</p><p>This structure will always have its key-field populated. Which other fields are</p><p>populated, and why, depends on the value of Operation and what triggered this notification.</p> |
| **time** | google.protobuf.Timestamp | <p>Time holds the timestamp of this Device's last modification.</p> |
| **type** | arista.subscriptions.Operation | <p>Operation indicates how the Device value in this response should be considered.</p><p>Under non-subscribe requests, this value should always be INITIAL. In a subscription,</p><p>once all initial data is streamed and the client begins to receive modification updates,</p><p>you should not see INITIAL again.</p> |






 <!-- end messages -->

 <!-- end enums -->

 <!-- end HasExtensions -->


<a name="arista.inventory.v1.DeviceService"></a>

### DeviceService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetOne | [DeviceRequest](#arista.inventory.v1.DeviceRequest) | [DeviceResponse](#arista.inventory.v1.DeviceResponse) | <p>GetOne returns a unary model as specified by the key in the request.</p><p>The key must be provided and all fields populated (unless otherwise specified).</p> |
| GetAll | [DeviceStreamRequest](#arista.inventory.v1.DeviceStreamRequest) | [DeviceStreamResponse](#arista.inventory.v1.DeviceStreamResponse) stream | <p>GetAll returns all entities for this model, with optional filtering.</p> |
| Subscribe | [DeviceStreamRequest](#arista.inventory.v1.DeviceStreamRequest) | [DeviceStreamResponse](#arista.inventory.v1.DeviceStreamResponse) stream | <p>Subscribe first returns all initial state known to the system,</p><p>then will send deltas as entities are changed.</p> |

 <!-- end services -->



