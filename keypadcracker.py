import itertools
import pyautogui
import time

def waitTime(wait):
    if wait:
        time.sleep(float(wait))
    else:
        time.sleep(0)

while True:
    selected = input("Enter Key : \n")
    if selected == "1":
        one = pyautogui.position()
        print("One Pos : ", one)
    elif selected == "2":
        two = pyautogui.position()
        print("Two Pos : ", two)
    elif selected == "3":
        three = pyautogui.position()
        print("Three Pos : ", three)
    elif selected == "4":
        four = pyautogui.position()
        print("Four Pos : ", four)
    elif selected == "5":
        five = pyautogui.position()
        print("Five Pos : ", five)
    elif selected == "6":
        six = pyautogui.position()
        print("Six Pos : ", six)
    elif selected == "7":
        seven = pyautogui.position()
        print("Seven Pos : ", seven)
    elif selected == "8":
        eight = pyautogui.position()
        print("Eight Pos : ", eight)
    elif selected == "9":
        nine = pyautogui.position()
        print("Nine Pos : ", nine)
    elif selected == "0":
        zero = pyautogui.position()
        print("Zero Pos : ", zero)
    elif selected == "e":
        enter = pyautogui.position()
        print("Enter Pos : ", enter)
    elif selected == "c":
        clear = pyautogui.position()
        print("Clear Pos : ", clear)
    elif selected == "l":
        length = input("Input code length\n")
    elif selected == "t":
        wait = input("Input delay between presses\n")
    elif selected == "s":
        for x in (itertools.product("1234567890", repeat=int(length))):
            print("Trying Code: ", x)
            if clear:
                    waitTime(wait)
                    pyautogui.click(clear)
            for z in x:
                waitTime(wait)
                if z == "1":
                    pyautogui.click(one)
                elif z == "2":
                    pyautogui.click(two)
                elif z == "3":
                    pyautogui.click(three)
                elif z == "4":
                    pyautogui.click(four)
                elif z == "5":
                    pyautogui.click(five)
                elif z == "6":
                    pyautogui.click(six)
                elif z == "7":
                    pyautogui.click(seven)
                elif z == "8":
                    pyautogui.click(eight)
                elif z == "9":
                    pyautogui.click(nine)
                elif z == "0":
                    pyautogui.click(zero)
                waitTime(wait)
            pyautogui.click(enter)
                    
            
