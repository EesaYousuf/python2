

# Dictionary in python:Dictionaries are used to store data values in key:value pairs,they are unordered ,mutable(changeable)and dont allow duplicate keys
"""dict={
    "name":"apancollage",
    "subjects":["python","c","java"],
    "topics":("dict","set"),
    "age":35,
    "is_adult":True,
    12.99:40.3
}
print(dict)
print(type(dict))
print(dict["name"])
dict["name"]="fairoz"
print(dict)"""
# nested dictionary
"""student={
    "name":"eesa_yousuf",
    "subjects":{
        "english":30,
        "maths":90,
        "urdu":100,
        "computer":67
    }
}
print(student)
print(student["name"],["maths"])"""
# methods of dictionary
# mydict.keys()..>returns all keys
# mydict.values()..>returns all values 
# mydict.items()..returns all(key,value)pairs as tuples
# mydict.get("key")returns the key according to value
# mydict.update(newdict)inserts the specified items to the dictionary
"""print(student.keys())     
print(list(student.keys()))
print(len(student))
print(student.items)
print(student.get)"""
# WAP to enter marks of 3 subjects from the user and store them in a dictionary .start with an empty dictionary and add one by one ,use subject name as key and marks as value
marks={

}
x=int(input("enter marks of phys:"))
marks.update({"phys:x"})
x=int(input("enter marks of chmistry:"))
marks.update({"chmistry:x"})
x=int(input("enter marks of maths:"))
marks.update({"maths:x"})
x=int(input("enter marks of computer:"))
marks.update({"computer:x"})
print(marks)
