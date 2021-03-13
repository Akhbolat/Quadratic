from math import*              # import th
def quadratic(a,b,c):
      D=b*b-4*a*c
      x1= (-b+sqrt(D))/(2*a)
      x2= (-b-sqrt(D))/(2*a)
      return x1, x2;

a1=int(input('Enter the A:'))
b1=int(input('Enter the B:'))
c1=int(input('Enter the C:'))

result=quadratic(a1,b1,c1)
print('Result', result)