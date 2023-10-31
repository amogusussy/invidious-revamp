#!/usr/bin/env python3
from flask import (
    Flask,
    request,
    render_template
)
import _config as config
from src import invidious_api


app = Flask(__name__, static_folder="static", static_url_path="")

@app.route("/")
def home():
    return "To do later"

@app.route("/watch")
def watch():
    id = request.args.get("v", "")

    instance = "yt.artemislena.eu"


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
