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
    
    def get_coords(self, width, height, x=None, y=None):
        """Returns start position of object based on attributes
        If x and y == None, use self.x and self.y.
        """
        if x == None or y == None:
            x = self.x
            y = self.y
        
        if not self.abs_pos:
            x = round(x * width)
            y = round(y * height)
        
        if self.rel_corner == "top-right":
            x = width - x
        elif self.rel_corner == "bottom-left":
            y = height - y
        elif self.rel_corner == "bottom-right":
            x = width - x
            y = height - y
        
        return x, y
            


class Line(ScreenObject):
    """A general line from (x0, y0) to (x1, y1)"""
    
    def __init__(self, x0, y0, x1, y1, abs_pos=False, rel_corner="top-left", char="O"):
        super().__init__(x0, y0, abs_pos, rel_corner)
        
        self.x1, self.y1 = x1, y1
        self.char = char
    
    def draw(self, lines):
        """When this function is called, it draws the object onto lines
        Read https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm for algorithm
        """
        width = len(lines[0])
        height = len(lines)
        x0, y0 = self.get_coords(width, height)
        x1, y1 = self.get_coords(width, height, self.x1, self.y1)
        
        dx = x1 - x0
        dy = y1 - y0
        
        # For horizontal or vertical lines
        if dy == 0:
            self.draw_hline(lines, x0, y0, x1, y1)
            return
        if dx == 0:
            self.draw_vline(lines, x0, y0, x1, y1)
            return
        
        #x1, y1 = dx, dy
        
        octant = self.find_octant(dx, dy)
        x0, y0 = self.switch_to_octant_zero(octant, x0, y0)
        x1, y1 = self.switch_to_octant_zero(octant, x1, y1)
        
        # Recalculate dx and dy for new coordinates
        dx = x1 - x0
        dy = y1 - y0
        
        D = 2*dy - dx
        y = y0
        for x in range(x0, x1):
            real_x, real_y = self.switch_from_octant_zero(octant, x, y)
            try:
                lines[real_y][real_x] = self.char
            except IndexError:
                # IndexError raised if coordinates outside of lines
                pass
            
            if D >= 0:
                y = y + 1
                D = D - dx
            D = D + dy
    
    def draw_hline(self, lines, x0, y0, x1, y1):
        if x1 > x0: d = 1
        else: d = -1
        try:
            for x in range(x0, x1+d, d):
                lines[y0][x] = self.char
        except IndexError:
            pass
    
    def draw_vline(self, lines, x0, y0, x1, y1):
        if y1 > y0: d = 1
        else: d = -1
        try:
            for y in range(y0, y1+d, d):
                lines[y][x0] = self.char
        except IndexError:
            pass
    
    def find_octant(self, x, y):
        """Find what octant (x, y) is in"""
        if x > 0 and y > 0:
            if x >= y: 
                return 0 # First octant
            else:
                return 1 # Second octant
        if x < 0 and y > 0:
            if y > -x:
                return 2 # Third octant
            else:
                return 3 # Fourth octant
        if x < 0 and y < 0:
            if -x > -y:
                return 4 # Fifth octant
            else:
                return 5 # Sixth octant
        if x > 0 and y < 0:
            if -y > x:
                return 6 # Seventh octant
            else:
                return 7 # Eight octant
    
    def switch_to_octant_zero(self, octant, x, y):
        """Switches (x, y) from current octant to first octant"""
        if octant == 0: return x, y
        if octant == 1: return y, x
        if octant == 2: return y, -x
        if octant == 3: return -x, y
        if octant == 4: return -x, -y
        if octant == 5: return -y, -x
        if octant == 6: return -y, x
        if octant == 7: return x, -y
    
    def switch_from_octant_zero(self, octant, x, y):
        """Switches (x, y) from first octant to original octant"""
        if octant == 0: return x, y
        if octant == 1: return y, x
        if octant == 2: return -y, x
        if octant == 3: return -x, y
        if octant == 4: return -x, -y
        if octant == 5: return -y, -x
        if octant == 6: return y, -x
        if octant == 7: return x, -y



class Rect(ScreenObject):
    """A rectangle with corners defined by (x0, y0) and (x1, y1)"""
    
    def __init__(self, x0, y0, x1, y1, abs_pos=False, rel_corner="top-left", char="O"):
        super().__init__(x0, y0, abs_pos, rel_corner)
        
        self.x1, self.y1 = x1, y1
        self.char = char
        self.lines = []
        
        # Define lines
        line_coords = [(x0, y0, x1, y0),
                       (x1, y0, x1, y1),
                       (x1, y1, x0, y1),
                       (x0, y1, x0, y0)]
        for c in line_coords:
            line = Line(c[0], c[1], c[2], c[3], abs_pos, rel_corner, char)
            self.lines.append(line)
        
    def draw(self, lines):
        for line in self.lines:
            line.draw(lines)



class Text(ScreenObject):
    """A text field"""
    
    def __init__(self, x, y, text, abs_pos=False, rel_corner="top-left"):
        super().__init__(x, y, abs_pos, rel_corner)
        
        self.text = text
    
    def draw(self, lines):
        length = len(self.text)
        width = len(lines[0])
        height = len(lines)
        
        x, y = self.get_coords(width, height)
        
        for i in range(length):
            try:
                lines[y][x+i] = self.text[i]
            except IndexError:
                pass
            
