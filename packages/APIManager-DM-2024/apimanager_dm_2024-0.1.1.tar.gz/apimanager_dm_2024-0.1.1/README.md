# Simple API Manager

Main class is *APIManager* which have two methods:

- request_get(**endpoint** *[, headers]*)
- request_post(**endpoint** *[, data, headers]*)

## Usage
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