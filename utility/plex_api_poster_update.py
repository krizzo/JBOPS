#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Push Movie and TV Show poster images to Plex.

Updates plex poster images from 'Movies' and 'TV Shows' directories in scripts working
directory. Optinoally specify a dir in the format of ./posters/dir/<LIBRARY_NAME>/*.jpg

Author: krizzo
Requires: plexapi

 Example:
    python plex_api_poster_update.py [-f ./posters/dir/library_posters]

"""

from plexapi.server import PlexServer, CONFIG

print(f"CONFIG: {CONFIG}")

# username = CONFIG.data['auth'].get('myplex_username', PLEX_URL)
# password = CONFIG.data['auth'].get('myplex_password', PLEX_URL)

# account = PlexServer(, '<PASSWORD>')

# plex = account.resource('<SERVERNAME>').connect()  # returns a PlexServer instance

# library_name = ['Movies', 'TV Shows']  # Your library names
