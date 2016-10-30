#! /usr/bin/env python3

class City:
    def __init__(self, city_name):
        self.city_name = city_name

class CityList:
    def __init__(self):
        self.clist = {}

    def add_city(self, name):
        self.clist[name] = City(name)

    def remove_city(self, name):
        if name in self.clist:
            del self.clist[name]

    def get_city(self, name):
        return self.clist[name]

    def get_list(self):
        return self.clist
