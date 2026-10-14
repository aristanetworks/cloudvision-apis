---
title: "Client Best Practices"
---

Below is a list of best-practices (or at least concepts to consider) when
implementing a client that interacts with these APIs. Much of this will
overlap with the details under [Uniform RPCs](/docs/rpcs/), but with a focus on
nuanced behavior (rather than modeling, inputs, outputs, etc).

## New Enum Values

We hold ourselves subject to `buf`'s [breaking changes](https://buf.build/docs/breaking/rules/)
rules. This means any release of a model is **functionally** backward-compatible.
The *"functionally"* distinction is important here because it means we will not
break the *existing* functionality of an older client; it does not mean that we will
not provide new functionality the older client may or may not understand.

Imagine we have some `v1.0` enum such as:

```protobuf
// BuildStatus enum in v1.0
enum BuildStatus {
  BUILD_STATUS_QUEUED    = 1;
  BUILD_STATUS_FAILED    = 2;
  BUILD_STATUS_SUCCESS   = 3;
}
```

but later we wish to add `BUILD_STATUS_RUNNING` for when the build is between
the `QUEUED` and the terminal states (`FAILED`/`SUCCESS`). The model is allowed to
be updated to the following because it is a forward and backward compatible change:


```protobuf
// BuildStatus enum in v1.1
enum BuildStatus {
  // ... existing entries ...
  BUILD_STATUS_RUNNING   = 4;
}
```

The caveat is that a `v1.0` client will not know about the `RUNNING` variant.
If a `v1.0` client has some code like:

```go
switch msg.BuildStatus {
case BUILD_STATUS_QUEUED:  // handled
case BUILD_STATUS_FAILED:  // handled
case BUILD_STATUS_SUCCESS: // handled

default:
	return fmt.Errorf("unknown build status")
}
```

then the client will error/panic/etc. This can and should be avoided, though, because
under the backward-compatibility guarantees we can say the client **must** be okay to
drop that message (otherwise it would not be functionally compatible).

:::note
**Most** languages that use numbers to represent enums (Go, Python, C/C++, etc.) all
simply use the new integer rather than throwing an error -- but the error case can/should
be handled the same way.
:::


Instead, this case should be handled like so:

```go
switch msg.BuildStatus {
// ... existing handlers ...
default:
	log.Errorf("unknown build status: %d", msg.BuildStatus) 
	// otherwise ignore this message 
	return nil
}
```

The message can be dropped/ignored and the client may not have the *maximal*
information, but it strictly has **no less** information than it had in `v1.0`.

A useful counter-example to the above that *does* break functional-compatability
and may make this concept clearer is if we update the enum to:

```protobuf
// BuildStatus enum in v1.2
enum BuildStatus {
  // ... existing entries ...
  BUILD_STATUS_CANCELED   = 5;
}
```

where the `CANCELED` variant is a new *terminal* state. Thus, the `v1.0` client
**cannot** tell when the build is in a terminal state and thus **does** lose
functionality (which would break our contract with the client). The client is
*worse* if it drops this message, and we do not allow that.

## Filtering on non-key fields in `Subscribe`

When you issue a [`Subscribe`](/docs/rpcs/subscribe/) with a filter
(regardless of if it's a `PartialEquality` or `Custom` filter), **all** messages that
are sent on the stream **must** pass the filter. This creates issues when a `Delete`
operation is received from the database without all the contents being filtered
against.

For instance, say you have some filter:

```go
Foo {
    Key: FooKey {
        WorkspaceId: "ABC123",
    },
    Status: PENDING,
}
```

that subscribes to all `Foo` entities in the workspace `ABC123` that are `PENDING`.
This is a reasonable subscription to make. However, if a user/system issues a `Foo::Delete`
on any entity that matches this filter, we **do not** guarantee the database will send the
`Status` field along with the delete message. The server is *always* able to reconstruct
the `Key` for a `Delete`, but that is the only guaranteed-available data (hence why the
`Delete` request is only the `key` field).

So when that `Delete` operation is received by the subscription handler, there is no
`Status` value and thus it fails the filter. Failing the filter means the client does
not receive the message about it being deleted.

The only fix for this would be to re-fetch the full data/state on every delete operation,
but this could be costly and cause other side effects in an eventually-consistent system.

:::note
This only is an issue if you care about set-membership. For instance, if you
only care about when a `Foo` moves into `PENDING` state but not that it is deleted,
moves to `COMPLETED`, etc. then it's a non-issue.
:::

### Suggested Resolution

The suggestion is in a `Subscribe`, filter only by guaranteed field (generally the
`key` unless documented otherwise). This casts a **broad** net and minimizes any chance
for unintended filtering. The client can do equivalent filtering (if needed) using either
language-specific filtering idioms or a [gRPC interceptor](https://grpc.io/docs/guides/interceptors/)
directly on the stream.

## Message Ordering

All responses in these APIs contain a timestamp that represents the last time that entity
was updated *as of that message being constructed*. However, you will notice that none of the
[RPC](/docs/rpcs/) docs specify any ordering guarantees (other than `Susbcribe`, but more on
that later). This is because we make no guarantee on ordering **unless it is functionally required**.

For example, if you make a [GetAll](/docs/rpcs/getall/) request on an API that has the entities:
```
A: updated @ T3
B: updated @ T1
C: updated @ T5
```

then the following are all valid orders on the stream:

```
[A, B, C]
[A, C, B]
[B, A, C]
[B, C, A]
[C, A, B]
[C, B, A]
```

### Subscription Ordering

There is a specification on [Subscribe](/docs/rpcs/subscribe/), however.
This is primarily that we **guarantee** the `SyncComplete` sentinel will come **before**
any partial update. This is documented in the RPC-specific docs, but it worth noting.

However, *within* any single phase of a subscription (the initial-sync or ongoing-updates)
there is **no order guarantee**. The initial-sync phase follows the same ordering guarantees
as `GetAll` described above (there is none). Likewise, in the ongoing-updates phase there is
no strict guarantee that you receive updates in timestamp order. Generally, in the ongoing-updates
phase you will receive updates for *the same entity* in order but this is not guaranteed across entities.
