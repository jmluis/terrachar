#!/usr/bin/env python
import base64
import logging.handlers
from StringIO import StringIO
from io import BytesIO
from logging import handlers

import requests
from PIL import Image, ImageFilter
from flask import Flask, send_file, Response, json
from werkzeug.contrib.cache import SimpleCache  # change to memcached later

import player

app = Flask(__name__)

formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
handler = handlers.RotatingFileHandler('pyterrachar.log', maxBytes=100000, backupCount=5)
handler.setLevel(logging.WARNING)
handler.setFormatter(formatter)
app.logger.addHandler(handler)
app.config.from_object('PYTERRACHAR_SETTINGS')

cache = SimpleCache()


@app.route('/')
def hello():
    return "nothing to see here"


@app.route('/get_player/<name>')
def get_player(name):
    player = fetch_player(name)
    if player is None:
        parsed = fetch_player_data(name)
        if isinstance(parsed, Response):
            return parsed
        player = cache_player(name=name, info=parsed)
    return send_file(BytesIO(base64.b64decode(player)), mimetype='image/png')


@app.route('/active_players')
def get_actives():
    parsed = fetch_actives()
    if isinstance(parsed, Response):
        return parsed
    players = {}
    for i in range(0, parsed['count']):
        player_data = parsed['players'][i]
        player = cache_player(player_data['Name'], player_data)
        players[player_data['Name']] = player
    return json.jsonify(count=len(players), players=players)

if __name__ == '__main__':
    app.run()

def make_player(info):
    char = player.Player()
    char.load_data(info)
    return char


def fetch_actives():
    try:
        req = requests.get(app.config['BASE_REST'] + 'active_players')
        parsed = json.loads(req.text)
    except requests.RequestException:
        return json.jsonify({'error': 'could not connect to server'})
    except ValueError as e:
        app.logger.error('IOError fetch_actives ' + e.message)
        return json.jsonify({'error': 'value error in json'})
    if 'error' in parsed:
        return json.jsonify(parsed)
    return parsed


def fetch_player_data(name):
    try:
        req = requests.get(app.config['BASE_REST'] + 'player', params={'name': name})
        parsed = json.loads(req.text)
    except requests.RequestException:
        return json.jsonify({'error': 'could not connect to server'})
    except ValueError as e:
        app.logger.error('IOError fetch_player_data ' + e.message)
        return json.jsonify({'error': 'value error in json'})
    if 'error' in parsed:
        return json.jsonify(parsed)
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
    img = img.filter(ImageFilter.BLUR)
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
