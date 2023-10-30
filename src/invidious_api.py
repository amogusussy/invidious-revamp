import requests
import _config as config
import json
from datetime import datetime


class Video:
    def __init__(self, id, instance):
        self.data = json.loads(
            requests.get(f"https://{instance}/api/v1/videos/{id}").content
        )
        self.data['viewCount'] = self.readable_views()
        self.data['published'] = self.upload_date()
        self.data['likeCount'] = self.readable_likes('likeCount')
        self.data['dislikeCount'] = self.readable_likes('dislikeCount')
        self.data['descriptionHtml'] = self.data['descriptionHtml'].replace("\n", "<br>")

    def get_data(self):
        return self.data

    def readable_views(self):
        return_val = f"{self.data['viewCount']:,}"
        print(return_val)
        return return_val


    def upload_date(self):
        return datetime.fromtimestamp(self.data['published']).strftime("%d %b %Y")

    def readable_likes(self, key):
        value = self.data[key]
        if value < 1000:
            return str(value)
        elif value < 10000:
            return '{:.1f}K'.format(value / 1000)
        elif value < 1000000:
            return '{:.0f}K'.format(round(value / 1000))
        else:
            return '{:.1f}M'.format(value / 1000000)

class Comments:
    def __init__(self, id, instance):
        self.comments = json.loads(
            requests.get(f"https://{instance}/api/v1/comments/{id}").content
        )

    def get_comments(self):
        return self.comments
