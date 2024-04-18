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

    def request_post(self, endpoint, data, headers):
        url = f"{self.base_url}/{endpoint}"

        response_object = requests.post(url, json=data, headers=headers)
        if response_object.status_code == 200:
            return response_object
        else:
            response_object.raise_for_status()


def test(text):
    print(text)


# if __name__ == "__main__":
#     api_manager = APIManipulator("https://fakestoreapi.com")
#     response = api_manager.request_get("users")
#     response_json = response.json()
#
#     # for item in response_json:
#     #     print(item)
#
#     send_obj_status = api_manager.request_post("users", {
#         "name": "David",
#         "age": 20,
#     })
#
#     # send_obj_status = requests.post("https://fakestoreapi.com/users", json={
#     #     "name": "David",
#     #     "age": 20,
#     # })
#
#     print(send_obj_status)
