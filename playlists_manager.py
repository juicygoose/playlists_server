#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 16:37:25 2017

@author: ajousse
"""

import pathlib
import json
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class PlaylistsManager:
    def __init__(self, playlists_file = 'tracks-playlist.json'):
        self.file_name = playlists_file
        self.google_developer_key = 'AIzaSyCSeuIW3gsBqKnU5Dk-5BK8n-0B2vHJCkg'
        self.youtube_api_service = 'youtube'
        self.youtube_api_version = 'v3'

    def searchTrackOnYoutube(self, track):
        try:
            youtube = build(self.youtube_api_service, self.youtube_api_version,
                            developerKey=self.google_developer_key)
            search_response = youtube.search().list(
                                    q=track,
                                    part='id,snippet',
                                    maxResults=1).execute()
            if 'items' in search_response:
                for item in search_response['items']:
                    if item['id']['kind'] == 'youtube#video':
                        return item['id']['videoId']
        except HttpError as e:
            return None

    def addTrack(self, new_track):
        track_dict = {}
        track_id = self.searchTrackOnYoutube(new_track)
        if track_id is not None:
            track_dict[new_track] = 'https://www.youtube.com/watch?v={}'.format(track_id)
        else:
            track_dict[new_track] = 'No url found'

        filepath = pathlib.Path(self.file_name)
        if filepath.exists():
            with filepath.open() as file:
                data = json.load(file)
        else:
            data = {'playlists': [{'isActive': True}]}

        if track_id is not None:
            data['playlists'][0][new_track] = 'https://www.youtube.com/watch?v={}'.format(track_id)
        else:
            data['playlists'][0][new_track] = 'No url found'

        with filepath.open('w') as file:
            json.dump(data, file)

    def getPlaylists(self):
        filepath = pathlib.Path(self.file_name)
        if filepath.exists():
            with filepath.open() as playlists:
                return json.load(playlists)
        else:
            return None

