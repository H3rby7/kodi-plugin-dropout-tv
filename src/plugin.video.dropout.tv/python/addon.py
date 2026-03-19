import sys
import requests
import xbmcgui
import xbmcplugin

from lib.constants import PluginConstants
from lib.auth.cookies import load_cookies_to_session
from lib.auth.get_token import get_bearer_token
from lib.api.products import get_featured_items

constants = PluginConstants(
  addon_handle=int(sys.argv[1]),
  site_id=36348,
  hub_id=1221449,
  url_login="https://watch.dropout.tv/login",
  url_browse="https://watch.dropout.tv/browse",
  url_api_featured="https://api.vhx.tv/products/featured_items"
)

xbmcplugin.setContent(constants.addon_handle, 'tvshows')

session = requests.Session()
load_cookies_to_session(constants, session)
err, bearerToken = get_bearer_token(constants, session)

if err:
  xbmcplugin.addDirectoryItem(handle=constants.addon_handle, url="plugin://", listitem=xbmcgui.ListItem('Could not get FeaturedItems!'))
  xbmcplugin.endOfDirectory(constants.addon_handle)
else:
  features = get_featured_items(constants, session, bearerToken)
  for collection in features['_embedded']['items']:
    # these items can be a series, live or even videos
    # in case of being a video they dont have a slug attr.
    slug = collection.get('slug', '')
    li = xbmcgui.ListItem(collection['name'])
    li.setArt({'thumb': collection['thumbnail']['large']})
    xbmcplugin.addDirectoryItem(handle=constants.addon_handle, url=f"plugin://{slug}", listitem=li, isFolder=True)

  xbmcplugin.endOfDirectory(constants.addon_handle)
