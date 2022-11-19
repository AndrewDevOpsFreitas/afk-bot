import pyautogui as pag
import random
import time

while True:
    initialPosition = pag.position()
    time.sleep(30)
    currentPosition = pag.position()
    
    if initialPosition == currentPosition:
        #print("not moved")
        x = random.randint(600,700)
        y = random.randint(200,600)
        pag.moveTo(x,y,0.5)