print("hello world!")

# How to comment in Python
print("I m a SSE.....\n This is new line now..")


'''
multiline comment ...
dg dfgdf
ghf hfgh
d gsd fsd f
'''

"""
this is another multiline comments... using  3 time double quote..
"""
  
# use of sep statement in print metod..
print("Hello", "World", "India", sep='@@')
print("Using slash n here Amit ", "gupta", sep="\n")
#  use of end param in print method...
print("Hi amit you are ending with 2 $$ synboles", end="$$\n")
print("Hi amit you are ending with 2 $$ synboles", "Okay this is another", end="999\n")
print("Hi...")

# Scape sequence character
    # 1) \n
    # 2) \t
    # 3) # pound symbole for comment any line in python
    # 4) \  back slash 
    # 5) 


## Variable in Python...
print("-------------------------Variable in Python-------------------------------")
a = 10
b = "string type.."
c = 12.24  # float type
d = None
e = True
print(type(a), type(b), type(c),type(d),type(e), sep="\n")


print("-------------------------Data Types in Python-------------------------------")
print("number", "str", "float", "bool", sep="\n")


print("-------------------------List  in Python-------------------------------")
## List => Collection of different data elements
list_1 = list([1,2,3,'amit', True, 12.5])
for n in list_1:
    print(n)


print("-------------------Tuple in Python-------------------------------------")
tple = tuple((1,5,'3', True, [2,3,4], 12.4))
# tple[2] = 5555
for t in tple:
    print("Tuple = ", t)
    

print("-------------------Dict in Python-------------------------------------")
dt = dict({'a':12,'b':23, 'c':"amit"})
for k,v in dt.items():
    print(k,v)


print("-------------------Operators in Python-------------------------------------")
x = 10
y = 20
print("Addition = ", x+y)
print("Subtraction = ", x-y)
print("Multiplication = ", x*y)
print("Division = ", x/y)
print("Floor division Operator = ", x//y)
print("Module Operator = ", x%y)
print("Exponentional Operator = ", 3**3)


print("-------------------Type Casting in Python-------------------------------------")
a1 = 23
a2 = "23"
# print("without type casting = ", (a1)+(a2))  # Error comes..
print("with type casting = ", int(a1)+ int(a2))

# t2 = "12rr"
# print(int(t2))  ## Get error...


print("-------------------User input in Python-------------------------------------")
# input = int(input("Enter any Name: "))
# print("Input = ", input)
# print("Type of input value: ", type(input))


print("-------------------String Operations in Python-------------------------------------")
name = "Harish Das"
print("name = ", name)
# for n in name:
    # print("Each character in name: ", n)
print("Length of name: ", len(name))
name_withoutspace =  len("".join([x for x in "this is my name".split(" ")]))
print(name_withoutspace)
# ------------ String slicing-----------------------------
nme = "Harry, Shubham"
print(nme[:5])
tt = "harry"
print(tt[-4:-2])


print("-------------------If Else Statement in Python-------------------------------------")
marks = 44  #int(input("Enter your marks: "))
result = "Pass in First Division" if (marks>50) else "Fail" if marks<35  else "Pass only"
print("You are ",result)
# ----------------------------------------------
# num = int(input("Enter any 2 digit number "))
# while True:
#     if(num <35):
#         print("You are fail pls enter another number")
#         num = int(input("Enter any 2 digit number "))
#     if( num >35):
#         print("You are pass now")
#         break

# print("I am happy now!")


print("-------------------Example of if else in Python-------------------------------------")
import time

""" 
Print message according to current time: 
4AM-12PM= Good Morning
12PM-4PM = Good After Noon
4PM-7PM = Good Evenin
7PM-4APM = Good Night
"""
message = ""
current_time= int(time.strftime("%H"))

if (current_time >= 4 and current_time <= 12):
    message = "Good Morning"
elif (current_time > 12 and current_time <= 16):
    message = "Good After Noon"
elif (current_time > 16 and current_time <= 19):
    message = "Good Evening"
else:
    message = "Good Night"
print(current_time)
print(message)
# ---------------------------------------------


print("-------------------match statement in Python-------------------------------------")
num = 33 # int(input("Enter you marks = "))
match num:
    case _ if num<35:
        print("You are Fail bro!")
    case _ if num<50:
        print("you are pass in third division")
    case _ if num<70:
        print("You are pass in Second division")
    case _ if num<90:
        print("You are pass in first division")
    case _ if num >= 90 and num<=100:
        print("You are Top in class and state.")
    case _:
        print("this is default statement")
# ==========================================================================================


print("-------------------break|continue statement in Python-------------------------------------")
for x in range(1,20):
    if (x ==15):
        continue
    print("x = ", x)

for x in range(1,20):
    if (x ==15):
        break
    print("x = ", x)
# ==========================================================================================


print("-------------------Function in Python-------------------------------------")
def squareNum(n):
    return n*n

for x in range(1,11):
    print(squareNum(x))
# ==========================================================================================


print("-------------------List methods in Python-------------------------------------")
lst = [4,6,8,9,2,1,33,22,11,44,67,54,21]
print(lst)

# 1) lst.append(90)
# 2) lst.sort()
# 3) lst.sort(reverse=True)
# 6) lst.reverse()
# 4) lst.count(4)
# 5) lst.index(9)
# 6) new_l = lst.copy()  // copy method
# 7) lst.insert(index, number_to_insert_at_specified_index)
# 8) list_one.extend(list_two)   # add list_two all element in list_one
# 9) k = lst + m  # add elements of lst and m in k

# Tuple Methods
tple = (33,44,55,66,12,21,23,32,43)

# 1) tple.count(44)
# 2) tple.index(value, start, end)  (44, 2,7)  or tple.index(44)
# 3) len(tple)

r= tple.index(55, 1,5)
print(r)
#---------------------------------------------------------------------------


print("------------------- in Python-------------------------------------")
# import random
# random_num = random.randint(1, 100)
# print(random_num)
# x = 34.2742343
# print(f"x = {x:.2f}")
# print(f"Hi amit you are a {{good}} {x} score")

# def function():
#     """ this i doc string..
#     """
#     print("Hi..")    
# function()
# print(function.__doc__)
# ======================================================

# def facto(n, obj={}):
#     if n == 0 or n==1:
#         return 1
#     if n in obj:
#         return obj[n]
#     obj[n] = n * facto(n-1)
#     return obj[n]
# print(facto(8))
# ======================================================

# f = open("my_file.txt", 'r')
# txt = f.read()
# # print(txt)
# # f.close()

# ft = open("my_file.txt", 'a')
# ft.write("\nHi Amit this is in second line")
# ft.close()

# f = open("my_file.txt", 'r')
# txt = f.read()
# print(txt)

with open('my_file.txt', 'w') as f:
    f.write("\n Okay now i am writing with open function.")

with open('my_file.txt', 'r') as f:
    t = f.read()
    print(t)
