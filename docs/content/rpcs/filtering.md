---
title: Filtering
weight: 3
pre: "<b>- </b>"
---

Filtering is provided through a default and an (optional) additional model-specific mechanism. By default, all models support "partial equality filtering". Models that provide a custom filtering method will document this filter-message in its model documentation.


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
