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

# THIS FILE IS RESPONSABLE FOR THE CONSTRUCTION OF MANY OBJECTS

from . import classes


def get_available_markets(data):
    """
    Extracts available markets from the data.

    :param data: The data containing available markets information.
    :return: Available markets or None if not found.
    """
    try:
        return data["available_markets"]
    except KeyError:
        return None


# BASE ARGUMENTS FOR ALL CLASSES
def base_arguments(data):
    """
    Generates base arguments for all classes.

    :param data: The data to generate base arguments from.
    :return: Dictionary of base arguments.
    """
    arguments = dict(
        data=data,
        type=data["type"] if "type" in data else "",
        name=data["name"] if "name" in data else "",
        url=data["external_urls"]["spotify"] if "external_urls" in data else "",
        id=data["id"] if "id" in data else "",
    )
    return arguments


# BASE ARGUMENTS FOR TRACK-LIKE CLASSES
def track_base_arguments(data):
    """
    Generates base arguments for track-like classes.

    :param data: The data to generate base arguments from.
    :return: Dictionary of base arguments.
    """
    arguments = dict(explicit=data["explicit"], duration_ms=data["duration_ms"])
    return arguments


def artist(data):
    """
    Creates an Artist object from the provided data.

    :param data: The data to create the Artist object from.
    :return: An instance of Artist.
    """
    return classes.Artist(**base_arguments(data))


def track(data):
    """
    Creates a Track object from the provided data.

    :param data: The data to create the Track object from.
    :return: An instance of Track.
    """
    base = base_arguments(data)
    track_base = track_base_arguments(data)

    arguments = dict(
        preview=data["preview_url"],
        artists=[artist(artist_data) for artist_data in data["artists"]],
        album=album(data["album"]),
        available_markets=get_available_markets(data),
        disc_number=data["disc_number"],
        popularity=data["popularity"],
    )
    return classes.Track(**{**base, **track_base, **arguments})


def album(data):
    """
    Creates an Album object from the provided data.

    :param data: The data to create the Album object from.
    :return: An instance of Album.
    """
    base = base_arguments(data)

    arguments = dict(
        images=[
            classes.AlbumCover(image["width"], image["height"], image["url"])
            for image in data["images"]
        ],
        artists=[artist(artist_data) for artist_data in data["artists"]],
        available_markets=get_available_markets(data),
        release_date=data["release_date"],
        total_tracks=data["total_tracks"],
    )
    return classes.Album(**{**base, **arguments})


def episode(data):
    """
    Creates an Episode object from the provided data.

    :param data: The data to create the Episode object from.
    :return: An instance of Episode.
    """
    base = base_arguments(data)
    track_base = track_base_arguments(data)

    arguments = dict(
        preview=data["audio_preview_url"],
        description=data["description"],
        html_description=data["html_description"],
        images=data["images"],
        language=data["language"],
        languages=data["languages"],
        release_date=data["release_date"],
    )
    return classes.Episode(**{**base, **track_base, **arguments})


def playlist(data):
    """
    Creates a Playlist object from the provided data.

    :param data: The data to create the Playlist object from.
    :return: An instance of Playlist.
    """
    base = base_arguments(data)

    arguments = dict(
        images=[
            classes.AlbumCover(image["width"], image["height"], image["url"])
            for image in data.get("images", [])
        ],
        tracks=[
            track(track_data) for track_data in data.get("tracks", {}).get("items", [])
        ],
        description=data.get("description"),
        public=data.get("public", False),
        total_tracks=data.get("tracks", {}).get("total", 0),
    )
    return classes.Playlist(**{**base, **arguments})