import flask
import urllib
from repository import URLRepository

app = flask.Flask(__name__)

@app.route("/s", methods=["POST"])
def shortener():
    body = flask.request.get_json()
    try:
        if body["title"] == None or body["url"] == None:
            flask.abort(500)
        title = urllib.parse.quote(body["title"])
        URLRepository.save(body["url"], title)
        return flask.jsonify({"title": title})
    except RuntimeError:
        flask.abort(410)

@app.route("/s/<title>", methods=["GET"])
def redirect(title: str):
    url = URLRepository.findOne(title)
    if url != None:
        if url.startswith("http://") or url.startswith("https://"):
            return flask.redirect(url)
        return flask.redirect(f"https://{url}")
    flask.abort(404)
