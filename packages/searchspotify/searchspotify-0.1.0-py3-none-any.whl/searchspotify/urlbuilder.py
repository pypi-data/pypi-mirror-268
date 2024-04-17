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

# THIS FILE IS RESPONSABLE FOR BUILDING DYNAMIC URLS


def search_endpoint(
    keywords: str,
    allowed_types: list,
    filters: dict,
    market: str = None,
    limit: int = None,
    offset: int = None,
):
    """
    Constructs the Spotify API search endpoint URL based on provided parameters.

    :param keywords: Keywords for the search.
    :param allowed_types: List of allowed types to search for.
    :param filters: Dictionary of filters to apply to the search.
    :param market: Market to search in (optional).
    :param limit: Maximum number of items to return (optional).
    :param offset: Offset for pagination (optional).
    :return: Constructed search endpoint URL.
    """
    endpoint = "https://api.spotify.com/v1/"

    if "::" in keywords:
        entity_type, entity_id = keywords.split("::")
        # Construct the endpoint based on the entity type and ID
        endpoint += f"{entity_type}s/{entity_id}"
    else:
        endpoint += "search?"

        # FORMAT QUERY ITEMS AND FILTERS
        query_items = keywords.split(" ")
        for filter_name, value in filters.items():
            value = value.replace(" ", "%20")
            item = f"{filter_name}:{value}"
            query_items.append(item)

        # REQUIRED ARGUMENTS
        query = "q=" + "%20".join(query_items)
        types = "type=" + ",".join(allowed_types)
        arguments = [query, types]

        # OPTIONAL ARGUMENTS
        if market:
            arguments.append(f"market={market}")
        if limit:
            arguments.append(f"limit={limit}")
        if offset:
            arguments.append(f"offset={offset}")

        endpoint += "&".join(arguments)

    return endpoint