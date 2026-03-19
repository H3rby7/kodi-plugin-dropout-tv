import xbmcgui
import xbmcplugin

from ..constants import PluginConstants
from ..api.model import Item

def render_series(constants: PluginConstants, item: Item):
  slug = item.get('slug', '')
  # TODO: Slug should not be empty at this point but hey...
  li = xbmcgui.ListItem(item['name'])
  li.setArt({'thumb': item['thumbnail']['large']})
  xbmcplugin.addDirectoryItem(handle=constants.addon_handle, url=f"plugin://{slug}", listitem=li, isFolder=True)
