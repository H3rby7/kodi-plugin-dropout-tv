import xbmc

logLevel = xbmc.LOGWARNING

class Logger():
  """
  Logger Wrapper for prettier formatting and 'loglevel' setting support
  """
  def __init__(self, name=None):
    self.name = name
  
  def _log(self, msg: str, level: int):
    if level >= logLevel:
      xbmc.log(f"plugin.video.droput.tv:{self.name}.py >>> {msg}", level)

  def debug(self, msg: str):
    self._log(msg, xbmc.LOGDEBUG)

  def info(self, msg: str):
    self._log(msg, xbmc.LOGINFO)

  def warn(self, msg: str):
    self._log(msg, xbmc.LOGWARNING)

  def error(self, msg: str):
    self._log(msg, xbmc.LOGERROR)

  def fatal(self, msg: str):
    self._log(msg, xbmc.LOGFATAL)

def getLogger(name=None):
  """
  Return a logger with the specified name or root
  """
  if not name:
    return Logger("root")
  return Logger(name)

def setLogLevel(minLevel: int):
  """
  Set minimum log level
  """
  global logLevel
  logLevel = minLevel
