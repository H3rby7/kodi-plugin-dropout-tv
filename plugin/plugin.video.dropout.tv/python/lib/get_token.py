import logging

import requests
logger = logging.getLogger(__name__)

import xbmcplugin

from constants import PluginConstants
from html_parser_utils import get_bearer_token_from_text
from html_parser_utils import get_csrf
from cookies import store_cookies_from_session

def login(constants: PluginConstants, session: requests.Session, csrf_param: str, csrf_token: str):
  """
  Log in with the provided credentials and return the retrieved bearer token.

  Also stores the cookies.
  """
  logger.debug(f"Logging in...")
  email = xbmcplugin.getSetting(constants.addon_handle, 'email')
  password = xbmcplugin.getSetting(constants.addon_handle, 'password')
  login_payload = {
    "email": email,
    "password": password,
    csrf_param: csrf_token
  }

  logger.info(f"POST Login credentials to get bearer token...")
  r = session.post(constants.url_login, data=login_payload)
  # TODO: If response != 200 or is 200, but 'wrong credentials'
  store_cookies_from_session(constants, session)

  token = get_bearer_token_from_text(constants, r.text)
  # TODO: Throw/Handle if token is still 'None'
  return token

def get_bearer_token(constants: PluginConstants, session: requests.Session):
  """
  Wrapper to get Bearer Token.

  Uses existing session from FS - Logs back in if necessary
  """
  logger.info(f"GET Browse page to get session cookies...")
  r = session.get(constants.url_browse)
  # TODO: If response != 200
  store_cookies_from_session(constants, session)

  bearerToken = get_bearer_token_from_text(constants, r.text)
  if bearerToken is not None:
    return bearerToken

  logger.debug("Bearer Token is 'None', falling back to login")
  csrf_param, csrf_token = get_csrf(constants, r.text)
  return login(constants, session, csrf_param, csrf_token)
