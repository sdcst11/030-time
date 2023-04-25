## SDSS Computing Studies Python Assignment
### Assignment #9 Pyaugotui and Automation (Marks 10)

Objectives:
* Use pyautogui locate image functions
* Use pyautogui mouse controls
* Use pyautogui pixel commands
* Solve a complex problem through planning using code structures
* Make use of prebuilt modules not native to the Python basic installation
* Have programs receive automatic inputs.

Automation is becoming a huge deal, with robots replacing people doing menial tasks every day.  Robots can be quite sophisticated, and are often able to mimic the roles that humans once filled.

Today, we will be exploring the creation of a robot to play a simple game. The simplest games are clicker games, although some of these can become quite complicated.  In fact, a program can not only beat these games, but solve more open ended games that might not appear to be simple on the surface.

To create a robot to play the game, you really need to understand the sequences required to play the game.  There may be multiple screens; how do you navigate between them?  There may be times that your bot becomes out of sync. How do you detect problems and then have them fix themselves automatically?  These are questions that we will need to address when we create our robots.

We will also be making use of 2 built in modules and 1 installed module. Some of these modules have their oown dependencies that we will need to install manually

random
time
pyautogui
pillow (a pyautogui dependency)
opencv-python (a pyaugotui dependency)

Modules that are installed and required for a project are called **dependencies**. Often a project may have many, many dependencies.  This can impose a security risk if the developer is not trusted.

Pay close attention to today's example files, as they will be very important in understanding how the code structures work.

Pyautogui is a module written for python that incorporates a number of different tools together in one package.  We will be using it for automating tasks by looking for graphical elements on screen and then deciding what to do with them

A great source for finding the pyautogui documentation is https://pyautogui.readthedocs.io/en/latest/
This documentation page will help you install the module.

#### Import time commands ####
example0:
see how we can use the time() and sleep() methods in the time module

#### Install pyautogui ####
Install modules directly to your user account.
This is often not the best approach as it installs the module globally to your computer rather than to a specific project. If you were a developer, you might install specific modules for specific projects to help you keep track of the dependences.
We will use the commands
```
py -m pip install <module_name> --user
```

#### How to Take Screenshots ####
* windows-I to open up your settings
* search for "print screen".  The option to have print screen to take a screenshot should be found
* open up the link and change the print screen to take a screen shot option to checked (it's a button)
* to save a screenshot to your clipboard, press print-screen button (BlueFn > Print Screen)
* it should give you the option to open snip and sketch where you can save it. You may need to open your notification center

#### Locate Image Commands ####
example1:
using the pyautogui locate image commands

example1a:
how to restrict your image search to a specific region of the screen (speeds up the search)

example1b:
how to make the search "less strict". Sometimes pixelation in the image result in the image not being found. Lowering the confidence can help find images, but lowering it too much can find false positives, especially with numbers. For example, a 0 could be mistaken for an 8 if you're too loose in your confidence

#### Getting Input ####
Look at some of the commands on https://pyautogui.readthedocs.io/en/latest/msgbox.html.  Try experimenting with some of them to get user input while your autobot is running.

#### Mouse Commands ####
Take a look at: https://pyautogui.readthedocs.io/en/latest/mouse.html
Some of the most important commands are:
* pyautogui.position() - gets the current coordinates of the mouse
* pyautogui.click() - clicks the mouse at the current location or you can specificy the location as a tuple
* pyautogui.mouseDown() - presses the mouse button down (but does not release it)
* pyautogui.mouseUp() - releases the mouse button if it is down
* pyautogui.moveTo() - moves the mouse to a specific coordinate


##### Task 0: Planning sequences of Events
Write down the sequence of events or actions that you will need to program
into your game.  You may want to check pauses if your game needs to wait
for actions to complete. You will be submitting this document as part of
your assessment.

##### Task 1: Working with Time
Create a program that will ask the user to type in a series of words.  Once they have finished typing them all in correctly
