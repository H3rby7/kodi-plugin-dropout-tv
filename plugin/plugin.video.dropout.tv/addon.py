import sys
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')

url = 'http://localhost/some_video.mkv'
li = xbmcgui.ListItem('My First Video!')
li.setArt({'thumb': 'DefaultVideo.png'})
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)
