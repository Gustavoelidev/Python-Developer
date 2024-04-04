class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("O nome deve ser uma string")
        self._name = value

p = Person("Fulano", 12)
print(vars(p))