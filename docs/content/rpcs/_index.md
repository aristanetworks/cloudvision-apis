---
title: Uniform RPCs
weight: 2
---

As stated previously, APIs are accesible over [gRPC](https://grpc.io/) with a standardized set of RPCs.

These methods will behave consistently across models.


## Read Methods

All readable models have the following RPC signatures:

```protobuf
service ExampleConfigService {
  rpc GetOne (ExampleConfigRequest) returns (ExampleConfigResponse);
  rpc GetAll (ExampleConfigStreamRequest) returns (stream ExampleConfigStreamResponse);
  rpc Subscribe (ExampleConfigStreamRequest) returns (stream ExampleConfigStreamResponse);
}
```

The `ExampleConfigRequest`, `ExampleConfigResponse`, `ExampleConfigStreamRequest`, and `ExampleConfigStreamResponse` are generated wrappers for a given model (`ExampleConfig`, in this example). By generating these wrappers we provide further consistency in request parameters.


## Write Methods

All wriable models have the following RPC signatures:

```protobuf
service ExampleConfigService {
  rpc Set (ExampleConfigSetRequest) returns (ExampleConfigSetResponse);
  rpc Delete (ExampleConfigDeleteRequest) returns (ExampleConfigDeleteResponse);
}
```
The `ExampleConfigSetRequest`, `ExampleConfigSetResponse`, `ExampleConfigDeleteRequest`, and `ExampleConfigDeleteResponse` are generated wrappers for a given model (`ExampleConfig`, in this example). By generating these wrappers we provide further consistency in request parameters.
