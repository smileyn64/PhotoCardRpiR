#!/usr/bin/env python

import sys
import time

import dot3k.backlight as backlight
import dot3k.joystick as nav
import dot3k.lcd as lcd
from dot3k.menu import Menu, MenuOption

# Add the root examples dir so Python can find the plugins
sys.path.append('../../Pimoroni/displayotron/examples/')

from plugins.utils import Backlight, Contrast


#Classes Declaration
# TODO: Faire les classes de menus
class Idle(MenuOption):
    def __init__(self, arg):
        MenuOption.__init__(self)

class State(MenuOption):
    def __init__(self,arg):
        MenuOption.__init__(self)

class Copy(MenuOption):
    def __init__(self, arg):
        MenuOption.__init__(self)

MyIdle = Idle()
MyState = State()
MyCopy = Copy()

# Menu argument: structure, lcd, idle_handler = None, idle_time = 60
menu = Menu({
        'Etat': MyState,
        'Copie': MyCopy,
        'Options': {
            'Display': {
                'Contrast': Contrast(lcd),
                'Backlight': Backlight(backlight)
                        },
                    },
            },lcd,MyIdle,30)

# Menu Command

repeat_delay = 0.5

@nav.on(nav.UP)
def handle_up(pin):
    menu.up()
    nav.repeat(nav.UP, menu.up, repeat_delay, 0.9)

@nav.on(nav.DOWN)
def handle_down(pin):
    menu.down()
    nav.repeat(nav.DOWN, menu.down, repeat_delay, 0.9)

@nav.on(nav.LEFT)
def handle_left(pin):
    menu.left()
    nav.repeat(nav.LEFT, menu.left, repeat_delay, 0.9)

@nav.on(nav.RIGHT)
def handle_right(pin):
    menu.right()
    nav.repeat(nav.RIGHT, menu.right, repeat_delay, 0.9)

@nav.on(nav.BUTTON)
def handle_button(pin):
    menu.select()

# Loop
while 1:
    menu.redraw()
    time.sleep(0.05)
