---
title: GetOne
weight: 10
pre: "<b>a. </b>"
---


`GetOne` returns a single instance of a resource.

{{% notice note %}}
The `Key` field is required to be fully-specified because `GetOne` needs to identify exactly-one
resource to fetch.
{{% /notice %}}

#### RPC Definition

The protobuf definition of `GetOne` is defined as such (for `ExampleConfig`):

```protobuf
rpc GetOne (ExampleConfigRequest) returns (ExampleConfigResponse);
```

#### Request Type

The generated request for a model (`ExampleConfig`, here) looks like so:

```protobuf
message ExampleConfigRequest {
  // Key uniquely identifies a ExampleConfig instance to retrieve.
  // This value must be populated (non-null) and all fields set.
  ExampleKey key = 1;

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
message ExampleConfigResponse {
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
