#! /usr/bin/env python3

class City:
    """A class for city"""
    def __init__(self, city_name):
        self.city_name = city_name

class CityList:
    """A class for containing cities"""
    def __init__(self):
        self.clist = {}

    def add_city(self, city):
        self.clist[city.city_name] = city

    def remove_city(self, name):
        if name in self.clist:
            del self.clist[name]

    def get_city(self, name):
        return self.clist[name]

    def get_list(self):
        return self.clist
