# practice sets of loops in python
# Q1>> WAP to print multiplication table of a given number using for loop
"""num=int(input("enter the number"))
for i in range(1,11):
    print(f"{num}X{i}={num*i}")"""
    #Q2>>>WAP to greet all the persons names stored in a list l1 and which starts with s 
    # l1=["raza","sana","fairoz","yousuf"] 
# l1=["raza","sana","fairoz","yousuf"]
# for name in l1:
#     if name.startswith("f"):
#         print("hello" + name)
""" Q3>>>WAP to find whether a given number  is prime or not

"""
num=int(input("enter the number:"))
prime=True
for i in range(2,num):
    if(num%i ==0):
        prime=False
        break
if prime:
    print("this number is prime")
else:
    print("this number is not prime")    

         


