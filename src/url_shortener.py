import flask
from repository import URLRepository

app = flask.Flask(__name__)

@app.route("/s", methods=["POST"])
def shortener():
    body = flask.request.get_json()
    hashed_url = URLRepository.save(body["url"])
    return flask.jsonify({"hashed_url": hashed_url})

@app.route("/s/<hashed_url>", methods=["GET"])
def redirect(hashed_url: str):
    url = URLRepository.findOne(hashed_url)
    if url != None:
        if url.startswith("http://") or url.startswith("https://"):
            return flask.redirect(url)
        return flask.redirect(f"https://{url}")
    flask.abort(404)
