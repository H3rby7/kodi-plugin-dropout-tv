class PluginConstants():
  """
  Plugin Constants
  """
  def __init__(
      self,
      base_url: str,
      addon_handle: int,
      site_id: int,
      hub_id: int,
      url_login: str,
      url_browse: str,
      url_api_featured: str
    ):
    self.base_url = base_url
    self.addon_handle = addon_handle
    self.site_id = site_id
    self.hub_id = hub_id
    self.url_login = url_login
    self.url_browse = url_browse
    self.url_api_featured = url_api_featured
