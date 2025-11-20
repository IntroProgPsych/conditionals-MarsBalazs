# if = does some code only if a condition is true
# Else is going to do nothing

age = int(input("Type you age"))

if age>=18 and age<100:
    print ("You are an adult")
elif age>=100:
   print("You are not human!!!")
elif age<0:
    print("You don't exist!!!")
else:
    print("You are a child")

