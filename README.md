# Delayed windows shutdown

Sets the time-out period before shutdown (in minutes) and click on "Set time" button

If you need to aborts a system shutdown click on "Clear time" button

![image](https://github.com/DmitryZSer/Delayed-os-shutdown/assets/128312523/7c3e2091-74e4-43f6-aae6-b9e4125a6bba)

How to build:
```
pip install pyinstaller
```
```Win
pyinstaller --onefile --noconsole --icon=red_win.ico -n="Delayed os shutdown"  delayed_os_sd_win.py
```
```Linux
pyinstaller --onefile --noconsole --icon=little_linux.png --add-data "little_linux.png:." n="Delayed os shutdown" delayed_os_sd_linux.py
chmod +x dist/delayed_os_sd_linux
```
