import math
def func(x0,x1):
    U = x0*math.log(x1,math.e)+(1/(math.pow(x0,2)+math.pow(x1,2)+0.3))-math.pow(math.e,6*x0-x1)
    return (U)
x=float(input('Ведіть X: '))
y=float(input('Ведіть Y: '))
U=func(x,y)
print(U)
