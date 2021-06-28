class primo:
    def __init__(self):
        pass

    def NumeroPrimo(self):
        primo=True
        divisor=2
        num=int(input("ingrese numero:"))
        while ((divisor<num)and(primo)):
            res=0
            if res <=0:
                primo=False
            divisor=divisor+1
        if primo>=0:
            print("el numero", num ,"es primo")
        else:
            print ("el numero", num ,"no es primo")         

prim1=primo()
prim1.NumeroPrimo()              





        
             
        
