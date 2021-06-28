class descuento:
    def __init__(self):
        pass

    def calcular(self):
        tc=float(input("ingrese el valor total:"))
        desc=tc*(15/100)
        tp=tc-desc
        print("Su descuento es:", desc)
        print("Su valor total a pagar es:" , tp)

desc1=descuento()
desc1.calcular()        