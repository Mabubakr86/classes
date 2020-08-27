class Field:
    concession = 'South Gharieb'

    def __init__(self, name, prod, wc, area):
        self.name = name
        self.prod = prod
        # validation in constructor
        if wc > .9:
            raise ValueError('Ask FM')
        self._wc = wc  
        self._area = area

    def calc_net(self):
        return self.prod * self._wc

    @classmethod
    def add_age(cls, year):
        return cls.concession + f' since {year}'

    @classmethod
    def form_name(cls,letters,prod,wc,area):
        new_name = ''.join(letters)
        return cls(name=new_name, prod=prod, wc=wc,area=area)

    @staticmethod
    def prod_in_m3(bbls):
        return bbls/6.29

    @property           #getter decorator
    def area(self):
        return self._area
    @area.setter        #setter decorator
    def area(self,value):
        if value < 1000:
            raise ValueError('It is Too Small')
        elif value > 100000:
            raise ValueError('It is too large')
        self._area = value

    @property
    def wc(self):
        return self._wc
    @wc.setter
    def wc(self, value):
        if value > .9:
            raise ValueError('Ask Field Manager')
        self._wc = value





if __name__ == '__main__':
    #create object instance from constructor (which call init)
    hana = Field('hana', 700, .6, 2000)

    #create object instance from class method factory
    hoshia = Field.form_name(['h','o','sh','ia'], 500,.56, 1500)

    #accessing attributes , methods (instance, class, static)
    print(hoshia.name)
    print(hoshia.calc_net())
    print(hoshia.add_age('2000'))
    print(Field.prod_in_m3(hoshia.prod))

    #controlling area attribute assignment through setter property 
    # hoshia.area = 2
    # hoshia.area = 2000000
    hoshia.area = 2000
    print(hoshia.area)    #note that now area (not _arae) is an attribute due to properrty 

    #controlling wc attribute assignment through constructor validation
    # fadl = Field('fadl', 100, .99, 750)

    #controlling wc attribute assignment through setter property
    fadl = Field('fadl', 100, .67, 750)
    # fadl.wc = .99

  