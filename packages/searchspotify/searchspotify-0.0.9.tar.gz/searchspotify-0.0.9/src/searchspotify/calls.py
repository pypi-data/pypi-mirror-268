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

# THIS FILE IS RESPONSABLE FOR API CALLS

from requests import get, post

from . import urlbuilder


def call_acess_token(credentials):
    """
    Calls Spotify API to obtain an access token using client credentials.

    :param credentials: Encoded client credentials.
    :return: Response object containing the access token.
    """
    endpoint = "https://accounts.spotify.com/api/token"
    data = {"grant_type": "client_credentials"}
    headers = {"Authorization": f"Basic {credentials}"}
    return post(url=endpoint, data=data, headers=headers)


def call_search(acess_token, args):
    """
    Calls Spotify API to search for entities using the provided access token and arguments.

    :param access_token: Access token for authentication.
    :param args: Tuple of arguments for the search endpoint.
    :return: Response object containing the search results.
    """
    endpoint = urlbuilder.search_endpoint(*args)
    headers = {"Authorization": f"Bearer {acess_token}"}
    return get(url=endpoint, headers=headers)


def call_track_preview(track_id, access_token):
    """
    Calls Spotify API to retrieve the preview URL for a given track.

    :param track_id: Spotify track ID.
    :param access_token: Access token for authentication.
    :return: Preview URL if available, None otherwise.
    """
    endpoint = f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = get(url=endpoint, headers=headers)
    if response.status_code == 200:
        track_data = response.json()
        if "preview_url" in track_data:
            return track_data["preview_url"]
    return None
