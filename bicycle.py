class Bicycle(object):
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost
        
    def bicycle_details(self):
        return "{0} weighs {1} kilograms and costs ${2} to produce.".format(self.name, self.weight, self.cost)
    
class Bike_Shop(Bicycle):
    def __init__(self, name, inventory, profit):
        self.name = name
        self.inventory = []
        self.profit = 0
        
    def inventory(self):
        print "The {} shop has an inventory of:".format(self.name)
        
        for bike_model in self.inventory:
            print "Name : {}".format(bike_model.name)
            print "-Price: {}".format(bike_model.cost)
            print "-Weight: {} kg".format(bike_model.weight)
        print "\n \n"
		    
        
    
class customer(Bicycle):
    def __init__(self, name, money):
        self.name=name
        self.money = money
