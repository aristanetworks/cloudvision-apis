---
title: event.v1
---



- [arista/event.v1/event.proto](#arista/event.v1/event.proto)
    - [Event](#event)
    - [EventAck](#eventack)
    - [EventAnnotationConfig](#eventannotationconfig)
    - [EventComponent](#eventcomponent)
    - [EventComponent.ComponentsEntry](#componentsentry)
    - [EventComponents](#eventcomponents)
    - [EventData](#eventdata)
    - [EventData.DataEntry](#dataentry)
    - [EventKey](#eventkey)
    - [EventNote](#eventnote)
    - [EventNoteConfig](#eventnoteconfig)
    - [EventNotes](#eventnotes)
    - [EventNotes.NotesEntry](#notesentry)
    - [EventNotesConfig](#eventnotesconfig)
    - [EventNotesConfig.NotesEntry](#notesentry)
  
    - [ComponentType](#arista.event.v1.ComponentType)
    - [EventSeverity](#arista.event.v1.EventSeverity)
  
- [arista/event.v1/services.gen.proto](#arista/event.v1/services.gen.proto)
    - [EventAnnotationConfigDeleteRequest](#eventannotationconfigdeleterequest)
    - [EventAnnotationConfigDeleteResponse](#eventannotationconfigdeleteresponse)
    - [EventAnnotationConfigRequest](#eventannotationconfigrequest)
    - [EventAnnotationConfigResponse](#eventannotationconfigresponse)
    - [EventAnnotationConfigSetRequest](#eventannotationconfigsetrequest)
    - [EventAnnotationConfigSetResponse](#eventannotationconfigsetresponse)
    - [EventAnnotationConfigStreamRequest](#eventannotationconfigstreamrequest)
    - [EventAnnotationConfigStreamResponse](#eventannotationconfigstreamresponse)
    - [EventRequest](#eventrequest)
    - [EventResponse](#eventresponse)
    - [EventStreamRequest](#eventstreamrequest)
    - [EventStreamResponse](#eventstreamresponse)
  
    - [EventAnnotationConfigService](#arista.event.v1.EventAnnotationConfigService)
    - [EventService](#arista.event.v1.EventService)
  




<a name="arista/event.v1/event.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## arista/event.v1/event.proto



<a name="arista.event.v1.Event"></a>

### Event
Event is a telemetry event


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [EventKey](#eventkey) | <p>key is the event instance identifier</p> |
| **severity** | [EventSeverity](#eventseverity) | <p>severity is the severity of the event</p> |
| **title** | google.protobuf.StringValue | <p>title is the title of the event</p> |
| **description** | google.protobuf.StringValue | <p>description is the description of the event</p> |
| **event_type** | google.protobuf.StringValue | <p>event_type is the type of the event</p> |
| **data** | [EventData](#eventdata) | <p>data is the data of the event</p> |
| **components** | [EventComponents](#eventcomponents) | <p>components is the components on which the event occurred</p> |
| **ack** | [EventAck](#eventack) | <p>ack is the acknowledgement status of the event</p> |
| **notes** | [EventNotes](#eventnotes) | <p>notes is the notes of the event</p> |
| **last_updated_time** | google.protobuf.Timestamp | <p>last_updated_time is the time of the most recent update to the event</p> |







<a name="arista.event.v1.EventAck"></a>

### EventAck
EventAck contains acknowledgement information of an event


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **ack** | google.protobuf.BoolValue | <p>ack is the acknowledgement state of an event</p> |
| **acker** | google.protobuf.StringValue | <p>acker is the user that acknowledged the event</p> |
| **ack_time** | google.protobuf.Timestamp | <p>ack_time is the time of acknowledgement</p> |







<a name="arista.event.v1.EventAnnotationConfig"></a>

### EventAnnotationConfig
EventAnnotationConfig configures an event annotation


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [EventKey](#eventkey) | <p>key is the event instance identifier</p> |
| **ack** | google.protobuf.BoolValue | <p>ack is the acknowledgement state of an event</p> |
| **notes** | [EventNotesConfig](#eventnotesconfig) | <p>notes is the notes on an event</p> |







<a name="arista.event.v1.EventComponent"></a>

### EventComponent
EventComponent describes an entity on which the event occured


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **type** | [ComponentType](#componenttype) | <p>type is the type of component</p> |
| **components** | [EventComponent.ComponentsEntry](#eventcomponent.componentsentry)[...] | <p>components identifies the entity on which the event occured</p> |







<a name="arista.event.v1.EventComponent.ComponentsEntry"></a>

### EventComponent.ComponentsEntry



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | string | <p></p> |
| **value** | string | <p></p> |







<a name="arista.event.v1.EventComponents"></a>

### EventComponents
EventComponents contains entities on which an event occured


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **components** | [EventComponent](#eventcomponent)[...] | <p>components describes the components on which an event occured</p> |







<a name="arista.event.v1.EventData"></a>

### EventData
EventData is additional event data


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **data** | [EventData.DataEntry](#eventdata.dataentry)[...] | <p>data is event data specific to the type of this event</p> |







<a name="arista.event.v1.EventData.DataEntry"></a>

### EventData.DataEntry



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | string | <p></p> |
| **value** | string | <p></p> |







<a name="arista.event.v1.EventKey"></a>

### EventKey
EventKey uniquely identifies an event


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | google.protobuf.StringValue | <p>key is the event data identifier</p> |
| **timestamp** | google.protobuf.Timestamp | <p>timestamp is the time the event occured</p> |







<a name="arista.event.v1.EventNote"></a>

### EventNote
Eventnote is the state of a note


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **note** | google.protobuf.StringValue | <p>note is the text of the note</p> |
| **note_creator** | google.protobuf.StringValue | <p>note_creator is the creator of the note</p> |







<a name="arista.event.v1.EventNoteConfig"></a>

### EventNoteConfig
EventNoteConfig configures a note


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **note** | google.protobuf.StringValue | <p>note is the text of the note</p> |







<a name="arista.event.v1.EventNotes"></a>

### EventNotes
EventNotes is the notes of an event state


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **notes** | [EventNotes.NotesEntry](#eventnotes.notesentry)[...] | <p>notes is keyed by the time desired</p> |







<a name="arista.event.v1.EventNotes.NotesEntry"></a>

### EventNotes.NotesEntry



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | int64 | <p></p> |
| **value** | [EventNote](#eventnote) | <p></p> |







<a name="arista.event.v1.EventNotesConfig"></a>

### EventNotesConfig
EventNotesConfig configures the notes of an event


| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **notes** | [EventNotesConfig.NotesEntry](#eventnotesconfig.notesentry)[...] | <p>notes is keyed by desired note time in Unix time, in milliseconds</p> |







<a name="arista.event.v1.EventNotesConfig.NotesEntry"></a>

### EventNotesConfig.NotesEntry



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | int64 | <p></p> |
| **value** | [EventNoteConfig](#eventnoteconfig) | <p></p> |






 <!-- end messages -->


<a name="arista.event.v1.ComponentType"></a>

### ComponentType
ComponentType describes the type of entity on which the event occured

| Name | Number | Description |
| ---- | ------ | ----------- |
| COMPONENT_TYPE_UNSPECIFIED | 0 | <p></p> |
| COMPONENT_TYPE_DEVICE | 1 | <p></p> |
| COMPONENT_TYPE_INTERFACE | 2 | <p></p> |
| COMPONENT_TYPE_TURBINE | 3 | <p></p> |



<a name="arista.event.v1.EventSeverity"></a>

### EventSeverity
EventSeverity is the severity level of the event

| Name | Number | Description |
| ---- | ------ | ----------- |
| EVENT_SEVERITY_UNSPECIFIED | 0 | <p></p> |
| EVENT_SEVERITY_INFO | 1 | <p></p> |
| EVENT_SEVERITY_WARNING | 2 | <p></p> |
| EVENT_SEVERITY_ERROR | 3 | <p></p> |
| EVENT_SEVERITY_CRITICAL | 4 | <p></p> |


 <!-- end enums -->

 <!-- end HasExtensions -->

 <!-- end services -->




<a name="arista/event.v1/services.gen.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## arista/event.v1/services.gen.proto



<a name="arista.event.v1.EventAnnotationConfigDeleteRequest"></a>

### EventAnnotationConfigDeleteRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [EventKey](#eventkey) | <p>Key indicates which EventAnnotationConfig instance to remove.</p><p>This field (and all keys, unless otherwise specified) must always be set.</p> |







<a name="arista.event.v1.EventAnnotationConfigDeleteResponse"></a>

### EventAnnotationConfigDeleteResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [EventKey](#eventkey) | <p>Key echoes back the key of the deleted EventAnnotationConfig instance.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the (UTC) timestamp at which the system recognizes the</p><p>deletion. The only guarantees made about this timestamp are:</p><p>- it is after the time the request was received</p><p>- a time-ranged query with StartTime==DeletedAt will not include this instance.</p> |







<a name="arista.event.v1.EventAnnotationConfigRequest"></a>

### EventAnnotationConfigRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [EventKey](#eventkey) | <p>Key uniquely identifies a EventAnnotationConfig instance to retrieve.</p><p>This value (and all fields, unless otherwise specified) must be populated.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the time for which you are interested in the data.</p><p>If no time is given, the server will use the time at twhich it makes the request.</p> |







<a name="arista.event.v1.EventAnnotationConfigResponse"></a>

### EventAnnotationConfigResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [EventAnnotationConfig](#eventannotationconfig) | <p>Value is the value requested.</p><p>This structure will be fully-populated as it exists in the datastore. If</p><p>optional fields were not given at creation, these fields will be empty or</p><p>set to default values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time carries the (UTC) timestamp of the last-modification of the</p><p>EventAnnotationConfig instance in this response.</p> |







<a name="arista.event.v1.EventAnnotationConfigSetRequest"></a>

### EventAnnotationConfigSetRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [EventAnnotationConfig](#eventannotationconfig) | <p>EventAnnotationConfig carries the value to set into the datastore.</p><p>See the documentation on the EventAnnotationConfig struct for which fields are required.</p> |







<a name="arista.event.v1.EventAnnotationConfigSetResponse"></a>

### EventAnnotationConfigSetResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [EventAnnotationConfig](#eventannotationconfig) | <p>Value carries all the values given in the EventAnnotationConfigSetRequest as well</p><p>as any server-generated values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the (UTC) timestamp at which the system recognizes the</p><p>creation. The only guarantees made about this timestamp are:</p><p>- it is after the time the request was received</p><p>- a time-ranged query with StartTime==CreatedAt will include this instance.</p> |







<a name="arista.event.v1.EventAnnotationConfigStreamRequest"></a>

### EventAnnotationConfigStreamRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **partial_eq_filter** | [EventAnnotationConfig](#eventannotationconfig)[...] | <p>PartialEqFilter provides a way to server-side filter a GetAll/Subscribe.</p><p>This requires all provided fields to be equal to the response.</p><p>While transparent to users, this field also allows services to optimize internal</p><p>subscriptions if filter(s) are sufficiently specific.</p> |
| **time** | arista.time.TimeBounds | <p>TimeRange allows limiting response data to within a specified time window.</p><p>If this field is populated, at least one of the two time fields are required.</p><p>This field is not allowed in the Subscribe RPC.</p> |







<a name="arista.event.v1.EventAnnotationConfigStreamResponse"></a>

### EventAnnotationConfigStreamResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [EventAnnotationConfig](#eventannotationconfig) | <p>Value is a value deemed relevant to the initiating request.</p><p>This structure will always have its key-field populated. Which other fields are</p><p>populated, and why, depends on the value of Operation and what triggered this notification.</p> |
| **time** | google.protobuf.Timestamp | <p>Time holds the timestamp of this EventAnnotationConfig's last modification.</p> |
| **type** | arista.subscriptions.Operation | <p>Operation indicates how the EventAnnotationConfig value in this response should be considered.</p><p>Under non-subscribe requests, this value should always be INITIAL. In a subscription,</p><p>once all initial data is streamed and the client begins to receive modification updates,</p><p>you should not see INITIAL again.</p> |







<a name="arista.event.v1.EventRequest"></a>

### EventRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **key** | [EventKey](#eventkey) | <p>Key uniquely identifies a Event instance to retrieve.</p><p>This value (and all fields, unless otherwise specified) must be populated.</p> |
| **time** | google.protobuf.Timestamp | <p>Time indicates the time for which you are interested in the data.</p><p>If no time is given, the server will use the time at twhich it makes the request.</p> |







<a name="arista.event.v1.EventResponse"></a>

### EventResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [Event](#event) | <p>Value is the value requested.</p><p>This structure will be fully-populated as it exists in the datastore. If</p><p>optional fields were not given at creation, these fields will be empty or</p><p>set to default values.</p> |
| **time** | google.protobuf.Timestamp | <p>Time carries the (UTC) timestamp of the last-modification of the</p><p>Event instance in this response.</p> |







<a name="arista.event.v1.EventStreamRequest"></a>

### EventStreamRequest



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **partial_eq_filter** | [Event](#event)[...] | <p>PartialEqFilter provides a way to server-side filter a GetAll/Subscribe.</p><p>This requires all provided fields to be equal to the response.</p><p>While transparent to users, this field also allows services to optimize internal</p><p>subscriptions if filter(s) are sufficiently specific.</p> |
| **time** | arista.time.TimeBounds | <p>TimeRange allows limiting response data to within a specified time window.</p><p>If this field is populated, at least one of the two time fields are required.</p><p>This field is not allowed in the Subscribe RPC.</p> |







<a name="arista.event.v1.EventStreamResponse"></a>

### EventStreamResponse



| Field Name | Type  | Description |
| ---------- | ----  | ----------- |
| **value** | [Event](#event) | <p>Value is a value deemed relevant to the initiating request.</p><p>This structure will always have its key-field populated. Which other fields are</p><p>populated, and why, depends on the value of Operation and what triggered this notification.</p> |
| **time** | google.protobuf.Timestamp | <p>Time holds the timestamp of this Event's last modification.</p> |
| **type** | arista.subscriptions.Operation | <p>Operation indicates how the Event value in this response should be considered.</p><p>Under non-subscribe requests, this value should always be INITIAL. In a subscription,</p><p>once all initial data is streamed and the client begins to receive modification updates,</p><p>you should not see INITIAL again.</p> |






 <!-- end messages -->

 <!-- end enums -->

 <!-- end HasExtensions -->


<a name="arista.event.v1.EventAnnotationConfigService"></a>

### EventAnnotationConfigService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetOne | [EventAnnotationConfigRequest](#arista.event.v1.EventAnnotationConfigRequest) | [EventAnnotationConfigResponse](#arista.event.v1.EventAnnotationConfigResponse) | <p>GetOne returns a unary model as specified by the key in the request.</p><p>The key must be provided and all fields populated (unless otherwise specified).</p> |
| GetAll | [EventAnnotationConfigStreamRequest](#arista.event.v1.EventAnnotationConfigStreamRequest) | [EventAnnotationConfigStreamResponse](#arista.event.v1.EventAnnotationConfigStreamResponse) stream | <p>GetAll returns all entities for this model, with optional filtering.</p> |
| Subscribe | [EventAnnotationConfigStreamRequest](#arista.event.v1.EventAnnotationConfigStreamRequest) | [EventAnnotationConfigStreamResponse](#arista.event.v1.EventAnnotationConfigStreamResponse) stream | <p>Subscribe first returns all initial state known to the system,</p><p>then will send deltas as entities are changed.</p> |
| Set | [EventAnnotationConfigSetRequest](#arista.event.v1.EventAnnotationConfigSetRequest) | [EventAnnotationConfigSetResponse](#arista.event.v1.EventAnnotationConfigSetResponse) | <p>Set allows setting values for the entity specified by the key in the request.</p><p>The key must be provided and all fields set (unless otherwise specified).</p> |
| Delete | [EventAnnotationConfigDeleteRequest](#arista.event.v1.EventAnnotationConfigDeleteRequest) | [EventAnnotationConfigDeleteResponse](#arista.event.v1.EventAnnotationConfigDeleteResponse) | <p>Delete will remove the entity specified by the key within the request.</p><p>The key must be provided and all fields populated (unless otherwise specified).</p> |


<a name="arista.event.v1.EventService"></a>

### EventService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetOne | [EventRequest](#arista.event.v1.EventRequest) | [EventResponse](#arista.event.v1.EventResponse) | <p>GetOne returns a unary model as specified by the key in the request.</p><p>The key must be provided and all fields populated (unless otherwise specified).</p> |
| GetAll | [EventStreamRequest](#arista.event.v1.EventStreamRequest) | [EventStreamResponse](#arista.event.v1.EventStreamResponse) stream | <p>GetAll returns all entities for this model, with optional filtering.</p> |
| Subscribe | [EventStreamRequest](#arista.event.v1.EventStreamRequest) | [EventStreamResponse](#arista.event.v1.EventStreamResponse) stream | <p>Subscribe first returns all initial state known to the system,</p><p>then will send deltas as entities are changed.</p> |

 <!-- end services -->



