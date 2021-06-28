class centinela:
    def __init__(self):
        pass

    def calcularN(self):
        suma,prod=0,1
        num=int(input("ingrese numero: "))
        while num in (num<-1 and num>-1):
            suma=suma+num
            prod=prod*num
            num=int(input("ingrese numero: "))
        print("total de la suma es: ", suma)
        print("total del producto es :", prod)


cent1=centinela()
cent1.calcularN()        

