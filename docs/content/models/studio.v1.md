---
title: studio.v1
---



- [arista/studio.v1/studio.proto](#arista/studio.v1/studio.proto)
    - [AssignedTags](#assignedtags)
    - [AssignedTagsConfig](#assignedtagsconfig)
    - [BooleanInputFieldProps](#booleaninputfieldprops)
    - [CollectionInputFieldProps](#collectioninputfieldprops)
    - [FloatInputFieldProps](#floatinputfieldprops)
    - [GroupInputFieldProps](#groupinputfieldprops)
    - [InputField](#inputfield)
    - [InputFields](#inputfields)
    - [InputFields.ValuesEntry](#valuesentry)
    - [InputSchema](#inputschema)
    - [Inputs](#inputs)
    - [InputsConfig](#inputsconfig)
    - [InputsKey](#inputskey)
    - [IntegerInputFieldProps](#integerinputfieldprops)
    - [Layout](#layout)
    - [ResolverInputFieldProps](#resolverinputfieldprops)
    - [StringInputFieldProps](#stringinputfieldprops)
    - [Studio](#studio)
    - [StudioConfig](#studioconfig)
    - [StudioKey](#studiokey)
    - [Template](#template)
  
    - [InputFieldType](#arista.studio.v1.InputFieldType)
    - [ResolverFieldDisplayMode](#arista.studio.v1.ResolverFieldDisplayMode)
    - [ResolverFieldInputMode](#arista.studio.v1.ResolverFieldInputMode)
    - [TemplateType](#arista.studio.v1.TemplateType)
  
- [arista/studio.v1/services.gen.proto](#arista/studio.v1/services.gen.proto)
    - [AssignedTagsConfigDeleteRequest](#assignedtagsconfigdeleterequest)
    - [AssignedTagsConfigDeleteResponse](#assignedtagsconfigdeleteresponse)
    - [AssignedTagsConfigRequest](#assignedtagsconfigrequest)
    - [AssignedTagsConfigResponse](#assignedtagsconfigresponse)
    - [AssignedTagsConfigSetRequest](#assignedtagsconfigsetrequest)
    - [AssignedTagsConfigSetResponse](#assignedtagsconfigsetresponse)
    - [AssignedTagsConfigStreamRequest](#assignedtagsconfigstreamrequest)
    - [AssignedTagsConfigStreamResponse](#assignedtagsconfigstreamresponse)
    - [AssignedTagsRequest](#assignedtagsrequest)
    - [AssignedTagsResponse](#assignedtagsresponse)
    - [AssignedTagsStreamRequest](#assignedtagsstreamrequest)
    - [AssignedTagsStreamResponse](#assignedtagsstreamresponse)
    - [InputsConfigDeleteRequest](#inputsconfigdeleterequest)
    - [InputsConfigDeleteResponse](#inputsconfigdeleteresponse)
    - [InputsConfigRequest](#inputsconfigrequest)
    - [InputsConfigResponse](#inputsconfigresponse)
    - [InputsConfigSetRequest](#inputsconfigsetrequest)
    - [InputsConfigSetResponse](#inputsconfigsetresponse)
    - [InputsConfigStreamRequest](#inputsconfigstreamrequest)
    - [InputsConfigStreamResponse](#inputsconfigstreamresponse)
    - [InputsRequest](#inputsrequest)
    - [InputsResponse](#inputsresponse)
    - [InputsStreamRequest](#inputsstreamrequest)
    - [InputsStreamResponse](#inputsstreamresponse)
    - [StudioConfigDeleteRequest](#studioconfigdeleterequest)
    - [StudioConfigDeleteResponse](#studioconfigdeleteresponse)
    - [StudioConfigRequest](#studioconfigrequest)
    - [StudioConfigResponse](#studioconfigresponse)
    - [StudioConfigSetRequest](#studioconfigsetrequest)
    - [StudioConfigSetResponse](#studioconfigsetresponse)
    - [StudioConfigStreamRequest](#studioconfigstreamrequest)
    - [StudioConfigStreamResponse](#studioconfigstreamresponse)
    - [StudioRequest](#studiorequest)
    - [StudioResponse](#studioresponse)
    - [StudioStreamRequest](#studiostreamrequest)
    - [StudioStreamResponse](#studiostreamresponse)
  
    - [AssignedTagsConfigService](#arista.studio.v1.AssignedTagsConfigService)
    - [AssignedTagsService](#arista.studio.v1.AssignedTagsService)
    - [InputsConfigService](#arista.studio.v1.InputsConfigService)
    - [InputsService](#arista.studio.v1.InputsService)
    - [StudioConfigService](#arista.studio.v1.StudioConfigService)
    - [StudioService](#arista.studio.v1.StudioService)
  




<a name="arista/studio.v1/studio.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## arista/studio.v1/studio.proto



<a name="arista.studio.v1.AssignedTags"></a>

### AssignedTags
AssignedTags is the state of studio assignment


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [StudioKey](#studiokey) | <p></p> |
| **created_at** | google.protobuf.Timestamp | <p></p> |
| **created_by** | google.protobuf.StringValue | <p></p> |
| **last_modified_at** | google.protobuf.Timestamp | <p></p> |
| **last_modified_by** | google.protobuf.StringValue | <p></p> |
| **query** | google.protobuf.StringValue | <p></p> |







<a name="arista.studio.v1.AssignedTagsConfig"></a>

### AssignedTagsConfig
AssignedTagsConfig is the configuration to assign a studio to the set of devices matching a tag query


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [StudioKey](#studiokey) | <p></p> |
| **remove** | google.protobuf.BoolValue | <p>remove specifies that the resource identified by the key is to be removed from mainline</p><p>Other data fields are not allowed when this field is set to true</p> |
| **query** | google.protobuf.StringValue | <p></p> |







<a name="arista.studio.v1.BooleanInputFieldProps"></a>

### BooleanInputFieldProps



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **default_value** | google.protobuf.BoolValue | <p>default_value represents the default value of the boolean input field (optional)</p><p>optional</p> |







<a name="arista.studio.v1.CollectionInputFieldProps"></a>

### CollectionInputFieldProps



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **base_field_id** | google.protobuf.StringValue | <p>base_field_id represent the ID of the collection input field's base field</p><p>required</p> |
| **key** | google.protobuf.StringValue | <p>key specifies a key in the collection that identifies each element</p><p>It only supports the group base field type `INPUT_FIELD_TYPE_GROUP`. The key field specified the ID of the</p><p>group member and each element of the collection can be uniquely identified by the key.</p><p>If the type of the base field is:</p><p>- `INPUT_FIELD_TYPE_GROUP`: the value of specified by the key field will used as the collection element's key.</p><p>The key field specifies the ID of the group member, the group member type must be one of the following field types:</p><p>`INPUT_FIELD_TYPE_INTEGER`, `INPUT_FIELD_TYPE_FLOAT`, `INPUT_FIELD_TYPE_STRING`.</p><p>optional</p> |







<a name="arista.studio.v1.FloatInputFieldProps"></a>

### FloatInputFieldProps



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **default_value** | google.protobuf.FloatValue | <p>default_value represents the default value of the float input field (optional)</p><p>optional</p> |
| **static_options** | fmp.RepeatedFloat | <p>static_options represents the list of valid float values (optional)</p><p>optional</p> |
| **dynamic_options** | fmp.RepeatedString | <p>dynamic_options contains a pointer expression that reference an input field with a collection of</p><p>float input values which will be used as a list of valid values (optional)</p><p>optional</p> |







<a name="arista.studio.v1.GroupInputFieldProps"></a>

### GroupInputFieldProps



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **members** | fmp.RepeatedString | <p>members represents all the fields in the group input field</p><p>required</p> |







<a name="arista.studio.v1.InputField"></a>

### InputField



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **id** | google.protobuf.StringValue | <p>id represents the ID of the input field, which should be unique within the input schema resource</p><p>required</p> |
| **type** | [InputFieldType](#inputfieldtype) | <p>type represents the type of the input field</p><p>required</p> |
| **name** | google.protobuf.StringValue | <p>type represents the variable name use to reference the value of the input field</p><p>required</p> |
| **label** | google.protobuf.StringValue | <p>label represents the label of the input field</p><p>required</p> |
| **description** | google.protobuf.StringValue | <p>description represents the description of the input field (optional)</p><p>optional</p> |
| **required** | google.protobuf.BoolValue | <p>required indicates whether the input field requires a value, defaults to `false` if unset (optional)</p><p>optional</p> |
| **boolean_props** | [BooleanInputFieldProps](#booleaninputfieldprops) | <p>boolean_props contains properties for input fields of INPUT_FIELD_TYPE_BOOLEAN type (optional)</p><p>optional</p> |
| **integer_props** | [IntegerInputFieldProps](#integerinputfieldprops) | <p>integer_props contains properties for input fields of INPUT_FIELD_TYPE_INTEGER type (optional)</p><p>optional</p> |
| **float_props** | [FloatInputFieldProps](#floatinputfieldprops) | <p>float_props contains properties for input fields of INPUT_FIELD_TYPE_FLOAT type (optional)</p><p>optional</p> |
| **string_props** | [StringInputFieldProps](#stringinputfieldprops) | <p>string_props contains properties for input fields of INPUT_FIELD_TYPE_STRING type (optional)</p><p>optional</p> |
| **group_props** | [GroupInputFieldProps](#groupinputfieldprops) | <p>group_props contains properties for input fields of INPUT_FIELD_TYPE_GROUP type (optional)</p><p>optional</p> |
| **collection_props** | [CollectionInputFieldProps](#collectioninputfieldprops) | <p>collection_props contains properties for input fields of INPUT_FIELD_TYPE_COLLECTION type (optional)</p><p>optional</p> |
| **resolver_props** | [ResolverInputFieldProps](#resolverinputfieldprops) | <p>resolver_props contains properties for input fields of INPUT_FIELD_TYPE_RESOLVER type (optional)</p><p>optional</p> |
| **auto_fill_action_id** | google.protobuf.StringValue | <p>auto_fill_action_id represents the link between the field and the autofill script that provides a value for it (optional)</p><p>optional</p> |







<a name="arista.studio.v1.InputFields"></a>

### InputFields



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **values** | [InputFields.ValuesEntry](#inputfields.valuesentry)[...] | <p>values contains all input field configuration, mapped by each input field's respective field ID</p><p>required</p> |







<a name="arista.studio.v1.InputFields.ValuesEntry"></a>

### InputFields.ValuesEntry



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | string | <p></p> |
| **value** | [InputField](#inputfield) | <p></p> |







<a name="arista.studio.v1.InputSchema"></a>

### InputSchema
InputSchema specifies the input schema definition of a studio, consisting of a set of input fields,
and optionally their layout information


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **fields** | [InputFields](#inputfields) | <p></p> |
| **layout** | [Layout](#layout) | <p></p> |







<a name="arista.studio.v1.Inputs"></a>

### Inputs
Inputs is the state of inputs to a studio


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [InputsKey](#inputskey) | <p></p> |
| **created_at** | google.protobuf.Timestamp | <p></p> |
| **created_by** | google.protobuf.StringValue | <p></p> |
| **last_modified_at** | google.protobuf.Timestamp | <p></p> |
| **last_modified_by** | google.protobuf.StringValue | <p></p> |
| **inputs** | google.protobuf.StringValue | <p>inputs is the entire set of inputs, a single JSON string starting with root.</p><p>This is the result of applying workspace-specific InputsConfig changes on top of mainline.</p> |







<a name="arista.studio.v1.InputsConfig"></a>

### InputsConfig
InputsConfig provides values to the input fields of a studio


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [InputsKey](#inputskey) | <p></p> |
| **remove** | google.protobuf.BoolValue | <p>remove specifies that the resource identified by the key is to be removed from mainline</p><p>Other data fields are not allowed when this field is set to true</p> |
| **inputs** | google.protobuf.StringValue | <p>inputs is the value of the input field as a JSON string. It can be the value for a</p><p>simple or complex input field</p> |







<a name="arista.studio.v1.InputsKey"></a>

### InputsKey
Inputskey is the key of the InputsConfig and Inputs resources


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **studio_id** | google.protobuf.StringValue | <p>studio_id is the unique identifier of the studio</p> |
| **workspace_id** | google.protobuf.StringValue | <p>workspace_id is the unique identifier of the workspace</p><p>empty string ("") stands for the "mainline"</p> |
| **path** | fmp.RepeatedString | <p>path is the sequence of elements that uniquely identify an input field</p><p>empty sequence stands for the "root", or the entire set of inputs</p> |







<a name="arista.studio.v1.IntegerInputFieldProps"></a>

### IntegerInputFieldProps



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **default_value** | google.protobuf.Int64Value | <p>default_value represents the default value of the integer input field (optional)</p><p>optional</p> |
| **static_options** | fmp.RepeatedInt64 | <p>static_options represents the list of valid integer values (optional)</p><p>optional</p> |
| **dynamic_options** | fmp.RepeatedString | <p>dynamic_options contains a pointer expression that reference an input field with a collection of</p><p>integer input values which will be used as a list of valid values (optional)</p><p>optional</p> |
| **range** | google.protobuf.StringValue | <p>range represents the range constraint imposed on the integer value; eg. "-10..10", "min..10", "-10..max" (optional)</p><p>optional</p> |







<a name="arista.studio.v1.Layout"></a>

### Layout
Layout specifies the display properties input fields


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | google.protobuf.StringValue | <p>json string</p> |







<a name="arista.studio.v1.ResolverInputFieldProps"></a>

### ResolverInputFieldProps



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **base_field_id** | google.protobuf.StringValue | <p>base_field_id represent the ID of the resolver input field's base field</p><p>required</p> |
| **display_mode** | [ResolverFieldDisplayMode](#resolverfielddisplaymode) | <p>display_mode represents the resolver input field's display mode</p><p>required</p> |
| **input_mode** | [ResolverFieldInputMode](#resolverfieldinputmode) | <p>input_mode represents the resolver input field's input mode</p><p>required</p> |
| **input_tag_label** | google.protobuf.StringValue | <p>input_tag_label represents the tag label to allow in tag inputs (optional)</p><p>optional</p> |
| **tag_filter_query** | google.protobuf.StringValue | <p>tag_filter_query specifies the tags that can be used in a resolver</p><p>optional</p> |







<a name="arista.studio.v1.StringInputFieldProps"></a>

### StringInputFieldProps



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **default_value** | google.protobuf.StringValue | <p>default_value represents the default value of the string input field (optional)</p><p>optional</p> |
| **static_options** | fmp.RepeatedString | <p>static_options represents the list of valid string values (optional)</p><p>optional</p> |
| **dynamic_options** | fmp.RepeatedString | <p>dynamic_options contains a pointer expression that reference an input field with a collection of</p><p>string input values which will be used as a list of valid values (optional)</p><p>optional</p> |
| **length** | google.protobuf.StringValue | <p>length represents the length constraint imposed on the string value; eg. "5..10", "min..10", "5..max" (optional)</p><p>optional</p> |
| **pattern** | google.protobuf.StringValue | <p>pattern represents the regexp-based pattern constraint imposed on the string value; eg. "^[0-9a-fA-F]*$" (optional)</p><p>optional</p> |
| **format** | google.protobuf.StringValue | <p>format represents the format imposed on string value; supported formats: "ip", "ipv6", "mac" (optional)</p><p>optional</p> |







<a name="arista.studio.v1.Studio"></a>

### Studio
Studio state


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [StudioKey](#studiokey) | <p></p> |
| **created_at** | google.protobuf.Timestamp | <p></p> |
| **created_by** | google.protobuf.StringValue | <p></p> |
| **last_modified_at** | google.protobuf.Timestamp | <p></p> |
| **last_modified_by** | google.protobuf.StringValue | <p></p> |
| **display_name** | google.protobuf.StringValue | <p>Below are config fields, with workspace changes applied on top of mainline</p><p>Note that this resource will be present in a workspace only if the studio is modified</p><p>(via the StudioConfig resource)</p> |
| **description** | google.protobuf.StringValue | <p></p> |
| **template** | [Template](#template) | <p></p> |
| **input_schema** | [InputSchema](#inputschema) | <p></p> |
| **input_validation_results** | arista.workspace.v1.InputValidationResults | <p></p> |







<a name="arista.studio.v1.StudioConfig"></a>

### StudioConfig
Studio configuration


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [StudioKey](#studiokey) | <p></p> |
| **remove** | google.protobuf.BoolValue | <p>remove specifies that the resource identified by the key is to be removed from mainline</p><p>Other data fields are not allowed when this field is set to true</p> |
| **display_name** | google.protobuf.StringValue | <p>Changes to the below data fields in a workspace are applied on top of</p><p>mainline content at the time the workspace was created</p> |
| **description** | google.protobuf.StringValue | <p></p> |
| **template** | [Template](#template) | <p></p> |
| **input_schema** | [InputSchema](#inputschema) | <p></p> |







<a name="arista.studio.v1.StudioKey"></a>

### StudioKey
Studio key


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **studio_id** | google.protobuf.StringValue | <p>studio_id is the unique identifier of the studio</p> |
| **workspace_id** | google.protobuf.StringValue | <p>workspace_id is the unique identifier of the workspace</p><p>empty string ("") stands for the "mainline"</p> |







<a name="arista.studio.v1.Template"></a>

### Template
Template of the studio, with its type


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **type** | [TemplateType](#templatetype) | <p></p> |
| **body** | google.protobuf.StringValue | <p></p> |






 <!-- end messages -->


<a name="arista.studio.v1.InputFieldType"></a>

### InputFieldType


| Name | Number | Description |
| ---- | ------ | ----------- |
| INPUT_FIELD_TYPE_UNSPECIFIED | 0 | <p></p> |
| INPUT_FIELD_TYPE_BOOLEAN | 1 | <p></p> |
| INPUT_FIELD_TYPE_INTEGER | 2 | <p></p> |
| INPUT_FIELD_TYPE_FLOAT | 3 | <p></p> |
| INPUT_FIELD_TYPE_STRING | 4 | <p></p> |
| INPUT_FIELD_TYPE_GROUP | 5 | <p></p> |
| INPUT_FIELD_TYPE_COLLECTION | 6 | <p></p> |
| INPUT_FIELD_TYPE_RESOLVER | 7 | <p></p> |



<a name="arista.studio.v1.ResolverFieldDisplayMode"></a>

### ResolverFieldDisplayMode


| Name | Number | Description |
| ---- | ------ | ----------- |
| RESOLVER_FIELD_DISPLAY_MODE_UNSPECIFIED | 0 | <p></p> |
| RESOLVER_FIELD_DISPLAY_MODE_ALL | 1 | <p></p> |
| RESOLVER_FIELD_DISPLAY_MODE_SPARSE | 2 | <p></p> |



<a name="arista.studio.v1.ResolverFieldInputMode"></a>

### ResolverFieldInputMode


| Name | Number | Description |
| ---- | ------ | ----------- |
| RESOLVER_FIELD_INPUT_MODE_UNSPECIFIED | 0 | <p></p> |
| RESOLVER_FIELD_INPUT_MODE_SINGLE_DEVICE_TAG | 1 | <p></p> |
| RESOLVER_FIELD_INPUT_MODE_SINGLE_INTERFACE_TAG | 2 | <p></p> |
| RESOLVER_FIELD_INPUT_MODE_MULTI_DEVICE_TAG | 3 | <p></p> |
| RESOLVER_FIELD_INPUT_MODE_MULTI_INTERFACE_TAG | 4 | <p></p> |



<a name="arista.studio.v1.TemplateType"></a>

### TemplateType


| Name | Number | Description |
| ---- | ------ | ----------- |
| TEMPLATE_TYPE_UNSPECIFIED | 0 | <p></p> |
| TEMPLATE_TYPE_MAKO | 1 | <p></p> |
| TEMPLATE_TYPE_JINJA | 2 | <p></p> |
| TEMPLATE_TYPE_GO | 3 | <p></p> |


 <!-- end enums -->

 <!-- end HasExtensions -->

 <!-- end services -->




<a name="arista/studio.v1/services.gen.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## arista/studio.v1/services.gen.proto



<a name="arista.studio.v1.AssignedTagsConfigDeleteRequest"></a>

### AssignedTagsConfigDeleteRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [StudioKey](#studiokey) | <p>Key indicates which AssignedTagsConfig instance to remove.</p><p>This field must always be set.</p> |







<a name="arista.studio.v1.AssignedTagsConfigDeleteResponse"></a>

### AssignedTagsConfigDeleteResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [StudioKey](#studiokey) | <p>Key echoes back the key of the deleted AssignedTagsConfig instance.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the (UTC) timestamp at which the system recognizes the</p><p>deletion. The only guarantees made about this timestamp are:</p><p>- it is after the time the request was received</p><p>- a time-ranged query with StartTime==DeletedAt will not include this instance.</p> |







<a name="arista.studio.v1.AssignedTagsConfigRequest"></a>

### AssignedTagsConfigRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [StudioKey](#studiokey) | <p>Key uniquely identifies a AssignedTagsConfig instance to retrieve.</p><p>This value must be populated.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the time for which you are interested in the data.</p><p>If no time is given, the server will use the time at which it makes the request.</p> |







<a name="arista.studio.v1.AssignedTagsConfigResponse"></a>

### AssignedTagsConfigResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [AssignedTagsConfig](#assignedtagsconfig) | <p>Value is the value requested.</p><p>This structure will be fully-populated as it exists in the datastore. If</p><p>optional fields were not given at creation, these fields will be empty or</p><p>set to default values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time carries the (UTC) timestamp of the last-modification of the</p><p>AssignedTagsConfig instance in this response.</p> |







<a name="arista.studio.v1.AssignedTagsConfigSetRequest"></a>

### AssignedTagsConfigSetRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [AssignedTagsConfig](#assignedtagsconfig) | <p>AssignedTagsConfig carries the value to set into the datastore.</p><p>See the documentation on the AssignedTagsConfig struct for which fields are required.</p> |







<a name="arista.studio.v1.AssignedTagsConfigSetResponse"></a>

### AssignedTagsConfigSetResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [AssignedTagsConfig](#assignedtagsconfig) | <p>Value carries all the values given in the AssignedTagsConfigSetRequest as well</p><p>as any server-generated values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the (UTC) timestamp at which the system recognizes the</p><p>creation. The only guarantees made about this timestamp are:</p><p>- it is after the time the request was received</p><p>- a time-ranged query with StartTime==CreatedAt will include this instance.</p> |







<a name="arista.studio.v1.AssignedTagsConfigStreamRequest"></a>

### AssignedTagsConfigStreamRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **partial_eq_filter** | [AssignedTagsConfig](#assignedtagsconfig)[...] | <p>PartialEqFilter provides a way to server-side filter a GetAll/Subscribe.</p><p>This requires all provided fields to be equal to the response.</p><p>While transparent to users, this field also allows services to optimize internal</p><p>subscriptions if filter(s) are sufficiently specific.</p> |
| **time** | arista.time.TimeBounds | <p>TimeRange allows limiting response data to within a specified time window.</p><p>If this field is populated, at least one of the two time fields are required.</p><p>This field is not allowed in the Subscribe RPC.</p> |







<a name="arista.studio.v1.AssignedTagsConfigStreamResponse"></a>

### AssignedTagsConfigStreamResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [AssignedTagsConfig](#assignedtagsconfig) | <p>Value is a value deemed relevant to the initiating request.</p><p>This structure will always have its key-field populated. Which other fields are</p><p>populated, and why, depends on the value of Operation and what triggered this notification.</p> |
| **time** | google.protobuf.Timestamp | <p>Time holds the timestamp of this AssignedTagsConfig's last modification.</p> |
| **type** | arista.subscriptions.Operation | <p>Operation indicates how the AssignedTagsConfig value in this response should be considered.</p><p>Under non-subscribe requests, this value should always be INITIAL. In a subscription,</p><p>once all initial data is streamed and the client begins to receive modification updates,</p><p>you should not see INITIAL again.</p> |







<a name="arista.studio.v1.AssignedTagsRequest"></a>

### AssignedTagsRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [StudioKey](#studiokey) | <p>Key uniquely identifies a AssignedTags instance to retrieve.</p><p>This value must be populated.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the time for which you are interested in the data.</p><p>If no time is given, the server will use the time at which it makes the request.</p> |







<a name="arista.studio.v1.AssignedTagsResponse"></a>

### AssignedTagsResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [AssignedTags](#assignedtags) | <p>Value is the value requested.</p><p>This structure will be fully-populated as it exists in the datastore. If</p><p>optional fields were not given at creation, these fields will be empty or</p><p>set to default values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time carries the (UTC) timestamp of the last-modification of the</p><p>AssignedTags instance in this response.</p> |







<a name="arista.studio.v1.AssignedTagsStreamRequest"></a>

### AssignedTagsStreamRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **partial_eq_filter** | [AssignedTags](#assignedtags)[...] | <p>PartialEqFilter provides a way to server-side filter a GetAll/Subscribe.</p><p>This requires all provided fields to be equal to the response.</p><p>While transparent to users, this field also allows services to optimize internal</p><p>subscriptions if filter(s) are sufficiently specific.</p> |
| **time** | arista.time.TimeBounds | <p>TimeRange allows limiting response data to within a specified time window.</p><p>If this field is populated, at least one of the two time fields are required.</p><p>This field is not allowed in the Subscribe RPC.</p> |







<a name="arista.studio.v1.AssignedTagsStreamResponse"></a>

### AssignedTagsStreamResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [AssignedTags](#assignedtags) | <p>Value is a value deemed relevant to the initiating request.</p><p>This structure will always have its key-field populated. Which other fields are</p><p>populated, and why, depends on the value of Operation and what triggered this notification.</p> |
| **time** | google.protobuf.Timestamp | <p>Time holds the timestamp of this AssignedTags's last modification.</p> |
| **type** | arista.subscriptions.Operation | <p>Operation indicates how the AssignedTags value in this response should be considered.</p><p>Under non-subscribe requests, this value should always be INITIAL. In a subscription,</p><p>once all initial data is streamed and the client begins to receive modification updates,</p><p>you should not see INITIAL again.</p> |







<a name="arista.studio.v1.InputsConfigDeleteRequest"></a>

### InputsConfigDeleteRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [InputsKey](#inputskey) | <p>Key indicates which InputsConfig instance to remove.</p><p>This field must always be set.</p> |







<a name="arista.studio.v1.InputsConfigDeleteResponse"></a>

### InputsConfigDeleteResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [InputsKey](#inputskey) | <p>Key echoes back the key of the deleted InputsConfig instance.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the (UTC) timestamp at which the system recognizes the</p><p>deletion. The only guarantees made about this timestamp are:</p><p>- it is after the time the request was received</p><p>- a time-ranged query with StartTime==DeletedAt will not include this instance.</p> |







<a name="arista.studio.v1.InputsConfigRequest"></a>

### InputsConfigRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [InputsKey](#inputskey) | <p>Key uniquely identifies a InputsConfig instance to retrieve.</p><p>This value must be populated.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the time for which you are interested in the data.</p><p>If no time is given, the server will use the time at which it makes the request.</p> |







<a name="arista.studio.v1.InputsConfigResponse"></a>

### InputsConfigResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [InputsConfig](#inputsconfig) | <p>Value is the value requested.</p><p>This structure will be fully-populated as it exists in the datastore. If</p><p>optional fields were not given at creation, these fields will be empty or</p><p>set to default values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time carries the (UTC) timestamp of the last-modification of the</p><p>InputsConfig instance in this response.</p> |







<a name="arista.studio.v1.InputsConfigSetRequest"></a>

### InputsConfigSetRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [InputsConfig](#inputsconfig) | <p>InputsConfig carries the value to set into the datastore.</p><p>See the documentation on the InputsConfig struct for which fields are required.</p> |







<a name="arista.studio.v1.InputsConfigSetResponse"></a>

### InputsConfigSetResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [InputsConfig](#inputsconfig) | <p>Value carries all the values given in the InputsConfigSetRequest as well</p><p>as any server-generated values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the (UTC) timestamp at which the system recognizes the</p><p>creation. The only guarantees made about this timestamp are:</p><p>- it is after the time the request was received</p><p>- a time-ranged query with StartTime==CreatedAt will include this instance.</p> |







<a name="arista.studio.v1.InputsConfigStreamRequest"></a>

### InputsConfigStreamRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **partial_eq_filter** | [InputsConfig](#inputsconfig)[...] | <p>PartialEqFilter provides a way to server-side filter a GetAll/Subscribe.</p><p>This requires all provided fields to be equal to the response.</p><p>While transparent to users, this field also allows services to optimize internal</p><p>subscriptions if filter(s) are sufficiently specific.</p> |
| **time** | arista.time.TimeBounds | <p>TimeRange allows limiting response data to within a specified time window.</p><p>If this field is populated, at least one of the two time fields are required.</p><p>This field is not allowed in the Subscribe RPC.</p> |







<a name="arista.studio.v1.InputsConfigStreamResponse"></a>

### InputsConfigStreamResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [InputsConfig](#inputsconfig) | <p>Value is a value deemed relevant to the initiating request.</p><p>This structure will always have its key-field populated. Which other fields are</p><p>populated, and why, depends on the value of Operation and what triggered this notification.</p> |
| **time** | google.protobuf.Timestamp | <p>Time holds the timestamp of this InputsConfig's last modification.</p> |
| **type** | arista.subscriptions.Operation | <p>Operation indicates how the InputsConfig value in this response should be considered.</p><p>Under non-subscribe requests, this value should always be INITIAL. In a subscription,</p><p>once all initial data is streamed and the client begins to receive modification updates,</p><p>you should not see INITIAL again.</p> |







<a name="arista.studio.v1.InputsRequest"></a>

### InputsRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [InputsKey](#inputskey) | <p>Key uniquely identifies a Inputs instance to retrieve.</p><p>This value must be populated.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the time for which you are interested in the data.</p><p>If no time is given, the server will use the time at which it makes the request.</p> |







<a name="arista.studio.v1.InputsResponse"></a>

### InputsResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [Inputs](#inputs) | <p>Value is the value requested.</p><p>This structure will be fully-populated as it exists in the datastore. If</p><p>optional fields were not given at creation, these fields will be empty or</p><p>set to default values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time carries the (UTC) timestamp of the last-modification of the</p><p>Inputs instance in this response.</p> |







<a name="arista.studio.v1.InputsStreamRequest"></a>

### InputsStreamRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **partial_eq_filter** | [Inputs](#inputs)[...] | <p>PartialEqFilter provides a way to server-side filter a GetAll/Subscribe.</p><p>This requires all provided fields to be equal to the response.</p><p>While transparent to users, this field also allows services to optimize internal</p><p>subscriptions if filter(s) are sufficiently specific.</p> |
| **time** | arista.time.TimeBounds | <p>TimeRange allows limiting response data to within a specified time window.</p><p>If this field is populated, at least one of the two time fields are required.</p><p>This field is not allowed in the Subscribe RPC.</p> |







<a name="arista.studio.v1.InputsStreamResponse"></a>

### InputsStreamResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [Inputs](#inputs) | <p>Value is a value deemed relevant to the initiating request.</p><p>This structure will always have its key-field populated. Which other fields are</p><p>populated, and why, depends on the value of Operation and what triggered this notification.</p> |
| **time** | google.protobuf.Timestamp | <p>Time holds the timestamp of this Inputs's last modification.</p> |
| **type** | arista.subscriptions.Operation | <p>Operation indicates how the Inputs value in this response should be considered.</p><p>Under non-subscribe requests, this value should always be INITIAL. In a subscription,</p><p>once all initial data is streamed and the client begins to receive modification updates,</p><p>you should not see INITIAL again.</p> |







<a name="arista.studio.v1.StudioConfigDeleteRequest"></a>

### StudioConfigDeleteRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [StudioKey](#studiokey) | <p>Key indicates which StudioConfig instance to remove.</p><p>This field must always be set.</p> |







<a name="arista.studio.v1.StudioConfigDeleteResponse"></a>

### StudioConfigDeleteResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [StudioKey](#studiokey) | <p>Key echoes back the key of the deleted StudioConfig instance.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the (UTC) timestamp at which the system recognizes the</p><p>deletion. The only guarantees made about this timestamp are:</p><p>- it is after the time the request was received</p><p>- a time-ranged query with StartTime==DeletedAt will not include this instance.</p> |







<a name="arista.studio.v1.StudioConfigRequest"></a>

### StudioConfigRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [StudioKey](#studiokey) | <p>Key uniquely identifies a StudioConfig instance to retrieve.</p><p>This value must be populated.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the time for which you are interested in the data.</p><p>If no time is given, the server will use the time at which it makes the request.</p> |







<a name="arista.studio.v1.StudioConfigResponse"></a>

### StudioConfigResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [StudioConfig](#studioconfig) | <p>Value is the value requested.</p><p>This structure will be fully-populated as it exists in the datastore. If</p><p>optional fields were not given at creation, these fields will be empty or</p><p>set to default values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time carries the (UTC) timestamp of the last-modification of the</p><p>StudioConfig instance in this response.</p> |







<a name="arista.studio.v1.StudioConfigSetRequest"></a>

### StudioConfigSetRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [StudioConfig](#studioconfig) | <p>StudioConfig carries the value to set into the datastore.</p><p>See the documentation on the StudioConfig struct for which fields are required.</p> |







<a name="arista.studio.v1.StudioConfigSetResponse"></a>

### StudioConfigSetResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [StudioConfig](#studioconfig) | <p>Value carries all the values given in the StudioConfigSetRequest as well</p><p>as any server-generated values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the (UTC) timestamp at which the system recognizes the</p><p>creation. The only guarantees made about this timestamp are:</p><p>- it is after the time the request was received</p><p>- a time-ranged query with StartTime==CreatedAt will include this instance.</p> |







<a name="arista.studio.v1.StudioConfigStreamRequest"></a>

### StudioConfigStreamRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **partial_eq_filter** | [StudioConfig](#studioconfig)[...] | <p>PartialEqFilter provides a way to server-side filter a GetAll/Subscribe.</p><p>This requires all provided fields to be equal to the response.</p><p>While transparent to users, this field also allows services to optimize internal</p><p>subscriptions if filter(s) are sufficiently specific.</p> |
| **time** | arista.time.TimeBounds | <p>TimeRange allows limiting response data to within a specified time window.</p><p>If this field is populated, at least one of the two time fields are required.</p><p>This field is not allowed in the Subscribe RPC.</p> |







<a name="arista.studio.v1.StudioConfigStreamResponse"></a>

### StudioConfigStreamResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [StudioConfig](#studioconfig) | <p>Value is a value deemed relevant to the initiating request.</p><p>This structure will always have its key-field populated. Which other fields are</p><p>populated, and why, depends on the value of Operation and what triggered this notification.</p> |
| **time** | google.protobuf.Timestamp | <p>Time holds the timestamp of this StudioConfig's last modification.</p> |
| **type** | arista.subscriptions.Operation | <p>Operation indicates how the StudioConfig value in this response should be considered.</p><p>Under non-subscribe requests, this value should always be INITIAL. In a subscription,</p><p>once all initial data is streamed and the client begins to receive modification updates,</p><p>you should not see INITIAL again.</p> |







<a name="arista.studio.v1.StudioRequest"></a>

### StudioRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [StudioKey](#studiokey) | <p>Key uniquely identifies a Studio instance to retrieve.</p><p>This value must be populated.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the time for which you are interested in the data.</p><p>If no time is given, the server will use the time at which it makes the request.</p> |







<a name="arista.studio.v1.StudioResponse"></a>

### StudioResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [Studio](#studio) | <p>Value is the value requested.</p><p>This structure will be fully-populated as it exists in the datastore. If</p><p>optional fields were not given at creation, these fields will be empty or</p><p>set to default values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time carries the (UTC) timestamp of the last-modification of the</p><p>Studio instance in this response.</p> |







<a name="arista.studio.v1.StudioStreamRequest"></a>

### StudioStreamRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **partial_eq_filter** | [Studio](#studio)[...] | <p>PartialEqFilter provides a way to server-side filter a GetAll/Subscribe.</p><p>This requires all provided fields to be equal to the response.</p><p>While transparent to users, this field also allows services to optimize internal</p><p>subscriptions if filter(s) are sufficiently specific.</p> |
| **time** | arista.time.TimeBounds | <p>TimeRange allows limiting response data to within a specified time window.</p><p>If this field is populated, at least one of the two time fields are required.</p><p>This field is not allowed in the Subscribe RPC.</p> |







<a name="arista.studio.v1.StudioStreamResponse"></a>

### StudioStreamResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [Studio](#studio) | <p>Value is a value deemed relevant to the initiating request.</p><p>This structure will always have its key-field populated. Which other fields are</p><p>populated, and why, depends on the value of Operation and what triggered this notification.</p> |
| **time** | google.protobuf.Timestamp | <p>Time holds the timestamp of this Studio's last modification.</p> |
| **type** | arista.subscriptions.Operation | <p>Operation indicates how the Studio value in this response should be considered.</p><p>Under non-subscribe requests, this value should always be INITIAL. In a subscription,</p><p>once all initial data is streamed and the client begins to receive modification updates,</p><p>you should not see INITIAL again.</p> |






 <!-- end messages -->

 <!-- end enums -->

 <!-- end HasExtensions -->


<a name="arista.studio.v1.AssignedTagsConfigService"></a>

### AssignedTagsConfigService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetOne | [AssignedTagsConfigRequest](#arista.studio.v1.AssignedTagsConfigRequest) | [AssignedTagsConfigResponse](#arista.studio.v1.AssignedTagsConfigResponse) | <p></p> |
| GetAll | [AssignedTagsConfigStreamRequest](#arista.studio.v1.AssignedTagsConfigStreamRequest) | [AssignedTagsConfigStreamResponse](#arista.studio.v1.AssignedTagsConfigStreamResponse) stream | <p></p> |
| Subscribe | [AssignedTagsConfigStreamRequest](#arista.studio.v1.AssignedTagsConfigStreamRequest) | [AssignedTagsConfigStreamResponse](#arista.studio.v1.AssignedTagsConfigStreamResponse) stream | <p></p> |
| Set | [AssignedTagsConfigSetRequest](#arista.studio.v1.AssignedTagsConfigSetRequest) | [AssignedTagsConfigSetResponse](#arista.studio.v1.AssignedTagsConfigSetResponse) | <p></p> |
| Delete | [AssignedTagsConfigDeleteRequest](#arista.studio.v1.AssignedTagsConfigDeleteRequest) | [AssignedTagsConfigDeleteResponse](#arista.studio.v1.AssignedTagsConfigDeleteResponse) | <p></p> |


<a name="arista.studio.v1.AssignedTagsService"></a>

### AssignedTagsService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetOne | [AssignedTagsRequest](#arista.studio.v1.AssignedTagsRequest) | [AssignedTagsResponse](#arista.studio.v1.AssignedTagsResponse) | <p></p> |
| GetAll | [AssignedTagsStreamRequest](#arista.studio.v1.AssignedTagsStreamRequest) | [AssignedTagsStreamResponse](#arista.studio.v1.AssignedTagsStreamResponse) stream | <p></p> |
| Subscribe | [AssignedTagsStreamRequest](#arista.studio.v1.AssignedTagsStreamRequest) | [AssignedTagsStreamResponse](#arista.studio.v1.AssignedTagsStreamResponse) stream | <p></p> |


<a name="arista.studio.v1.InputsConfigService"></a>

### InputsConfigService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetOne | [InputsConfigRequest](#arista.studio.v1.InputsConfigRequest) | [InputsConfigResponse](#arista.studio.v1.InputsConfigResponse) | <p></p> |
| GetAll | [InputsConfigStreamRequest](#arista.studio.v1.InputsConfigStreamRequest) | [InputsConfigStreamResponse](#arista.studio.v1.InputsConfigStreamResponse) stream | <p></p> |
| Subscribe | [InputsConfigStreamRequest](#arista.studio.v1.InputsConfigStreamRequest) | [InputsConfigStreamResponse](#arista.studio.v1.InputsConfigStreamResponse) stream | <p></p> |
| Set | [InputsConfigSetRequest](#arista.studio.v1.InputsConfigSetRequest) | [InputsConfigSetResponse](#arista.studio.v1.InputsConfigSetResponse) | <p></p> |
| Delete | [InputsConfigDeleteRequest](#arista.studio.v1.InputsConfigDeleteRequest) | [InputsConfigDeleteResponse](#arista.studio.v1.InputsConfigDeleteResponse) | <p></p> |


<a name="arista.studio.v1.InputsService"></a>

### InputsService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetOne | [InputsRequest](#arista.studio.v1.InputsRequest) | [InputsResponse](#arista.studio.v1.InputsResponse) | <p></p> |
| GetAll | [InputsStreamRequest](#arista.studio.v1.InputsStreamRequest) | [InputsStreamResponse](#arista.studio.v1.InputsStreamResponse) stream | <p></p> |
| Subscribe | [InputsStreamRequest](#arista.studio.v1.InputsStreamRequest) | [InputsStreamResponse](#arista.studio.v1.InputsStreamResponse) stream | <p></p> |


<a name="arista.studio.v1.StudioConfigService"></a>

### StudioConfigService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetOne | [StudioConfigRequest](#arista.studio.v1.StudioConfigRequest) | [StudioConfigResponse](#arista.studio.v1.StudioConfigResponse) | <p></p> |
| GetAll | [StudioConfigStreamRequest](#arista.studio.v1.StudioConfigStreamRequest) | [StudioConfigStreamResponse](#arista.studio.v1.StudioConfigStreamResponse) stream | <p></p> |
| Subscribe | [StudioConfigStreamRequest](#arista.studio.v1.StudioConfigStreamRequest) | [StudioConfigStreamResponse](#arista.studio.v1.StudioConfigStreamResponse) stream | <p></p> |
| Set | [StudioConfigSetRequest](#arista.studio.v1.StudioConfigSetRequest) | [StudioConfigSetResponse](#arista.studio.v1.StudioConfigSetResponse) | <p></p> |
| Delete | [StudioConfigDeleteRequest](#arista.studio.v1.StudioConfigDeleteRequest) | [StudioConfigDeleteResponse](#arista.studio.v1.StudioConfigDeleteResponse) | <p></p> |


<a name="arista.studio.v1.StudioService"></a>

### StudioService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetOne | [StudioRequest](#arista.studio.v1.StudioRequest) | [StudioResponse](#arista.studio.v1.StudioResponse) | <p></p> |
| GetAll | [StudioStreamRequest](#arista.studio.v1.StudioStreamRequest) | [StudioStreamResponse](#arista.studio.v1.StudioStreamResponse) stream | <p></p> |
| Subscribe | [StudioStreamRequest](#arista.studio.v1.StudioStreamRequest) | [StudioStreamResponse](#arista.studio.v1.StudioStreamResponse) stream | <p></p> |

 <!-- end services -->



