from flask import Flask, send_file, jsonify, Response
from io import BytesIO
import base64
import pyTerrachar
import logging
import logging.handlers

BASE_REST = "http://localhost:7878/cterrachar/"

app = Flask(__name__)
if __name__ == '__main__':
    formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    handler = logging.handlers.RotatingFileHandler('pyterrachar.log', maxBytes=100000, backupCount=5)
    handler.setLevel(logging.WARNING)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

@app.route('/')
def hello():
    return "nothing to see here"


@app.route('/get_player/<name>')
def get_player(name):
    player = pyTerrachar.fetch_player(name)
    if player is None:
        parsed = pyTerrachar.fetch_player_data(name)
        if isinstance(parsed, Response):
            return parsed
        player = pyTerrachar.cache_player(name=name, info=parsed)
    return send_file(BytesIO(base64.b64decode(player)), mimetype='image/png')


@app.route('/active_players')
def get_actives():
    parsed = pyTerrachar.fetch_actives()
    if isinstance(parsed, Response):
        return parsed
    players = {}
    for i in range(0, parsed['count']):
        player_data = parsed['players'][i]
        player = pyTerrachar.cache_player(player_data['Name'], player_data)
        players[player_data['Name']] = player
    return jsonify(count=len(players), players=players)