#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2020-2023 (c) Randy W @xtdevs, @xtsea
# Nimbus ~ UserBot
# Copyright (C) 2023 NimbusTheCloud, ufoptg, @TrueSaiyan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# This file is a part of < https://github.com/ufoptg/Nimbus/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/ufoptg/Nimbus/blob/main/LICENSE/>.
# If not, see <https://www.gnu.org/licenses/>.

# THIS FILE IS RESPONSABLE FOR MANY CLASS DECLARATIONS

import json
import math
from base64 import b64encode
from urllib.request import urlretrieve

from . import calls, constructor


class Authenticator:
    """
    Handles authentication and token retrieval for Spotify API.
    """

    def __init__(self, client_id: str, client_secret: str):
        """
        Initializes the Authenticator with client credentials.

        :param client_id: Spotify client ID.
        :param client_secret: Spotify client secret.
        """
        self.credentials = self.encode_credentials(client_id, client_secret)

    def encode_credentials(self, client_id, client_secret):
        """
        Encodes client credentials for token retrieval.

        :param client_id: Spotify client ID.
        :param client_secret: Spotify client secret.
        :return: Encoded credentials.
        """
        credentials = f"{client_id}:{client_secret}"
        encoded_credentials = b64encode(credentials.encode("utf-8"))
        return str(encoded_credentials, "utf-8")

    def get_acess_token(self):
        """
        Retrieves access token using encoded credentials.

        :return: Access token.
        """
        response = calls.call_acess_token(self.credentials)
        return response.json()["access_token"]


# OBJECTS
# Base class for all classes
class Base:
    """
    Base class for all Spotify API objects.
    """

    def __init__(self, data, type, name, url, id):
        """
        Initializes Base object.

        :param data: Data dictionary.
        :param type: Object type.
        :param name: Name of the object.
        :param url: URL of the object.
        :param id: ID of the object.
        """
        self.data = data
        self.type = type
        self.name = name
        self.url = url
        self.id = id

    def export_json(self, path: str):
        """
        Exports object data to JSON file.

        :param path: File path.
        """
        file = open(path, "w")
        json.dump(self.data, file, indent=4)
        file.close()


class TrackBase(Base):
    """
    Base class for track-like Spotify API objects.
    """

    def __init__(self, data, type, name, url, id, explicit, duration_ms):
        """
        Initializes TrackBase object.

        :param data: Data dictionary.
        :param type: Object type.
        :param name: Name of the object.
        :param url: URL of the object.
        :param id: ID of the object.
        :param explicit: Explicit content indicator.
        :param duration_ms: Duration of the object in milliseconds.
        """
        super().__init__(data, type, name, url, id)
        self.explicit = explicit
        self.duration_ms = duration_ms

    def get_formatted_duration(self) -> dict:
        """
        Gets the formatted duration of the object.

        :return: Dictionary containing hours, minutes, and seconds.
        """
        duration_in_seconds = self.duration_ms / 1000
        hours = 0
        mins = math.floor(duration_in_seconds // 60)

        if mins >= 60:
            hours = math.floor(mins // 60)
            mins = math.floor(mins % 60)

        secs = math.floor(duration_in_seconds % 60)

        return {"hours": hours, "minutes": mins, "seconds": secs}

    def get_string_duration(self) -> str:
        """
        Gets the duration of the object as a formatted string.

        :return: Formatted duration string.
        """
        duration = self.get_formatted_duration()
        format = self.__format_duration

        hours = format(str(duration["hours"]))
        mins = format(str(duration["minutes"]))
        secs = format(str(duration["seconds"]))

        if int(hours):
            return f"{hours}:{mins}:{secs}"
        else:
            return f"{mins}:{secs}"

    def __format_duration(self, value: str):
        """
        Formats duration value.

        :param value: Value to format.
        :return: Formatted value.
        """
        if len(value) < 2:
            return "0" + value
        else:
            return value


class Artist(Base):
    """
    Represents an artist on Spotify.
    """

    def __init__(self, data: dict, type: str, name: str, url: str, id: str):
        """
        Initializes Artist object.

        :param data: Data dictionary.
        :param type: Object type.
        :param name: Name of the artist.
        :param url: URL of the artist.
        :param id: ID of the artist.
        """
        super().__init__(data, type, name, url, id)


class AlbumCover:
    """
    Represents the cover image of an album.
    """

    def __init__(self, width, height, url):
        """
        Initializes AlbumCover object.

        :param width: Width of the image.
        :param height: Height of the image.
        :param url: URL of the image.
        """
        self.width = width
        self.height = height
        self.url = url

    def export_image(self, path):
        """
        Exports the image to a file.

        :param path: File path.
        """
        urlretrieve(self.url, path)


class Album(Base):
    """
    Represents an album on Spotify.
    """

    def __init__(
        self,
        data: dict,
        type: str,
        name: str,
        url: str,
        id: str,
        images: list,
        artists: list,
        available_markets: list,
        release_date: str,
        total_tracks: int,
    ):
        """
        Initializes Album object.

        :param data: Data dictionary.
        :param type: Object type.
        :param name: Name of the album.
        :param url: URL of the album.
        :param id: ID of the album.
        :param images: List of album cover images.
        :param artists: List of artists associated with the album.
        :param available_markets: List of available markets.
        :param release_date: Release date of the album.
        :param total_tracks: Total number of tracks in the album.
        """
        super().__init__(data, type, name, url, id)
        self.images = images
        self.artists = artists
        self.available_markets = available_markets
        self.release_date = release_date
        self.total_tracks = total_tracks


class AlbumTrack:
    """
    Represents a track in an album.
    """

    def __init__(self, track_data):
        """
        Initializes AlbumTrack object.

        :param track_data: Data dictionary for the track.
        """
        self.spotify_url = track_data.get("external_urls", {}).get("spotify")
        self.track_name = track_data.get("name")
        self.artists = ", ".join(
            artist.get("name", "") for artist in track_data.get("artists", [])
        )
        self.track_number = track_data.get("track_number")
        self.duration_ms = track_data.get("duration_ms", 0)

    def get_formatted_duration(self) -> dict:
        """
        Gets the formatted duration of the object.

        :return: Dictionary containing hours, minutes, and seconds.
        """
        duration_in_seconds = self.duration_ms / 1000
        hours = 0
        mins = math.floor(duration_in_seconds // 60)

        if mins >= 60:
            hours = math.floor(mins // 60)
            mins = math.floor(mins % 60)

        secs = math.floor(duration_in_seconds % 60)

        return {"hours": hours, "minutes": mins, "seconds": secs}

    def get_string_duration(self) -> str:
        """
        Gets the duration of the object as a formatted string.

        :return: Formatted duration string.
        """
        duration = self.get_formatted_duration()
        format = self.__format_duration

        hours = format(str(duration["hours"]))
        mins = format(str(duration["minutes"]))
        secs = format(str(duration["seconds"]))

        if int(hours):
            return f"{hours}:{mins}:{secs}"
        else:
            return f"{mins}:{secs}"

    def __format_duration(self, value: str):
        """
        Formats duration value.

        :param value: Value to format.
        :return: Formatted value.
        """
        if len(value) < 2:
            return "0" + value
        else:
            return value


class Albums:
    """
    Represents an album.
    """

    def __init__(self, album_data):
        """
        Initializes Album object.

        :param album_data: Data dictionary for the album.
        """
        self.album_name = album_data.get("name", "Unknown Album")
        self.artists = ", ".join(
            artist.get("name", "") for artist in album_data.get("artists", [])
        )
        self.release_date = album_data.get("release_date")
        self.total_tracks = album_data.get("total_tracks", 0)
        self.thumbnail_url = (
            album_data.get("images", [])[0].get("url")
            if album_data.get("images")
            else None
        )
        self.label = album_data.get("label")
        self.popularity = album_data.get("popularity")
        self.tracks = [
            AlbumTrack(track) for track in album_data.get("tracks", {}).get("items", [])
        ]

    def total_duration(self):
        """
        Calculate the total duration of all tracks in the album.

        :return: Total duration as a formatted string.
        """
        total_seconds = sum(track.duration_ms for track in self.tracks) / 1000
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)
        return f"{hours}:{minutes}:{seconds}"

    def total_duration_string(self):
        """
        Calculate the total duration of all tracks in the album as a formatted string.

        :return: Total duration as a formatted string.
        """
        total_seconds = sum(track.duration_ms for track in self.tracks) / 1000
        total_duration_track = AlbumTrack({"duration_ms": total_seconds * 1000})
        return total_duration_track.get_string_duration()


class TrackPreview:
    """
    Represents a preview of a track.
    """

    def __init__(self, url):
        """
        Initializes TrackPreview object.

        :param url: URL of the track preview.
        """
        self.url = url

    def export_audio(self, path):
        """
        Exports the audio preview to a file.

        :param path: File path.
        """
        urlretrieve(self.url, path)


class Track(TrackBase):
    """
    Represents a track on Spotify.
    """

    def __init__(
        self,
        data: dict,
        type: str,
        name: str,
        url: str,
        id: str,
        explicit: bool,
        duration_ms: int,
        preview: TrackPreview,
        artists: list,
        album: Album,
        available_markets: list,
        disc_number: int,
        popularity: int,
    ):
        """
        Initializes Track object.

        :param data: Data dictionary.
        :param type: Object type.
        :param name: Name of the track.
        :param url: URL of the track.
        :param id: ID of the track.
        :param explicit: Explicit content indicator.
        :param duration_ms: Duration of the track in milliseconds.
        :param preview: Track preview object.
        :param artists: List of artists associated with the track.
        :param album: Album object associated with the track.
        :param available_markets: List of available markets.
        :param disc_number: Disc number of the track.
        :param popularity: Popularity of the track.
        """
        super().__init__(data, type, name, url, id, explicit, duration_ms)
        self.preview = preview
        self.artists = artists
        self.album = album
        self.available_markets = available_markets
        self.disc_number = disc_number
        self.popularity = popularity


class Episode(TrackBase):
    """
    Represents an episode on Spotify.
    """

    def __init__(
        self,
        data: dict,
        type: str,
        name: str,
        url: str,
        id: str,
        explicit: bool,
        duration_ms: int,
        preview: str,
        description: str,
        html_description: str,
        images: list,
        language: str,
        languages: list,
        release_date: str,
    ):
        """
        Initializes Episode object.

        :param data: Data dictionary.
        :param type: Object type.
        :param name: Name of the episode.
        :param url: URL of the episode.
        :param id: ID of the episode.
        :param explicit: Explicit content indicator.
        :param duration_ms: Duration of the episode in milliseconds.
        :param preview: URL of the episode preview.
        :param description: Description of the episode.
        :param html_description: HTML description of the episode.
        :param images: List of images associated with the episode.
        :param language: Language of the episode.
        :param languages: List of languages available for the episode.
        :param release_date: Release date of the episode.
        """
        super().__init__(data, type, name, url, id, explicit, duration_ms)
        self.preview = preview
        self.description = description
        self.html_description = html_description
        self.images = images
        self.language = language
        self.languages = languages
        self.release_date = release_date


class Playlist(Base):
    """
    Represents a playlist on Spotify.
    """

    def __init__(
        self,
        data: dict,
        type: str,
        name: str,
        url: str,
        id: str,
        description: str,
        images: list,
        tracks: list,
        public: bool,
        total_tracks: int,
    ):
        """
        Initializes Playlist object.

        :param data: Data dictionary.
        :param type: Object type.
        :param name: Name of the playlist.
        :param url: URL of the playlist.
        :param id: ID of the playlist.
        :param description: Description of the playlist.
        :param images: List of images associated with the playlist.
        :param tracks: List of tracks in the playlist.
        :param public: Public visibility indicator.
        """
        super().__init__(data, type, name, url, id)
        self.description = description
        self.images = images
        self.tracks = tracks
        self.public = public
        self.total_tracks = total_tracks


class PlaylistTrack:
    """
    Represents a track in a playlist.
    """

    def __init__(self, track_data):
        """
        Initializes PlaylistTrack object.

        :param track_data: Data dictionary for the track.
        """
        self.spotify_url = track_data.get("external_urls", {}).get("spotify")
        self.track_name = track_data.get("name")
        self.artists = ", ".join(
            artist.get("name", "") for artist in track_data.get("artists", [])
        )
        self.album = track_data.get("album", {}).get("name")
        self.release_date = track_data.get("album", {}).get("release_date")
        self.preview_url = track_data.get("preview_url")
        self.thumbnail_url = track_data.get("album", {}).get("images", [])[0].get("url")
        self.duration_ms = track_data.get("duration_ms", 0)

    def get_formatted_duration(self) -> dict:
        """
        Gets the formatted duration of the object.

        :return: Dictionary containing hours, minutes, and seconds.
        """
        duration_in_seconds = self.duration_ms / 1000
        hours = 0
        mins = math.floor(duration_in_seconds // 60)

        if mins >= 60:
            hours = math.floor(mins // 60)
            mins = math.floor(mins % 60)

        secs = math.floor(duration_in_seconds % 60)

        return {"hours": hours, "minutes": mins, "seconds": secs}

    def get_string_duration(self) -> str:
        """
        Gets the duration of the object as a formatted string.

        :return: Formatted duration string.
        """
        duration = self.get_formatted_duration()
        format = self.__format_duration

        hours = format(str(duration["hours"]))
        mins = format(str(duration["minutes"]))
        secs = format(str(duration["seconds"]))

        if int(hours):
            return f"{hours}:{mins}:{secs}"
        else:
            return f"{mins}:{secs}"

    def __format_duration(self, value: str):
        """
        Formats duration value.

        :param value: Value to format.
        :return: Formatted value.
        """
        if len(value) < 2:
            return "0" + value
        else:
            return value


class Playlists:
    """
    Represents a collection of playlists.
    """

    def __init__(self, playlist_data):
        """
        Initializes Playlists object.

        :param playlist_data: Data dictionary for the playlists.
        """
        self.playlist_name = playlist_data.get("name", "Unknown Playlist")
        self.description = playlist_data.get("description", "")
        self.total_tracks = playlist_data.get("tracks", {}).get("total", 0)
        self.thumbnail_url = playlist_data.get("images", [])[0].get("url")
        self.tracks = [
            PlaylistTrack(item.get("track"))
            for item in playlist_data.get("tracks", {}).get("items", [])
        ]

    def total_duration(self):
        """
        Calculate the total duration of all tracks in the playlist.

        :return: Total duration as a string.
        """
        total_seconds = sum(track.duration_ms for track in self.tracks) / 1000
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)
        return f"{hours}:{minutes}:{seconds}"

    def total_duration_string(self):
        """
        Calculate the total duration of all tracks in the album as a formatted string.

        :return: Total duration as a formatted string.
        """
        total_seconds = sum(track.duration_ms for track in self.tracks) / 1000
        total_duration_track = PlaylistTrack({"duration_ms": total_seconds * 1000})
        return total_duration_track.get_string_duration()


# CLIENT OBJECTS


class Results(Base):
    """
    Represents results obtained from Spotify API.
    """

    def __init__(self, data):
        """
        Initializes Results object.

        :param data: Data dictionary.
        """
        self.data = data

    def __get_items(self, type):
        """
        Retrieves items from the data dictionary based on the type.

        :param type: Type of items to retrieve.
        :return: List of items.
        """
        if type == "artist":
            try:
                data = self.data["artists"]["items"]
                func = constructor.artist
            except KeyError:
                return []

        elif type == "track":
            try:
                data = self.data["tracks"]["items"]
                func = constructor.track
            except KeyError:
                return []

        elif type == "album":
            try:
                data = [item["album"] for item in self.data["tracks"]["items"]]
                func = constructor.album
            except KeyError:
                return []

        elif type == "episode":
            try:
                data = self.data["episodes"]["items"]
                func = constructor.episode
            except KeyError:
                return []

        elif type == "playlist":
            try:
                data = self.data["playlists"]["items"]
                func = constructor.playlist
            except KeyError:
                return []

        return [func(item) for item in data]

    def get_playlist(self) -> "Playlists":
        """
        Retrieves playlist items from the results.

        :return: Playlists object.
        """
        try:
            playlist_data = self.data
            return Playlists(playlist_data)
        except KeyError:
            return None

    def get_album(self) -> "Albums":
        """
        Retrieves album items from the results.

        :return: Albums object.
        """
        try:
            album_data = self.data
            return Albums(album_data)
        except KeyError:
            return None

    def get_tracks(self) -> list:
        """
        Retrieves track items from the results.

        :return: List of track items.
        """
        return self.__get_items("track")

    def get_artists(self) -> list:
        """
        Retrieves artist items from the results.

        :return: List of artist items.
        """
        return self.__get_items("artist")

    def get_albums(self) -> list:
        """
        Retrieves album items from the results.

        :return: List of album items.
        """
        return self.__get_items("album")

    def get_episodes(self) -> list:
        """
        Retrieves episode items from the results.

        :return: List of episode items.
        """
        return self.__get_items("episode")

    def get_playlists(self) -> list:
        """
        Retrieves playlist items from the results.

        :return: List of playlist items.
        """
        return self.__get_items("playlist")
