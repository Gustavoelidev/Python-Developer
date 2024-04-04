class Animal:
    name = ""
    size = ""
    color = ""

    def eat(self):
        print("Animal se alimentando")

class Horse(Animal):
    race = ""

    def escape(self):
        print("Cavalo fugiu")

class Lion(Animal):
    mane = True

    def hund(self):
        print("Leão cacando")


h = Horse()
h.name = "Carpeando"
h.escape()
h.eat()

l = Lion()
l.name = "Lion"
l.color = "marrom"
l.hund()
l.eat()