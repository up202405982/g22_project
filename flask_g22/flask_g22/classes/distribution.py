from classes.gclass import Gclass
class Distribution(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    att =['_id', '_powerplant_id', '_region_id','_distribution_date', '_energy_supplied']
    header = 'Distribution'
    des = ['Id','PowerplantId','Região','Data da distribuição', 'Energia fornecida']


    def __init__(self, id, powerplant_id, region_id, distribution_date, energy_supplied):
        super().__init__()

        id = Distribution.get_id(id)
        self._id = id
        self._powerplant_id = int(powerplant_id)
        self._region_id = int(region_id)
        self._distribution_date = str(distribution_date)
        self._energy_supplied = int(energy_supplied)

        Distribution.obj[id] = self
        Distribution.lst.append(id)

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def powerplant_id(self):
        return self._powerplant_id
    @powerplant_id.setter
    def powerplant_id(self, powerplant_id):
        self._powerplant_id = powerplant_id
    
    @property
    def region_id(self):
        return self._region_id
    
    @region_id.setter
    def region_id(self, region_id):
        self._region_id = region_id 
    
    @property
    def distribution_date(self):
        return self._distribution_date
    
    @distribution_date.setter
    def distribution_date(self, distribution_date):
        self._distribution_date = distribution_date
        
    @property
    def energy_supplied(self):
        return self._energy_supplied
    
    @energy_supplied.setter
    def energy_supplied(self, energy_supplied):
        self._energy_supplied = energy_supplied
