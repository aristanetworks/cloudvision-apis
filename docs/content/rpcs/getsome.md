---
title: GetSome
weight: 11
pre: "<b>b. </b>"
---


`GetSome` returns multiple instances of a resource.

{{% notice note %}}
GetSome is supported on all keyed resources.\
However, in certain releases, this may have been missing. See Support section below for details.
{{% /notice %}}

{{% notice note %}}
The `Keys` field is required to be fully-specified because `GetSome` needs to identify resources to fetch.
{{% /notice %}}

#### RPC Definition

The protobuf definition of `GetSome` is defined as such (for `ExampleConfig`):

```protobuf
rpc GetSome (ExampleConfigSomeRequest) returns (stream ExampleConfigSomeResponse);
```

#### Request Type

The generated request for a model (`ExampleConfig`, here) looks like so:

```protobuf
message ExampleConfigSomeRequest {
  // Keys identifies the ExampleConfig instances to retrieve.
  // This value must be populated (non-null) and all fields set.
  repeated ExampleKey keys = 1;

  // Time indicates the time for which you are interested in the data.
  // If no time is given, the server will use the time at which it makes the request.
  //
  // This time is used as an upper-bound. The returned value may have been set at
  // an earlier time, however, it was the value as of the supplied time.
  google.protobuf.Timestamp time = 2;
}
```

#### Response Type

The generated response for a model (`ExampleConfig`, here) looks like so:


```protobuf
message ExampleConfigSomeResponse {
  // Value is the value requested.
  // This structure will be fully-populated as it exists in the datastore. If
  // optional fields were not given at creation, these fields will be empty or
  // set to default values.
  ExampleConfig value = 1;

  // Time carries the (UTC) timestamp of the last-modification of the
  // ExampleConfig instance in this response.
  //
  // As stated in the request above, this time will likely not match the request
  // exactly. But it will be before-or-equal to the requested time.
  google.protobuf.Timestamp time = 2;
};
```

#### Support
Supported for configlet.v1, connectivitymonitor.v1, tag.v2 in CloudVision-as-a-Service.

Supported for configlet.v1, connectivitymonitor.v1, tag.v2 from CVP 2024.2.0
