from ..logger import getLogger
logger = getLogger(__name__)

import requests
from typing import TypedDict, List, Optional

from ..constants import PluginConstants
from .bearer_auth import BearerAuth
from .requestlogger import logResponse

from .shared_models import Link, Image

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

def get_collection(constants: PluginConstants, session: requests.Session, bearerToken: str, id: int):
  """
  Calls api.vhx.tv for a collection
  """
  # More complicated, collection is paginated, can contain videos and more collections
  # https://dev.vhx.tv/docs/api/#collection-items-list
  url = f"{constants.url_api_collections}/{id}/items"
  logger.debug(f"Calling: {url}")
  r = session.get(url, auth=BearerAuth(bearerToken))

  logResponse(constants, r)
  response: FeaturedItemsResponse = r.json()
  logger.debug(f"Received entries: {response.get('count')}")
  return response

class PaginationLinks(TypedDict):
  first: Link
  last: Link
  next: Link
  prev: Link
  self_link: Link

class CollectionPageLink(TypedDict):
  href: str

class ItemLinks(TypedDict):
  collection_page: CollectionPageLink

class ImageVariant(TypedDict, total=False):
  large: Optional[str]
  source: str

class AdditionalImages(TypedDict, total=False):
  aspect_ratio_12_5_logo: Optional[ImageVariant]
  aspect_ratio_16_14: Optional[ImageVariant]
  aspect_ratio_16_6: Optional[ImageVariant]
  aspect_ratio_16_9_background: Optional[ImageVariant]

class Item(TypedDict):
  _links: ItemLinks
  additional_images: AdditionalImages
  created_at: str
  description: str
  id: int
  name: str
  seasons_count: int
  short_description: str
  slug: str
  thumbnail: Image
  trailer_url: str
  type: str
  updated_at: str

class Embedded(TypedDict):
  items: List[Item]

class FeaturedItemsResponse(TypedDict):
  _embedded: Embedded
  _links: PaginationLinks
  count: int
  total: int
