class person:
    def __init__(self, first, last, ticket, attendance):
        self.firstName = first
        self.lastName  = last
        self.ticket = ticket
        self.attend = attendance
    def __str__(self):
        return f"{self.firstName} {self.lastName} has a ticket price of ${self.ticket}"
    def hasBeen(self, attendance):
        if self.attend == True:
            return f"{self.firstName} {self.lastName} has already attended the carnival."
        else:
            return f"{self.firstName} {self.lastName} hasn't attended the carnival."

