class Movie:
    def __init__(self, name, year_launch, include_plan, note, duration_minutes):
        self.name = name
        self.year_launch = year_launch
        self.include_plan = include_plan
        self.total_notas = float(note)  # Inicialmente, total_notas é igual à nota inicial
        self.total_avaliadores = 1  # Inicialmente, um avaliador
        self.duration_minutes = duration_minutes

    def __str__(self):
        return f"Filme: {self.name}"

    def technical_sheet(self):
        print("## Dados do filme ##")
        print(f"Nome do filme: {self.name}")
        print(f"Ano de lançamento: {self.year_launch}")
        print(f"Filme está no plano? {'Sim' if self.include_plan else 'Não'}")
        print(f"Avaliação do filme: {self.total_notas}")
        print(f"Nota média de avaliação: {self.calcular_nota_media():.2f}")
        print(f"Duração do filme: {self.duration_minutes} minutos")
        print(f"Total de avaliadores: {self.total_avaliadores}")

    def avaliar_filme(self, nota):
        if 0 <= nota <= 10:
            self.total_notas += nota
            self.total_avaliadores += 1
            print(f"O filme '{self.name}' foi avaliado com a nota {nota}.")
        else:
            print("A nota deve estar entre 0 e 10.")

    def calcular_nota_media(self):
        return self.total_notas / self.total_avaliadores


# Exemplo de uso:
mario = Movie("Mario", "2002-01-01", True, 5.0, 135)
top_gun = Movie("Top Gun", "2022-01-01", True, 5.0, 300)

# Avaliar um filme
mario.avaliar_filme(7.5)
mario.avaliar_filme(8.0)  # Supondo mais uma avaliação

# Exibir dados do filme
mario.technical_sheet()
