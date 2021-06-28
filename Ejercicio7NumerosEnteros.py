class Enteros:
    def __init__(self):
        pass

    def calcularNumentero (self):
        num1,num2,num3=0,0,0
        num1=int(input("Ingrese numero 1:"))
        num2=int(input("Ingrese numero 2:"))
        num3=int(input("Ingrese numero 3:"))
        if (num1>num2) and (num1>num3):
            numMayor=num1
        else:
            if (num2>num3):
                numMayor=num2
            else:
                numMayor=num3 
                #print("el numero mayor es:", numMayor)   
        print("el numero mayor es:",numMayor)

ent1=Enteros()
ent1.calcularNumentero()                
