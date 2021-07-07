from pynput.mouse import Button, Controller
from datetime import datetime
from time import sleep
from random import randint
import pyautogui,time

mouse = Controller()
time.sleep(2)
try:
    while 1:
        if (str(datetime).find("02:45:")+1):
            exit()
        else:
            mouse.click(Button.left, 1)
            mouse.release(Button.left)
            pos = randint(50,50)
            sleepPos = randint(1,30)
            # print("Position, sleepPos",pos,sleepPos)
            mouse.position = (697+pos, 436+pos)

            pyautogui.keyDown('alt')
            time.sleep(.2)
            pyautogui.press('tab')
            time.sleep(.2)
            pyautogui.keyUp('alt')

            sleep(sleepPos)

except KeyboardInterrupt:
    exit()
