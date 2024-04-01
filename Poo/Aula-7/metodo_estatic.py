"""
1 - O método estático não possui o parâmetro self.
2 - O método de classe pode acessar mas não pode modificar o estado da classe
3 - Usamos o decorator @staticmethod em python para criar um método estático
"""

class  Language:
    def __init__(self, nome, trail):
        self.nome = nome
        self.trail = trail

    @staticmethod
    def courses_trail(trail):
        if trail == "Python Fundamentos":
            courses = ["Dominio de Python", "Modulos e pip"]
        elif trail == "Automacao com o python":
            courses = ["Automacao de tarefas", "Web e Scraping"]
        else:
            courses = ["A definir"]
        return courses

print(Language.courses_trail("Python Fundamentos"))
print(Language.courses_trail("Automacao com o python"))
print(Language.courses_trail("Analise de dados"))