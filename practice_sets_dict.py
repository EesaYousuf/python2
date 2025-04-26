# pratice sets and dictionary
# Q!.WAP to create a dictionary of hindi words with values as their english translation provide user with an option to look it up
"""my_dict={
    "pankha":"fan",
    "dabba":"box",
    "vastu":"items"

}
print("options are",my_dict.keys())
a=input("enter the hindi word\n")
print("the meaning of your word is:",my_dict[a])
# below line will not throw an error if the key is not present in the dictionary
print("the meaning of your word is:",my_dict.get(a))
# Q2.WAP to input eight numbers from the user and display all the unique numbers 
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
num3=int(input("Enter number 3:"))
num4=int(input("Enter number 4:"))
num5=int(input("Enter number 5:"))
num6=int(input("Enter number 6:"))
num7=int(input("Enter number 7:"))
num8=int(input("Enter number 8:"))
s={num1,num2,num3,num4,num5,num6,num7,num8}
print(s)"""
"""# Q3:can we have a set with 18(int) and "18"(str) as a values in it
s={18,"18"}
print(s)
print(len(s))"""
# Q 4.What will be the length of the following set  s,
s=set()
s.add(20)
s.add(20.0)
s.add("20")
print(s)
print(type(s))
print(len(s))
# Q 5.s={} ,what is the type of s
s={}
print(type(s))
# set
s=()
print(type(s))
# Q 6:create an empty dictionary allow 4 frinds to enter their favourite language as values and use keys as their names .assume that the names  are unique
favlang={

}
a=input("Enter your favorite language shubham\n ")
b=input("Enter your favorite language sana\n ")
c=input("Enter your favorite language fairoz\n")
d=input("Enter your favorite language adeeba\n ")
e=input("Enter your favorite language sameer\n ")
favlang['shubham']=a
favlang['sana']=b
favlang['fairoz']=c
favlang['adeeba']=d
favlang['sameer']=e
print(favlang)