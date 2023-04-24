class Factura:
    numar_curent = 1

    def __init__(self, valoare_factura, ) -> None:
        self.__numar = Factura.numar_curent
        self.valoare_factura = valoare_factura
        Factura.numar_curent += 1

    @property
    def numar(self):
        return self.__numar


p1 = Factura('200')
p2 = Factura('100')
print(p1.numar)
print(p2.numar)
