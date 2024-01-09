from datetime import date

def newAction(amount, reason):
    return {
        "date": date.today(),
        "amount": amount,
        "reason": reason
    }

class Bank():
    def __init__(self, name):
        self.name = name
        self.total = 0
        self.actions = []

    def addMoneY(self, amount, reason):
        """
            This function add/removes money
             parameters: amount-> the amount we add,  reason -> the reason of the action 
        """
        self.total += amount
        self.actions.append(newAction(amount, reason))

    def printHistory(self):
        for action in self.actions:
            print(action["date"], ' ', action["amount"], ' ', action["reason"], '\n' )


