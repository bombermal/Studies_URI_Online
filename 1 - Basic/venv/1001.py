#1001
def func1001():
    a = int(input())
    b = int(input())
    X = a+b
    print("X = "+str(X))

#1002
def func1002():
    pi = 3.14159
    r = float(input())
    print("A=%.4f" % (pi*r**2))

#1003
def func1003():
    a = int(input())
    b = int(input())
    SOMA = a+b
    print("SOMA = "+ str(SOMA))

#1004
def func1004():
    a = int(input())
    b = int(input())
    print("PROD = "+ str(a*b))

#1005
def func1005():
    a = float(input())
    b = float(input())
    print("MEDIA = %.5f" %((a*3.5+b*7.5)/11.))

#1006
def func1006():
    a = float(input())
    b = float(input())
    c = float(input())
    print("MEDIA = %.1f" %((a*2+b*3+c*5)/10.))

#1007
def func1007():
    a  = int(input())
    b  = int(input())
    c  = int(input())
    d  = int(input())

    print("DIFERENCA = %d" %(a*b-c*d))

#1008
def func1008():
    a = int(input())
    b = int(input())
    c = float(input())

    print("NUMBER = %d" % (a))
    print("SALARY = U$ %.2f" %(b*c))

func1008()