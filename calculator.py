a=int(input("enter first number"))
op=input("enter oprator")
b=int(input("enter second number"))

if op=="+":
   print("your addition is",a+b)

elif op=="-":
   print("your substraction is",a-b)

elif op=="*":
   print("your multiplication is",a*b)

elif op=="/":
   #print("division is",a/b)

   if(b==0):
      print("do not divisible by zero")
   else:
      print(a/b) 

else:
   print("invalid number")