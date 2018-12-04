import flask
from repository import URLRepository

app = flask.Flask(__name__)

@app.route("/s", methods=["POST"])
def shortener():
    body = flask.request.get_json()
    try:
        URLRepository.save(body["url"], body["title"])
    except RuntimeError:
        flask.abort(410)
    return flask.jsonify({"title": body["title"]})

@app.route("/s/<title>", methods=["GET"])
def redirect(title: str):
    url = URLRepository.findOne(title)
    if url != None:
        if url.startswith("http://") or url.startswith("https://"):
            return flask.redirect(url)
        return flask.redirect(f"https://{url}")
    flask.abort(404)
