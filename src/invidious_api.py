import requests
import _config as config
import json


class Video:
    def __init__(self, id, instance):
        self.data = json.loads(
            requests.get(f"https://{instance}/api/v1/videos/{id}").content
        )

    def get_data(self):
        return self.data
