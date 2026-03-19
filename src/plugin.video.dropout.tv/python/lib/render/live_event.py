import xbmcgui
import xbmcplugin

from ..constants import PluginConstants
from ..api.model import Item

def render_live_event(constants: PluginConstants, item: Item):
  name = item['name']
  li = xbmcgui.ListItem(f"{name} - UNIMPLEMENTED")
  li.setArt({'thumb': item['thumbnail']['large']})
  xbmcplugin.addDirectoryItem(handle=constants.addon_handle, url="UNIMPLEMENTED", listitem=li, isFolder=False)
