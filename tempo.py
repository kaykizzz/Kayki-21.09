class tempo:
    def __init__(self, hora=0, minuto = 0, segundo = 0):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

        print(f'TEMPO: {self.hora} : {self.minuto} : {self.segundo} ')
hora1 = int(input("Hora: "))

t = tempo(hora1,29,50)