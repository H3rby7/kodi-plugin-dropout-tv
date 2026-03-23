from ..logger import getLogger
logger = getLogger(__name__)

import xbmcgui
import xbmcplugin

from typing import Tuple

from ..constants import PluginConstants
from ..api.videos import VideoResponse

def play_video(constants: PluginConstants, video: VideoResponse) -> Tuple[bool, xbmcgui.ListItem]:
  err, href = _get_video_url(constants, video)
  if err:
    return False, xbmcgui.ListItem()

  # TODO: Continue here:
  # href is the generic URL, contains no AUTH
  # Maybe we need to add a proxy-http server here to do the GET-URLs as described here:
  # (maybe making the requests with the stored session would already be sufficient.)
  # https://github.com/xbmc/inputstream.adaptive/wiki/How-to-provide-custom-manifest-and-license#how-to-make-a-python-http-proxy-server
  # ORRRR add headers (kind of unclear what headers need to be set...):
  # https://github.com/xbmc/inputstream.adaptive/wiki/Dev.-FAQ#http-error-401
  listitem = xbmcgui.ListItem(path=href, offscreen=True)

  # These two lines are needed to prevent the HTTP HEAD request from Kodi core, used to determine the mimetype
  listitem.setMimeType('application/dash+xml')
  listitem.setContentLookup(False)

  listitem.setProperty('inputstream', 'inputstream.adaptive')
  listitem.setProperty('inputstream.adaptive.manifest_type', 'mpd') # Deprecated on Kodi 21, removed on Kodi 22

  return True, listitem

def _get_video_url(constants: PluginConstants, video: VideoResponse) -> Tuple[str, str]:
  """
  Find matching 'file' href or error.

  Returns Tuple ERR, URL
  """
  for f in video['_embedded']['files']:
    if f['format'] == 'mpd':
      href = f['_links']['self'].get('href')
      if isinstance(href, str):
        return '', href
  return 'No MPD file found, only supports MPD at this moment', ''
