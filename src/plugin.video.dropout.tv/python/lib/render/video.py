from ..logger import getLogger
logger = getLogger(__name__)

import xbmcgui
import xbmcplugin

from typing import Tuple

from ..constants import PluginConstants

def play_video(constants: PluginConstants, videoUrl: str) -> Tuple[bool, xbmcgui.ListItem]:
  listitem = xbmcgui.ListItem(path=videoUrl, offscreen=True)

  # These two lines are needed to prevent the HTTP HEAD request from Kodi core, used to determine the mimetype
  listitem.setMimeType('application/dash+xml')
  listitem.setContentLookup(False)

  listitem.setProperty('inputstream', 'inputstream.adaptive')
  listitem.setProperty('inputstream.adaptive.manifest_type', 'mpd') # Deprecated on Kodi 21, removed on Kodi 22

  return True, listitem
