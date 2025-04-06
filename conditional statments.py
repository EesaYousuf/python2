# conditional statements in python
# if_elif_else(syntax)
"""if(condition):
    statement1
elif(conditin):
    statement2
else:
    statementN   """    
# Traffic lights code
"""light=input("light:")
if(light=="red"):
    print("stop")
elif(light=="yellow"):
    print("look")
elif(light=="green"):
    print("you can go")
else:
    print("light is broken")  """
    # Grade of students
"""marks=int(input(" marks:"))
if(marks>=90):
    print("A")
elif(marks>=80 and marks<90):
    print("B")
elif(marks>=70 and marks<80):
    print("C")
else:
    print("D")"""
    # Clever if/ ternary operator
    # syntax
    # <var>=(False_val,True_val)[condition]
# example
# age=int(input("age:"))
# vote=("yes","no")[age>=18]
# print(vote)

# Example2
# salary=float(input("salary:"))
# tax=salary*(0.1,0.2)[salary>=50000]
# print(tax)
# calculate simple intrest
"""a=float(input("a:"))
b=float(input("b:"))
c=float(input("c"))
print(a*b*c/100)"""
p=float(input("p:"))
r=float(input("r:"))
t=float(input("t:"))
si=(p*r*t)/100
print(si)

