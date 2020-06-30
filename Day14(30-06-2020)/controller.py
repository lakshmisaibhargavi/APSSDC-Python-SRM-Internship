from package import math1
from package.math2 import isEven,isOdd
from package import math2 as m2

#print(dir(math1))

#print('add=',math1.add(5,25))
#print('sub=',math1.sub(56,54))

#print(isEven(14))
#print(isOdd(45))
obj = m2.MyLogics

print(obj.isPrime(53))
