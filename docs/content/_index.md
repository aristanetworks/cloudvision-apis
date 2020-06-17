# CloudVision APIs

Cloudvision APIs are state based, resource-oriented APIs modeled in [Protobuf](https://developers.google.com/protocol-buffers)
and accessed over [gRPC](https://grpc.io/) using a standardized set of RPC verbs.

CloudVision is a powerful platform that processes and stores tremendous amounts of network data.
It knows the topology of the network, device configuration, interface activity and other network events.
These APIs allow access to fleet-wide data access and control, forming a management-plane with consistent usage.

## Data Driven

Functionality is defined in a data-oriented (rather than action-oriented) form.
Designing the APIs to use state-synchronization confers some desirable traits:

{{% notice note %}}
For more information on modelling, see the [Modeling](/cloudvision-apis/modeling) page.
{{% /notice %}}

#### Uniform APIs

Adding a new API simply means creating a new model. Once a model is made, a set of consistent API
verbs can then be generated for it. These verbs are named and behave the same across all models.
For clients this makes it near trivial to adapt usage of one API to another.


#### Ergonomic Asynchronous APIs

Synchronous APIs, while simple, have some classic problems. Take for example a `DoReboot` operation.
This operation has numerous failure modes:

1. Request Timeouts: perhaps the operation took longer than the client expected
2. Network Interruption: similar to (1), but it's entirely possible for a connection to break
3. Device Bootlooping: perhaps rebooting is constantly failing. You must wait for a timeout to see that error.
4. Service Interruption: perhaps the reboot service (or host machine) has unrelated issues during the request

In each of these cases, the client is now responsible of determining which failure mode occurred and how
to proceed.

In a state-sharing paradigm a reboot request might be performed by setting a reboot request attribute to
the current time. The service can return from this request almost immediately (only durably writing the request).
Then the client can subscribe to a `last-reboot` attribute and knows the device has been rebooted successfully
when that attribute’s timestamp exceeds that of the reboot request. State sharing allows the various components
involved in an action not to need to care about each other; they just need to synchronize state when they 
come up, and then they’ll do the right thing.



## Portable

By modelling in `protobuf` and exposing `gRPC` RPCs, this data and management is accessible from nearly any
environment in [nearly any language](https://grpc.io/docs/languages/).

{{% notice note %}}
For Arista-supported clients, see the [Existing Clients](/cloudvision-apis/clients/existing) page.<br/>
Alternatively, a basic guide on [creating your own](/cloudvision-apis/clients/creating).
{{% /notice %}}

In addition to pure-gRPC clients, HTTP REST mappings are easily generated through the great gRPC ecosystem.
Thus, APIs can be utilized from nearly anywhere.


## gRPC Ecosystem

Another benefit of using `protobuf` and `gRPC` is the vast ecosystem surrounding them.
While portable client-generation is useful a well-supported ecosystem provides even more tooling.


{{% notice note %}}
This list is not extensive, nor an endorsement of any project.
Many more tools can be found on the [awesome-grpc](https://github.com/grpc-ecosystem/awesome-grpc) page.
{{% /notice %}}

* GUIs
    - [BloomRPC](https://github.com/uw-labs/bloomrpc)
    - [Milkman](https://github.com/warmuuh/milkman)
* CLI Tools
    - [GRPCurl](https://github.com/fullstorydev/grpcurl)
    - [evans](https://github.com/ktr0731/evans)
* Talks and Tutorials
    - [gRPC Overview: Talk at Slack by Varun Talwar](https://www.slideshare.net/VarunTalwar4/grpc-overview)
    - [gRPC: Google's high-performance, open-source RPC framework by Sameer Ajmani](https://www.youtube.com/watch?v=sZx3oZt7LVg)
    - [gRPC: The Story of Microservices at Square](https://www.youtube.com/watch?v=-2sWDr3Z0Wo)
    - ... and _many_ more!
