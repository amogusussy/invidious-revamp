import requests
from src import numberHelpers as number_helpers
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
        self.data['likeCount'] = number_helpers.readable_number(self.data['likeCount'])
        self.data['descriptionHtml'] = self.data['descriptionHtml'].replace("\n", "<br>")

    def get_data(self):
        return self.data

    def readable_views(self):
        return_val = f"{self.data['viewCount']:,}"
        return return_val


    def upload_date(self):
        return datetime.fromtimestamp(self.data['published']).strftime("%d %b %Y")

class Comments:
    def __init__(self, id, instance):
        self.comments = json.loads(
            requests.get(f"https://{instance}/api/v1/comments/{id}").content
        )
        self.comments['commentCount'] = number_helpers.readable_number(
            self.comments['commentCount']
        )
        for comment in self.comments['comments']:
            if "replies" not in comment:
                comment['replies'] = {
                    'replyCount': 0,
                    'continuation': ''
                }
            comment['likeCount'] = number_helpers.readable_number(comment['likeCount'])

    def get_comments(self):
        return self.comments

    def num_comments(self):
        return self.comments["commentCount"]


class Channel:
    def __init__(self, channel_id, instance):
        self.data = json.loads(
            requests.get(f"https://{instance}/api/v1/channels/{channel_id}").content
        )
    
    def get_channel_info(self):
        return self.data
