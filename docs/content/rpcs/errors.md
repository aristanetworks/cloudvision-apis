---
title: Error Handling
weight: 2
pre: "<b>- </b>"
---

Errors returned by the API follow the [gRPC status code](https://github.com/grpc/grpc/blob/master/doc/statuscodes.md) guidelines. This provides many niceties:

1. Language-native idioms (exceptions, return codes, etc.)
2. Easily mappable to HTTP error codes (used for HTTP access to RPCs)
3. Uses metadata rather than a global schema for more detailed errors


### Example: Go

#### Unary RPCs

```go
resp, err := example.GetOne(ExampleConfigRequest{Key: key})
if err != nil {
    log.Printf("failed to get %+v: %s\n", key, err)
    return err
}
```

#### Streaming RPCs

```go
stream, err := example.GetAll(ExampleConfigStreamRequest{...})
if err != nil {
    log.Fatalf("failed to initialize GetAll stream: %s", err)
}
for {
    value, err := stream.Recv()
    if err == io.EOF {
        // all done
        break
    } else if err != nil {
        // stream was broken due to error
        log.Fatalf("stream was interrupted: %s", err)
    }

    log.Printf("%+v\n", value)
}
```

### Example: Python

#### Unary RPCs

```python
try:
    response = example_stub.Set(ExampleConfigSetRequest(...))
except grpc.RpcError as e:
    print('Set failed: {0}: {1}'.format(e.code(), e.details()))
    raise e
```

#### Streaming RPCs

```python
try:
  for resource in example_stub.GetAll(ExampleConfigStreamRequest(...)):
    # process resource
except grpc.RpcError as e:
  print('GetAll failed: {0}: {1}'.format(e.code(), e.details()))
  raise e
```
