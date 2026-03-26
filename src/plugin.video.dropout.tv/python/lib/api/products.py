from ..logger import getLogger
logger = getLogger(__name__)

import requests
from typing import TypedDict, List, Optional

from ..constants import PluginConstants
from .bearer_auth import BearerAuth
from ..logger.requestlogger import logResponse

from .shared_models import Link, Image, PaginationLinksBase, ItemBase

def get_featured_items(constants: PluginConstants, session: requests.Session, bearerToken: str):
  """
  Calls api.vhx.tv for featured items
  """
  query = {
    'site_id': constants.site_id,
    'hub_id': constants.hub_id,
  }

  url = constants.url_api_featured
  logger.debug(f"Calling: {url} with params={query}")
  r = session.get(url, params=query, auth=BearerAuth(bearerToken))

  logResponse(constants, r)
  response: FeaturedItemsResponse = r.json()
  logger.debug(f"Received entries: {response.get('count')}")
  return response

class PaginationLinks(PaginationLinksBase):
  self_link: Link

class ImageVariant(TypedDict, total=False):
  large: Optional[str]
  source: str

class AdditionalImages(TypedDict, total=False):
  aspect_ratio_12_5_logo: Optional[ImageVariant]
  aspect_ratio_16_14: Optional[ImageVariant]
  aspect_ratio_16_6: Optional[ImageVariant]
  aspect_ratio_16_9_background: Optional[ImageVariant]

class Item(ItemBase):
  additional_images: AdditionalImages
  seasons_count: int
  trailer_url: str

class Embedded(TypedDict):
  items: List[Item]

class FeaturedItemsResponse(TypedDict):
  _embedded: Embedded
  _links: PaginationLinks
  count: int
  total: int
