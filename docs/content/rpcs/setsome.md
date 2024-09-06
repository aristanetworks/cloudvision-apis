---
title: SetSome
weight: 15
pre: "<b>f. </b>"
---

`SetSome` updates multiple instances of a keyed resource. Updates can be whole or partial (see: nullable fields) using only fields populated in the request. 

{{% notice note %}}
SetSome is supported on all keyed resources.\
However, in certain releases, this may have been missing. See Support section below for details.
{{% /notice %}}

{{% notice note %}}
The `Values` field is required to be fully-specified because `SetSome` needs to identify 
resources to update.
{{% /notice %}}

A `*SetSomeResponse` will "echo" back the key of a resource that failed to set. It will also contain an error description on why the resource failed to set.

```protobuf
rpc Set (ExampleConfigSetSomeRequest) returns (stream ExampleSetSomeResponse);
```

#### Request Type

The generated request for a model (`ExampleConfig`, here) looks like so:

```protobuf
message ExampleConfigSetSomeRequest {
  // values contains a list of ExampleConfig values to write.
  // It is possible to provide more values than can fit within either:
  //     - the maxiumum send size of the client
  //     - the maximum receive size of the server
  // If this error occurs you must reduce the number of values sent.
  // See gRPC "maximum message size" documentation for more information.
  // ExampleConfig carries the value to set into the datastore.
  repeated ExampleConfig values = 1;
};
```

#### Response Type

The generated response for a model (`ExampleConfig`, here) looks like so:

```protobuf
message ExampleConfigSetResponse {
  // Key is the key of the resource that failed to set.
  ExampleKey key = 1;
  // Error indicates the reason why the set failed for the resource.
  string error = 2;
};
```

#### Support
Supported for configlet.v1, event.v1, studio.v1, tag.v2, workspace.v1 in CloudVision-as-a-Service.

Supported for tag.v2, studio.v1 from CVP 2023.2.0

Supported for configlet.v1, event.v1 from CVP 2024.2.0


