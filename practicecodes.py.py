# CHAPTER ONE PRACTICE SET
# PROBLEM-1
STRING = '''TWINKLE TWINKLE LITTLE STAR,
HOW I WONDER WHAT YOU ARE!
UP ABOVE THE WORLD SO HIGH, 
LIKE A DIMOND IN THE SKY.''' 
print(STRING)

# PROBLEM-2 USE OF REPLE TO CREATE A TABLE OF 5
# PROBLEM-3 USE OF A PLAYSOUND MODULE
# PROBLEM-4 USE OF OS MODULE
# *********************************************************************************************

# CHAPTER TWO PRACTICE SET
# PROBLEM-1
a = 10
b = 20
print("The sum of a and b is",a+b)

# PROBLEM-2
num = 15
print("The remainder of given number when divided by 2 is",num%2)

#PROBLEM-3
str = input("Enter your string: ")
print(type(str))

#PROBLEM-4
a = 34
b = 80
print(a>b)

# PROBLEM-5
num1 = int(input("Enter your number1: "))
num2 = int(input("Enter your number2: "))
avg = (num1+num2)/2
print("The average of number1 and number2 is",avg)

# PROBLEM-6
num = int(input("Enter your number: "))
sqrt = num*num
print("The square root of the given number is",sqrt)
#**************************************************************************************

# CHAPTER-3 PRACTICE SET

# PROBLEM-1
name = input("Enter your name: ")
print("Good afternoon,",name)

# PROBLEM-2
letter = '''Dear, <|NAME|>
\tGreetings from Gleam IT Solutions, I am happy to in form you-
You are selected !!

Hopefully your onboarding date will be 21-Feb
Date: <|DATE|>
 '''
name = input("Enter your name: ")
date = input("Enter today's date: ")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)

print(letter)

# PROBLEM-3
str = "Hey this is harsh  wanna talk to you"
print(str.count("  ")) #IT WILL GIVE YOU NUMBERS OF DOUBLESPACES
print(str.find("  ")) #iT WILL GIVE YOU POSITION AT WHERE DOUBLESPACE OCCUR

# PROBLEM-4
str = "Hey this is harsh  wanna talk to you"
str = str.replace("  "," ")
print(str)

str = "Hey this is harsh  wanna talk to you.Hey this is harsh  wanna talk to you.Hey this is harsh  wanna talk to you"
str = str.replace("  "," ")
str = str.replace("harsh","akriti")
print(str)

# PROBLEM-5 FORMATING LETTER USING ESC
# letter = "Dear Harsh, This python requirement is good for you.Thankyou!!"
letter = "Dear Harsh,\n\t This python requirement is good for you.\nThankyou!!"
print(letter)
# ************************************************************************************************

# CHAPTER-4 PRACTICE SET
# PROBLEM-1

f1 = input("Your fruit: ")
f2 = input("Your fruit: ")
f3 = input("Your fruit: ")
f4 = input("Your fruit: ")
f5 = input("Your fruit: ")
f6 = input("Your fruit: ")
f7 = input("Your fruit: ")

myfruitlist=[f1,f2,f3,f4,f5,f6,f7]
print(myfruitlist)

# PROBLEM-2
mark1 = int(input("Enter marks 1: "))
mark2 = int(input("Enter marks 2: "))
mark3 = int(input("Enter marks 3: "))
mark4 = int(input("Enter marks 4: "))
mark5 = int(input("Enter marks 5: "))
mark6 = int(input("Enter marks 6: "))

marks = [mark1,mark2,mark3,mark4,mark5,mark6]
marks.sort()
print(marks)

# PROBLEM-3
tuple = (1,3,5,2,6)
print(tuple)
print(type(tuple))
tuple[1] = 0 # ITS SHOWING TUPLE CANNOT CHANGE
print(tuple)

# PROBLEM-4
list = [10,12,13,15]
print(list[0]+list[1]+list[2]+list[3]) # BOTH ARE THE VALID WAYS WITH SAME RESULT
print(sum(list))

# PROBLEM-5
a = (7,0,8,0,0,9)
print("The numbers of zeros in a is",a.count(0))
# *******************************************************************************************

# CHAPTER-5 DICTIONARY PRACTICE SET
#################################
# Example of a nested dictionary
dict = {
    "name": {"harsh": "babu"}
}

print(dict["name"]["harsh"])
##################################
# PROBLEM-1
myDict = {
    "Pankha": "Fan",
    "Vastu": "Item",
    "Dabba": "Box"
}
# print("Options are",myDict.keys())
a = input("Enter your option")
# print("Enlish translation is",myDict[a])
print("Enlish translation is",myDict.get(a)) # This line will not throw error if key is not present in dict.


# PROBLEM-2
num1 = int(input("Enter your numer1: "))
num2 = int(input("Enter your numer2: "))
num3 = int(input("Enter your numer3: "))
num4 = int(input("Enter your numer4: "))
num5 = int(input("Enter your numer5: "))
num6 = int(input("Enter your numer6: "))
num7 = int(input("Enter your numer7: "))
num8 = int(input("Enter your numer8: "))

set = {num1,num2,num3,num4,num5,num6,num7,num8}
print(set)

# PROBLEM-3
set = {18,"18"}
print(set)
print(type(set))

# PROBLEM-4
s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(s)
print(len(s))

# PROBLEM-6 
favlang = {}
a = input("Enter fav lang for shubham: ")
b = input("Enter fav lang for Ankit: ")
c = input("Enter fav lang for Harsh: ")
d = input("Enter fav lang for Vikas: ")

favlang["Shubham"] = a
favlang["Ankit"] = b
favlang["Harsh"] = c
favlang["Vikas"] = d

print(favlang)

# PROBLEM-7 
favlang = {}
a = input("Enter fav lang shubham: ")
b = input("Enter fav lang shub: ")
c = input("Enter fav lang shubham: ") # IF KEYS ARE SAME THAN IT WILL GIVE YOU THE LATEST VALUE ONLY
d = input("Enter fav lang shum: ") # IF VALUES ARE SAME NO PROBLEM

favlang["Shubham"] = a
favlang["Shub"] = b
favlang["Shubham"] = c
favlang["Shum"] = d

print(favlang)
# ****************************************************************************************************

# CHAPTER-6 PRACTICE SET

# QQ
age = int(input("Enter the age: "))
if age>=18:
    print("Yes age is greater than 18")
else:
    print("No age is lesser than 18")

# PROBLEM-1
num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
num3 = int(input("Enter number3: "))
num4 = int(input("Enter number4: "))

if num1>num4:
    f1 = num1
else:
    f1 = num4
if num2>num3:
    f2 = num2
else:
    f2 = num3
if f1>f2:
    print("The highest of given numbers is",f1)
else:
    print("The highest of given numbers is",f2)

# PROBLEM-2
mark1 = int(input("Enter your marks1: "))
mark2 = int(input("Enter your marks2: "))
mark3 = int(input("Enter your marks3: "))

if (mark1 or mark2 or mark3)< 33:
    print("You are fail due-to less marks in subject")
elif (mark1+mark2+mark3)/3 < 40:
    print("You are fail due_to less marks overall")
else:
    print("You are pass")

# PROBLEM-3
text = input("Enter your text")
if("make alot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
elif("click in this" in text):
    spam = True
else:
    spam = False
if spam:
    print("Your text consist spam")
else:
    print("This is not spam")

# PROBLE-4
username = input("Enter your username: ")
if len(username)>10:
    print("Username contain more than 10 characters")
else:
    print("Username not contain more than 10 characters")

# PROBLEM-5
list = ["Harsh","Shubham","Akriti","Sonali","Siddharth"]
name = input("Enter your name: ")
if name in list:
    print("Yes name is present in the list")
else:
    print("No name is not present in list")

# PROBLEM-6
marks = int(input("Enter your marks: "))
if marks>= 90:
    grade = "Ex"
elif marks>=80:
    grade = "A"    
elif marks>=70:
    grade = "B"    
elif marks>=60:
    grade = "C"    
elif marks>=50:
    grade = "D"    
elif marks<50:
    grade = "F"    
print("Your grade is",grade)

# PROBLEM-7
post = input("Enter your post: ")
if "Harsh" in post:
    print("Yes this post is about the Harsh")
else:
    print("No this post is not about the Harsh")

# *********************************************************************************************

# CHAPTER-7 PRACTICE SET
# QQ-1
i = 1
while i <= 50:
    print(i)
    i = i+1

# QQ-2
list = ["Harsh","Sonali","Akriti","Pranav"]
i = 0
while i < len(list):  # USING WHILE LOOP
    print(list[i])
    i = i+1

list = ["Harsh","Sonali","Akriti","Pranav"]
for i in list:  # USING FOR LOOP
    print(i)

for i in range(20): # USE OF BREAK IN LOOP
    print(i)
    if i == 6:
        break

for i in range(20):  # USE OF CONTINUE IN LOOP
    if i == 6:
        continue
    print(i)

# PROBLEM-1
num = int(input("Enter your number: "))
for i in range(1,11):
    print(f"{num}x{i}={num*i}")

num = int(input("Enter your number"))
for i in range(1,11):
    print(str(num)+"x"+str(i)+"="+str(i*num))
    
# PROBLEM-2 
list = ["Harsh","Sohan","Hemant","Rahul"]
for name in list:
    if name.startswith("H"):
        print("Hello",name)

# PROBLEM-3
num = int(input("Enter your number: "))
i = 0
while i<11:
    print(f"{num}x{i}={num*i}")
    i = i+1

# PROBLEM-4
num = int(input("Enter your number: "))
prime = True
for i in range(2,num):
    if (num%i==0):
        prime = False
        break
if prime:
    print("Your given number is prime")
else:
    print("No given number is not prime")










