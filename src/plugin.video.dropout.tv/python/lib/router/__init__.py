from ..logger import getLogger
logger = getLogger(__name__)

import requests
import xbmcgui
import xbmcplugin
from urllib.parse import parse_qs

from ..constants import PluginConstants
from ..auth.cookies import load_cookies_to_session
from ..auth.get_token import get_bearer_token
from ..api.products import get_featured_items
from ..api.collections import get_collection
from ..api.videos import get_video
from ..render.item import render_item

def resolve_route(constants: PluginConstants):
  args = parse_qs(constants.query[1:])
  logger.debug(f"Router called with: {args}")
  route = args.get('type', ['none'])[0]
  if route == 'series' or route == 'season':
    id = int(args['id'][0], 10)
    return show_collection(constants, id)
  if route == 'video':
    id = int(args['id'][0], 10)
    return show_video(constants, id)

  # Fallback / Default
  return show_featured(constants)

def show_video(constants: PluginConstants, id: int):
  session = requests.Session()
  load_cookies_to_session(constants, session)
  err, bearerToken = get_bearer_token(constants, session)

  if err:
    logger.error("Could not access dropout.tv")
    xbmcplugin.addDirectoryItem(handle=constants.addon_handle, url=constants.base_url, listitem=xbmcgui.ListItem('Could not get FeaturedItems!'))
    xbmcplugin.endOfDirectory(constants.addon_handle, updateListing=False, succeeded=False, cacheToDisc=False)
    return
  
  logger.info("Getting Video")
  video = get_video(constants, session, bearerToken, id)

  logger.debug(f"Video is: {video}")
  xbmcplugin.addDirectoryItem(handle=constants.addon_handle, url=constants.base_url, listitem=xbmcgui.ListItem('Go Back...'), isFolder=True)
  xbmcplugin.endOfDirectory(constants.addon_handle, cacheToDisc=False)

def show_featured(constants: PluginConstants):
  session = requests.Session()
  load_cookies_to_session(constants, session)
  err, bearerToken = get_bearer_token(constants, session)

  if err:
    logger.error("Could not access dropout.tv")
    xbmcplugin.addDirectoryItem(handle=constants.addon_handle, url=constants.base_url, listitem=xbmcgui.ListItem('Could not get Collection!'))
    xbmcplugin.endOfDirectory(constants.addon_handle, updateListing=False, succeeded=False, cacheToDisc=False)
    return

  logger.info("Getting Collection")
  features = get_featured_items(constants, session, bearerToken)
  for item in features['_embedded']['items']:
    render_item(constants, item)

  xbmcplugin.endOfDirectory(constants.addon_handle, cacheToDisc=False)

def show_collection(constants: PluginConstants, id: int):
  session = requests.Session()
  load_cookies_to_session(constants, session)
  err, bearerToken = get_bearer_token(constants, session)

  if err:
    logger.error("Could not access dropout.tv")
    xbmcplugin.addDirectoryItem(handle=constants.addon_handle, url=constants.base_url, listitem=xbmcgui.ListItem('Could not get FeaturedItems!'))
    xbmcplugin.endOfDirectory(constants.addon_handle, updateListing=False, succeeded=False, cacheToDisc=False)
    return

  logger.info("Getting Collection")
  collection = get_collection(constants, session, bearerToken, id)
  for item in collection['_embedded']['items']:
    render_item(constants, item)

  xbmcplugin.endOfDirectory(constants.addon_handle, cacheToDisc=False, updateListing=True)
