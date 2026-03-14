import logging
logger = logging.getLogger(__name__)

import argparse
import argcomplete

parser = argparse.ArgumentParser()
parser.add_argument('-ll', '--log-level', action='store', dest='log_level', help='Log Level', default='INFO')
parser.add_argument('-u', '--username', action='store', dest='user', help='Username')
parser.add_argument('-p', '--password', action='store', dest='pass', help='Password')
argcomplete.autocomplete(parser)

try:
    args = parser.parse_args()
except ImportError:
    logger.critical("Import error, there are missing dependencies to install.  'apt-get install python3-argcomplete "
          "&& activate-global-python-argcomplete3' may solve")
except AttributeError:
    parser.print_help()
except Exception as err:
    logger.error("Error:", err)

logging.basicConfig(level=args.log_level)

import requests
from bs4 import BeautifulSoup
import json

session = requests.Session()

LOGIN_URL = "https://watch.dropout.tv/login"

def write_log_response(name, response):
  with open(f"responses/{name}-response.html", "wb") as f:
    f.write(response.content)
  logger.debug("Response Body is:")
  logger.debug(response.content)
  with open(f"responses/{name}-headers.json", "w") as f:
    json.dump(dict(response.headers), f, indent=2, sort_keys=True)
  logger.debug("Response Headers are:")
  logger.debug(f"{response.headers}")

def get_csrf_dict(soup):
  param = soup.select_one("head meta[name='csrf-param']")["content"]
  token = soup.select_one("head meta[name='csrf-token']")["content"]
  logger.info(f"Extracted CSRF header data > {param}:{token}")
  return [param, token]

def login():
  logger.info(f"GET Login page to get session cookies...")
  r = session.get(LOGIN_URL)
  write_log_response("login-GET", r)
  logger.debug(f"Session cookies are: {session.cookies.get_dict()}")

  soup = BeautifulSoup(r.text, "lxml")
  csrfHeader = get_csrf_dict(soup)

  login_payload = {
    "email": "user@example.com",
    "password": "password"
    # 'utf8': '%E2%9C%93'
  }
  login_payload[csrfHeader[0]] = csrfHeader[1]

  logger.info(f"POST Login credentials to get bearer token...")

  r = session.post(LOGIN_URL, data=login_payload)
  write_log_response("login-POST", r)

  return "eyMOCK.MOCK.MOCK"

if __name__ == "__main__":
  logger.warning("Reverse Engineering Droput.tv WEB")
  bearerToken = login()

  logger.info(f"Retreived token: {bearerToken}")
