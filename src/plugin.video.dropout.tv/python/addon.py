from lib.logger import getLogger
from lib.logger import setLogLevel
logger = getLogger(__name__)

import sys
import xbmcplugin

from lib.constants import PluginConstants
from lib.router import resolve_route

constants = PluginConstants(
  base_url=sys.argv[0],
  addon_handle=int(sys.argv[1]),
  query=sys.argv[2],
  site_id=36348,
  hub_id=1221449,
  url_login="https://watch.dropout.tv/login",
  url_browse="https://watch.dropout.tv/browse",
  url_api_featured="https://api.vhx.tv/products/featured_items",
  url_api_collections="https://api.vhx.tv/collections",
  url_api_videos="https://api.vhx.tv/videos"
)

settingsLogLevel = xbmcplugin.getSetting(constants.addon_handle, 'loglevel').strip()
setLogLevel(int(settingsLogLevel) if settingsLogLevel else 2)

logger.debug(f"{sys.argv}")

xbmcplugin.setContent(constants.addon_handle, 'tvshows')

resolve_route(constants)
