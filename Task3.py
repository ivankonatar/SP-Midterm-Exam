
class Person():
    def __init__(self, name, surname, date_of_birth, address):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.address = address

    def __str__(self):
        return " Ja se zovem {0} {1} ".format(self.name, self.surname)

class Employee(Person):
    def __init__(self, name, surname, date_of_birth, address, company, position, years_employed, base_salary ):
        Person.__init__(self, name, surname, date_of_birth, address)
        self.company = company
        self.position = position
        self.years_employed = years_employed
        self.base_salary  = base_salary
    def __str__(self):
        return " company {0} position {1} ".format(self.company, self.position)

    def get_salary(self):
        return "Plata zaposlenog " + str(
            int(Employee(Person).base_salary) + int(self.base_salary)/100*int(self.years_employed)) + "EUR."
    def get_tax(self):
        return "Bruto plata:"+ str(self.get_salary()+self.get_salary()/100*70)

Osoba_01= Person("Ivan","Konatar","11.05.1995.","Podgorica")