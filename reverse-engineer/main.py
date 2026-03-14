import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://watch.dropout.tv/"

def write_log_response(name, content):
  with open(f"responses/{name}", "wb") as f:
    f.write(content)
  logger.debug("Response Body is:")
  logger.debug(content)

def get_show_links():
  logger.info("Getting show links")

  r = requests.get(BASE_URL)
  write_log_response("landing.html", r.content)
  

  soup = BeautifulSoup(r.text, "lxml")

  links = []

  for a in soup.select("a[href]"):
    href = a["href"]

    if "/videos/" in href:
      links.append(BASE_URL + href)

  return links


if __name__ == "__main__":
  logger.warning("Reverse Engineering Droput.tv WEB")
  shows = get_show_links()

  for s in shows[:10]:
    logger.warning(f"Found Show: {s}")
