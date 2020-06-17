---
title: Subscribe
weight: 12
pre: "<b>c. </b>"
---

`Subscribe` first fetches (and optionally filters) resources at their current state (effectively a `GetAll`). Once existing state has been sent to the client, any updates (partial or whole) to resource entities are streamed back to the client.


{{% notice note %}}
`Subscribe` has the same signature as `GetAll`, though `Subscribe` does not allow setting the `time` field in the stream request as it is only concerned with current-time and onward. An error will be returned if `time` is set.
{{% /notice %}}


{{% notice note %}}
Filters work the same as in GetAll.
{{% /notice %}}


#### RPC Definition

The protobuf definition of `GetAll` is defined as such (for `ExampleConfig`):

```protobuf
rpc Subscribe (ExampleConfigStreamRequest) returns (stream ExampleConfigStreamResponse);
```
