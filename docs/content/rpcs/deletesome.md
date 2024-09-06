---
title: DeleteSome
weight: 17
pre: "<b>h. </b>"
---

`DeleteSome` deletes a resource and streams back the resources that failed to be deleted and a description for the failure.

{{% notice note %}}
DeleteSome is supported on all keyed resources.\
However, in certain releases, this may have been missing. See Support section below for details.
{{% /notice %}}

{{% notice note %}}
The `Keys` field is required to be fully-specified because `DeleteSome` needs to identify resources to delete.
{{% /notice %}}

#### RPC Definition

The protobuf definition of `DeleteSome` is defined as such (for `ExampleConfig`):

```protobuf
rpc DeleteSome (ExampleConfigDeleteSomeRequest) returns (stream ExampleConfigDeleteSomeResponse);
```

#### Request Type

The generated request for a model (`ExampleConfig`, here) looks like so:


```protobuf
message ExampleConfigDeleteSomeRequest {
  // Keys indicates which ExampleConfig instances to remove.
  // This field must always be set.
  repeated ExampleKey keys = 1;
};
```

#### Response Type

The generated response for a model (`ExampleConfig`, here) looks like so:

```protobuf
// ExampleConfigDeleteSomeResponse is only sent when there is an error.
message ExampleConfigDeleteSomeResponse {
  // Key echoes back the key of ExampleConfig instance that failed to be deleted.
  ExampleKey key = 1;

  // Error is a description of the error encountered while deleting the
  // ExampleConfig instance.
  string error = 2;
};
```

#### Support
Supported for configlet.v1, studio.v1, tag.v2, workspace.v1 in CloudVision-as-a-Service.

Supported for configlet.v1, studio.v1, tag.v2 from CVP 2024.2.0
