from ..logger import getLogger
logger = getLogger(__name__)

import xbmcplugin
import requests

from ..constants import PluginConstants

def logResponse(constants: PluginConstants, r: requests.Response):
  if "true" == xbmcplugin.getSetting(constants.addon_handle, 'logrequests').strip().lower():
    logger.debug(f"BODY: \n{r.content}")
