from lib.logger import getLogger
from lib.logger import setLogLevel
logger = getLogger(__name__)

import sys
import requests
import xbmcgui
import xbmcplugin

from lib.constants import PluginConstants
from lib.auth.cookies import load_cookies_to_session
from lib.auth.get_token import get_bearer_token
from lib.api.products import get_featured_items
from lib.render.item import render_item

constants = PluginConstants(
  base_url=int(sys.argv[0]),
  addon_handle=int(sys.argv[1]),
  site_id=36348,
  hub_id=1221449,
  url_login="https://watch.dropout.tv/login",
  url_browse="https://watch.dropout.tv/browse",
  url_api_featured="https://api.vhx.tv/products/featured_items"
)

settingsLogLevel = xbmcplugin.getSetting(constants.addon_handle, 'loglevel').strip()
setLogLevel(int(settingsLogLevel) if settingsLogLevel else 2)

logger.debug(f"{sys.argv}")

xbmcplugin.setContent(constants.addon_handle, 'tvshows')

session = requests.Session()
load_cookies_to_session(constants, session)
err, bearerToken = get_bearer_token(constants, session)

if err:
  logger.error("Could not access dropout.tv")
  xbmcplugin.addDirectoryItem(handle=constants.addon_handle, url="plugin://", listitem=xbmcgui.ListItem('Could not get FeaturedItems!'))
  xbmcplugin.endOfDirectory(constants.addon_handle, updateListing=False, succeeded=False, cacheToDisc=False)
else:
  logger.info("Getting Featured Items")
  features = get_featured_items(constants, session, bearerToken)
  for item in features['_embedded']['items']:
    render_item(constants, item)

  xbmcplugin.endOfDirectory(constants.addon_handle, cacheToDisc=False)
