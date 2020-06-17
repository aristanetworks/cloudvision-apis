# CloudVision APIs

## Introduction

Cloudvision APIs are state based, resource-oriented APIs in which resources are divided into configuration data models (known as `config`) and operational and/or derived state models (known as `state`). Resources are modeled in [Protobuf](https://developers.google.com/protocol-buffers) and accessed over [gRPC](https://grpc.io/) with a standardized set of RPCs.


## Errors

Errors returned by the API follow the [gRPC status code](https://github.com/grpc/grpc/blob/master/doc/statuscodes.md) guidelines.

### Example: Python

#### Unary RPCs

```python
try:
    response = example_stub.Set(ExampleConfigSetRequest(...))
except grpc.RpcError as e:
    print('Set failed: {0}: {1}'.format(e.code(), e.details()))
    raise e
```

#### Server Streaming RPCs

```python
try:
  for resource in example_stub.GetAll(ExampleConfigStreamRequest(...)):
    # process resource
except grpc.RpcError as e:
  print('GetAll failed: {0}: {1}'.format(e.code(), e.details()))
  raise e
```

## Working with Protobuf

Examples of how to use the Python generated Protobuf code can be found [here](https://developers.google.com/protocol-buffers/docs/reference/python-generated).

## Resources

Users call these APIs by setting config resources and reading state resources. Each instance of a resource has a key that uniquely identifies the instance. The key of a model is always the Protobuf message field named `key`. Protobuf messages that serve as keys have the Protobuf option `fmp.model_key = true`.

## Config Models

Config models describe the user's interaction with the system. Fields in these models are only populated by the user. Config models are read-writeable, meaning they have read and write methods defined on the models. Config models are denoted with the Protobuf message extension `fmp.model = "rw"`.

## State Models

State models describe the operational state of the system. Fields in these models are populated by the system and not modifiable, and only have read methods defined. State models are denoted with the Protobuf message extension `fmp.model = "ro"`.

## Protobuf Modeling

Resources are modeled as Protobuf messages. All primitive fields, maps, and repeated fields are wrapped in nullable messages to distinguish between fields that are unset and fields set to the zero value of that type.

## RPC Methods

### Read Methods

Read methods have the following RPC signatures:

```protobuf
service ExampleConfigResource {
  rpc GetOne (ExampleConfigRequest) returns (ExampleConfigResponse);
  rpc GetAll (ExampleConfigStreamRequest) returns (stream ExampleConfigStreamResponse);
  rpc Subscribe (ExampleConfigStreamRequest) returns (stream ExampleConfigStreamResponse);
}
```

#### GetOne

GetOne returns a single instance of a resource.
It can optionally take a timestamp to specify at what historical time a resource shoud be fetched.

The `Key` field is required to be fully-specified because `GetOne` needs to identify exactly-one
resource to fetch.

```protobuf
rpc GetOne (ExampleConfigRequest) returns (ExampleConfigResponse);
```

Request type:

```protobuf
message ExampleConfigRequest {
  // Key uniquely identifies a ExampleConfig instance to retrieve.
  // This value must be populated.
  ExampleKey key = 1;

  // Time indicates the time for which you are interested in the data.
  // If no time is given, the server will use the time at which it makes the request.
  google.protobuf.Timestamp time = 2;
}
```

Response type:

```protobuf
message ExampleConfigResponse {
  // Value is the value requested.
  // This structure will be fully-populated as it exists in the datastore. If
  // optional fields were not given at creation, these fields will be empty or
  // set to default values.
  ExampleConfig value = 1;

  // Time carries the (UTC) timestamp of the last-modification of the
  // ExampleConfig instance in this response.
  google.protobuf.Timestamp time = 2;
};
```
<!--- add a code snippet to GetOne in python --->

#### GetAll

GetAll gets and filters all resource instances.

For the filtering options available, see the *Filtering* section.
These are the same for `Subscribe`.

```protobuf
rpc GetAll (ExampleConfigStreamRequest) returns (stream ExampleConfigStreamResponse);
```

Request type:

```protobuf
message ExampleConfigStreamRequest {
  // PartialEqFilter provides a way to server-side filter a GetAll/Subscribe.
  // This requires all provided fields to be equal to the response.
  //
  // While transparent to users, this field also allows services to optimize internal
  // subscriptions if filter(s) are sufficiently specific.
  repeated ExampleConfig partial_eq_filter = 1;

  //
  // NOTE: Models are allowed to also contain a "implementation specific" filter
  //       which is more targetted, simple, or otherwise helpful.
  //       This filter type will be defined in the protobuf definition.
  //

  // TimeRange allows limiting response data to within a specified time window.
  // If this field is populated, at least one of the two time fields are required.
  //
  // This field is not allowed in the Subscribe RPC.
  arista.time.TimeBounds time = 3;
};
```

##### Time bounds

GetAll allows retrieving the history of one or many instances of a resource. These options are passed through the TimeBounds message:

```protobuf
message TimeBounds {
    google.protobuf.Timestamp start = 1;
    google.protobuf.Timestamp end = 2;
}
```

The fields `start` and `end` can be used in the following combinations:

- `end`: returns the state of resources at `end`.
- `start`: returns the state of resources at `start` and updates until now.
- `start` and `end`: returns the state of resources at `start` as well as any changes until `end`.

<!--- add a code snippet to GetAll with a filter and time range
snippet should also include reading from a stream--->

#### Subscribe

Subscribe gets resources at their current state and any updates to those resources.

```protobuf
rpc Subscribe (ExampleConfigStreamRequest) returns (stream ExampleConfigStreamResponse);
```

Subscribe has the same signature as GetAll, though Subscribe does not allow setting the `time` field in the stream request.

Filters work the same as in GetAll.

### Write Methods

Write methods have the following RPC signatures:

```protobuf
service ExampleConfigResource {
  rpc Set (ExampleConfigSetRequest) returns (ExampleSetResponse);
  rpc Delete (ExampleConfigDeleteRequest) returns (ExampleConfigDeleteResponse);
}
```

#### Set

Set updates a resource. `Set` only updates the fields that have been set.
The endpoint returns the time the `Set` becomes effective internally and the service's known-state of the resource.

The echo will be the original update-request at a minimum, and may include more data.
This allows services to do fast, write-only, updates to internal storage. If the service needs to query existing
state first then more data can be provided to the client. If you need a full model after a `Set` operation, you can issue
a `GetOne` with the returned `time`.

The `Key` field is required to be fully-specified because `Set` needs to identify exactly-one
resource to delete.


```protobuf
rpc Set (ExampleConfigSetRequest) returns (ExampleSetResponse);
```

Request type:

```protobuf
message ExampleConfigSetRequest {
  // ExampleConfig carries the value to set into the datastore.
  ExampleConfig value = 1;
};
```

Response type:

```protobuf
message ExampleConfigSetResponse {
  ExampleConfig value = 1;

  // Time indicates the (UTC) timestamp at which the system recognizes the
  // creation. The only guarantees made about this timestamp are:
  //
  //    - it is after the time the request was received
  //    - a time-ranged query with StartTime==CreatedAt will include this instance.
  //
  google.protobuf.Timestamp time = 2;
};
```

##### Updating maps

Set maps are merged with the existing map.

To delete all of the values in a map, set the wrapper message of the map and leave the map empty.

##### Updating repeated fields

Set `repeated` fields replace the existing array. For example, <!--- add updating repeated example here --->

To delete all of the values in a `repeated` field, set the wrapper message of the `repeated` and leave the `repeated` empty.

##### Updating subresources

Subresources are resources that are a child of another resource. A collection of subresources with compound keys is represented by a `repeated` field, though this collection should be treated as unordered and uses the same update semantics as maps. If multiple subresources with the same key are specified, the last one in the repeated ordering is assumed to be value.

##### Example: Update

Given an example proto:

```protobuf
syntax = "proto3";

import "google/protobuf/wrappers.proto";

message MapValue {
  google.protobuf.StringValue string_val = 1;
  google.protobuf.Int64Value int_val = 2;
}

message MapWrapper {
  map<string, MapValue> map = 1;
}

message RepeatedWrapper {
  repeated string repeated = 1;
}

message ExampleModel {
  google.protobuf.StringValue string_val = 1;
  google.protobuf.Int64Value int_val = 2;
  RepeatedWrapper repeated = 3;
  MapWrapper map = 4;
}
```

And a model:

```python
string_val {
  value: "one"
}
int_val {
  value: 2
}
repeated {
  repeated: "five"
  repeated: "six"
}
map {
  map {
    key: "four"
    value {
      string_val {
        value: "red"
      }
      int_val {
        value: 45
      }
    }
  }
  map {
    key: "three"
    value {
      string_val {
        value: "blue"
      }
      int_val {
        value: 42
      }
    }
  }
  map {
    key: "two"
    value {
      string_val {
        value: "purple"
      }
      int_val {
        value: 32
      }
    }
  }
}
```

Applying the following update:

```python
string_val {
  value: "two"
}
repeated {
  repeated: "eight"
  repeated: "nine"
}
map {
  map {
    key: "five"
    value {
      string_val {
        value: "orange"
      }
      int_val {
        value: 100
      }
    }
  }
  map {
    key: "four"
    value {
      string_val {
        value: "green"
      }
    }
  }
  map {
    key: "three"
    value {
      string_val {
        value: "yellow"
      }
      int_val {
        value: 12
      }
    }
  }
}
```

results in the updated model:

```python
string_val {
  value: "two"
}
int_val {
  value: 2
}
repeated {
  repeated: "eight"
  repeated: "nine"
}
map {
  map {
    key: "five"
    value {
      string_val {
        value: "orange"
      }
      int_val {
        value: 100
      }
    }
  }
  map {
    key: "four"
    value {
      string_val {
        value: "green"
      }
      int_val {
        value: 45
      }
    }
  }
  map {
    key: "three"
    value {
      string_val {
        value: "yellow"
      }
      int_val {
        value: 12
      }
    }
  }
  map {
    key: "two"
    value {
      string_val {
        value: "purple"
      }
      int_val {
        value: 32
      }
    }
  }
}
```

#### Delete

Delete deletes a resource. Delete returns the time the delete was received.

The `Key` field is required to be fully-specified because `Delete` needs to identify exactly-one
resource to delete.

```protobuf
rpc Delete (ExampleConfigDeleteRequest) returns (ExampleConfigDeleteResponse);
```

Request type:

```protobuf
message ExampleConfigDeleteRequest {
  // Key indicates which ExampleConfig instance to remove.
  // This field must always be set.
  ExampleKey key = 1;
};
```

Response type:

```protobuf
message ExampleConfigDeleteResponse {
  // Key echoes back the key of the deleted ExampleConfig instance.
  ExampleKey key = 1;

  // Time indicates the (UTC) timestamp at which the system recognizes the
  // deletion. The only guarantees made about this timestamp are:
  //
  //    - it is after the time the request was received
  //    - a time-ranged query with StartTime==DeletedAt will not include this instance.
  //
  google.protobuf.Timestamp time = 2;
};
```


Filtering
------------------------------------------------------------

### Partial-Equality Filters

Unless intentionally disabled (and sufficiently documented), services provide a default filtering mechanism. The input type is the same as the model you are filtering, and if you wish to filter on a given field you set that field to non-nil.

Given:
    - response: the model that may or may not be sent to the client
    - filter: a single filter model (request allows giving multiple)

For every response in the stream, we iterate the filter list. If the filter has a field set to non-null we compare it to the response's field value. If the values are equal we continue to the next field in the filter. If the field values do not match we "fail" the filter and move on to the next filter in the list.


If a response fails all filters, it is *not* sent to the client.

If a response succeeds *any* filter, it *is* sent to the client.



### Service-Specific Filtering

Models are allowed to also contain an "implementation specific" filter which can be more targeted, featureful, or otherwise helpful.


This filter type will be defined in the protobuf definition. This type should be well documented in the protobuf as well as generated documentation.

```
message CustomFilteredStreamRequest {
  ...

  // -- documentation from the filter message type --
  CustomFilter filter = 2;

  ...
```



## Appendix

### Connecting to CVP

On-prem CVP deployments listen on port 8443, while CloudVision as a Service listens on port 443.

### Authentication

Our APIs support token based and mutual TLS based [authentication](https://grpc.io/docs/guides/auth/).

#### Example requirements

This example uses the [`requests`](https://pypi.org/project/requests/) Python package. You can install it with

```bash
python -m pip install requests
```

#### Example: token from login

```python
import requests
import json
import grpc

CV_HOST = "your_cvp_hostname_or_ip"
CV_API_PORT = "8443"
USERNAME = "your_cvp_username"
PASSWORD = "your_cvp_password"


r = requests.post('https://' + CV_HOST + '/cvpservice/login/authenticate.do',
  auth=(USERNAME, PASSWORD))

channel_credentials = grpc.ssl_channel_credentials()
call_credentials = grpc.access_token_call_credentials(r.json()['sessionId'])
combined_credentials = grpc.composite_channel_credentials(channel_credentials, call_credentials)
channel = grpc.secure_channel(CV_HOST + ':' + CV_API_PORT, combined_credentials)
```

#### Example: loading SSL/TLS root certificates

If CVP is using a certificate signed by a certificate authority that is not installed as a root certificate, specify it like so:

```python
import requests
import json
import grpc

CV_HOST = "your_cvp_hostname_or_ip"
CV_API_PORT = "8443"
USERNAME = "your_cvp_username"
PASSWORD = "your_cvp_password"

# The certificate authority that signed the CVP certificate.
# If the CVP certificate is self-signed, this is just the certificate itself.
# The default location of CVP's self-signed certificate on a node is /etc/nginx/cvp.crt
CA_PUB_CERT_PATH = "/path/to/ca.pem"

r = requests.post('https://' + CV_HOST + '/cvpservice/login/authenticate.do',
  auth=(USERNAME, PASSWORD),
  verify=CA_PUB_CERT_PATH)

call_credentials = grpc.access_token_call_credentials(r.json()['sessionId'])
with open(CA_PUB_CERT_PATH, 'rb') as cert_file:
  channel_credentials = grpc.ssl_channel_credentials(cert_file.read())
combined_credentials = grpc.composite_channel_credentials(channel_credentials, call_credentials)
channel = grpc.secure_channel(CV_HOST + ':' + CV_API_PORT, combined_credentials)
```

Or download the certificate used by the server. Note that this is insecure.

```python
import requests
import json
import ssl
import tempfile
import grpc

CV_HOST = "your_cvp_hostname_or_ip"
CV_API_PORT = "8443"
USERNAME = "your_cvp_username"
PASSWORD = "your_cvp_password"

cert = bytes(ssl.get_server_certificate((CV_HOST, 443)))

r = requests.post('https://' + CV_HOST + '/cvpservice/login/authenticate.do',
  auth=(USERNAME, PASSWORD),
  verify=False)

call_credentials = grpc.access_token_call_credentials(r.json()['sessionId'])
channel_credentials = grpc.ssl_channel_credentials(cert)
combined_credentials = grpc.composite_channel_credentials(channel_credentials, call_credentials)
channel = grpc.secure_channel(CV_HOST + ':' + CV_API_PORT, combined_credentials)
```


#### Example: token from file

```python
import grpc

CV_HOST = "your_cvp_hostname_or_ip"
CV_API_PORT = "8443"

# The certificate authority that signed the CVP certificate.
# If the CVP certificate is self-signed, this is just the certificate itself.
# The default location of CVP's self-signed certificate on a node is /etc/nginx/cvp.crt
CA_PUB_CERT_PATH = "/path/to/ca.pem"

with open('cloudvision_access_token.txt', 'r') as f:
    call_credentials = grpc.access_token_call_credentials(f.read().strip())
with open(CA_PUB_CERT_PATH, 'rb') as cert_file:
  channel_credentials = grpc.ssl_channel_credentials(cert_file.read())
combined_credentials = grpc.composite_channel_credentials(channel_credentials, call_credentials)
channel = grpc.secure_channel(CV_HOST + ':' + CV_API_PORT, combined_credentials)
```

#### Example: token from environment variable

```python
import grpc

CV_HOST = "your_cvp_hostname_or_ip"
CV_API_PORT = "8443"

# The certificate authority that signed the CVP certificate.
# If the CVP certificate is self-signed, this is just the certificate itself.
# The default location of CVP's self-signed certificate on a node is /etc/nginx/cvp.crt
CA_PUB_CERT_PATH = "/path/to/ca.pem"

call_credentials = grpc.access_token_call_credentials(os.environ['CLOUDVISION_ACCESS_TOKEN'])
with open(CA_PUB_CERT_PATH, 'rb') as cert_file:
  channel_credentials = grpc.ssl_channel_credentials(cert_file.read())
combined_credentials = grpc.composite_channel_credentials(channel_credentials, call_credentials)
channel = grpc.secure_channel(CV_HOST + ':' + CV_API_PORT, combined_credentails)
```
