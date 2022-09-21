class pessoa:
    Nome = ""
    Dia = 0
    Mes = 0
    Ano = 0
    Altura = 0


    def __init__(self):
        print("Preencha os Dados Por Gentileza!!!")

    def mostrarIdade(self):
        print(f"Nome: {self.Nome:}")
        print(f"Data de Nascimento: {self.Dia} / {self.Mes} / {self.Ano}")
        print(f"Altura: {self.Altura}")
        print(f"A pessoa tem {2022-self.Ano} anos.")
       

d1 = pessoa()
d1.Nome = input("Digite o seu nome: ")
d1.Dia = int(input("Digite o dia de Nascimento: "))
d1.Mes = int(input("Digite o Mês de Nascimento:"))
d1.Ano = int(input("Digite o Ano de nascimento: "))
d1.Altura = float(input("Qual a sua altura: "))

d1.mostrarIdade()


