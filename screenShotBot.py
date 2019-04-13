from pynput.keyboard import Key, Controller
import time
import os

keyboard = Controller()
timeGap = 0.1


# ---- KEYS ----

def enter(period):
    keyboard.press(Key.enter)
    time.sleep(period)
    keyboard.release(Key.enter)
    time.sleep(period)

def tab(period):    
    keyboard.press(Key.tab)
    time.sleep(period)
    keyboard.release(Key.tab)
    time.sleep(period)


# ---- METHODS ----
    
def nextTab():
    keyboard.press(Key.alt)
    time.sleep(timeGap)
    tab(timeGap)
    keyboard.release(Key.alt)
    time.sleep(timeGap)

def snipASnap():
    keyboard.press(Key.alt)
    time.sleep(timeGap)
    keyboard.press("m")
    time.sleep(timeGap)
    keyboard.release("m")
    time.sleep(timeGap)
    keyboard.release(Key.alt)
    time.sleep(timeGap)
    for i in range(4):
        keyboard.press(Key.down)
        time.sleep(timeGap/10)
        keyboard.release(Key.down)
        time.sleep(timeGap/10)
    enter(timeGap)

def save(name):
    keyboard.press(Key.ctrl)
    time.sleep(timeGap)
    keyboard.press("s")
    time.sleep(timeGap)
    keyboard.release("s")
    time.sleep(timeGap)
    keyboard.release(Key.ctrl)
    time.sleep(timeGap)
    keyboard.type(name)
    time.sleep(timeGap)
    enter(0.1)

def openSnipping():
    keyboard.press(Key.cmd)
    time.sleep(timeGap)
    keyboard.release(Key.cmd)
    time.sleep(timeGap)
    keyboard.type("Snipping")
    time.sleep(timeGap)
    enter(timeGap)


# ---- BIGGER METHODS ----
    
def takeAPicAndName(name):
    openSnipping()
    snipASnap()
    save(name)


# ---- RUNNING CODE ----

basic = 'Page_'
for i in range(5):
    name = basic+str(i+1)
    takeAPicAndName(name)


