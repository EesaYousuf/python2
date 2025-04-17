# lists in python
"""""
A built in data type that stores set of values
it can store elements of different types(integer,float,string,etc)
string ...are immutable
lists >>mutable

    """
# Example of lists
student=["eesa",89.4,17,"odina"]
print(student)
marks=[90,50,70,78,99,100]
print(marks[1:4])
list1=[1,2,3,4,5]
list2=["one","two","three"]
list3=[True,False]
list4=[5j,1+2]
print(type(list1))
print(type(list2))
print(type(list3))
print(type(list4))
# properties of lists
print(list1[0])
print(list2[0:1])
print(list3[:2])
# palindrome program
li=[1,2,3]
li1=[3,1,2]
copy_li=li.copy()
copy_li.reverse()
if(copy_li==li):
    print("palindrome")
else:
    print("not palindrome")    
