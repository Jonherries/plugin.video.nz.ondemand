import os, sys, xbmcaddon, resources.tools
from datetime import date

import resources.tools as tools
import resources.config as config
settings = config.__settings__

class shine:
 def item(self):
  self.channel = 'Shine'
  item = tools.xbmcItem(False)
  item.fanart = os.path.join('extrafanart', self.channel + '.jpg')
  info = item.info
  info["Title"] = 'Shine TV (Live Stream)'
  info["Thumb"] = os.path.join(settings.getAddonInfo('path'), "resources/images/%s.png" % self.channel)
  info["Plot"] = "Shine TV is a television network of the Rhema Broadcasting Group Inc - New Zealand's largest Christian media organisation. On-air since December 2002, Shine broadcasts 24 hours nationwide on the SKY digital and Freeview Satellite platforms, with regional channels in Canterbury, Nelson and Wellington."
  info["Date"] = date.today().strftime("%d.%m.%Y")
  quality = 'high'
  if settings.getSetting('%s_quality' % self.channel) == "Low":
   quality = 'low'
  elif settings.getSetting('%s_quality' % self.channel) == "Medium":
   quality = 'med'
  info["FileName"] = "http://wms-rbg.harmonycdn.net/shinetv-%s?MSWMExt=.asf" % quality
  return item