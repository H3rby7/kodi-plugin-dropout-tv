import xbmc
import xbmcgui
import xbmcplugin

from ..constants import PluginConstants
from ..api.collections import Item

def render_item(constants: PluginConstants, item: Item):
  li = xbmcgui.ListItem(item['name'])
  li.setArt({'thumb': item['thumbnail']['large']})
  query = _createQueryParams(item)
  xbmcplugin.addDirectoryItem(handle=constants.addon_handle, url=f"{constants.base_url}?{query}", listitem=li, isFolder=(item['type'] is not "video"))

def _createQueryParams(item: Item):
  query = f"id={item['id']}&type={item['type']}"
  slug = item.get('slug')
  if slug:
    query = f"{query}&slug={slug}"
  return query
