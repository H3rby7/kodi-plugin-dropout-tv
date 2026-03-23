import logging
logger = logging.getLogger(__name__)

import argparse
import argcomplete

parser = argparse.ArgumentParser()
parser.add_argument('-ll', '--log-level', action='store', dest='log_level', help='Log Level', default='INFO')
parser.add_argument('-lr', '--log-responses', action='store', dest='log_respones', help='Log Responses', default=False)
parser.add_argument('-lh', '--log-headers', action='store', dest='log_headers', help='Log Headers', default=False)
parser.add_argument('-lt', '--log-tokens', action='store', dest='log_tokens', help='Log Tokens', default=False)
parser.add_argument('-e', '--email', action='store', dest='email', help='email address')
parser.add_argument('-p', '--password', action='store', dest='password', help='Password')
argcomplete.autocomplete(parser)

args = None
try:
    args = parser.parse_args()
except ImportError:
    logger.critical("Import error, there are missing dependencies to install.  'apt-get install python3-argcomplete "
          "&& activate-global-python-argcomplete3' may solve")
except AttributeError:
    parser.print_help()
except Exception as err:
    logger.error("Error:", err)

if args is None:
  exit(1)

logging.basicConfig(level=args.log_level)

from pathlib import Path
import json
import re

import requests
from requests.auth import AuthBase
from requests.utils import dict_from_cookiejar
from requests.utils import cookiejar_from_dict
from bs4 import BeautifulSoup

SITE_ID = 36348
"""Dropout TV Site ID in api.vhx.tv"""

HUB_ID = 1221449
"""Dropout TV Hub ID??? in api.vhx.tv"""

LOGIN_URL = "https://watch.dropout.tv/login"
"""Dropout TV Login URL"""

BROWSE_URL = "https://watch.dropout.tv/browse"
"""Dropout TV Standard Landing Page"""

COOKIE_FILE = "stored-cookies.json"
"""File Path to store cookies"""

FEATURED_ITEMS_URL = "https://api.vhx.tv/products/featured_items"
"""API URL to Featured Items - Exemplary endpoint"""

class BearerAuth(AuthBase):
  """
  Python Requests Bearer Token Auth Support
  """
  def __init__(self, token):
    self.token = token
  def __call__(self, r):
    r.headers["authorization"] = "Bearer " + self.token
    return r

def store_cookies(session):
  """
  Store the session's cookies to 'COOKIE_FILE'
  """
  logger.debug(f"Storing cookies to '{COOKIE_FILE}' ...")
  cookies = dict_from_cookiejar(session.cookies)
  Path(COOKIE_FILE).write_text(json.dumps(cookies))
  logger.info(f"Stored cookies to '{COOKIE_FILE}'.")

def load_cookies(session):
  """
  Load cookies from 'COOKIE_FILE' and add to the session.

  If 'COOKIE_FILE' does not exist, does nothing.
  """
  logger.debug(f"Loading cookies from '{COOKIE_FILE}'...")
  cookies_file = Path(COOKIE_FILE)
  if cookies_file.is_file():
    logger.debug(f"Cookie file '{COOKIE_FILE}' exists ")
    cookies = json.loads(cookies_file.read_text())
    cookies = cookiejar_from_dict(cookies)
    session.cookies.update(cookies)
    logger.info(f"Loaded cookies from '{COOKIE_FILE}'.")
  else:
    logger.info(f"No cookie file found at '{COOKIE_FILE}'.")

def write_log_response(name, response):
  """
  Reverse Engineering Debug Utility.

  Writes response and headers to the filesystem.
  Logs response and headers, if enabled by flags.
  """
  if 'json' in response.headers['content-type']:
    with open(f"responses/{name}-response.json", "w") as f:
      json.dump(response.json(), f, indent=2, sort_keys=True)
  elif 'html' in response.headers['content-type']:
    with open(f"responses/{name}-response.html", "wb") as f:
      f.write(response.content)
  else:
    with open(f"responses/{name}-response.txt", "wb") as f:
      f.write(response.content)

  if args is not None and args.log_respones:
    logger.debug("Response Body is:")
    logger.debug(response.content)

  with open(f"responses/{name}-headers.json", "w") as f:
    json.dump(dict(response.headers), f, indent=2, sort_keys=True)

  if args is not None and args.log_headers:
    logger.debug("Response Headers are:")
    logger.debug(f"{response.headers}")

def login(session, email, password, csrf_param, csrf_token):
  """
  Log in with the provided credentials and return the retrieved bearer token.

  Also stores the cookies.
  """
  logger.debug(f"Logging in...")
  login_payload = {
    "email": email,
    "password": password,
    csrf_param: csrf_token
  }

  logger.info(f"POST Login credentials to get bearer token...")
  r = session.post(LOGIN_URL, data=login_payload)
  write_log_response("login-POST", r)
  # TODO: If response != 200 or is 200, but 'wrong credentials'
  store_cookies(session)

  token = get_bearer_token_from_text(r.text)
  # TODO: Throw/Handle if token is still 'None'
  return token

def get_bearer_token_from_text(text):
  """
  Search for the value of window.TOKEN within the text.

  Usually this value is present within the html requests to dropout.tv after being logged in.
  """
  match = re.search(r'window\.TOKEN\s*=\s*"([^"]+)"', text)
  token = match.group(1) if match else None

  logged_token = token if args is not None and args.log_tokens else "***"
  logger.info(f"Retreived token: {logged_token}")
  return token

def get_csrf(text):
  """
  Get the CSRF param and token from a text.

  Usually these values are present within <meta> tags inside the <head> of the html
  """
  logger.debug("Extracting csrf-param and csrf-token...")
  soup = BeautifulSoup(text, "lxml")
  csrf_param = soup.select_one("head meta[name='csrf-param']")["content"]
  csrf_token = soup.select_one("head meta[name='csrf-token']")["content"]
  logged_token = csrf_token if args is not None and args.log_tokens else "***"
  logger.info(f"Extracted CSRF csrf-param '{csrf_param}' with csrf-token: {logged_token}")
  return csrf_param, csrf_token

def get_bearer_token(session, email, password):
  """
  Wrapper to get Bearer Token.

  Uses existing session from FS - Logs back in if necessary
  """
  logger.info(f"GET Browse page to get session cookies...")
  r = session.get(BROWSE_URL)
  write_log_response("browse-GET", r)
  # TODO: If response != 200
  store_cookies(session)

  bearerToken = get_bearer_token_from_text(r.text)
  if bearerToken is not None:
    return bearerToken

  logger.debug("Bearer Token is 'None', falling back to login")
  csrf_param, csrf_token = get_csrf(r.text)
  return login(session, email, password, csrf_param, csrf_token)

def get_featured_items(bearerToken):
  """
  Calls api.vhx.tv for featured items
  """
  query = {
    'site_id': SITE_ID,
    'hub_id': HUB_ID,
  }
  r = session.get(FEATURED_ITEMS_URL, params=query, auth=BearerAuth(bearerToken))
  write_log_response("featured_items-GET", r)

if __name__ == "__main__":
  logger.warning("Reverse Engineering Dropout.tv WEB")
  session = requests.Session()
  load_cookies(session)
  bearerToken = get_bearer_token(session, args.email, args.password)

  # Probably do need to call the dropout.tv pages html 
  # parse the iframe src
  # call iframe src to parse the m3u8 urls

  get_featured_items(bearerToken)
