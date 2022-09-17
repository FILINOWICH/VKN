import math
x = float(input('Введіть Х: '))
y = math.tan(2*x)+math.cos(4*x-math.sqrt(x))-(2/math.pow(math.fabs(x+1)+0.1,1/3))
print(y)
