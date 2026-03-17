import sys
import xbmcgui
import xbmcplugin

from lib.constants import PluginConstants

constants = PluginConstants(
  addon_handle=int(sys.argv[1]),
  site_id=36348,
  hub_id=1221449,
  url_login="https://watch.dropout.tv/login",
  url_browse="https://watch.dropout.tv/browse",
  url_api_featured="https://api.vhx.tv/products/featured_items"
)

xbmcplugin.setContent(constants.addon_handle, 'tvshows')

url = 'http://localhost/some_video.mkv'
li = xbmcgui.ListItem('My First Video!')
li.setArt({'thumb': 'DefaultVideo.png'})
xbmcplugin.addDirectoryItem(handle=constants.addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(constants.addon_handle)
