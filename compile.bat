@echo off
pyinstaller Valbot.py --onedir --noconfirm --add-data "assets/;assets/"
pause