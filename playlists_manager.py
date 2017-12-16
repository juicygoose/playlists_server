#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 16:37:25 2017

@author: ajousse
"""

import pathlib
import json

class PlaylistsManager:
    def __init__(self):
        self.file_name = 'tracks-playlist.json'

    def addTrack(self, new_track):
        filepath = pathlib.Path(self.file_name)
        if filepath.exists():
            with filepath.open() as file:
                data = json.load(file)
        else:
            data = {'playlist1':[]}
        data['playlist1'].append(new_track)
        with filepath.open('w') as file:
            json.dump(data, file)

    def getPlaylists(self):
        with open(self.file_name, 'r') as playlists:
            return json.load(playlists)
