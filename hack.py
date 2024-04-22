import pyautogui
import keyboard
import time
import time

time.sleep(2)
"""
while True:
    if keyboard.is_pressed('s'):
        print(pyautogui.position())
        while keyboard.is_pressed('s'):
            pass

"""
while True:
    bezi = True
    time2 = time.time()
    while bezi:
        if keyboard.is_pressed('esc'):
            quit()
        
        
        while True:
            if keyboard.is_pressed('esc'):
                quit()
            pyautogui.press("enter")
            pyautogui.leftClick(x=804, y=653)
            pyautogui.leftClick(x=936, y=649)
            pyautogui.leftClick(x=1082, y=653)

            
            
            
            pyautogui.leftClick(x=641, y=645)
            pyautogui.leftClick(x=650, y=715)
            pyautogui.leftClick(x=648, y=771)
            

            if time.time() - time2 > 70:
                
                pyautogui.leftClick(x=28, y=76)
                pyautogui.press("enter")
                bezi = False
                time2 = time.time()

            
