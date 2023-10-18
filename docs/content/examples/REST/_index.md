---
title: REST API Examples
weight: 100
chapter: false
---



{{% children /%}}

{{% notice info %}}

Examples scripts: [examples_cvprac.py](https://github.com/aristanetworks/cloudvision-apis/blob/trunk/docs/content/examples/REST/_index.files/examples_cvprac.py), 
[examples_python_rest.py](https://github.com/aristanetworks/cloudvision-apis/blob/trunk/docs/content/examples/REST/_index.files/examples_python_rest.py)

{{% /notice %}}

{{% notice note %}}
REST bindings for Resource APIs were introduced in CVP 2021.1.0
{{% /notice %}}

{{% notice note %}}
When fetching a state from NetDB between two arbitrary dates, the result returned will contain data that existed between those two dates and not just data that was created between those dates. For instance if BGP events are queried between 2023-05-01 10:00 and 2023-05-01 12:00 the result will contain events that were active in the range of 10 AM to 12 PM. If there were events that started before 10 AM and were not resolved (still active) at that time, the result will contain those events too.
{{% /notice %}}
