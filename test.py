import pyautogui
import time
import random

now = time.time()
loc = pyautogui.locateCenterOnScreen("assets/winIcon.png",confidence=0.8)
print(loc)
pyautogui.moveTo(loc)
duration = time.time() -now
print(duration)