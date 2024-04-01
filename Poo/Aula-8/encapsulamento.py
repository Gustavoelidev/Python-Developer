class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def show(self):
        print(f"Name: {self.name}, Salary: {self.__salary}")

fulano = Employee("Fulano", 5000)
fulano2 = Employee("Fulano2", 4000)
fulano.__salary = 40000
fulano.show()
fulano2.show()