import requests


class APIManager:
    def __init__(self, base_url):
        self.base_url = base_url

    def request_get(self, endpoint, headers=None):
        url = f"{self.base_url}/{endpoint}"

        response_object = requests.get(url, headers=headers)
        if response_object.status_code == 200:
            return response_object
        else:
            response_object.raise_for_status()

    def request_post(self, endpoint, data, headers = None):
        url = f"{self.base_url}/{endpoint}"

        response_object = requests.post(url, json=data, headers=headers)
        if response_object.status_code == 200:
            return response_object
        else:
            response_object.raise_for_status()


if __name__ == "__main__":
    manager = APIManager("https://jsonplaceholder.typicode.com")
    response = manager.request_get("posts")
    response_json = response.json()

    # for item in response_json:
    #     print(item)

    send_obj_status = manager.request_post("posts", {
        "name": "David",
        "age": 20,
    })

    print(send_obj_status)
