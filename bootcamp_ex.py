# def parametro(a, b, c):
#     return a + b + c

# if __name__ == '__main__':
#     print(parametro(1, 2, 3))


class Coche():
    def __init__(self):
        self.puertas = 0

    def npuertas(self, puertas):
        self.puertas = puertas
        print('Mi coche tiene {} puertas'.format(self.puertas))
    
miCoche = Coche()
miCoche.npuertas(5)
