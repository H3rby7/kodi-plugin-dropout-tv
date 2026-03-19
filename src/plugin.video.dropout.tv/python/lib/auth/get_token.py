from ..logger import getLogger
logger = getLogger(__name__)

import requests
from typing import Optional, Tuple

import xbmcplugin
import xbmcaddon

from ..constants import PluginConstants
from .html_parser_utils import get_bearer_token_from_text
from .html_parser_utils import get_csrf
from .cookies import store_cookies_from_session

def get_credentials(constants: PluginConstants) -> Tuple[Optional[str], str, str]:
  """
  Get Credentials from settings, or opens settings if they are not yet set.
  """
  email = xbmcplugin.getSetting(constants.addon_handle, 'email')
  password = xbmcplugin.getSetting(constants.addon_handle, 'password')
  if not email or not password:
    xbmcaddon.Addon().openSettings()
    return "Missing Credentials", "", ""
  else:
    return None, email, password

def login(constants: PluginConstants, session: requests.Session, csrf_param: str, csrf_token: str) -> Tuple[Optional[str], str]:
  """
  Log in with the provided credentials and return the retrieved bearer token.

  Also stores the cookies.
  """
  logger.debug(f"Logging in...")
  err, email, password = get_credentials(constants)
  if err:
    return err, ""

  logger.debug(f"Credentials are present.")
  login_payload = {
    "email": email,
    "password": password,
    csrf_param: csrf_token
  }

  logger.info(f"POST Login credentials to get bearer token...")
  r = session.post(constants.url_login, data=login_payload)
  # TODO: If response != 200 or is 200, but 'wrong credentials'
  store_cookies_from_session(constants, session)

  err, token = get_bearer_token_from_text(constants, r.text)
  return err, token

def get_bearer_token(constants: PluginConstants, session: requests.Session) -> Tuple[Optional[str], str]:
  """
  Wrapper to get Bearer Token.

  Uses existing session from FS - Logs back in if necessary
  """
  logger.info(f"GET Browse page to get session cookies...")
  r = session.get(constants.url_browse)
  # TODO: If response != 200
  store_cookies_from_session(constants, session)

  err, bearerToken = get_bearer_token_from_text(constants, r.text)
  if not err:
    return None, bearerToken

  logger.debug(f"Error when tryint to get bearer token: {err}, falling back to login")
  err, csrf_param, csrf_token = get_csrf(constants, r.text)
  if err:
    return err, ""

  return login(constants, session, csrf_param, csrf_token)
