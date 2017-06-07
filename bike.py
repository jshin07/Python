class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print "This bike is ${}, can go up to {}, and has {} miles so far.".format(self.price, self.max_speed, self.miles)
        return self

    def ride(self):
        print "Riding: ", self.miles + 10 , "miles"
        return self

    def reverse(self):
        print "Reversing" ,self.miles - 5 , "miles"


bike1= Bike(200,"50mph")
bike2= Bike(50,"10mph")
bike3= Bike(1000,"100mph")

bike1.displayInfo().ride().ride().ride().reverse()
bike2.displayInfo().ride().ride().reverse()
bike3.displayInfo().ride().reverse()
