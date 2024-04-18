<h2>Simple API Manipulator</h2>

Main class is <i>APIManager</i> which have two methods: <br>
request_get(<b>endpoint</b> <i>[, headers]</i>) <br>
request_post(<b>endpoint</b> <i>[, data, headers]</i>)

<h3>Usage</h3>
```python
from api_manager import APIManager

manager = APIManager("EXAMPLE_URL")

response = manager.request_get("ENDPOINT") # returns request.Response object

response_post = manager.request_post("ENDPOINT",
    data={"number":20},
    headers={
        "Content-Type" : "text/json"
}) # returns request.Response object
```