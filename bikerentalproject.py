class BikeShop:

    def __init__(self,stock):
        self.stock=stock
    def displayBike(self):
        print("Total Bikes",self.stock)
    def rentForBike(self,q):
        if q<=0 : 
                print("Enter the Positive Value or greater then zero")
        elif q>self.stock :
                 print("Enter the Value (less then stock)")
        else :
            self.stock=self.stock-q
            print("Total price",q*1000)
            print("Total Bike",self.stock)
while True:
    obj=BikeShop(1000)
    uc=int(input('''
1 Display Stocks
2 Rent a Bike
3 Exit
'''))
    if uc==1:
        obj.displayBike()
    elif uc==2:
         n=int(input("Enter the Qty:  "))
         obj.rentForBike(n)
    else:
        break
            
    
    
    

            
             
