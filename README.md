# gnome-caffeine
Python3 Indicator to toggle the Screensaver for the Gnome Desktop (Caffeine)
![Alt text](/screenshot.png?raw=true "Screenshot")
___
### Run
- install the necessary Python Packages for your Linux Distribution
- install one Extensions for Gnome [appindicator](https://extensions.gnome.org/extension/615/appindicator-support/) or [topicons](https://extensions.gnome.org/extension/1031/topicons/)
```
python3 gnome-screensaver.py
```
___
### Create a Autostarter
Test it, befor you create a Autostarter and then copy the file to "/usr/local/src/".
Then create the file "~/.config/autostart/gnome-screensaver.desktop" with the content:
```
[Desktop Entry]
Type=Application
Name=Screensaver Indicator
Exec=/usr/local/src/gnome-screensaver.py
Icon=preferences-desktop-screensaver
Comment=Switch Screensaver Mode
```
