# CloudVision APIs

## Introduction

Cloudvision APIs are state based, resource-oriented APIs in which resources are divided into configuration data models
(known as `config`) and operational and/or derived state models (known as `state`). Resources are modeled in
[Protobuf](https://developers.google.com/protocol-buffers) and accessed over [gRPC](https://grpc.io/) with a
standardized set of RPCs.

## Documentation

Documentation for these APIs is hosted at [aristanetworks.github.io/cloudvision-apis](https://aristanetworks.github.io/cloudvision-apis).

There, you can read more about:

* [Config and state models](https://aristanetworks.github.io/cloudvision-apis/modeling)
* [RPCs](https://aristanetworks.github.io/cloudvision-apis/rpcs)
* [Authentication](https://aristanetworks.github.io/cloudvision-apis/connecting)
* [Service-specific API documentation](https://aristanetworks.github.io/cloudvision-apis/models)
* [Examples](https://aristanetworks.github.io/cloudvision-apis/examples)

## Clients

Arista distributes pre-compiled clients for some languages. They are hosted in the following repositories:

* [Python](https://github.com/aristanetworks/cloudvision-python)
* [Golang](https://github.com/aristanetworks/cloudvision-go)

You may also generate your own. See [aristanetworks.github.io/cloudvision-apis](https://aristanetworks.github.io/cloudvision-apis/clients/creating)
for more details.

## Deprecation Policy

Deprecated APIs will containing the following at the top of the .proto file for the model:

```
option deprecated = true;
```

Announcements for API deprecation and the timeline for API removal are done as follows:

* For the cloud service (CVaaS), announcements are made on [status.arista.io](https://status.arista.io).
* For the on-premises product, announcements are made in the release notes of a particular version.
  APIs are removed two releases after deprecation is announced.
