from ..logger import getLogger
logger = getLogger(__name__)

import xbmcgui
import xbmcplugin

from typing import Dict

from ..constants import PluginConstants
from ..api.shared_models import ItemBase

def render_item(constants: PluginConstants, item: ItemBase):
  li = xbmcgui.ListItem(item['name'])
  li.setArt({'thumb': item['thumbnail']['large']})

  info = _createInfoDict(item)
  li.setInfo('video', info)
  query = _createQueryParams(item)
  isDirectory=item['type'] != "video"
  link = f"{constants.base_url}?{query}"

  logger.debug(f"Adding a {'dir' if isDirectory else 'file'} with url: {link} and info: {info}")
  xbmcplugin.addDirectoryItem(handle=constants.addon_handle, url=link, listitem=li, isFolder=isDirectory)

def _createQueryParams(item: ItemBase):
  """
  Map ItemBase to a url as expected by xbmcplugin.addDirectoryItem
  """
  query = f"id={item['id']}&type={item['type']}"
  slug = item.get('slug')
  if slug:
    query = f"{query}&slug={slug}"
  return query

def _createInfoDict(item: ItemBase) -> Dict[str, str]:
  """
  Map Itembase to a Dict[str, str] as expected by xbmcgui.ListItem.setInfo
  """
  d: Dict[str, str] = {}

  # Use 'title' attr if present, else use name
  v = item.get('title')
  if v is not None:
    d['title'] = v
  else:
    v = item.get('name')
    if v is not None:
      d['title'] = v

  v = item.get('description')
  if v is not None:
    d['plot'] = v
  return d
