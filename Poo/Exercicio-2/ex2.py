class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"Produto: {self.nome}, Preco: {self.preco:.2f}"

    def aplicar_desconto(self, percentual_desconto):
        desconto = self.preco * (percentual_desconto / 100)
        preco_final = self.preco - desconto
        return preco_final

produto1 = Produto("Camisa", 10)
print(produto1)

# preco com desconto

preco_com_desconto = produto1.aplicar_desconto(10)
print(f"Preco do produto com desoconto ficará R${preco_com_desconto:.2f}")



# A  classe Produto possui um método construtor __init__ que inicializa os atributos nome e preco do produto.
# O  método __str__ é definido para retornar uma representação em string do objeto Produto.
# O  método aplicar_desconto recebe um percentual de desconto e calcula o preço final com o desconto aplicado.
# Um exemplo de uso da classe é fornecido, onde um objeto Produto é criado, e em seguida, o método aplicar_desconto é chamado para aplicar um desconto de 10% ao preço do produto.