import xbmcgui
import xbmcplugin

from ..constants import PluginConstants
from ..api.model import Item

def render_series(constants: PluginConstants, item: Item):
  slug = item.get('slug', '')
  # TODO: Slug should not be empty at this point but hey...
  li = xbmcgui.ListItem(item['name'])
  li.setArt({'thumb': item['thumbnail']['large']})
  xbmcplugin.addDirectoryItem(handle=constants.addon_handle, url=f"{constants.base_url}?slug={slug}&type=collection&id={item['id']}", listitem=li, isFolder=True)
