---
title: Modeling
weight: 1
---

Resources are modeled in [Protobuf](https://developers.google.com/protocol-buffers) and accessed over [gRPC](https://grpc.io/) with a standardized set of RPCs (discussed in later sections). These models are divided into two types:

- **config**: models which allow user-modification, exposing modifiable/tunable options.
- **state**: models which expose read-only operational and/or derived state based on _config_ data.



## Config Models

Config models describe the user's interaction with the system. Fields in these models are populated by the user (or by defaults).

Config models are read-writeable, meaning their APIs expose both read and write methods. The Protobuf message extension `fmp.model = "rw"` denotes that a given model is used as _config_ and the generated RPCs will expose both read and write method sets.



## State Models

State models describe the operational state of the system. Fields in these models are populated by the system and are not modifiable (except through the relevant _config_ model). 

State models only have read methods defined and are denoted with the Protobuf message extension `fmp.model = "ro"`.

While not required, _state_ models are allowed to "echo" the associated _config_ model for convenience of the user. You should check the relevant model(s) before expecting this behaviour, however.


## High Level Config-State Flow

Below is a diagram explaining the data flow from writing a Config to the system creating/updating State.
_Typically_, this process is asynchronous and the client will receive a response to the `Set` request before
the state is readable. Verification and durably storing the config are the only gating requirements to responding to
the Config write-request.

While the config request is an input to deriving the state, there are other (possible) inputs into state:

- non-configurable on-device settings or data (ex: device boot time)
- CloudVision configuration (ex: default user permissions)
- related config/state models (if noted in documentation)
- etc

Subscribing to State (ideally, with a filter) allows the client to wait for any asynchronous processing.

![State-Config Data Flow](/cloudvision-apis/images/config-state-flow.svg)

All responses from [RPCs](/cloudvision-apis/rpcs/) include a timestamp. This timestamp should be viewed as the time at
which the system durably stored an action (whether config or state). Thus, all state requests will return a
timestamp >= than that of the config that initiated the action.


## Nullable Types

To make partial updates (both by users into the system as well as updates from the system) possible all primitive fields, maps, and repeated fields are wrapped in nullable messages. This nullability allows both the user and the system to differentiate between unset and zero-valued fields.

For example:

```proto
message Nullability {
    // This value will contain "" when not set by the user/system.
    // It is not possible to know whether "" is the intended value, or simply omitted.
    string unwrapped_string = 1;

    // This value will contain null when not set by the user/system.
    // When the wrapper message is non-null, an empty string ("") has
    // the context of being intentionally set.
    google.protobuf.StringValue wrapped_string = 2;
}
```

A list of the available wrapper types can be seen [here](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf), though models may define their own for maps or repeated (array) fields.


## Keys

All models (whether config or state) contain a _key_ message.

This key contains the minimal set of data needed to uniquely identify a given model entity. Model keys may be as simple as a single string (say, a name) or as complex as containing references to a datacenter, device, interface, or any combination of them. The complexity of the key depends entirely on the model at hand.

Messages used for keys are denoted in protobuf with the extension: `fmp.model_key = true`.
