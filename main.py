from string import Template
from bank import Bank

account = Bank('Bank')
account.addMoneY(100, "salary")
account.addMoneY(-50, "haircut")
account.printHistory()