---
title: Subscribe
weight: 12
pre: "<b>c. </b>"
---

`Subscribe` first returns the initial state (fully-specified messages) and then any received updates.

The first messages received are effectively the result of a [GetAll](/cloudvision-apis/rpcs/getall)).
Once existing state has been sent to the client, any changes to resource entities are streamed back to the client. The
_update_ messages will represent what was updated and can either be a diff/partial or a fully-specified model.

{{% notice note %}}
Any [filters](/cloudvision-apis/rpcs/filtering) apply both to the initial state and updates.
{{% /notice %}}

Clients can determine whether a given message is part of the initial `GetAll` or an update via the
`arista.subscriptions.Operation` enum field on the `StreamResponse` type for the given resource. This enum can
be found [here](https://github.com/aristanetworks/cloudvision-apis/blob/trunk/arista/subscriptions/subscriptions.proto).

The flow of messages follows these steps:

1. `N` messages with `arista.subscriptions.Operation::INITIAL`
2. One message with `arista.subscriptions.Operation::INITIAL_SYNC_COMPLETE`
    - this signifies the transition from initial data to udpates
    - prevents the client from needing to hold the last operation to find transition point
3. `N` messages with either:
    - `arista.subscriptions.Operation::UPDATED`
    - `arista.subscriptions.Operation::DELETED`
    - these can happen in any order or frequency until the subscription/connection is closed



#### RPC Definition

The protobuf definition of `GetAll` is defined as such (for `ExampleConfig`):

```protobuf
rpc Subscribe (ExampleConfigStreamRequest) returns (stream ExampleConfigStreamResponse);
```
