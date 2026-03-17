import logging
logger = logging.getLogger(__name__)

import xbmcplugin
import re
from bs4 import BeautifulSoup

from constants import PluginConstants

def _token_or_stars(constants: PluginConstants, token: str | None):
  """
  Returns the token, if token logging is enabled, else returns ***
  """
  log_token = "true" == xbmcplugin.getSetting(constants.addon_handle, 'logtokens').strip().lower()
  return token if log_token else "***"


def get_bearer_token_from_text(constants: PluginConstants, text: str):
  """
  Search for the value of window.TOKEN within the text.

  Usually this value is present within the html requests to dropout.tv after being logged in.
  """
  match = re.search(r'window\.TOKEN\s*=\s*"([^"]+)"', text)
  token = match.group(1) if match else None

  logger.info(f"Retreived token: {_token_or_stars(constants, token)}")
  return token

def get_csrf(constants: PluginConstants, text: str):
  """
  Get the CSRF param and token from a text.

  Usually these values are present within <meta> tags inside the <head> of the html
  """
  logger.debug("Extracting csrf-param and csrf-token...")
  soup = BeautifulSoup(text, "lxml")
  csrf_param = soup.select_one("head meta[name='csrf-param']")["content"]
  csrf_token = soup.select_one("head meta[name='csrf-token']")["content"]
  logger.info(f"Extracted CSRF csrf-param '{csrf_param}' with csrf-token: {_token_or_stars(constants, csrf_token)}")
  return csrf_param, csrf_token
