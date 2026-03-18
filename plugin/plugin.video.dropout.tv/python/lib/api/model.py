from dataclasses import dataclass
from typing import List, Optional

# --- Generic link structures ---
@dataclass
class Link:
  href: Optional[str]

@dataclass
class PaginationLinks:
  first: Link
  last: Link
  next: Link
  prev: Link
  self_link: Link  # renamed to avoid keyword clash

# --- Embedded item link ---
@dataclass
class CollectionPageLink:
  href: str

@dataclass
class ItemLinks:
  collection_page: CollectionPageLink

# --- Images ---
@dataclass
class ImageVariant:
  large: Optional[str] = None
  source: str = ""

@dataclass
class AdditionalImages:
  aspect_ratio_12_5_logo: Optional[ImageVariant] = None
  aspect_ratio_16_14: Optional[ImageVariant] = None
  aspect_ratio_16_6: Optional[ImageVariant] = None
  aspect_ratio_16_9_background: Optional[ImageVariant] = None

@dataclass
class Thumbnail:
  blurred: str
  large: str
  medium: str
  small: str
  source: str

# --- Main item ---
@dataclass
class Item:
  _links: ItemLinks
  additional_images: AdditionalImages
  created_at: str  # or datetime
  description: str
  id: int
  name: str
  seasons_count: int
  short_description: str
  slug: str
  thumbnail: Thumbnail
  trailer_url: str
  type: str
  updated_at: str  # or datetime

# --- Embedded wrapper ---
@dataclass
class Embedded:
  items: List[Item]

# --- Root response ---
@dataclass
class FeaturedItemsResponse:
  _embedded: Embedded
  _links: PaginationLinks
  count: int
  total: int
