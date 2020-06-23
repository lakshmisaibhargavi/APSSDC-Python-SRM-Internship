'''a=int(input("enter a value"))
if a>0:
    print("the given number is positive number")
elif a==0:
    print("the value is zero")
else:
    print("the given number is negative number")
#check weather the given number even or odd
n=int(input("enter a value"))
if n%2==0:
    print("even")
else:
    print("odd")

#check given year is leap year or not
year=int(input("enter the year"))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("is a leap year")
       else:
           print("not a leap year")
   else:
       print("is leap")
else:
   print("not leap")

if (year%4==0 and year%100!=0)or(year%400==0):
    print("it is leap year")
else:
    print("it is not a leap year")

#check if the given number is factor of 1000
a = int(input("enter a value"))
if 1000%a==0:
    print("factor")
else:
    print("not a factor")

#check which is the largest number among 3 numbers

a,b,c = map(int,input().split())
print(max(a,b,c))'''
#check the given number is in the range between 100 and 1000
a=int(input("enter the value"))
if a>=100 and a<=1000:
    print("number is present")
else:
    print("number is not present")
























