#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 16:59:13 2017

@author: ajousse
"""

from playlists_manager import PlaylistsManager

import unittest
import json
import pathlib
import os

class PlaylistsManagerTestCase(unittest.TestCase):

    playlists_file = 'test_playlists.json'
    track_name = 'Tom Trago - The Elite'
    play_dict = {'playlists': [{track_name: 'https://www.youtube.com/watch?v=4ojouAHg0Ak', 'isActive': True}]}

    def test_add_track_ok(self):
        filepath = pathlib.Path(self.playlists_file)
        if filepath.exists():
            #Clean test directory
            os.remove(self.playlists_file)

        PlaylistsManager(self.playlists_file).addTrack(self.track_name)
        with open(self.playlists_file) as file:
            data = json.load(file)
            self.assertEqual(self.play_dict, data)

    def test_read_playlists_ok(self):
        filepath = pathlib.Path(self.playlists_file)
        if filepath.exists():
            #Clean test directory
            os.remove(self.playlists_file)

        mgr = PlaylistsManager(self.playlists_file)
        mgr.addTrack(self.track_name)
        self.assertEqual(mgr.getPlaylists(), self.play_dict)



