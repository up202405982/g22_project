"""
@author: António Brito / Carlos Bragança
(2025) objective: class Person
"""
# Class Person - generic version with inheritance
from classes.gclass import Gclass
class Region(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
  
    att = ['_id','_name','_area','_population']
   
    header = 'Region'
    
    des = ['Id','Name','Area','Population']

    def __init__(self, id, name, area, population):
        super().__init__()
        id = Region.get_id(id)
        self._id = id
        self._name = name
        self._area = int(area)
        self._population = int(population)

        Region.obj[id] = self
        Region.lst.append(id)
    
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id
   
    @property
    def name(self):
        return self._name    
    @name.setter
    def name(self, name):
        self._name = name
 
    @property
    def area(self):
        return self._area
    @area.setter
    def area(self, area):
        self._area = area
   
    @property
    def population(self):
        return self._population
    @population.setter
    def population(self, population):
        self._population = population

