#! /usr/bin/env python3

import os
import shutil
import time
from screen_objects import *

class View:
    """View class for containing objects on terminal"""
    def __init__(self):
        self.lines = []
        self.refresh_terminal_size()
        self.objects = []
    
    def refresh_terminal_size(self):
        """Update attribute with terminal size"""
        self.t_size = shutil.get_terminal_size()
    
    def render(self):
        """Update terminal size, redraw every object, and print the view.
        Will return input from user if Input object exists.
        """
        self.refresh_terminal_size()
        self.populate_lines()
        #print("Terminal size: %i x %i" %(self.t_size[0], self.t_size[1]))
        
        for obj in self.objects:
            obj.draw(self.lines)
        
        for line in self.lines:
            for char in line:
                if char != "input":
                    print(char, end="")
                else:
                    return input()
            print() # print newline
        
    def populate_lines(self, char=" "):
        """Recreate self.lines based on terminal size"""
        self.lines = [[char for x in range(self.t_size.columns)] for y in range(self.t_size.lines)]
    
    def add(self, obj):
        """Add new object to be showed on view. Will return result"""
        if issubclass(obj.__class__, ScreenObject):
            self.objects.append(obj)
            return True
        else:
            return False
    
    def remove(self, obj):
        """Remove object from view. Will return result"""
        if obj in self.objects:
            self.objects.remove(obj)
            return True
        return False
        


if __name__ == "__main__":
    v = View()
    line = Line(0.3, 0.2, 0.3, 0.7, char="X")
    v.add(line)
    line = Line(0.3, 0.2, 0.8, 0.2, char="X")
    v.add(line)
    line = Line(0.3, 0.7, 0.8, 0.7, char="X")
    v.add(line)
    line = Line(0.8, 0.2, 0.8, 0.7, char="X")
    v.add(line)
    line = Line(0.8, 0.7, 0.3, 0.2, char="X")
    v.add(line)
    line = Line(0.8, 0.2, 0.3, 0.7, char="X")
    v.add(line)
    line = Line(2, 2, 8, 8, char="O", abs_pos=True)
    v.add(line)
    rect = Rect(0.1, 0.1, 0.9, 0.9, char="I")
    v.add(rect)
    text = Text(0.15, 0.15, "Hello, World")
    v.add(text)
    inp = Input(0.5, 0, "test$")
    v.add(inp)
    while True:
        v.render()
        time.sleep(1)
    
