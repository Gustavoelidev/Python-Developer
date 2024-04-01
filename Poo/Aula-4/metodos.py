class Movie:
    def __init__(self, name, yearLaunch, includePlan, note, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includePlan = includePlan
        self.note = note
        self.durationMinutes = durationMinutes

        def __str__(self):
            return f"Filme: {self.name}"

        def techinal_sheet(self):
            print("## Dados do filme ##")
            print(f"Nome do filme: {self.name}")
            print(f"Ano de lancamento: {self.yearLaunch}")
            print(f"Filme está no plano? {self.includePlan}")
            print(f"Avaliacao do filme: {self.note}")
            print(f"Duracao do filme: {self.durationMinutes}")

mario = Movie("Mario", "2002-01-01", True, "5.0", 135)
top_gun = Movie("Top Gun", " 2022-01-01", True, "5.0", 300)

mario.techinal_sheet()
top_gun.techinal_sheet()


