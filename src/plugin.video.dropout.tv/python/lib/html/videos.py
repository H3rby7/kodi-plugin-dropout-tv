from ..logger import getLogger
logger = getLogger(__name__)

import requests
from typing import Tuple, Optional
from bs4 import BeautifulSoup

from ..constants import PluginConstants
from ..logger.requestlogger import logResponse

def get_video(constants: PluginConstants, session: requests.Session, droupoutHref: str) -> Tuple[Optional[str], str]:
  """
  Calls dropout.tv HTML for video
  """
  logger.debug(f"Calling: {droupoutHref}")
  r = session.get(droupoutHref)

  logResponse(constants, r)
  err, iframeUrl = get_video_iframe_from_text(constants, r.text)
  if err:
    return err, ""
  
  logger.debug(f"Calling: {iframeUrl}")
  r = session.get(iframeUrl)

  logResponse(constants, r)
  return "not implemented", ""

def get_video_iframe_from_text(constants: PluginConstants, text: str) -> Tuple[Optional[str], str]:
  """
  Search for the iframe with title='Video Player'
  """
  soup = BeautifulSoup(text, "html.parser")

  # TODO: The html returned here does not contain the iframe.
  # TODO: Maybe a recaptcha issue?
  # TODO: Also currentuser etc. is not set...
  iframe_tag = soup.select_one("iframe[title='Video Player']")
  if not iframe_tag:
    return "HTML does not contain Video Player iframe", ""

  href: str = iframe_tag["src"]

  if not isinstance(href, str):
    return "HTML does not contain Video Player iframe", ""

  logger.info(f"Extracted iframe href '{href}'")
  return None, href