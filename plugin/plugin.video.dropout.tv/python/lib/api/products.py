import logging
logger = logging.getLogger(__name__)

import requests

from ..constants import PluginConstants
from bearer_auth import BearerAuth
from model import FeaturedItemsResponse

def get_featured_items(constants: PluginConstants, session: requests.Session, bearerToken: str):
  """
  Calls api.vhx.tv for featured items
  """
  query = {
    'site_id': constants.site_id,
    'hub_id': constants.hub_id,
  }
  r = session.get(constants.url_api_featured, params=query, auth=BearerAuth(bearerToken))
  return FeaturedItemsResponse(**r.json())
