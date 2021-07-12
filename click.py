from pynput.mouse import Button, Controller
from datetime import datetime
from time import sleep
from random import randint
import pyautogui,time

mouse = Controller()
inp = int(input("Number of windows 1,2 or 3: "))

time.sleep(2)
try:
    while 1:
        if (str(datetime).find("02:45:")+1):
            exit()
        else:
            mouse.click(Button.left, 1)
            mouse.release(Button.left)
            pos = randint(-25,25)
            sleepPos = randint(1,30)
            # print("Position, sleepPos",pos,sleepPos)
            mouse.position = (1600+pos, 900+pos)

            if inp>1:
                pyautogui.keyDown('alt')
                time.sleep(.2)
                pyautogui.press('tab')
                time.sleep(.2)
                pyautogui.keyUp('alt')

            sleep(sleepPos)

            mouse.click(Button.left, 1)
            mouse.release(Button.left)
            pos = randint(-25,25)
            sleepPos = randint(1,30)
            # print("Position, sleepPos",pos,sleepPos)      
            mouse.position = (1600+pos, 900+pos)

            if inp>2:
                pyautogui.keyDown('alt')
                time.sleep(.2)
                pyautogui.press('tab')
                time.sleep(.2)
                pyautogui.press('tab')
                time.sleep(.2)
                pyautogui.keyUp('alt')
            sleep(sleepPos)

except KeyboardInterrupt:
    exit()
