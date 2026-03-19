from typing import TypedDict, List, Optional

class Link(TypedDict, total=False):
  href: Optional[str]

class Image(TypedDict):
  blurred: str
  """'blurred' may only be available for featured items"""
  large: str
  medium: str
  small: str
  source: str
