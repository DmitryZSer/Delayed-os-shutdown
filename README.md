# Delayed shutdown

Sets the time-out period before shutdown (in minutes) and click on "Set time" button

If you need to aborts a system shutdown click on "Clear time" button

![image](https://github.com/user-attachments/assets/f98f848e-7818-4db5-8580-c8883148d440)

How to build:
```
pip install pyinstaller
```
```Win
pyinstaller --onefile --noconsole --icon=red_win.ico -n="Delayed os shutdown"  delayed_os_sd_win.py
```
```Linux
pyinstaller --onefile --noconsole --icon=little_linux.png --add-data "little_linux.png:." -n="Delayed os shutdown" delayed_os_sd_linux.py
chmod +x dist/"Delayed os shutdown"
```
