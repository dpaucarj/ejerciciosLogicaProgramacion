class factorial:
    def __init__(self):
        pass

    def calcularFactorial(self):
        num=int(input("ingrese numero:"))
        i=1
        for i in range(1,num+1):
            num1=int(input("ingrese numero1:"))
            fact=1
            j=1
            for j in range(1,num1+1):
                fact=fact*j
            #print("el factorial del numero:", num, "es", fact)
            print("el factorial del numero{}" "es{}".format(num,fact))
        print("el factorial del numero{}" "es{}".format(num,fact))
facto=factorial()
facto.calcularFactorial()
