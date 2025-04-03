from classes.gclass import Gclass

import datetime
class Person(Gclass):
    obj = dict()
    lst= list()
    pos=0
    sortkey = ''
    att =['id', 'powerplant_id', 'region_id','distribution_date', 'energy_supplied']
    header = 'Energy'
    des = ('Id', '')

