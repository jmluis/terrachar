from flask import Flask, send_file, jsonify
from io import BytesIO
import base64
import pyTerrachar

BASE_REST = "http://localhost:7878/cterrachar/"

app = Flask(__name__)

@app.route('/')
def hello():
    return "nothing to see here"


@app.route('/get_player/<name>')
def get_player(name):
    player = pyTerrachar.fetch_player(name)
    if player is None:
        parsed = pyTerrachar.fetch_player_data(name)
        if 'error' in parsed:
            return jsonify(parsed)
        player = pyTerrachar.cache_player(name=name, info=parsed)
    return send_file(BytesIO(base64.b64decode(player)), mimetype='image/png')


@app.route('/active_players')
def get_actives():
    parsed = pyTerrachar.fetch_actives()
    players = {}
    for i in range(0, parsed['count']):
        player_data = parsed['players'][i]
        player = pyTerrachar.cache_player(player_data['Name'], player_data)
        players[player_data['Name']] = player
    return jsonify(count=len(players), players=players)