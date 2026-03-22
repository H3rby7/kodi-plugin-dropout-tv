from ..logger import getLogger
logger = getLogger(__name__)

import requests
from typing import TypedDict, List, Optional

from ..constants import PluginConstants
from .bearer_auth import BearerAuth
from .requestlogger import logResponse

from .shared_models import Link, Image, ItemBase

def get_video(constants: PluginConstants, session: requests.Session, bearerToken: str, id: int):
  """
  Calls api.vhx.tv for video
  """
  url = f"{constants.url_api_videos}/{id}"
  logger.debug(f"Calling: {url}")
  r = session.get(url, auth=BearerAuth(bearerToken))

  logResponse(constants, r)
  response: VideoResponse = r.json()
  logger.debug(f"Received entries: {response.get('count')}")
  return response

class Metadata(TypedDict):
  director: str
  writers: List[str]
  release_year: int
  series_name: str
  season_name: str
  season_number: int
  episode_number: int
  custom_icon: Image
  # advertising_keywords: List[str]

class SubtitleLinks(TypedDict):
  srt: Link
  vtt: Link

class Subtitles(TypedDict):
  _links: SubtitleLinks
  label: str
  srclang: str
  kind: str

class Tracks(TypedDict):
  subtitles: List[Subtitles]

class Duration(TypedDict):
  seconds: int
  formatted: str

class FileSize(TypedDict):
  formatted: str
  bytes: int

class FileLinks(TypedDict):
  self: Link

class File(TypedDict):
  _links: FileLinks
  quality: str
  format: str
  method: str
  size: FileSize
  mime_type: str

class Embedded(TypedDict):
  files: List[File]

class PaginationLinks(TypedDict):
  self: Link
  files: Link

class VideoResponse(ItemBase):
  _embedded: Embedded
  _links: PaginationLinks
  title: str
  status: str
  duration: Duration
  tracks: Tracks
  # "advertising": {}
  metadata: Metadata
  plans: List[str]
  time_available: str
  time_unavailable: str
  files_count: int
  plays_count: int
  finishes_count: int
  # "live_event_id": null,
  # "live_video": false,
  # "live_status": null,
  # "scheduled_at": null,
