# practice set on conditional statements
"""Q1..WAP to find greatest of four numbers entered by the user"""
"""num1=int(input("enter first number from the 1:"))
num2=int(input("enter first number from the 2:"))
num3=int(input("enter first number from the 3:"))
num4=int(input("enter first number from the 4:"))
num5=int(input("enter first number from the 5:"))
if(num1>num4):
    f1=num4
else:
    f2=num2
if(num2>num3):
    f1=num2
else:
    f2=num1
if(f1>f2):
    print(str(f1) +"is greatest")
else:
    print(str(f2) + "is greatest")   """  

# WAP  to find out whether a student is pass or fail,if it requries total 40% and at least 33% in each subject to pass .assume 3 subjects and take marks as an input from the user
sub1=int(input("enter first subject marks\:"))
sub2=int(input("enter 2nd subject marks\:"))
sub3=int(input("enter third subject marks\:"))
sub4=int(input("enter forth subject marks\:"))

if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail because you have less than 33% in one of the subject") 
elif(sub1+sub2+sub3)/3 <40:
        print("you are fail due to total percentage less than 40")
else:
      print("congatulation! you passed the exam")
      





