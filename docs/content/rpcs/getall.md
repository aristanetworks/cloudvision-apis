---
title: GetAll
weight: 11
pre: "<b>b. </b>"
---


`GetAll` fetches (and optionally filters) all resource instances.

For the filtering options available, see the *Filtering* section.
These are the same for `Subscribe`.


#### RPC Definition

The protobuf definition of `GetAll` is defined as such (for `ExampleConfig`):

```protobuf
rpc GetAll (ExampleConfigStreamRequest) returns (stream ExampleConfigStreamResponse);
```

#### Request Type

The generated request for a model (`ExampleConfig`, here) looks like so:


```protobuf
message ExampleConfigStreamRequest {
  // PartialEqFilter provides a way to server-side filter a GetAll/Subscribe.
  // This requires all provided fields to be equal to the response.
  //
  // While transparent to users, this field also allows services to optimize internal
  // subscriptions if filter(s) are sufficiently specific.
  repeated ExampleConfig partial_eq_filter = 1;

  //
  // NOTE: Models are allowed to also contain a "implementation specific" filter
  //       which is more targetted, simple, or otherwise helpful.
  //       This filter type will be defined in the protobuf definition.
  //

  // TimeRange allows limiting response data to within a specified time window.
  // If this field is populated, at least one of the two time fields are required.
  //
  // This field is not allowed in the Subscribe RPC.
  arista.time.TimeBounds time = 3;
};
```

##### Time bounds

GetAll allows retrieving the history of one or many instances of a resource. These options are passed through the TimeBounds message:

```protobuf
message TimeBounds {
    google.protobuf.Timestamp start = 1;
    google.protobuf.Timestamp end = 2;
}
```

The fields `start` and `end` can be used in the following combinations:

- `end`: returns the state of resources at `end`.
- `start`: returns the state of resources at `start` and updates until now.
- `start` and `end`: returns the state of resources at `start` as well as any changes until `end`.
