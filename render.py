#! /usr/bin/env python3

import os
import time


class View:
    
    def __init__(self):
        self.lines = []
        self.update()
    
    def update(self):
        self.t_size = os.get_terminal_size()
    
    def render(self):
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


if __name__ == "__main__":
    v = View()
    v.populate_lines(".")
    v.insert("O", 10, 10)
    v.insert_text("hello", 10, 11)
    v.render()
