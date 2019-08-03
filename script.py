# Author: Emmanuel Mireku
# Date: 6/13/2019

# import all the libraries needed here
import pyautogui
import time


def main():
    # move_mouse_to_chrome_and_click()  # Move the mouse to chrome and click on it
    # get_mouse_position()  # Get the position of the mouse
    open_chrome_with_start()  # Open chrome by using the start menu


# This function uses the start menu to open chrome and log in the user.
def open_chrome_with_start():
    pyautogui.press("win")  # press the windows key
    time.sleep(1)  # wait for a second
    pyautogui.typewrite("chrome")  # type "chrome" in the windows search field
    pyautogui.press("enter")  # press enter
    time.sleep(2)  # wait for 2 seconds
    pyautogui.hotkey("ctrl", "l")  # select the link field with the "CTRL + L" shortcut key
    pyautogui.typewrite("brockport.open.suny.edu")  # Type in the Brockport link
    pyautogui.press("enter")  # press enter
    time.sleep(2)  # wait for 2 seconds
    pyautogui.hotkey("win", "up")  # maximize the window with the "WIN + Up" shortcut key
    time.sleep(4)  # wait for 4 seconds, sometimes some browsers are slow that is why
    pyautogui.click(163, 544)  # click on the log in button


# get the position of the mouse; I got this code from pyautogui.org documentation
def get_mouse_position():
    print('Press Ctrl-C to quit.')
    try:
        while True:
            x, y = pyautogui.position()
            position_str = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(position_str, end='')
            print('\b' * len(position_str), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')


# This function moves the mouse to the location of chrome on my screen and click on it.
def move_mouse_to_chrome_and_click():
    chrome_absolute_pos = pyautogui.position(621, 744)  # get the absolute position/coordinates of chrome
    pyautogui.click(chrome_absolute_pos)  # click on chrome
    time.sleep(4)  # wait for 4 seconds so chrome can finish loading
    pyautogui.hotkey("win", "up")  # shortcut for maximizing chrome window
    time.sleep(3)  # wait for 3 seconds
    pyautogui.hotkey("ctrl", "t")  # shortcut for opening a new tab just in case another page is opened
    time.sleep(2)  # wait for new tab to open
    pyautogui.hotkey("ctrl", "l")  # select the link tab
    pyautogui.typewrite("brockport.open.suny.edu")  # type in the Brockport link
    pyautogui.keyDown("return")  # hit enter
    time.sleep(3)  # wait 3 seconds for the page to load
    pyautogui.click(163, 544)  # click on the log in button


if __name__ == '__main__':
    main()
