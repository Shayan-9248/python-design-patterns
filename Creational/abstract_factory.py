"""
    Creational:
      - Abstract Factory
            Car => Benz, Bmw => Suv, Coupe
                benz suv => gla, glc
                bmw suv => x1, x2

                benz coupe => cls, e-class
                bmw coupe => m2, m4
"""
# abstract_factory pattern allow us to create object that can be created/
#  in several different ways

from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def call_suv(self):
        pass
    
    @abstractmethod
    def call_coupe(self):
        pass
# --------------------------------------------
class Benz(Car):
    def call_suv(self):
        return Gla()
    
    def call_coupe(self):
        return Cls()


class Bmw(Car):
    def call_suv(self):
        return X1()
    
    def call_coupe(self):
        return M2()
# --------------------------------------------
class Suv(ABC):
    @abstractmethod
    def create_suv(self):
        pass


class Coupe(ABC):
    @abstractmethod
    def create_coupe(self):
        pass
# --------------------------------------------
class Gla(Suv):
    def create_suv(self):
        print('This is your Suv benz gla...')


class X1(Suv):
    def create_suv(self):
        print('This is your suv bmw x1...')
# --------------------------------------------
class Cls(Coupe):
    def create_coupe(self):
        print('This is your coupe benz cls...')


class M2(Coupe):
    def create_coupe(self):
        print('This is your coupe bmw m2...')
# --------------------------------------------
def client_suv(order):
    suv = order.call_suv()
    suv.create_suv()

def client_coupe(order):
    coupe = order.call_coupe()
    coupe.create_coupe()


client_coupe(Benz())
client_suv(Bmw())