#! /usr/bin/env python3

class City:
    def __init__(self, city_name):
        self.city_name = city_name

class CityList:
    def __init__(self):
        self.clist = []

    def add_city(self, name):
        self.clist.append(name)

    def remove_city(self, name):
        if name in self.clist:
            self.clist.remove(name)

    def get_list(self):
        return self.clist
