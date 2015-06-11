# The documentation written by Voinage was used as a template for this addon
# http://wiki.xbmc.org/?title=HOW-TO_write_plugins_for_XBMC
#
# This addon is licensed with the GNU Public License, and can freely be modified
# http://www.gnu.org/licenses/gpl-2.0.html

import urllib, urllib2, re, sys, xbmcplugin, xbmcgui

def INDEX():
    link = read_url('https://devimages.apple.com.edgekey.net/wwdc-services/ftzj8e4h/6rsxhod7fvdtnjnmgsun/videos.json')
    match = re.compile('title":"([^"]+)".*?playback":"([^"]+)".*?download_hd":"([^"]+)".*?year":([^"]+),',
                       re.DOTALL).findall(link)
    for name, thumbnail, url, year in match:
        liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png",
                           thumbnailImage=thumbnail)
    	liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": name } )
    	xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url,
                                     listitem=liz, isFolder=False)

def read_url(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB;'
                   ' rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link = response.read()
    response.close()
    return link


print ""
INDEX()

xbmcplugin.endOfDirectory(int(sys.argv[1]))
