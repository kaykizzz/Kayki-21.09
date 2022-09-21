class calculadora:
    valor1 = 0
    valor2 = 0
     
    def soma(self):
        print("SOMA: ",self.valor1 + self.valor2)

    def divisao(self):
        print("DIVISAO: ",self.valor1 / self.valor2)

    def subtracao(self):
        print("SUBTRAÇÃO: ",self.valor1 - self.valor2)

    def multiplicacao(self):
        print("MULTIPLICAÇÃO: ",self.valor1 * self.valor2)

cal1 = calculadora ()

cal1.valor1 = float(input("Informe o valor 1: "))
cal1.valor2 = float(input("Informe o valor 2: "))
print ("[ 1 ] SOMAR")
print ("[ 2 ] SUBTRAIR")
print ("[ 3 ] MULTIPLICAR")
print ("[ 4 ] DIVIDIR")

escolha = int(input("-> "))

if escolha == 1:
    cal1.soma()
elif escolha == 2:
    cal1.subtracao()
elif escolha == 3:
    cal1.multiplicacao()
elif escolha == 4:
    cal1.divisao()
else:
    print("Opção Invalida!")


'''cal1.soma()
cal1.divisao()
cal1.subtracao()
cal1.multiplicacao()'''
