from typing import TypedDict, List, Optional

class Link(TypedDict, total=False):
  href: str

class PaginationLinksBase(TypedDict):
  first: Link
  last: Link
  next: Link
  prev: Link

class Image(TypedDict):
  blurred: Optional[str]
  """'blurred' may only be available for thumbnail item images"""
  large: str
  medium: str
  small: str
  source: str

class ItemLinks(TypedDict):
  collection_page: Optional[Link]
  collections_page: Optional[Link]
  self: Optional[Link]
  items: Optional[Link]
  series: Optional[Link]
  season: Optional[Link]
  episodes: Optional[Link]
  comments: Optional[Link]
  files: Optional[Link]
  site: Optional[Link]
  video_page: Optional[Link]

class ItemBase(TypedDict):
  id: int
  name: str
  title: Optional[str]
  short_description: str
  description: str
  slug: Optional[str]
  thumbnail: Image
  type: str
  created_at: str
  updated_at: str
  _links: ItemLinks
