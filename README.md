# gnome-caffeine
Python3 Indicator to toggle the Screensaver for the Gnome Desktop (Caffeine)
![Alt text](/screenshot.png?raw=true "Screenshot")
___
### Run
- install the necessary Python Packages for your Linux Distribution (try and error)
- install one Extension for Gnome [appindicator](https://extensions.gnome.org/extension/615/appindicator-support/) or [topicons](https://extensions.gnome.org/extension/1031/topicons/)
```
python3 gnome-caffeine.py
```
___
### Install
Copy the Script to "/usr/local/src/" with:
```
sudo install -dm755 /usr/local/src
sudo install -dm755 /usr/local/share/applications
sudo install -m755 gnome-caffeine.py /usr/local/src
sudo install -m644 gnome-caffeine.desktop /usr/local/share/applications
```
___
### Setup the Autostarter
Copy the Desktop File to the Autostart Folder:
```
mkdir -p ~/.config/autostart/
cp /usr/local/share/applications/gnome-caffeine.desktop ~/.config/autostart/.
```
