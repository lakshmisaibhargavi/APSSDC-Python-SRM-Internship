'''for i in range(5,10,3):
    print(i)
for i in "apssdc":
    print(i,end="")
#to find number of digits in a given number
a="1234"
count=0
for i in a:
    count+=1#count=count+1
print(count)

#print the multiplication table from range between 10 to 20
#ex:5*10=50
#   5*11=
a=int(input("enter the table"))
for i in range(10,21):
    print(a,'*',i,'=',a*i)'''

#iterate the integers from 1 to 50, for multiples of 3 print
#"FIZZ" and mutiples of 5 print "BUZZ"
#and multiples  of both 3 and 5
#print "FIZZBUZZ"

for i in range(1,51):
    if i%3==0 and i%5==0:
        print("for both 3 and 5","FIZZBUZZ")
    elif i%5==0:
        print("for 5 multiples","BUZZ")
    elif i%3==0 :
        print("for both 3 ","FIZZ")
        
    














    
    


    
    
