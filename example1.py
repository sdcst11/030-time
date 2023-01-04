#!python3
import pyautogui
import time

"""
locateOnScreen :
find the location of your image and gives the location of the box as a tuple:
(left,top,width,height) 
"""
location = pyautogui.locateOnScreen('assets/winIcon.png')
print("locateOnScreen:", location)

"""
locateCenterOnScreen :
find the location of your image and gives the location of the center coordinate as a tuple:
(x,y) 
when it is a coordinate, you can move the mouse there
"""

location = pyautogui.locateCenterOnScreen('assets/winIcon.png')
print("locateCenterOnScreen:",location)
pyautogui.moveTo(location)



