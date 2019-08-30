# Author: Emmanuel Mireku
# Date: 6/13/2019

# import all the libraries needed here
import pyautogui
import time


def main():
    # move_mouse_to_chrome_and_click()
    # open_chrome_with_start()
    get_mouse_position()


def open_chrome_with_start(link, login_x, login_y):
    pyautogui.press("win")  # press the windows key
    time.sleep(1)  # wait for a second
    pyautogui.typewrite("chrome")  # type chrome in the windows search field
    pyautogui.press("enter")  # hit enter
    time.sleep(2)
    pyautogui.hotkey("ctrl", "l")  # select the link field
    pyautogui.typewrite(link)  # type in the link
    pyautogui.press("enter")  # hit enter
    time.sleep(2)
    pyautogui.hotkey("win", "up")  # maximize the window
    time.sleep(4)   # wait some seconds so that the page can finish loading
    pyautogui.click(login_x, login_y)  # click on the log in button


def get_mouse_position():  # get the mouse pos

    try:
        while True:
            x, y = pyautogui.position()
            position_str = f"current position of x is {str(x)} and y is {str(y)}"
            print(position_str)
    except KeyboardInterrupt:
        print("\n Finished")


def move_mouse_to_chrome_and_click(x, y, link, login_x, login_y):
    chrome_absolute_pos = pyautogui.position(x, y)  # get the position of chrome
    pyautogui.click(chrome_absolute_pos)  # click on chrome
    time.sleep(5)
    pyautogui.hotkey("win", "up")  # shortcut for maximizing chrome window
    time.sleep(3)
    pyautogui.hotkey("ctrl", "t")  # shortcut for opening a new tab
    time.sleep(2)
    pyautogui.hotkey("ctrl", "l")  # select the link
    time.sleep(2)
    pyautogui.typewrite(link)  # type in link
    pyautogui.keyDown("return")  # hit enter
    time.sleep(2)
    pyautogui.click(login_x, login_y)  # click on the log in button


if __name__ == '__main__':
    main()
