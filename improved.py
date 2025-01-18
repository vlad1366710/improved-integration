import math
import numpy 

def f(x):
    return((x+1)/math.sqrt(x*x+1))

def trapesia(a,b,n):
    h = (b-a)/n
    x=a
    s=0
    for i in range(n):
        x=x+h
        s=s+f(x)
    return(h/2*(f(a)+2*s+f(b)))
def simp(a,b,n):
    h = (b-a)/n/2
    x=a
    s=0
    for i in range(2*n):
        x=a+i*h
        if (i%2 ==0):
            s=s+2*f(x)
        else:
            s=s+4*f(x)
    return(h/3*(f(a)+s+f(b)))
def gaus(a,b,n):
    s=0
    m4 = numpy.array([0.347854845, 0.652145155, 0.652145155, 0.347854845]) 
    m5 = numpy.array([0.236926885, 0.478628670, 0.568888889, 0.478628670, 0.236926885]) 
    x4 = numpy.array([-0.861136312, -0.339981044, 0.339981044, 0.861136312]) 
    x5 = numpy.array([-0.906179846, -0.538469310, 0.0, 0.538469310, 0.906179846])
    for i in range(n):
        if (n == 4):
            s += m4[i] * f((b + a) / 2 + (b - a) / 2 * x4[i])
        elif(n == 5):
            s += m5[i] * f((b + a) / 2 + (b - a) / 2 * x5[i])
            
    return (b - a) / 2 * s

if __name__ == "__main__": 
    a=-0.4
    b=1.6
    esp=0.00001

    #метод трапеции
    n=10
    trap_1 = trapesia(a,b,n)
    trap_2 = trapesia (a,b,2*n)
    while(abs(trap_1-trap_2)>esp):
        trap_1=trap_2
        n=n*2
        trap_2=trapesia(a,b,n)

    trap_1 = trap_2
    trap_2 = trapesia(a,b,n*2)
    #рунге
    rezultat = trap_2+(trap_2-trap_1)/3.0
    print('Метод трапеции =',rezultat)
    #формула симпсона
    n=10
    trap_1 = simp(a,b,n)
    trap_2 = simp (a,b,2*n)
    while(abs(trap_1-trap_2)>esp):
        trap_1=trap_2
        n=n*2
        trap_2=simp(a,b,n)

    trap_1 = trap_2
    trap_2 = simp(a,b,n*2)
    #рунге
    rezultat = trap_2+(trap_2-trap_1)/15.0
    print('Формула симпсона =',rezultat)
    print('Формула гауса n=4, =',gaus(a,b,4))
    print('Формула гауса n=4, =',gaus(a,b,5))
    