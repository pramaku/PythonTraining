class Person:
    def __init__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def __str__(self):
        return "Person({0}, {1}, {2})".format(self.fname, self.lname, self.email)

    def fullName(self):
        return self.fname + ' ' + self.lname

    def getEmail(self):
        return self.email

class Employee(Person):
    def __init__(self, fname, lname, email, empId, sal):
        Person.__init__(self, fname, lname, email)
        self.empId = empId
        self.sal = sal

    def getSalary(self):
        return self.sal

    def __str__(self):
        return "Employee({0}, {1}, {2})".format(Person.__str__(self), self.empId, self.sal)

p = Employee('abc', 'xyz', 'abc@xyz.com', 100, 12000)
print p
print p.fullName()
print p.getSalary()
