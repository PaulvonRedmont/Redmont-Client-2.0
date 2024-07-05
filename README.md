# Redmont-Client-2.0

New and updated version of Redmont Client 1.0.

_Some notable changes:_
- Now uses ppadb and ADB to interact with Bluestacks
- Now allows users to retain full functionality of their keyboard and mouse while the client is running (older versions used pyautogui as a sort of macro)
- Has an 17% increased OCR accuracy rate by increasing image size when processing image

# How to install:

1) Download and install Bluestacks X (https://www.bluestacks.com/)
2) Download and install tesseract (used for Optical Character Recognition) at https://github.com/UB-Mannheim/tesseract/wiki
3) Download and unzip SDK Platform Tools from https://developer.android.com/tools/releases/platform-tools
4) Get the file path for the adb.exe file from the extracted folder and add it to the script under the `adb_path` variable
5) Get the file path for the tesseract.exe file from the extracted folder and add it to the script under the `tesseract_path` variable
6) pip install `pytesseract, pure-python-adb, pyspellchecker`
7) Enable ADB on Bluestacks under Settings < Advanced and restart Bluestacks
