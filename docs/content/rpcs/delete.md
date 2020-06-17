---
title: Delete
weight: 14
pre: "<b>e. </b>"
---

`Delete` deletes a resource and returns the time the delete became effective.

{{% notice note %}}
The `Key` field is required to be fully-specified because `Delete` needs to identify exactly-one
resource to delete.
{{% /notice %}}

#### RPC Definition

The protobuf definition of `GetOne` is defined as such (for `ExampleConfig`):

```protobuf
rpc Delete (ExampleConfigDeleteRequest) returns (ExampleConfigDeleteResponse);
```

#### Request Type

The generated request for a model (`ExampleConfig`, here) looks like so:


```protobuf
message ExampleConfigDeleteRequest {
  // Key indicates which ExampleConfig instance to remove.
  // This field must always be set.
  ExampleKey key = 1;
};
```

#### Response Type

The generated response for a model (`ExampleConfig`, here) looks like so:

```protobuf
message ExampleConfigDeleteResponse {
  // Key echoes back the key of the deleted ExampleConfig instance.
  ExampleKey key = 1;

  // Time indicates the (UTC) timestamp at which the system recognizes the
  // deletion. The only guarantees made about this timestamp are:
  //
  //    - it is after the time the request was received
  //    - a time-ranged query with StartTime==DeletedAt will not include this instance.
  //
  google.protobuf.Timestamp time = 2;
};
```


