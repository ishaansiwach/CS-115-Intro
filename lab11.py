# NAME:     Ishaan Siwach
# PLEDGE:   I pledge my honor that I have abided by the Stevens Honor System


''' CS 115 Fall 2023 - Lab 11'''


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Part 1 
' Implement missing sections of the Car class.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Car(object):
    '''Write the constructor. It should take in four arguments:
       - make (a string, the company name, a.k.a. brand)
       - model (a string)
       - mpg (miles per gallon, a float)
       - tank_capacity (capacity of the gas tank in gallons, a float)
       These should all be assigned to corresponding private fields, i.e., with
       names that start with '__'.  Use the names in the 'str' method provided below.
       '''
    def __init__(self, make, model, mpg, tank_capacity):
        """constructor for the car class with four variables"""
        self.__make=make
        self.__model=model
        self.__mpg=mpg
        self.__tank_capacity=tank_capacity


    '''Write getters for make, model, mpg, and tank_capacity.'''
    # TODO (note: you should have 4 "getter" methods, one for each attribute)

    def get_make(self):
        """returns the make of the car"""
        return self.__make

    def get_model(self):
        """returns the model of the car"""
        return self.__model

    def get_mpg(self):
        """returns the mpg of the car"""
        return self.__mpg

    def get_tank_capacity(self):
        """returns the tank capacity of the car"""
        return self.__tank_capacity


    '''Write setters for mpg and tank_capacity.'''
    # TODO (note: you should have 2 "setter" methods)

    def set_mpg(self, newMpg):
        """sets the mpg of the car"""
        self.__mpg=newMpg
        return

    def set_tank_capacity(self, newTank_capacity):
        """sets the tank capacity of the car"""
        self.__tank_capacity=newTank_capacity
        return


    '''Write a method called get_total_range.
       It returns the total distance the car can travel on a full tank of
       gas.'''
    # TODO
    def get_total_range(self):
        """returns the total distance the car can travel on a full tank of gas"""
        return self.mpg*self.tank_capacity


    def __str__(self):
        '''A string for printing information about a car (DO NOT CHANGE)'''
        return self.__make + ' ' + self.__model + ', MPG: ' + str(self.__mpg) \
            + ', tank capacity: ' + str(self.__tank_capacity)
    


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Part 2 
' Implement missing sections of the HybridCar class. 
' Make HybridCar be a subclass of Car.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class HybridCar(Car):  
    '''Write the constructor. It should take in 6 arguments:
    - the first four are the same as in the Car constructor
    - battery_kWh (battery power in kilowatt-hours, a float)
    - miles_per_kWh (miles per kilowatt-hours, a float)
    The additional fields must be private.
    '''
    def __init__(self,make,model,mpg,tank_capacity, battery_kWh, miles_per_kWh):
        """constructor for the hybrid car class with six variables"""
        Car.__init__(self,make,model,mpg,tank_capacity)
        self.__battery_kWh=battery_kWh
        self.__miles_per_kWh=miles_per_kWh


    '''Implement the following method.'''
    def get_battery_range(self):
        '''Returns the total distance the car can travel on a fully charged
        battery.
        '''
        return self.battery_kWh*self.miles_per_kWh


    '''Override the method get_total_range.
    Returns the total distance the car can travel on a full tank of
    gas and a fully charged battery.
    Do not do any math here except a single +. To get credit, you must call
    the methods you have already written.
    '''
    def get_total_range(self):
        """returns total range of the hybrid car"""
        return self.get_battery_range()+super().get_total_range()


    def __str__(self):
        '''A string for printing information about a car (DO NOT CHANGE)'''
        return super().__str__() + ', battery kWh: ' + \
            str(self.__battery_kWh) + ', miles/kWh: ' + \
            str(self.__miles_per_kWh)
