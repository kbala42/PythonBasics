'''
---------------------------------------------------------tw:@tek_elo
Araba sınıfı örneği
get ve set fonksiyonları
--------------------------------------------------------------------
'''
class VehicleRent:

    def __init__(self,stock):
        pass

    def displayStock(self):
        """
            diplay stock
        """
        pass

    def rentHourly(self,n):
        """
            rent hourly
        """
        pass

    def rentDaily(self,n):
        """
            rent daily
        """
        pass

    def returnVehicle(self,request, brand):
        """
            return a bill
        """
        pass

class CarRent(VehicleRent):

    def __init__(self):
        pass

    def discount(self):
        """
            discount
        """
        pass

class BikeRent(VehicleRent):

    def __init__(self):
        pass

class Customer:

    def __init__(self):
        pass

    def requestVehicle(self):
        """
            reuest vehicle
        """

    def returnVehicle(self):
        """
            return vehicle
        """