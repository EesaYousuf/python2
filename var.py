# data types in python
# integers,string,flot,boolean,none these are called primary datatypes
name="eesa"
age=24
price=30
print(type(name))
print(type(age))
print(type(price))
# string can be represented in three ways
name1='sk'
name2='''sk'''
name3="sk"
print(name1)
print(name2)
print(name3)
# Boolen datadype
age=23
old=False
a=None
print(type(old))
print(type(a))
# keywords:keywords are reserved words in python
# python is a case sensitive 
# print sum of two numbers
a=10
b=10
sum=(a+b)
print(sum)
# Expression Execution:string & Numeric values can operate together with *(repeation)
A,B=2,3
Txt="@"
print(Txt)
print(2*Txt*3)
# String $ string can operate with +(concatenation)
A,B="2",3
text="@"
print((A+text)*B)
# Numeric values can operate with all arithmetic operators
A,B=2,3
c=4
print(A+B*c)
# Arithmetic expression with integer and float will result in float
A,B=10,10.2
c=A*B
print(c)
# Result of division operator with two integers will be float
A,B=1,2
c=A/B
print(c)
# integer division with float and int will give int displayed as float
A,B=1.5,3
c=A//B
print(c,A/B)
# floor gives closest integer ,which is lesser than or equal to the float value
# Result of (A//B)is same as floor (A/B)
A,B=12,5
c=A//B
print(c)
# REmainder is negative when denominator is negative
A,B=-5,2
c=A%B
print(c)

