class Product(object):
    def __init__(self, price, item_name, weight, brand, cost):
        self.price = price
        self.item_name =item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"


    def displayInfo(self):
        print "Price:" , self.price
        print "Item Name:" , self.item_name
        print "Weight:" , self.weight
        print "Brand:" , self.brand
        print "Cost:" , self.cost
        print "Status:", self.status
        return self

    def sell(self):
        self.status = "sold"
        return self

    def tax(self, taxRate):
        self.price = int(self.price * (1+(0.01*taxRate)))
        return self

    def return_item(self, reason):
        if (reason == "defective"):
            self.status = "defective"
            self.price = 0
        elif (reason == "in_box"):
            self.status = "for sale"
        elif (reason == "opened"):
            self.status = "Used"
            self.price *= .20
        return self


product1= Product(30, "Belt", "3 lbs", "Gap", 5)
product2= Product(5, "Flip Flops", "2 lbs", "Street", 1)
product3= Product(100, "Bag", "5 lbs", "Channell", 10)

##TEST##
# product1.displayInfo()
# product2.tax(10).displayInfo()
# product2.return_item("defective").displayInfo()
# product3.tax(5).displayInfo()
# product2.sell().displayInfo()
