from typing import TypedDict, List, Optional

class Link(TypedDict, total=False):
  href: Optional[str]

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

class Thumbnail(TypedDict):
  blurred: str
  large: str
  medium: str
  small: str
  source: str

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
  thumbnail: Thumbnail
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
