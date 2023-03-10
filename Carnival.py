class person:
    def __init__(self, first, last, ticket, attendance = False):
        self.firstName = first
        self.lastName  = last
        self.ticket = ticket
        self.attend = attendance
    def hasBeen(self, attendance):
        if self.attend == True:
            return f"{self.firstName} {self.lastName} has already attended the carnival."
        else:
            return f"{self.firstName} {self.lastName} hasn't attended the carnival."

    def isStudent(self, tof):
        if tof == True:
            self.ticket = 5

    def isSenior(self, tof):
        if tof == True:
            self.ticket = 0
    
    def __str__(self):
        return f"{self.firstName} {self.lastName} has a ticket price of ${self.ticket}"

def instance():
    first = input("First name: ")
    last = input("Last name: ")
    isStu = input("Is he/her a currently enrolled student? (y/n): ").lower()
    if isStu == 'y':
        isStu = True
    else:
        pass
    isSen = input("Is he/her a senior citizen? (y/n): ").lower()
    if isSen == 'y':
        isSen = True
    else:
        pass 
    attend = input("Has he/she been to the carnival already? (y/n): ").lower()
    if attend == 'y':
        attend = True
    else:
        pass
    ticketDefault = 10
    MyPerson = person(first, last, ticketDefault, attend)
    print(str(MyPerson))
    MyPerson.isStudent(isStu)
    print(str(MyPerson))


instance()