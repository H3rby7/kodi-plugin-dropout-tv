from ..logger import getLogger
logger = getLogger(__name__)

import xbmcgui
import xbmcplugin

from typing import Dict

from ..constants import PluginConstants
from ..api.shared_models import ItemBase

def render_item(constants: PluginConstants, item: ItemBase):
  li = xbmcgui.ListItem(item['name'])

  # More ART options here:
  # https://xbmc.github.io/docs.kodi.tv/master/kodi-base/d8/d29/group__python__xbmcgui__listitem.html#gad3f9b9befa5f3d2f4683f9957264dbbe
  li.setArt({'thumb': item['thumbnail']['large']})

  info = _createInfoDict(item)
  li.setInfo('video', info)

  # Besser:
  # li.getVideoInfoTag()
  # und dort setzen
  query = _createQueryParams(item)
  isDirectory=item['type'] != "video"
  if not isDirectory:
    li.setProperty("IsPlayable", "true")
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
