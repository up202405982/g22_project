# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 15:22:58 2025

@author: up202406018
"""

# Class Person - generic version with inheritance
from classes.gclass import Gclass
class GridOperator(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # Attribute names list, identifier attribute must be the first one and callled 'id'
    att = ['_id','_name','contact']
    # Class header title
    header = 'GridOperator'
    # field description for use in, for example, input form
    des = ['Id','Name','Contact']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, name, contact):
        super().__init__()
        # Object attributes
        id = GridOperator.get_id(id)
        self._id = id
        self._name = name
        self._contact = contact
        
        # Add the new object to the dictionary of objects
        GridOperator.obj[id] = self
        # Add the id to the list of object ids
        GridOperator.lst.append(id)
    # id property getter method
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id
    # name property getter method
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    # dob property getter method
    @property
    def contact(self):
        return self._contact
    # dob property setter method
    @contact.setter
    def contact(self, contact):
        self._contact = contact
    # contact property getter method
    
   