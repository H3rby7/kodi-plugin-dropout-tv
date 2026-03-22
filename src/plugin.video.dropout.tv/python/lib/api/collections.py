from ..logger import getLogger
logger = getLogger(__name__)

import requests
from typing import TypedDict, List, Optional

from ..constants import PluginConstants
from .bearer_auth import BearerAuth
from .requestlogger import logResponse

from .shared_models import Link, Image, PaginationLinksBase, ItemBase

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
  response: CollectionsResponse = r.json()
  logger.debug(f"Received entries: {response.get('count')}")
  return response

class PaginationLinks(PaginationLinksBase):
  self: Link

class ItemLinks(TypedDict):
  self: Link
  items: Link
  collections_page: Link
  series: Link
  episodes: Link

class SeasonMetaData(TypedDict):
  season_number: int

class AdditionalImages(TypedDict, total=False):
  aspect_ratio_1_1: Optional[Image]
  aspect_ratio_2_3: Optional[Image]
  aspect_ratio_2_3_featured: Optional[Image]
  aspect_ratio_12_5_logo: Optional[Image]
  aspect_ratio_16_14: Optional[Image]
  aspect_ratio_16_6: Optional[Image]
  aspect_ratio_16_9_background: Optional[Image]

class Item(ItemBase):
  _links: ItemLinks
  additional_images: AdditionalImages
  episodes_count: int
  # featured_category_thumbnail_layout: str
  files_count: int
  geo_available: str
  geo_unavailable: str
  has_any_free_videos: bool
  has_free_videos: bool
  has_only_free_videos: bool
  has_only_public_videos: bool
  hide_item_title: bool
  item_id: int
  is_automatic: bool
  is_available: bool
  is_featured: bool
  items_count: int
  live_events_count: int
  metadata: SeasonMetaData
  # overlay_configuration: dict
  position: int
  plans: List[str]
  season_number: int
  seasons_count: int
  tags: Optional[List[str]]
  thumbnail_badges: List[str]
  # thumbnail_size: Optional[str]
  title: str
  trailer_url: str

class Embedded(TypedDict):
  items: List[Item]

class CollectionsResponse(TypedDict):
  _embedded: Embedded
  _links: PaginationLinks
  count: int
  total: int
