#! /usr/bin/env python3

import math

class ScreenObject:
    """A general object to be drawn onto screen
    
    Attributes:
        x:
        y:
            x,y float in range [0,1] when abs_pos == False
            x,y integer in range [0, screen-size] when abs_pos == True
        rel_corner: {"top-left", "top-right", "bottom-left", "bottom-right"}
            Defines what corner the position should be based from
        abs_pos: Boolean
            True if position is absolute
            False if position is portion of screen width/height
    """
    
    def __init__(self, x, y, abs_pos=False, rel_corner="top-left"):
        self.x, self.y = x, y
        self.abs_pos = abs_pos
        self.rel_corner = rel_corner
    
    def get_startpos(self, width, height):
        """Returns start position of object based on attributes"""
        if self.abs_pos:
            x = self.x
            y = self.y
        else:
            x = round(self.x * width)
            y = round(self.y * height)
        
        if self.rel_corner == "top-right":
            x = width - x
        elif self.rel_corner == "bottom-left":
            y = height - y
        elif self.rel_corner == "bottom-right":
            x = width - x
            y = height - y
        
        return x, y
            


class HLine(ScreenObject):
    """A horizontal line object"""
    
    def __init__(self, x, y, char="-", length=0, full_width=False, 
                 abs_pos=False, rel_corner="top-left", abs_length=False):
        super().__init__(x, y, abs_pos, rel_corner)
        
        self.char = char
        self.length = length
        self.full_width = full_width
        self.abs_length = abs_length
    
    def draw(self, lines):
        width = len(lines[0])
        height = len(lines)
        x, y = self.get_startpos(width, height)
        
        if self.abs_length:
            length = self.length
        else:
            length = round(self.length * width + 0.5)
        print(x, y, length)
        if self.full_width:
            lines[y] = [self.char for i in range(width)]
        else:
            try:
                for i in range(length):
                    lines[y][x+i] = self.char
            except IndexError:
                # IndexError raised if length surpasses screen size
                pass


class VLine(ScreenObject):
    """A vertical line object"""
    
    def __init__(self, x, y, char="|", length=0, full_height=False,
                 abs_pos=False, rel_corner="top-left", abs_length=False):
        super().__init__(x, y, abs_pos, rel_corner)
        
        self.char = char
        self.length = length
        self.full_height = full_height
        self.abs_length = abs_length
    
    def draw(self, lines):
        width = len(lines[0])
        height = len(lines)
        x, y = self.get_startpos(width, height)
        
        if self.abs_length:
            length = self.length
        else:
            length = round(self.length * height + 0.5)
        print(x, y, length)
        if self.full_height:
            for i in range(height):
                lines[i][x] = self.char
        else:
            try:
                for i in range(length):
                    lines[y+i][x] = self.char
            except IndexError:
                pass




