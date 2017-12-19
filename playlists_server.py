#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 16:22:48 2017

@author: ajousse
"""

from playlists_manager import PlaylistsManager

from flask import Flask, jsonify, request, render_template, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def routeHome():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/home', methods=['POST'])
def goToAddTrackForm():
    return redirect(url_for('addTrackForm'))

@app.route('/add-track')
def addTrackForm():
    return render_template('add-track.html')

@app.route('/add-track', methods=['POST'])
def addTrackPost():
    try:
        new_track = request.form['newTrack']
        mgr = PlaylistsManager()
        mgr.addTrack(new_track)
        mgr.searchTrackOnYoutube(new_track)

        return redirect(url_for('getPlaylists'))

    except Exception as e:
        return jsonify(str(e)), 500

@app.route('/playlists')
def getPlaylists():
    try:
        pl = PlaylistsManager().getPlaylists()
        if pl is not None:
            return jsonify(PlaylistsManager().getPlaylists()), 200
        else:
            return redirect(url_for('home'))

    except Exception as e:
        return jsonify(str(e)), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)