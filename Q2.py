import math
def quadradoP(x):
    s = int(math.sqrt(x))
    return s*s == x
 
def pert(n):
    return quadradoP(5*n*n + 4) or quadradoP(5*n*n - 4)
    
for i in range(1,11):
     if (pert(i) == True):
         print (i,"Pertence a sequência de Fibonacci")
     else:
         print (i,"Não pertence a sequência de Fibonacci")
