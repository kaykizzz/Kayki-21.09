class bola:
    cor = ""
    circ = 0
    material = ""
    def mostrarCor(self):
        print("="*30)
        print(f'  COR: {self.cor}')
        print("="*30)

    def calc(self, raio):
        self.circ = (raio**2) * 3.14
        print(f'Circunferência: {self.circ} cm')
b1 = bola()
b1.mostrarCor()
Valor = float(input("Informe o valor do raio: "))
b1.calc(valor)



