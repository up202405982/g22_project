# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 12:46:51 2025

@author: admin
"""

# Class Person - generic version with inheritance
from classes.gclass import Gclass
class Powerplant(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # Attribute names list, identifier attribute must be the first one and callled 'id'
    att = ['_id','_name','_capacity','plant_type', '_operator.id']
    # Class header title
    header = 'Powerplant'
    # field description for use in, for example, input form
    des = ['Id','Name','Capacity','Plant_type', 'Operator_Id']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, name, capacity, plant_type, operator_id):
        super().__init__()
        # Object attributes
        id = Powerplant.get_id(id)
        self._id = id
        self._name = str(name)
        self._capacity = int(capacity)
        self._plant_type = str(plant_type)
        self._operator_id = int(operator_id)
        # Add the new object to the dictionary of objects
        Powerplant.obj[id] = self
        # Add the id to the list of object ids
        Powerplant.lst.append(id)
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
    
    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity 
    
    @property
    def plant_type(self):
        return self._plant_type
    
    @plant_type.setter
    def plant_type(self, plant_type):
        self._plant_type = plant_type
        
    @property
    def operator_id(self):
        return self._operator_id
    
    @operator_id.setter
    def operator_id(self, operator_id):
        self._operator_id = operator_id
    
