#!/usr/bin/python3
#
# Screensaver Indicator
#
# Created by John Smith
#
### BEGIN LICENSE
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 3, as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
### END LICENSE

import os,sys,gi,random,fcntl
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, Gio, GLib
from gi.repository import AppIndicator3 as appindicator

def quitApplication(widget):
    sys.exit(0)

def toggleSwitch(widget):
    isActive=widget.get_active()
    if isActive:
      gsettings_schema.set_value(DelayKey,GLib.Variant.new_uint32(DelaySec))
      ind.set_status(appindicator.IndicatorStatus.ACTIVE)
    else:
      gsettings_schema.set_value(DelayKey,GLib.Variant.new_uint32(0))
      ind.set_status(appindicator.IndicatorStatus.ATTENTION)

def renderMenu():
    global menu_switch
    global menu_quit

    # Menu Items
    menu_switch = Gtk.CheckMenuItem('Screensaver')
    menu_switch.connect("toggled", toggleSwitch)
    menu_switch.set_active(True)
    menu.append(menu_switch)

    menu.append(Gtk.SeparatorMenuItem.new())

    menu_quit = Gtk.MenuItem('Quit')
    menu_quit.connect("activate", quitApplication)
    menu.append(menu_quit)

    menu.show_all()
    ind.set_menu(menu)

##### Main Loop
if __name__ == "__main__":
  # Lock File
  try:
    lockFile = open('/tmp/screensaver.lock','w')
    # Try to aquire lock
    fcntl.flock(lockFile, fcntl.LOCK_EX|fcntl.LOCK_NB)
    # File has not been locked before
    fileIsLocked = False
  except:
    # File is already locked
    fileIsLocked = True
  if fileIsLocked:
    sys.exit('Screensaver Indicator instance already running')
  lockFile.write('%d\n'%os.getpid())
  lockFile.flush()

  # Create Application Indicator
  icon_active = "preferences-desktop-screensaver"
  icon_attention = "system-lock-screen"
  ind = appindicator.Indicator.new ("ToggleScreensaver", icon_active, appindicator.IndicatorCategory.APPLICATION_STATUS)
  ind.set_attention_icon(icon_attention)
  ind.set_status(appindicator.IndicatorStatus.ACTIVE)

  # Main Env Vars
  DelaySchema = 'org.gnome.desktop.session'
  DelayKey = 'idle-delay'
  DelaySec = 300

  # gsettings
  gsettings_schema = Gio.Settings.new(DelaySchema)

  # Create Menu
  menu = Gtk.Menu()

  # Render menu items
  renderMenu()

  # Start GTK Main
  Gtk.main()
