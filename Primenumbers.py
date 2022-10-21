name = input("\n Enter your Name: ")
print(" What's up " + name + "!" '\n')
count=0
A=int(input(" Please enter a number: "))
for i in range (1,A+1):
 if A%i ==0:
    count+=1
if count ==2:
      print("\n Entered number is prime! \n")
else:
    print("\n Entered number is not a prime! \n")