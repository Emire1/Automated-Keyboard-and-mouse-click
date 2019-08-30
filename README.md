# Automated-Keyboard-and-mouse-click
This simple script can open chrome and log you in into your Brockport blackboard account if you have your password already saved.
This script uses both the mouse and keyboard to automate the task.



# Sources:
* PyautoGui: https://pyautogui.readthedocs.io/en/latest


# How to use:

Before you can use this program, you would have to know the absolute postion of the google chrome icon on your computer screen and also the login postion of the log in button for blackboard and that will be all. This program would only work for a user that already has their log in credentials saved in the blackboard website.

* In order to find the position of what you are looking for, you can run the **get_mouse_position()** and it will print the current x and y position where the mouse pointer is located. Then you can copy them save it for use later.

* After all the positons are saved, you can comment out the **get_mouse_position()** function and run either **open_chrome_with_start()** or **move_mouse_to_chrome_and_click()**.

**open_chrome_with_start(link, login_x, login_y)** only takes in the url and the x and y position of the login button. 
link is the string of the url and the login_x and login_y is the x and y psotion of the log in button of blackboard.

***EXAMPLE***:
**open_chrome_with_start("open.brockport.suny.edu", 222, 435)**
This will type in the link in chrome after it is opened and will click on position (222, 435) and log you in into your blackboard account.

**move_mouse_to_chrome_and_click(x, y, link, login_x, login_y)** takes in the postion of chrome, the url of blackboard, and the postion of blackboard log in button. x and y is the postion of chrome, link is the url of blackboard and login_x, and login_y is the position of the blackboard log in button. 

***EXAMPLE***: 
**move_mouse_to_chrome_and_click(1010, 233, "open.brockport.edu", 222, 435)**
This will move the mouse to postion (1010, 233) and double-click on it then open chrome, after that it will type in the link and then click on the (222, 435) position where the log in button is, which will log you in.



**NOTE**
This has only been tested on windows and I haven't tried it on mac and unix operating system


