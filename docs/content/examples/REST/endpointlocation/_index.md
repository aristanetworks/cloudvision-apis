---
title: Endpointlocation
weight: 100
chapter: false
---

{{% toc /%}}

{{% notice info %}}
Endpointlocation Resource APIs are supported from CVP 2021.1.0 or newer and in CloudVision-as-a-Service.
{{% /notice %}}

{{% notice tip %}}
[jq](https://stedolan.github.io/jq/) can be used to easily format and parse the outputs.
{{% /notice %}}

endpointlocation.v1
===================

## Get the location of an endpoint based on its MAC Address

### curl
```bash
curl -sS -kX GET --header 'Accept: application/json' -b access_token=`cat token.tok` \
   'https://www.arista.io/api/resources/endpointlocation/v1/EndpointLocation?key.searchTerm=50:08:00:5b:d1:46' | jq
```

Output:

```json
{
  "value": {
    "key": {
      "searchTerm": "50:08:00:5b:d1:46"
    },
    "deviceMap": {
      "values": {
        "ENDPOINT_50:08:00:5b:d1:46": {
          "identifierList": {
            "values": [
              {
                "type": "IDENTIFIER_TYPE_MAC_ADDR",
                "value": "50:08:00:5b:d1:46",
                "sourceList": {
                  "values": [
                    "IDENTIFIER_SOURCE_FDB",
                    "IDENTIFIER_SOURCE_LLDP"
                  ]
                }
              }
            ]
          },
          "deviceType": "DEVICE_TYPE_ENDPOINT",
          "locationList": {
            "values": [
              {
                "deviceId": "BAD032986065E8DC14CBB6472EC314A6",
                "deviceStatus": "DEVICE_STATUS_ACTIVE",
                "interface": "Port-Channel4",
                "vlanId": 120,
                "learnedTime": "2022-08-12T22:32:20.785182952Z",
                "macType": "MAC_TYPE_LEARNED_DYNAMIC",
                "likelihood": "LIKELIHOOD_VERY_LIKELY",
                "explanationList": {
                  "values": [
                    "EXPLANATION_DIRECT_CONNECTION"
                  ]
                },
                "identifierList": {
                  "values": [
                    {
                      "type": "IDENTIFIER_TYPE_MAC_ADDR",
                      "value": "50:08:00:5b:d1:46",
                      "sourceList": {
                        "values": [
                          "IDENTIFIER_SOURCE_FDB",
                          "IDENTIFIER_SOURCE_LLDP"
                        ]
                      }
                    }
                  ]
                }
              },
              {
                "deviceId": "0123F2E4462997EB155B7C50EC148767",
                "deviceStatus": "DEVICE_STATUS_ACTIVE",
                "interface": "Port-Channel4",
                "vlanId": 120,
                "learnedTime": "2022-08-12T22:32:20.813458919Z",
                "macType": "MAC_TYPE_PEER_DYNAMIC",
                "likelihood": "LIKELIHOOD_VERY_LIKELY",
                "explanationList": {
                  "values": [
                    "EXPLANATION_DIRECT_CONNECTION"
                  ]
                },
                "identifierList": {
                  "values": [
                    {
                      "type": "IDENTIFIER_TYPE_MAC_ADDR",
                      "value": "50:08:00:5b:d1:46",
                      "sourceList": {
                        "values": [
                          "IDENTIFIER_SOURCE_FDB",
                          "IDENTIFIER_SOURCE_LLDP"
                        ]
                      }
                    }
                  ]
                }
              },
              {
                "deviceId": "6323DA7D2B542B5D09630F87351BEA41",
                "deviceStatus": "DEVICE_STATUS_ACTIVE",
                "interface": "Vxlan1",
                "vlanId": 120,
                "learnedTime": "2022-08-12T22:32:20.823923349Z",
                "macType": "MAC_TYPE_EVPN_DYNAMIC_REMOTE",
                "likelihood": "LIKELIHOOD_LESS_LIKELY",
                "explanationList": {
                  "values": [
                    "EXPLANATION_VIRTUAL"
                  ]
                },
                "identifierList": {
                  "values": [
                    {
                      "type": "IDENTIFIER_TYPE_MAC_ADDR",
                      "value": "50:08:00:5b:d1:46",
                      "sourceList": {
                        "values": [
                          "IDENTIFIER_SOURCE_FDB"
                        ]
                      }
                    }
                  ]
                }
              },
              {
                "deviceId": "8520AF39790A4EC959550166DC5DEADE",
                "deviceStatus": "DEVICE_STATUS_ACTIVE",
                "interface": "Vxlan1",
                "vlanId": 120,
                "learnedTime": "2022-08-12T22:32:20.851241350Z",
                "macType": "MAC_TYPE_EVPN_DYNAMIC_REMOTE",
                "likelihood": "LIKELIHOOD_LESS_LIKELY",
                "explanationList": {
                  "values": [
                    "EXPLANATION_VIRTUAL"
                  ]
                },
                "identifierList": {
                  "values": [
                    {
                      "type": "IDENTIFIER_TYPE_MAC_ADDR",
                      "value": "50:08:00:5b:d1:46",
                      "sourceList": {
                        "values": [
                          "IDENTIFIER_SOURCE_FDB"
                        ]
                      }
                    }
                  ]
                }
              }
            ]
          },
          "deviceStatus": "DEVICE_STATUS_ACTIVE"
        }
      }
    }
  },
  "time": "0001-01-01T00:00:00Z"
}
```

## Get the location of an endpoint based on its IP Address

{{% notice info %}}
To successfully find the endpoint, the IP address of the endpoint has to exist in either the MAC or ARP or DHCP 
or inventory tables and in the LLDP neighbor table.
{{% /notice %}}

### curl

```bash
curl -sS -kX GET --header 'Accept: application/json' \
  -b access_token=`cat token.tok` \
  'https://192.0.2.79/api/resources/endpointlocation/v1/EndpointLocation?key.searchTerm=10.142.148.50' | jq
```

Output:

```json
{
  "value": {
    "key": {
      "searchTerm": "10.142.148.50"
    },
    "deviceMap": {
      "values": {
        "ENDPOINT_00:50:56:97:b8:f9": {
          "identifierList": {
            "values": [
              {
                "type": "IDENTIFIER_TYPE_MAC_ADDR",
                "value": "00:50:56:97:b8:f9",
                "sourceList": {
                  "values": [
                    "IDENTIFIER_SOURCE_ARP"
                  ]
                }
              },
              {
                "type": "IDENTIFIER_TYPE_IPV4_ADDR",
                "value": "10.142.148.50",
                "sourceList": {
                  "values": [
                    "IDENTIFIER_SOURCE_ARP"
                  ]
                }
              }
            ]
          },
          "deviceType": "DEVICE_TYPE_ENDPOINT",
          "locationList": {
            "values": [
              {
                "deviceId": "JPE14252456",
                "deviceStatus": "DEVICE_STATUS_ACTIVE",
                "interface": "Ethernet47",
                "learnedTime": "2022-08-13T01:13:11.492331146Z",
                "likelihood": "LIKELIHOOD_LIKELY",
                "explanationList": {
                  "values": [
                    "EXPLANATION_NON_INVENTORY_CONNECTION"
                  ]
                },
                "identifierList": {
                  "values": [
                    {
                      "type": "IDENTIFIER_TYPE_IPV4_ADDR",
                      "value": "10.142.148.50",
                      "sourceList": {
                        "values": [
                          "IDENTIFIER_SOURCE_ARP"
                        ]
                      }
                    },
                    {
                      "type": "IDENTIFIER_TYPE_MAC_ADDR",
                      "value": "00:50:56:97:b8:f9",
                      "sourceList": {
                        "values": [
                          "IDENTIFIER_SOURCE_ARP"
                        ]
                      }
                    }
                  ]
                }
              }
            ]
          },
          "deviceStatus": "DEVICE_STATUS_ACTIVE"
        }
      }
    }
  },
  "time": "0001-01-01T00:00:00Z"
}
```

## Get the location of all connected endpoints

### python

The GetAll RPC is not implemented in this resource API, however a combination of cloudvision.Connector
and the GetOne rAPI can be used to generate a report of all connected endpoints. An example that achieves this can be 
found on the [cloudvision-python](https://github.com/aristanetworks/cloudvision-python/blob/trunk/examples/Connector/get_endpoints_ext.py) repo.
