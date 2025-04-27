# WAP to find out whether a given name is present in a list or not
names=["eesa","sana","nasir","sameer","adeeba","samia","hadii","sanakhan"]
name=input("enter the name to check \n")
if name in names:
    print("your name is present in the list")
else:
    print("your name is not prsent in the list") 
    #WAP to calculate the grade of a student from his marks from the following schema
    # 90-100 -->EX
    # 80-90 -->A
    # 70-80 -->B
    # 60-70 -->C
    # 50-60 -->D
    # <50   -->f
marks=int(input("Enter your mars\n"))
if marks>=90:
    grade="EX"
elif marks>=80:
    grade="A"
elif marks>=70:
    grade="B"
elif marks>=60:
    garde="C"                   
elif marks>=50:
    garde="D "
else:
    grade="fail"
print("your grade is"+  grade )   

                        
