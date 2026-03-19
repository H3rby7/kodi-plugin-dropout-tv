import xbmc

from ..constants import PluginConstants
from ..api.model import Item
from .series import render_series
from .video import render_video
from .movie import render_movie
from .live_event import render_live_event

def render_item(constants: PluginConstants, item: Item):
  if "series" == (item['type']):
    return render_series(constants, item)
  if "live_event" == (item['type']):
    return render_live_event(constants, item)
  if "movie" == (item['type']):
    return render_movie(constants, item)
  if "video" == (item['type']):
    return render_video(constants, item)

  xbmc.log("Unknown Item Type", xbmc.LOGDEBUG)
