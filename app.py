from flask import Flask, jsonify, request, json
import requests
from werkzeug.exceptions import HTTPException
import logging # <-- added

app = Flask(__name__)
app.config['DEBUG'] = False


@app.route('/ping', methods=['GET'])
def ping_pong():
    """Expects 'ping' and returns 'pong!' in json form. """
    return jsonify('pong!')

@app.route('/word', methods=['GET'])
def rev_word():
    """Takes input of word and outputs the reverse of that word in json form. """
    word = requests.get('https://random-word-api.herokuapp.com/word?number=1')
    rev_word = word.json()[0][::-1]
    return jsonify(rev_word)

@app.route('/string_count', methods=['POST'])
def string_count():
    """Expects request.get_json to return the length of the inputted string. """
    string = request.get_json()
    length = len(string)
    return jsonify(length)

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors. """
    # start with the correct headers and status code from the error
    logging.exception(e) # <-- added
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

if __name__ == '__main__':
    app.run()
