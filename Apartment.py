class Apartment:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def __str__(self):
        return f"{self.name}'s unit cost is ${self.cost}"
    
    def Taxes(self, cost):
        cost = float(cost) * 1.10
        cost = str(round(cost, 2))
        return f"after taxes this unit will cost ${cost}"
        


def CreateTenets():
    TenetNum = int(input("Hello! How many tenets would you like in your apartment? "))
    MyTenets = {}

    for i in range(TenetNum):
        TenetName = input("Name: ")
        TenetCost = input("Unit Cost: ")
        MyTenets.update({TenetName:TenetCost})

    AllNames = list(MyTenets.keys())
    AllCosts = list(MyTenets.values())

    for i in range(len(AllNames)):
        MyApt = Apartment(AllNames[i], AllCosts[i])
        print(f"{str(MyApt)} and {MyApt.Taxes(cost=AllCosts[i])}")

    
CreateTenets()
    

