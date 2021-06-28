class vector:
    def __init__(self):
        pass
 
    def leerVector(self):
        i=1
        j=1
        k=1
        for i in range(1,20):
            numI=int(input("ingrese numero:"))
            if numI>0:
                AJ=numI
                j=j+1
            else:
                BK=numI
                k=k+1
        for i in range(1,j) :
            print(i)
        for i in range (1,k):
            print(i)

vec1=vector()
vec1.leerVector()


