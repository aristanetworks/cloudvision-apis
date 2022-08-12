---
title: gRPC
weight: 100
chapter: false
---

{{% notice tip %}}
For troubleshooting the following trace can be added before the `grpcurl` command:
`GRPC_GO_LOG_VERBOSITY_LEVEL=99 GRPC_GO_LOG_SEVERITY_LEVEL=info`
{{% /notice %}}

# gRPC API examples

gRPC APIs for both Resource APIs and cloudvision.Connector can be found at:
- https://github.com/aristanetworks/cloudvision-python
- https://github.com/aristanetworks/cloudvision-go

# gRPCurl Syntaxes

## List services

```bash
grpcurl -H 'Authorization: Bearer <token>' \
   -import-path <resource-path> \
   -proto <proto file> \
   -cacert <cvp cert> <host>:<port> list
```

## List methods of a service

```bash
grpcurl -H 'Authorization: Bearer <token>' \
   -import-path <resource-path> \
   -proto <proto file> \
   -cacert <cvp cert> <host>:<port> list <serviceName>
```

## Describe the details of the messages of the methods of a service

```bash
grpcurl -plaintext -msg-template -H 'Authorization: Bearer <token>' \
   -import-path <resource-path> \
   -proto <proto file> \
   -cacert <cvp cert> <host>:<port> describe <serviceName>.<method>
```

## Perform a call

```bash
grpcurl -H 'Authorization: Bearer <token>' \
   -import-path <resource-path> \
   -proto <proto file> \
   -cacert <cvp cert> -d '<JSON data>' <host>:<port> <serviceName>/<method>
```

# gRPCurl examples

## List event services

```bash
grpcurl  -H "Authorization: Bearer <token>" \
   -import-path $GOPATH/src/github.com/cloudvision-apis/ \
   -proto $GOPATH/src/github.com/cloudvision-apis/arista/event.v1/services.gen.proto \
   -cacert cvp.crt 192.0.2.100:443 list
```

Result:

```
arista.event.v1.EventAnnotationConfigService
arista.event.v1.EventService
```

## List methods of EventService

```bash
grpcurl  -H "Authorization: Bearer <token>" \
   -import-path $GOPATH/src/github.com/cloudvision-apis/ \
   -proto $GOPATH/src/github.com/cloudvision-apis/arista/event.v1/services.gen.proto \
   -cacert cvp.crt 192.0.2.100:443 list arista.event.v1.EventService
```

Result:

```
arista.event.v1.EventService.GetAll
arista.event.v1.EventService.GetOne
arista.event.v1.EventService.Subscribe
```

## Describe the details of the messages of the GetAll method of the EventService

```bash
grpcurl  -H "Authorization: Bearer <token>" \
   -import-path $GOPATH/src/github.com/cloudvision-apis/ \
   -proto $GOPATH/src/github.com/cloudvision-apis/arista/event.v1/services.gen.proto \
   -cacert cvp.crt 192.0.2.100:443 describe arista.event.v1.EventService.GetAll
```

Result:

```
arista.event.v1.EventService.GetAll is a method:
rpc GetAll ( .arista.event.v1.EventStreamRequest ) returns ( stream .arista.event.v1.EventStreamResponse );
```


## Describe the message template of the .arista.event.v1.EventStreamRequest message

```bash
grpcurl -plaintext -msg-template -H "Authorization: Bearer <token>" \
   -import-path $GOPATH/src/github.com/cloudvision-apis/ \
   -proto $GOPATH/src/github.com/cloudvision-apis/arista/event.v1/services.gen.proto \
   -cacert cvp.crt 192.0.2.100:443 describe .arista.event.v1.EventStreamRequest
```

Result:

```
arista.event.v1.EventStreamRequest is a message:
message EventStreamRequest {
  // PartialEqFilter provides a way to server-side filter a GetAll/Subscribe.
  // This requires all provided fields to be equal to the response.
  //
  // While transparent to users, this field also allows services to optimize internal
  // subscriptions if filter(s) are sufficiently specific.
  repeated .arista.event.v1.Event partial_eq_filter = 1;
  // TimeRange allows limiting response data to within a specified time window.
  // If this field is populated, at least one of the two time fields are required.
  //
  // This field is not allowed in the Subscribe RPC.
  .arista.time.TimeBounds time = 3;
}

Message template:
{
  "partialEqFilter": [
    {
      "key": {
        "key": "",
        "timestamp": "1970-01-01T00:00:00Z"
      },
      "severity": "EVENT_SEVERITY_UNSPECIFIED",
      "title": "",
      "description": "",
      "eventType": "",
      "data": {
        "data": {
          "": ""
        }
      },
      "components": {
        "components": [
          {
            "type": "COMPONENT_TYPE_UNSPECIFIED",
            "components": {
              "": ""
            }
          }
        ]
      },
      "ack": {
        "ack": false,
        "acker": "",
        "ackTime": "1970-01-01T00:00:00Z"
      },
      "notes": {
        "notes": {
          "0": {
            "note": "",
            "noteCreator": ""
          }
        }
      },
      "lastUpdatedTime": "1970-01-01T00:00:00Z"
    }
  ],
  "time": {
    "start": "1970-01-01T00:00:00Z",
    "end": "1970-01-01T00:00:00Z"
  }
}
```

## Describe the event severities


```bash
grpcurl  -H "Authorization: Bearer <token>" \
   -import-path $GOPATH/src/github.com/cloudvision-apis/ \
   -proto $GOPATH/src/github.com/cloudvision-apis/arista/event.v1/services.gen.proto \
   -cacert cvp.crt 192.0.2.100:443 describe arista.event.v1.EventSeverity
```

Result:

```
arista.event.v1.EventSeverity is an enum:
// EventSeverity is the severity level of the event
enum EventSeverity {
  EVENT_SEVERITY_UNSPECIFIED = 0;
  EVENT_SEVERITY_INFO = 1;
  EVENT_SEVERITY_WARNING = 2;
  EVENT_SEVERITY_ERROR = 3;
  EVENT_SEVERITY_CRITICAL = 4;
}
```


We can apply server-side filters using `partialEqFilter` or `partial_eq_filter` (so both snake_case and lowerCamelCase are supported) and apply various filters such as severity or eventType and others. 

 
Some of the variables are enums which means we can use both the variant and the discriminant, as in the below two examples we can get all ERROR severity events by setting severity to ​​`EVENT_SEVERITY_ERROR` or to `3`, both would yield the same result:

```
grpcurl -H "Authorization: Bearer <token>" \
   -import-path $GOPATH/src/github.com/cloudvision-apis/ \
   -proto $GOPATH/src/github.com/cloudvision-apis/arista/event.v1/services.gen.proto \
   -cacert cvp.crt  -d '{"partialEqFilter":[{"severity":"EVENT_SEVERITY_ERROR"}]}' 192.0.2.100:443 arista.event.v1.EventService/GetAll
```

or

```
grpcurl -H 'Authorization: Bearer <token>' \
   -import-path $GOPATH/src/github.com/cloudvision-apis/ \
   -proto $GOPATH/src/github.com/cloudvision-apis/arista/event.v1/services.gen.proto \
   -cacert cvp.crt  -d '{"partialEqFilter":[{"severity":3}]}' 192.0.2.100:443 arista.event.v1.EventService/GetAll
```

















