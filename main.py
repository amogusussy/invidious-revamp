#!/usr/bin/env python3
from flask import (
    Flask,
    request,
    render_template
)
import _config as config
from src import invidious_api
from src import request_helpers


app = Flask(__name__, static_folder="static", static_url_path="")
instance = "yt.artemislena.eu"

@app.route("/")
def home():
    return "To do later"


@app.route("/channel/<id>")
def channel(id):
    channel_id = request.view_args['id']
    instance = request_helpers.get_instance()

    channel = invidious_api.Channel(channel_id, instance)
    channel_info = channel.get_channel_info()

    return render_template(
        'channel.html',
        info=channel_info
    )


@app.route("/watch")
def watch():
    id = request.args.get("v", "")
    instance = request_helpers.get_instance()

    if id == "":
        return "Invalid video ID", 400
    api_request = invidious_api.Video(id, instance)
    data = api_request.get_data()
    comments = invidious_api.Comments(id, instance)
    comments = comments.get_comments()

    return render_template(
        "watch.html",
        data=data,
        comments=comments,
        instance=instance,
    )

if __name__ == "__main__":
    app.run(threaded=True, port=config.PORT, debug=True)
