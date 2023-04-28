def count_values():
       x=0
       while x<50:
             x+=1
             if x %1==x:
                   continue
             print(x)


       
def add_number():
 newnum =int(input("43")) 
 if isprime(newnum):
      print(newnum,"is prime")  
 else:
      print(newnum,"is not prime") 




List = [1,2,3,4,5,6,7,8,9]
sums = 0
for i in List:
    if i % 2 == 0 : 
        sums += i
print(sums)  



a = 7
b = 4

if a % b == 0:
    print(a, "is divisible by", b)
else:
    print(a, "is not divisible by", )