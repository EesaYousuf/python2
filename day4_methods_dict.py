
# Methods in dectionary

mydict={
    "Name":"My name is eesa",
    "Enrolment_no":30,
    "Batch_no":2024,
    "enrolled_course":"M.ech(AI)",
    "coding_skills":["c programming","dot_net","web_development","python","java","c++","Machine_learning","computer_vesion"],
    "Email":"eesayousufyousuf@gamil.com",
    "Pass_Word":"eesa@123",
    "pincode_no":193121,
    "userName":"eesa@123",
    "Another_dict":{
        "Name":"fairoz",
        "position":"web_developer",
        "company_name":"google",
        "Salary":5000000,
        "coding_skills":"python",
        "email":"fairozahamad@353gmail.com",
        "pass_word":"@eesafairoz123",
        "place":"USA"
    }
}
# print(mydict["coding_skills"][0])
# print(mydict["Pass_Word"])
# prints  the keys of the dictionary
print(type(mydict.keys())) 
# prints the keys of the dictionary
print(list(mydict.values()))
# prints the (key,value)for all contents of the dictionary
print(mydict.items())
print(mydict)
updatedict={
    "sameer":"friend",
    "sana":"sister",
    "deeba":"friend",
    "adeeba":"calssmate"
}
mydict.update(updatedict)
print(mydict.get("sameer"))
