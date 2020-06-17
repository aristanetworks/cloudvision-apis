---
title: Set
weight: 13
pre: "<b>d. </b>"
---

`Set` updates a resource. Updates can be whole or partial (see: nullable fields) using only fields populated in the request.

{{% notice note %}}
The `Key` field is required to be fully-specified because `Set` needs to identify exactly-one
resource to delete.
{{% /notice %}}


{{% notice note %}}
The endpoint returns the time the `Set` becomes effective internally and the service's known-state of the resource.
{{% /notice %}}

A `*SetResponse` will contain an "echo" of the resource. This echo will be the original update-request at a minimum, and may include more data.This allows services to do fast, write-only, updates to internal storage. If the service needs to query existing state first then more data can be provided to the client. If you need a full model after a `Set` operation, you can issue a `GetOne` with the returned `time`.


```protobuf
rpc Set (ExampleConfigSetRequest) returns (ExampleSetResponse);
```

#### Request Type

The generated request for a model (`ExampleConfig`, here) looks like so:

```protobuf
message ExampleConfigSetRequest {
  // ExampleConfig carries the value to set into the datastore.
  ExampleConfig value = 1;
};
```

#### Response Type

The generated response for a model (`ExampleConfig`, here) looks like so:

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

### Updating maps

Set maps are merged with the existing map.

To delete all of the values in a map, set the wrapper message of the map but leave the map itself empty.



### Updating repeated fields

Set `repeated` fields replace the existing array. For example:

```
t0:
    existing state: ['a', 'b', 'c']
t1:
    existing state: ['a', 'b', 'c']
    set request: ['a', 'q', 'z']
t2:
    existing state: ['a', 'q', 'z']
```

To delete all of the values in a `repeated` field, set the wrapper message of the `repeated` and leave the `repeated` empty.


### Updating subresources

Subresources are resources that are a child of another resource. A collection of subresources with compound keys is represented by a `repeated` field, though this collection should be treated as unordered and uses the same update semantics as maps (tuple keys are not allowed in protobuf maps). If multiple subresources with the same key are specified, the last one in the repeated ordering is assumed to be value.

## Example: Update

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
