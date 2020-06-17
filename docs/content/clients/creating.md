---
title: Creating a Client
weight: 2
---

A major advantage to Protobuf (and gRPC) is the ability to generate language bindings reliably and dependably.

The main gRPC site has tutorials for generating clients in many languages:

- [Java](https://grpc.io/docs/languages/java/basics/)
- [Node](https://grpc.io/docs/languages/node/basics/)
- [Ruby](https://grpc.io/docs/languages/ruby/basics/)
- [C#/.Net](https://grpc.io/docs/languages/csharp/basics/)
- ... and more

There is also an expansive ecosystem, so plenty of languages are supported.


### Tooling

In general, there are two main components to generating a language binding:

- `protoc`: The protobuf compiler which call the language-specific generator
    - typically installed via a package manager (`apt`, `yum`, `brew`, etc)
- `protoc-gen-{language}`: The language-specific generator
    - typically installed with the language's dependency manager, build tool, etc


### Generating

Regardless of language, client generation generally follows a pattern of:

```bash
$ protoc {includes} {lang-opts} {output-opts} {inputs}
```

We are primarily concerned with the `{includes}` and `{inputs}` bits. The rest of the options are up to you.

The `.proto` files used as inputs can be found in: [cloudvision-apis repo](https://github.com/aristanetworks/cloudvision-apis).
You should first clone (or download) that repository. Once you have it, generating a client is as simple as:

```bash
$ export CVAPIS=/some/path/to/cloudvision-apis
$ git clone https://github.com/aristanetworks/cloudvision-apis $CVAPIS
$ protoc -I $CVAPIS \
    {language-specific options go here} \
    $CVAPIS/arista/example.v1/example.proto $CVAPIS/arista/example.v1/services.gen.proto
```

In the above examples we generate the protobuf bindings (`example.proto`) as well as the gRPC services (`services.gen.go`)
in the same command. You are free to do them separately, however, different language generators handle this differently.
