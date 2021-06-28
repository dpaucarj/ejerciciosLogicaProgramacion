class controlador:
    def __init__(self):
        pass

    def calcularSumaProd(self):
        suma=0
        prod=1
        resp=input("ingrese caracter:")
        while (resp=='N')or(resp=='n'):
            #resp=input("ingrese caracter:")
            num=int(input("ingrese numero:"))
            suma=suma+num
            prod=prod*num
            print("desea continuar S/N")
            resp=input("ingrese caracter:")
        print("total de la suma es :", suma)
        print("total del producto es :", prod)

cal1=controlador()
cal1.calcularSumaProd()