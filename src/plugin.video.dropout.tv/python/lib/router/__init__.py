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
from ..html.videos import get_video
from ..render.item import render_item
from ..render.video import play_video

def resolve_route(constants: PluginConstants):
  args = parse_qs(constants.query[1:])
  logger.debug(f"Router called with: {args}")
  route = args.get('type', ['none'])[0]
  if route == 'series' or route == 'season':
    id = int(args['id'][0], 10)
    return show_collection(constants, id)
  if route == 'video':
    droupoutHref = args['video_url'][0]
    return get_and_play_video(constants, droupoutHref)

  # Fallback / Default
  return show_featured(constants)

def get_and_play_video(constants: PluginConstants, droupoutHref: str):
  session = requests.Session()
  load_cookies_to_session(constants, session)

  logger.info(f"Getting Video: {droupoutHref}")
  err, videoUrl = get_video(constants, session, droupoutHref)
  if err:
    logger.error(f"Error Playing Video: '{err}'")
    xbmcplugin.setResolvedUrl(constants.addon_handle, False, xbmcgui.ListItem())
    return

  success, listItem = play_video(constants, videoUrl)
  xbmcplugin.setResolvedUrl(constants.addon_handle, success, listItem)

def show_featured(constants: PluginConstants):
  session = requests.Session()
  load_cookies_to_session(constants, session)
  err, bearerToken = get_bearer_token(constants, session)

  if err:
    logger.error("Could not access dropout.tv")
    xbmcplugin.addDirectoryItem(handle=constants.addon_handle, url=constants.base_url, listitem=xbmcgui.ListItem('Could not get Collection!'))
    xbmcplugin.endOfDirectory(constants.addon_handle, updateListing=False, succeeded=False, cacheToDisc=False)
    return

  logger.info("Getting Featured Items")
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
