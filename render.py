#! /usr/bin/env python3

import os
import time
from screen_objects import *

class View:
    def __init__(self):
        self.lines = []
        self.update()
        self.objects = []
    
    def update(self):
        self.t_size = os.get_terminal_size()
    
    def render(self):
        self.update()
        self.populate_lines()
        print("Terminal size: %i x %i" %(self.t_size[0], self.t_size[1]))
        
        for obj in self.objects:
            obj.draw(self.lines)
        
        for line in self.lines:
            print("".join(line))
        
    def populate_lines(self, char="."):
        self.lines = [[char for x in range(self.t_size.columns)] for y in range(self.t_size.lines)]
    
    def insert(self, char, x, y):
        try:
            self.lines[y][x] = char
        except IndexError:
            # If x or y coordinates is bigger than window
            # TODO: consider doing something
            pass
    
    def insert_text(self, text, x, y):
        for pos in range(len(text)):
            self.insert(text[pos], x+pos, y)
    
    def add(self, obj):
        if issubclass(obj.__class__, ScreenObject):
            self.objects.append(obj)
            return True
        else:
            return False


if __name__ == "__main__":
    v = View()
    line = VLine(0.3, 0.2, length=0.5, char="X")
    v.add(line)
    line = HLine(0.3, 0.2, length=0.5, char="X")
    v.add(line)
    line = HLine(0.3, 0.7, length=0.5, char="X")
    v.add(line)
    line = VLine(0.8, 0.2, length=0.5, char="X")
    v.add(line)
    while True:
        v.render()
        time.sleep(1)
    
