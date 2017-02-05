#!/usr/bin/env python
import Image
from player import Player

from StringIO import StringIO
import base64
from io import BytesIO
from flask import json
import requests
from flask import Flask
from flask import send_file
from werkzeug.contrib.cache import SimpleCache

BASE_REST = "http://localhost:7878/cterrachar/"

app = Flask(__name__)
cache = SimpleCache()


@app.route('/')
def hello():
    return "nothing to see here"


@app.route('/get_player/<name>')
def get_player(name):
    player = fetch_player(name)
    if player is None:
        parsed = fetch_player_data(name)
        if 'error' in parsed:
            return json.jsonify(parsed)
        player = cache_player(name=name, info=parsed)
    return send_file(BytesIO(base64.b64decode(player)), mimetype='image/png')


@app.route('/active_players')
def get_actives():
    parsed = fetch_actives()
    players = {}
    for i in range(0, parsed['count']):
        player_data = parsed['players'][i]
        player = cache_player(player_data['Name'], player_data)
        players[player_data['Name']] = player
    return json.jsonify(count=len(players), players=players)


def make_player(info):
    char = Player()
    char.load_data(info)
    return char


def fetch_actives():
    req = requests.get(BASE_REST + 'active_players')
    parsed = json.loads(req.text)
    return parsed


def fetch_player_data(name):
    req = requests.get(BASE_REST + 'player', params={'name': name})
    parsed = json.loads(req.text)
    if 'error' in parsed:
        return parsed
    return parsed['player']


def fetch_player(name):
    return cache.get(name)


def cache_player(name, info):
    char = make_player(info)
    player = to_base64(draw_character(char))
    cache.set(key=name, value=player, timeout=5 * 60)  # timeout in 5 minutes
    return player


def to_base64(img):
    imgio = StringIO()
    img.save(imgio, 'PNG', quality=100)
    imgio.seek(0)
    b64 = base64.b64encode(imgio.getvalue())
    return b64


def draw_character(player):
    image = Image.new('RGBA', (40, 55), (0, 0, 0, 0))
    for piece in player.PALETTE:
        if piece is None:
            continue
        image.paste(im=piece, mask=piece)
    return image
