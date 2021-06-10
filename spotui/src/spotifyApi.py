import os
import spotipy
import spotipy.util as util
from spotui.src.config import get_config
from spotui.src.Logging import logging


class SpotifyApi:
    client = None

    def __init__(self):
        self.auth()

    def auth(self):
        config = get_config()
        user_config_dir = os.path.expanduser("~")
        cache_location = os.path.join(
            user_config_dir, '.config/spotui/SpoTUI_token.cache')
        self.user_name = config.get("spotify_api", "user_name")
        client_id = config.get("spotify_api", "client_id")
        client_secret = config.get("spotify_api", "client_secret")
        redirect_uri = config.get("spotify_api", "redirect_uri")
        scopes = "user-read-playback-state streaming playlist-read-collaborative user-modify-playback-state playlist-modify-public user-library-modify user-top-read user-read-currently-playing playlist-read-private playlist-modify-private user-read-recently-played user-library-read"
        self.token = util.prompt_for_user_token(
            self.user_name,
            scopes,
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            cache_path=cache_location
        )

        if self.token:
            self.client = spotipy.Spotify(auth=self.token)
        else:
            logging.warning("Can't get token for", self.user_name)

    def get_playing(self):
        try:
            self.auth()
            if not self.token:
                return False
            status = self.client.current_playback()
            return status
        except Exception as e:
            pass

    def search(self, query):
        try:
            self.auth()
            if not self.token:
                return False
            classes = ['track', 'show', 'playlist']
            items = [self.__search_all(c, query) for c in classes]
            flat_items = [item for sublist in items for item in sublist]
            return list(map(self.__map_tracks, flat_items))
        except Exception as e:
            pass

    def start_playback(self,
                       device_id,
                       track_uri=None,
                       context_uri=None,
                       offset=None):
        try:
            self.auth()
            if not self.token:
                return False
            self.client.start_playback(device_id, context_uri, track_uri,
                                       offset)
        except Exception as e:
            pass

    def pause_playback(self, device_id):
        try:
            self.auth()
            if not self.token:
                return False
            self.client.pause_playback(device_id)
        except Exception as e:
            pass

    def previous_track(self, device_id):
        try:
            self.auth()
            if not self.token:
                return False
            self.client.previous_track(device_id)
        except Exception as e:
            pass

    def next_track(self, device_id):
        try:
            self.auth()
            if not self.token:
                return False
            self.client.next_track(device_id)
        except Exception as e:
            pass

    def seek_track(self, device_id, position):
        try:
            self.auth()
            if not self.token:
                return False
            self.client.seek_track(position, device_id)
        except Exception as e:
            pass

    def get_top_tracks(self):
        try:
            self.auth()
            if not self.token:
                return []
            tracks = self.client.current_user_top_tracks()
            items = tracks["items"]
            while tracks["next"]:
                tracks = self.client.next(tracks)
                items += tracks["items"]
            return list(map(self.__map_tracks, items))
        except Exception as e:
            pass

    def get_recently_played(self):
        try:
            self.auth()
            if not self.token:
                return []
            tracks = self.client.current_user_recently_played()
            items = tracks["items"]
            # set used to identify unique tracks, prevent duplication of results
            track_uris = set()
            while tracks["next"]:
                tracks = self.client.next(tracks)
                items += tracks["items"]
                # remove all non-unique track-items from recently played list
                items = [item for item in items if item["track"]["uri"] not in track_uris \
                and (track_uris.add(item["track"]["uri"]) or True)]
            return list(map(self.__map_tracks, items))
        except Exception as e:
            pass

    def show_episodes(self, id):
        try:
            self.auth()
            if not self.token:
                return []
            tracks = self.client.show_episodes(id)
            items = tracks["items"]
            return list(map(self.__map_tracks, items))
        except Exception as e:
            pass

    def get_liked_tracks(self):
        try:
            self.auth()
            if not self.token:
                return []
            tracks = self.client.current_user_saved_tracks()
            items = tracks["items"]
            while tracks["next"]:
                tracks = self.client.next(tracks)
                items += tracks["items"]
            return list(map(self.__map_tracks, items))
        except Exception as e:
            pass

    def get_playlists(self):
        try:
            self.auth()
            if not self.token:
                return []

            # this grabs playlists spotify is trying to get the user to listen to
            # playlists = self.client.user_playlists('spotify')

            playlists = []
            offset = 0

            while True:
                get_playlists = self.client.current_user_playlists(offset=offset)["items"]
                playlists.extend(get_playlists)
                if len(get_playlists) < 50:
                    break
                offset += 50
                

            return list(map(self.__map_playlists, playlists))
        except Exception as e:
            return []
            pass

    def get_playlist_tracks(self, playlist_id):
        try:
            self.auth()
            if not self.token:
                return []
            results = self.client.user_playlist(self.user_name,
                                                playlist_id,
                                                fields="tracks,next")
            tracks = results["tracks"]
            items = tracks["items"]
            while tracks["next"]:
                tracks = self.client.next(tracks)
                items += tracks["items"]
            return list(map(self.__map_tracks, items))
        except Exception as e:
            pass

    def get_devices(self):
        try:
            self.auth()
            if not self.token:
                return []
            devices = self.client.devices()
            return list(map(self.__map_devices, devices["devices"]))
        except Exception as e:
            pass

    def shuffle(self, state):
        try:
            self.auth()
            if not self.token:
                return []
            devices = self.client.shuffle(state)
        except Exception as e:
            pass

    def repeat(self, state):
        try:
            self.auth()
            if not self.token:
                return []
            devices = self.client.repeat(state)
        except Exception as e:
            pass

    def __search_all(self, className, query):
        plural = className + 's'
        tracks = self.__extract_results(self.client.search(
            query, 50, 0, className), plural)
        return tracks

    def __extract_results(self, results, key):
        tracks = results[key]
        items = tracks['items']
        return items

    def __map_tracks(self, item):
        track = item["track"] if "track" in item else item
        return {
            "name": '(' + track['type'] + ') ' + track["name"] if track['type'] != 'track' else track['name'],
            "artist": track["artists"][0]["name"] if track['type'] == 'track' else track['publisher'] if track['type'] == 'show' else ' ',
            # "artist": 'james',
            "type": track['type'],
            "id": track["id"] if track['id'] else False,
            "uri": track["uri"],
        }

    def __map_playlists(self, playlist):
        return {
            "text": playlist["name"],
            "id": playlist["id"],
            "uri": playlist["uri"]
        }

    def __map_devices(self, device):
        return {"text": device["name"], "id": device["id"]}


client = SpotifyApi()
