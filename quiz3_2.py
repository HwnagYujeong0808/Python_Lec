class Wages:
    def __init__(self, name="", hours=0.0, wage=0.0):
        self.name= name
        self.hours = hours
        self.wage = wage

    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setHours(self, hours):
        self.hours = hours
    def getHours(self):
        return self.hours
    def setWage(self, wage):
        self.wage = wage
    def getWage(self):
        return self.wage

    def payForWeek(self):
        amount = self.hours * self.wage
        if self.hours > 40:
            amount = 40 * self.wage +((self.hours-40) * (1.5 * self.wage))
        return '{:,.2f}'.format(amount)

salary = Wages()
name = input('Enter person name: ')
hours = float(input('Enter number of hours worked: '))
wage = float(input('Enter hourly wage: '))

salary.setName(name)
salary.setHours(hours)
salary.setWage(wage)
print('pay for', salary.getName()+':', salary.payForWeek())
