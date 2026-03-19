import logging
logger = logging.getLogger(__name__)

import requests
import xbmcvfs
import xbmcplugin

import json

from ..constants import PluginConstants
from requests.utils import dict_from_cookiejar
from requests.utils import cookiejar_from_dict

def _get_cookie_file_path(constants: PluginConstants):
  """
  Gets filepath for cookie store.
  """
  path = xbmcplugin.getSetting(constants.addon_handle, 'cookiefile')
  logger.debug(f"Cookie file path is '{path}'.")
  return path

def store_cookies_from_session(constants: PluginConstants, session: requests.Session):
  """
  Store the session's cookies to the file
  """
  logger.debug(f"Storing cookies to cookie file...")
  path = _get_cookie_file_path(constants)

  with xbmcvfs.File(path, 'w') as f:
    cookies = dict_from_cookiejar(session.cookies)
    f.write(json.dumps(cookies))
    logger.info(f"Stored cookies to '{path}'.")

def load_cookies_to_session(constants: PluginConstants, session: requests.Session):
  """
  Load cookies and add to the session.

  If file does not exist, does nothing.
  """
  logger.debug(f"Loading cookies from cookie file")
  path = _get_cookie_file_path(constants)

  if xbmcvfs.exists(path):
    logger.debug(f"Cookie file '{path}' exists ")
    with xbmcvfs.File(path, 'r') as f:
      cookies = json.loads(f.read())
      cookies = cookiejar_from_dict(cookies)
      session.cookies.update(cookies)
      logger.info(f"Loaded cookies from '{path}'.")
  else:
    logger.info(f"No cookie file found at '{path}'.")
