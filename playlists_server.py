#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 16:22:48 2017

@author: ajousse
"""

from flask import Flask, jsonify, request, render_template
import json
import pathlib
import os

app = Flask(__name__)

class User():
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


def getLines():
    with open('logs.txt', 'r') as file:
        yield from file

@app.route('/home')
def returnMainPage():
    return '''
    <!doctype html>
    <html>
    <head>
    <title>Awesome log server</title>
    <meta name="description" content="Our first page">
    <meta name="keywords" content="html tutorial template">
    </head>
    <body>
    Get the freshest logs available at /logs
    </body>
    </html>
    '''

@app.route('/add-track')
def myForm():
    return render_template('add-track.html')

@app.route('/add-track', methods=['POST'])
def addTrack():
    try:
        newTrack = request.form['newTrack']
        filepath = pathlib.Path('tracks-playlist.json')
        if filepath.exists():
            with filepath.open() as file:
                data = json.load(file)
        else:
            data = {'playlist1':[]}
        data['playlist1'].append(newTrack)
        with filepath.open('w') as file:
            json.dump(data, file)

        return 'Track "{}" added to the playlist!'.format(newTrack), 200

    except Exception as e:
        return jsonify(str(e)), 500

@app.route('/playlists')
def getPlaylists():
    try:
        with open('tracks-playlist.json', 'r') as playlists:
            playlistsDict = json.load(playlists)
            return jsonify(playlistsDict), 200

    except Exception as e:
        return jsonify(str(e)), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)