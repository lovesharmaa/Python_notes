

# python :- python is a general high level programing language.
#        :- it was released in 1991 by GUIDO VAN ROSSUM .
#        :- python is an object oriented language . 


# what is software? 
# software is the collection of program .

# types of software              1- System software
#                                   2-Application software
#                                       2.1-backend
#                                       2.2-fronted
#                                   3- web application software
#                                   4-mobile application
#                                   5-AI and IOT  
# -------------------------------------------------------------------------------


# Why python?
# pyhton can work on different platforms(window mac linux)
# python has a simple sintax similar to the English language .
# pyhton has syntax that allow developers to write program with fewer lines than some other programing language .
# ----------------------------------------------------------------------------------

# what are Variables ? 
# -variables are used to store the vlaues 
# -variables are the containers to store the values 
# -variables are the short name of the values 

# x="india" (where x is variable and india is value)
 


#  Types of variables 
# -Single variable    x=23    y=india
# -multiple variable  x,y=23,46


# Limitation of variable
# - Variable only start with alphabats.
# - variable can be alpha numaric (x2)
# - Variable is case sensative 
# - in variables you can not use special characters
# - you can use under score (_) in variables.
# -----------------------------------------------------------------------------------------

# Indentation error :- Do not give the extra space in the starting of the code 

# ---------------------------------------------------------------------------------------------


# Comments -
# it is the statemet that we want to show but do not want to execute in code .

# Types of comments
# - Single comment (#)
# - multiple comment (""" """)

# ----------------------------------------------------------------------------------------------
# Data type :-
# 1. Numerical data - integer (int) ,  Float (Decimal) ,  Complex (like 21j)
# 2. Text type data - String (str)(always coded in double or single cotation)
# 3. Sequence data type - List (List always use in square braket  [] ) ex- ["love",54,54.55]
#                         Tuple (Tuple are written in round braket () ) ex- ("love",54,54.55)
#                         Range - range(starting,ending,stepsize)
# 4. Mapping data - Dictionary {key:values}
# 5. set data - set are written in curly braket {}
# 6. Boolen data - true , false 
# 7. None - None

# how to check the data type

# x=45
# t=type(x)
# print(t)

# x="love shamra"
# t=type(x)
# print(t)

# x=90.65
# t=type(x)
# print(t)


# ------------------------------------------------------------------------------------------------

# Forcasting of data-  forcasting of data refers to the change of data type from one to another .

# x=45
# print(type(x))
# change the data type of x into string
# x=str(x)
# print(type(x))


 
# Types of operator
# ---------------------------------------
# 1. Airthmatic operator
# 2. Assingment operator
# 3. Comparesion operator
# 4. Logical operator
# 5. Identity operator
# 6. Membership operator
# 7. Bitwise operator
# ----------------------------------------






# 1. Airthmatic
# -------------
# + Addition
# - substraction
# * multiplication
# / division
# % Modules:- it shows the reminder.
# ** Exponentation:- it is used  to add the power on number.
# // Floor division:- it show the value before the decimal.


# x=45
# y=20
# print("modulas",x%y)
# print("The remainder of",x,"and",y,"is",x%y)

# x=5
# y=3
# print(x*y)
# print("the exponant of",x,"and",y,"is",x**y)








# 2.Assingment operator
# -------------------------------------
# = : Assingment
# == : equal to
# != : not equal to  
# += :               (or)   x=x+1
# -= :               (or)   x=x-1
# *= :               (or)   x=x*1
# /= :               (or)  x=x/1


# not equals to 
# x=100
# y=200
# print(x==y)
# print(x!=y)


# x=50
# x=x+10
# x+=10
# print(x)

# x=40
# x/=10
# print(x)

# x=100
# x*=10
# print(x)









# 3. Comparasion operator
# -------------------------------------
# > Greater than
# < less than
# >=Greater than equals to 
# <=less than equals to 
# == equal to
# != not equal to 
# --------------------------------------------------------------------------------



# if_else :- it is used to divide the data in different different categories.
# -----------------------

# write a pyhton program to show the number if the number is grater than 10 than print yes else no .

# x=10
# if x>10:
# 	print("yes")
# else:
# 	print("no")



# check the number 15 wheather it is even or odd 

# x=15
# if x%2==0:
# 	print("the number is even")
# else:
# 	print("the number is odd")



# check 81 is divisible by 9 or not .

# x=81
# if x%9==0:
# 	print("yes")
# else:
# 	print("no")





 

# ---------------------------------------------------------------------------------------------


# user input :- it is a input where you enter the values in output screen.

# x=int(input("enter the number:-"))
# if x%2==0:
# 	print("even number")
# else:
# 	print("odd number")



# x=int(input("the number is : "))
# if x>200:
# 	print("greater than 200")
# else:
# 	print("less than 200")


# check the text is equals to Delhi then print yes else print no .
# x=str(input("enter any text :-"))
# if x=="delhi":
# 	print("yes")



# write a python progam to show the state and capital accourding to user input .

# x=str(input("enter the state name :-"))


# x="patna"
# if x=="patna":
# 	print("bihar")
# else:
# 	print("no")


























# Logical operator
# and :- it return True when both condition are True 
# or :- it return true when at least one condition is true 
# not:- 

# write a pyhton program to check the number is between 20 and 30 than print "yes" else print"no"

# x=25
# if x>20 and x<30:
# 	print("yes")
# else:
# 	print("no")


# write a python program to check and compare two variable
# which one is greater 


# x=int(input("enter first number:-  "))
# y=int(input("enter second number:-  ")) 
# if x>y:
# 	print(x,"is greater than",y)
# else:
# 	print(y,"is greater than",x)

# -----------------------

# write a pyhton program to check the the number is divisible by 5 and 10 .

# x=int(input("enter the number:- "))
# if x%5==0 and x%10==0:
# 	print("yes the number is divisible" )
# else:
	# print("no the number is not divisible by")

# ---------------

# write a python program to print  the last digit of any number if the number is odd .

# x=int(input("enter number:- "))
# if x%2==1:
# 	print(x%10)

# --------------------------

# Write a python program with the help of user input to
# check if the password is equal then print "correct password"
# else print "wrong password".

# p = 1234

# x=int(input("enter your pin:- "))
# if x==p:
# 	print("correct password")
# else:
# 	print("wrong password")

# ------------------------------

# write a pyhton program to print the discount and discounted amount 
# if amount is less than 5000 than 20% else 30% . 

# amount = float(input("enter the amount:- "))

# if amount<5000:
# 	d=amount*0.3
# 	a=amount-d
# else:
# 	d=amount*0.2
# 	a=amount-d
# print("Discount:- ",d)
# print("After discount:- ",a)


# -------------------------------------------------------------

# write a python program to show the Division
# if percentage is greater than equals to 60 than print First division
# if percentage is greater than equals to 45 then print Second division
# if percentage is greater than equals to 33 then print Third division 
# else print Fail

# x=int(input("Enter the percentage:- "))
# if x>=60:
# 	print("First division")
# elif x>=45:
# 	print("Second division")
# elif x>=33:
# 	print("Third division")
# else:
# 	print("Fail")

# ---------------------------------------------------------------------------





# Write a pyton program with the help of user input to check number with three 
# variable who is the greatest one .



# x=int(input("enter the first number:- "))
# y=int(input("enter the second number:- "))
# z=int(input("enter the second number:- "))

# if x>y and x>z:
# 	print("greatest number:- ",x)
# elif y>x and y>z:
# 	print("Greatest number:- ",y)
# elif z>x and z>y:
# 	print("Greatest number:- ",z)

# else:
# 	print("Equal",x,y,z)


# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------

# Swapping in pyhton
# membership operator
# identity operator

# -----------------------------------------------------------------

# What is Swapping in python ?

# When we exchange the value to other variable that is called swapping 
# in python.

# Example -

# x = 45
# y = 10

# print("x:-",x)
# print("y:-",y)

# print("After the update")

# x,y = y,x

# print("x:-",x)
# print("y:-",y)

# ---------------

# x = 20
# y = 30
# z = 40

# x,y,z = z,x,y

# print(x)
# print(y)
# print(z)

# -----------------

# x = 100
# y = 200
# z = 300

# # we have to change the variable into 

# # x = 300
# # y = 100
# # z = 200 with using only two variables . 

# x,z=z,x
# y,z=z,y

# print("x",x)
# print("y",y)
# print("z",z)

# -----------------------------

# x,y,z=10,20,30

# x,z,x=z,x,y
# y=x

# print(x)

# -------------------------------


# x,y = "59"
# z = 12

# x,y = z,x
# z,x = z,y
# x = y
# print(x)
# print(y)
# print(z)

# ----------------------------------------------------------------


# membreship operator:- 
#                     there are two types of functions in this operator
#                     "in" and "not in".

# x = "science"
# print("i"in x)
# print("I"in x)
# print("z"not in x)
# print("s"not in x) 




# x = [23,4,5,6,7,8,10]
# print(24 not in x)
# print(10 in x)





# write a pyhton program with the help of user 
# input to print 
# if your name contains a or i then print "yes" 
# else print "no".

# x=str(input("Enter your name:- "))

# if ("a"in x) or ("i" in x):
# 	print("yes")
# else:
# 	print("no")


# ------------------


# if there is sunday in x then print present else 
# print not present. 


# x = ["sunday","Monday","Tuesday","Wednesday"]

# y=str(input("Enter the day :- "))

# if (y in x):
# 	print("present")
# else:
# 	print("not present")

# ---------------------




# WRITE A PYTHON PROGRAM TO SHOW THE GRADE 
# IF NUMBER IS GREATER THAN 90 THEN PRINT "A+"
# IF NUMBER IS GREATER THAN 80 THEN PRINT "A"
# IF NUMBER IS GREATER THAN 70 THEN PRINT "B+"
# IF NUMBER IS GREATR THEN 60 THEN PRINT "B"
# IF NUMBER IS GREATER THAN 50 THEN PRINT "C"
# ELSE PRINT "D"

# x=int(input("Enter the number:- "))

# if x>90:
# 	print("A+")
# elif x>80:
# 	print("A")
# elif x>70:
# 	print("B+")
# elif x>60:
# 	print("B")
# elif x>50:
# 	print("C")

# else:
# 	print("D")


# ----------------------------

 # WRITE A QUEARY TO SHOW YEAR AND LEAP YEAR WITH THE HELP OF 
 # USER INPUT .

# x=int(input("Enter the year:- "))
# if x%4==0:
#  	print("leap year")
# else:
# 	print("Not a leap year")

# --------------------------------------------------------------------

          # if else elif statements questons 



# {1} Write a program to check wheather the given input number is 
#     divisible by 3 or else show the message
#      "number is not divisible by 3 "
           

# x=int(input("Enter the number:- "))
# if x%3==0:
#    print("yes the number is divisible by 3")
# else:
# 	print("Number is not divisible by 3")

# --------------


# {2} Write a program that check wheather the input is in odd number 
#      or an even number .


# x=int(input("Enter the number:- "))
# if x%2==0:
#    print("Even number")
# else:
#    print("Odd number") 

# ----------------------

# {3} Write an if/else statement with the following options:
#    If the variable age is greater than 18 ,"old enough", otherwise 
#    output "Too young".

# x=int(input("Enter the age:- "))
# if x>18:
# 	print("Old enough")
# else:
# 	print("Too young")


# --------------------------                                                 

# {4} Write a program that promote the user for their name , and
#    then display a special greeting to that person if their name is
#    the same as yours . If the name entered by the user is anything 
#    other than your name , your code should not produce any output .

# x=str(input("Enter the name:- "))
# if x=="love":
# 	print("same name")
# else:
# 	print(" ")

# ---------------------------

# {5} Write a program that takes a calendar year in YYYY format in a 
#     variable . Check & notify the user weather it is a leap year 
#     or not .


# x=int(input("Enter the year:- "))

# if x%4==0:
# 	print("yes the year",x,"is the leap year")
# else:
# 	print("no the year",x,"is not the leap year")


# ---------------------------------

# {6} Write a python program that accept two integer and display the 
#    larger . Also show if the two integer are equal .

# x=int(input("Enter the first number:-"))
# y=int(input("Enter the second number:- "))

# if x>y:
# 	print(x,"is larger")
# elif x==y:
# 	print("Both are equal")

# else:
# 	print(y,"is larger")

# ------------------------------------

# {7} Write a program that take input a number from user & state 
#      wheather the number is positive , negative and zero .

# x=int(input("Enter the number:- "))

# if x>0:
# 	print("Positive integer")
# elif x==0:
# 	print("Zero")
# else:
# 	print("Negative integer")

# ------------------------------------------


# {8} Write a program that takes a character (i.e. string of length 1)
#     and return true if it is a vowel , false if othervise .


# x=str(input("enter the letter:- "))

# if x==("a"",e","i","o","u"):
# 	print("True")
# else:
# 	print("False")

# ----------------------------------


# {9} If the variable age is a value below 18 the value of the variable 
#     voteable should be "Too young" , otherwise the value of 
#     voteable should be "Old enough"

# x=int(input("Enter the age:- "))

# if x<18:
# 	print("Too young")
# else:
# 	print("Old enough")

# ------------------------------------
# solution 11.

# x=int(input("enter the time:- "))

# if x>=0000 and x<=1200:
# 	print("Good Moorning")
# elif x>1200 and x<=1700:
# 	print("Good Afternoon")
# elif x>1700 and x<=2100:
# 	print("Good Evening")
# else:
# 	print("Good Night")


# ----------------------------------------------------------------------------

# x = "Data science"

# Show the data type of x 
# Show the lenght of the x 

# a=len(x)
# print("length of x :-",a)

# b=type(x)
# print("data type of x is",b)

# ------------------------------------------



# print("Phone pay :")
# print("-"*50)

# loc = 1234
# u = 9876

# x=int(input("Enter the pin:- "))
# y=int(input("Enter the UPI pin:- "))

# if x==loc:
# 	if y==u:
# 		print("Unlocked")

# 	else:
# 	    print("UPI pin is wrong")

# else:
# 	print("Wrong pin")




# ------------------

# print("-"*50)
# x = str(input("Name the Board:- "))
# print("-"*50)

# if x == "bseb":
# 	print("Welcome to Bihar board")
# 	print("-"*50)
# 	cl = int(input("Enter the class:- "))
# 	if cl == 9:
# 		print("Welcome to class 9th")
# 	elif cl == 10:
# 		print("Welcomr to class 10th")
# 	else:
# 		print("Not found")

# elif x == "cbse":
#     print("Welcome to Central Board")
#     print("-"*50)
#     cl = int(input("enter the class:- "))
#     if cl==11:
#     	print("Welcome to class 11th")
#     elif cl==12:
#     	print("welcome to class 12th")
#     else:
#     	print("Not found")

# else:
# 	print("You entered the Wrong Board")


# print("-"*50)




























# ind = int(input("Enter the score of India:-  "))
# aus = int(input("Enter the score of Australia:-  "))

# if ind>aus:
# 	w = "India"
# 	m=ind-aus
# else:
# 	w = "Australia"
# 	m=aus-ind
# print("Winner is:-",w)
# print(w,"won by",m,"runs")


# pak = int(input("Enter the score of pakistan:-  "))
# eng = int(input("Enter the score of england:-  "))

# if pak>eng:
# 	w2 = "pakistan"
# 	m2=pak-eng
# else:
# 	w2 = "England"
# 	m2=eng-pak
# print("Winner is:-",w2)
# print(w2,"won by",m2,"runs")




# x = int(input(f"score of {w}: "))
# y = int(input(f"score of {w2}: "))

# if x>y:
# 	win=w
# 	ma=x-y
# else:
# 	win=w2
# 	ma=y-x

# print("final winner is:",win)
# print(win,"won by:",ma)





# find the Area of circle 
# r=7
# pie=22/7
# print(pie*r**2)



# -------------------------------------------------------
#      strings 
# -------------------------------------------------------


# It is always written in dual or single cotation.


# x="love"

# print(x)

# print(type(x))

# print(len(x))



# -------------------------------------
# string functions
# ---------------------------------------


# x="love"
# if x=="LOVE":
# 	print("yes")
# else:
# 	print("no")


# upper:- it is used to convert the text in capital letters.

# x="data"
# y = x.upper()
# print(y)

# lower:- it is used to convert the text into small letters.
# x = "DATA"
# y = x.lower()
# print(y)

# trim:-



# title:- it is used to capitalize the first letter.

# x = "i have to attend the class"
# y = x.title()
# print(y)


# capitalize

# x = "i have to attend the class"
# y = x.capitalize()
# print(y)



# examples:-

# x = "patna"
# x = x.upper()
# print(x)



# x = "DELHI"
# x = x.lower()
# print(x)




# x = "delhi"
# x = x.title()
# print(x)




# x="love sharma"
# y=x.title()
# z=x.capitalize()

# print("title:-",y)
# print("capitalize:-",z)


# write a python program to check the text is equal or not 

# x = "science"
# y = "scIENCE"

# if x==y.lower():
# 	print("yes")
# else:
# 	print("no")








# swapcase:- it is used to convert the small letters into capital
              # and vice versa 
# x = "scIENCE"
# x=x.swapcase()
# print(x)



# ---------------------------------------------------------























# ---------------------------------------------------


# x = "himachal pradesh"

# reverse the text with the help of slicing

# print(x[-1::-1])




# x = "Arunachal pradesh"

# print(x[0:4])

# print(x[4:1:-1])

# print(x[3:6])

# print(x[5:2:-1])

# print(x[10::1])

# print(x[-1:-8:-1])

# print(x[1:5])

# print(x[0:7:3])

# print(x[6::-3])

# print(x[-4::].upper())

# -----------------------------------------------

# index:- it is used to show the position or index if alphabet.
# find:- same

# x = "data analyst"

# a = x.index(" ")
# print(f"index of space:{a}")

# a = x.find(" ")
# print(f"position of space :-{a}")

# --------------------



# x = "data analyst"    find the index of A ?

# y=x.index("a")
# print("position of first A",y)

# z=x.index("a",y+1)
# print("position of second A:-",z)

# w=x.index("a",z+1)
# print("position of third a :-",w)



# ---------------------

# x = "india"

# # second I position ?6

# i = x.find("i")
# i2 = x.find("i",i+1)
# print(i)

# ------------------------------------


# x = "data analyst"

# # count the total number of A from the text.

# # count():- it is used to count the particular alphabet from
# #             the text . 

# y = x.count("a")

# print("total number of a :",y)


# ----------------------------


# x = "Arunachal"

# # count the  total number of a 

# x = x.lower()
# print(x.count("a"))





# x = "pyhton is A Programing LAnguage"

# 1.count the total length without space
# 2.count the total number of a and p 
# 3. Extract the first five letters from the text.
# 4. Extract the last 3 alphabet from the text. 


# 1.
# y = len(x)-x.count(" ")
# print(f"lenght without space is {y}")




#2
# y = x.upper()
# z = y.count("A") + y.count("P")
# print(z)





#3
# a = x[0:5]
# print(f"The first five letter of the text is {a}")







#4
# a = x[-3::]
# print(a)





# ------------------------------------------



# replace :- it is used to replace the value from old text 
            # or alphabet to new text or alphabet .


# x = "data analyst"

# y = x.replace("a","*")

# print(y)

# z = x.replace(x[0:4],"*")
# print(z)


# ----------------------------------------------------

#split :- it is used to convert the string to list on the
             # base of a delimiter. 


# x = "python is a programming language " 

# y = x.split(" ")

# print(y)
# print(type(y))





#join :- it is used to convert the list to string .

 
# x = ['python', 'is', 'a', 'programming', 'language', '']

# print(x)
# print(type(x))

# print("_"*90)

# y = " ".join(x)
# print(y)
# b=type(y)
# print(b)



# --------------------------------------------------------------


# strip:- it is used to delete the extra space from the 
#          starting and ending of the text .

# x = "      data analyst       "
 
# print(x)

# y = x.strip()
# print(y)

# ---------------------------------------------------------

# format:- it is used to fill the values accourding to the position.


# x = "Hello {}"

# y = x.format("Good morning")
# print(y)






# x = "Hii {} My name is {} i am {} years old"

# y = x.format("Good morning","love sharma",22)
# print(y)

# ----------------------------------------------------


# startswit:- it is used to check the first alphabet form the text.

# x = "Rohit sharma"

# #if name starts with r then print yes else print no.

# y = x.startswith("R")
# print(y)


# -----------------------



# x = str(input("Enter the name:- "))
# p = x.startswith("r")
# if x==p:
# 	print("yes")
# else:
# 	print("no")

# ---------------------------------------------------------

# endswith:- it is used to check the last alphabet from the text.

# Write a pyhton program to check if name endswith r and a then 
# print "the name" else print "not found".

# x = str(input("Enter the name:-"))

# if x.endswith("r") or x.endswith("a"):
# 	print(x)
# else:
# 	print("not found")







# isupper

# x = "data"
# y = x.isupper()
# print(y)


# # islower

# print(x.islower())


# # isdigit
# print(x.isdigit())

# # isdecimal
# print(x.isdecimal())

# # isalpha()
# print(x.isalpha())

# # isalphanum()
# print(x.isalnum())

# # isspace()

# print(x.isspace())


# # istitle()
# print(x.istitle())



# x = "India"
# y = x.title()
# print(y)

# a = x[0:-1]
# b = x[-1].upper()
# print(a+b)












# x = "brillica"

# reverse the text 

# y = x[-1::-1]
# print(y)


# print the first and the last alphabet of the text 
# z = x[0]
# a = x[-1]
# print(z+a)

# count total number of i 

# y = x.count("i")
# print(y)



#print the text in which i is not there
# y = x.replace("i","") #brllca
# print(len(y))





# reverse the text according to the exoected output 
# x = "pyhton is an object oriented programing language"

# # expected output : {language programing oriented object an is pyhton}


# x = x.split(" ")
# a = x[-1::-1]
# p = " ".join(a)
# print(p)












# write a python program to check the text is in capital or not 

# x = str(input("enter the text:- "))

# if x==x.upper():
# 	print("yes")
# else:
# 	print("no")












#print yes is the first letter of text is capital else print no

# x = str(input("enter the name:- "))

# if x==x.title():
# 	print("yes")
# else:
# 	print("no")








# print the first threee digit if the length of the text is more than 5 else print no 

	
# x = str(input("enter the name :- "))

# if len(x)>5:
# 	print(x[0:3])
# else:
# 	print("no")








# x = str(input("Enter the text :- "))

# if x.isdigit():
# 	print(x)
# elif x.isspace():
# 	print(x)
# elif x.isalpha():
# 	print(x)
# elif x.isalnum():
# 	print(x)
# else:
# 	print("no")







# -----------------------------------------------------------------------
#                      practice for test
# -----------------------------------------------------------------------


# write a pyhton program to check the text is equal or not 
# x = "scIENCE"
# y = "science" 

# if y==x.lower():
# 	print("yes they are equal")
# else:
# 	print("no they are not equal")










# x = "himachal pradesh"           #reverse the text 
# y = x[-1::-1]
# print(y)








# x = "Arunachal pradesh"

#pra
# y = x[-7:-4]
# print(y)


#dar
# y = x[-4:-7:-1]
# print(y)



# using indexing the position of A in 

# x = "Data analyst"
# y = x[1]
# print(y)








# the position of I in india 

# x = "india"
# y = x[0]
# print(y)



# count the total number of A in data analyst 

# x = "data analyst"
# y = x.count("a")
# print(y)





# x = "pyhton is a programing language"



# find the length of the text without space 
# y = len(x)-count(" ")
# print(y)




# count the total number of  a and p.
# y = x.upper()
# y = y.count("A") + y.count("P")
# print(y)






# extract the first five letter from the text 

# y = x[0:5]
# print(y)





# write a python program to check if the name endswith r and a 
# then print the name else print not found .

# x = str(input("Enter the name:- "))
# if x.endswith("r") or x.endswith("a"):
# 	print(x)
# else:
# 	print("not found")







# x = "brillica"

#reverse the text 

# y = x[-1::-1]
# print(y)





#print the first and the last alphabet of the text together.

# y = x[0]
# z = x[-1]
# print(y+z)






# count the total number of i from the text 

# y = x.count("i")
# print(y)




# print the text in which i is not present .

# print(x.replace("i",""))







# reverce the words not the alphabets .


x = "python is an object oriented programing language"

y = x.split(" ")
z = y[-1::-1]
p = " ".join(z)
print(p)




# write a pyhton program to check the text is capital or not .

# x = str(input("Enter the text:- "))

# if x==x.upper():
# 	print("yes the text is in capital letter")
# else:
# 	print("no the text is not in capital letter")



# print the first three alphabet if the length of the text is more 
# than 5 else print no 


# x = str(input("Enter the text:- "))

# if len(x)>5:
# 	print(x[0:5])
# else:
# 	print("not found")







 
# -----------------------------------------------

# print hello world 10 times

# x = 10 
# while x>1:
# 	print("Hello world")
# 	x-=1





# print your name 10 times 

# x = 11

# while x>1:
# 	print("Love sharma")
# 	print(x)
# 	x-=1






# print the counting from 1 to 50 


# x = 50

# while x>0:
# 	print(x)
# 	x-=1




# print the counting from 10 to 40 .

# x = 40
# y = 10

# while x>=y:
# 	print(y)
# 	y+=1




# print backward counting from 30 to 1 

# x = 30
# y = 0

# while x>y:
# 	print(x)
# 	x-=1





# print counting with the help of user input 

# x = int(input("enter the number:- "))

# while x>0:
# 	print(x)
# 	x-=1





# print the table of 5 

# x = 5
# y = 51

# while x<y:
# 	print(x)
# 	x+=5



# By using user input write a code by which the tables can be coded

# x = int(input("Enter the table name:- "))

# y = 1
# while y<11:
# 	print(x*y)
# 	y+=1




# print hello world 15 times 

# x = 15
# while x>1:
# 	print("hello world",x)
# 	x-=1




# print counting from 40 to 50 

# x = 40
# y = 50

# while x<=y:
# 	print(x)
# 	x+=1



# print the backward counting from 60 to 40

# x = 60
# y = 39


# while x>y:
# 	print(x)
# 	x-=1



# print the table by using the user input .

# x = int(input("Enter the table name :- "))
# y = 1

# while y<11:
# 	print(x*y)
# 	y+=1




# print the even number from 1 to 20 .

# x = 1 
# y = 21

# while x<y:
# 	if x%2==0:
# 		print (x)
# 	x+=1



# print all even number form 40 to 50 .

# x = 40
# y = 51

# while x<=y:
# 	if x%2==0:
# 		print(x)
# 	x+=1



# print all number form 58 to 89 which is divisible by 7

# x = 58
# y = 89

# while x<y:
# 	if x%7==0:
# 		print(x)
# 	x+=1



# print all number from 1 to 100 which is divisible by 5 and 8 both .


# x = 1
# y = 100

# while x<y:
# 	if x%5==0 and x%8==0:
# 		print(x)
# 	x+=1







# print all number from 100 to 200 which are divisible by both
# 10 and 5 



# x = 100
# y = 200

# while x<=y:
# 	if x%10==0 and x%5==0:
# 		print(x)
# 	x+=1





# print all even number from 340 to 300 .

# x = 340
# y = 300

# while x>=y:
# 	if x%2==0:
# 		print(x)
# 	x-=1








# print square value of the number from 1 to 10 .

# x = 1
# y = 10

# while x<=10:
# 	print(x**2)
# 	x+=1




# print the sum of number from 1 to 10

# x = 1
# y = 10
# s = 0
# while x<=y:
# 	s+=x
# 	x+=1
# print(s)







# find the average of first 5 number 

# x = 1 
# y = 5
# s = 0
# while x<=y:
# 	s+=x
# 	x+=1
# print("the average of first 5 number is ",s/y)





# count total number of even number from  1 to 25 .

# x = 1
# y = 25
# c = 0
# while x<=y:
# 	if x%2==0:
# 		c+=1
# 	x+=1
# print("the total number of even number from 1 to 25 :- ",c)







# count the total number of odd number from 20 to 36 .

# x = 20
# y = 36
# c = 0
# while x<=y:
# 	if x%2!=0:
# 		c+=1
# 	x+=1
# print(f"There is {c} odd number between 20 to 36")




# count the total number from 1 to 80 which is all divisible by 7

# x = 1
# y = 80
# c = 0
# while x<=y:
# 	if x%7==0:
# 		c+=1
# 	x+=1
# print(f"There are {c} numbers from 1 to 80 which are divisible by 7")



# print the number from 80 to 50 and skip the numbers from 60 to 70

# x = 50 
# y = 80
# while x<=y:
# 	x+=1
# 	if x>=60 and x<=70:
# 		continue
# 	else:
# 		print(x)




# 1. print number from 100 to 140

# for x in range(100,140):
# 	print(x)



# 2. print backward Counting from 20 to 10

# for x in range(20,10,-1):
# 	print(x)



# 3. print all even number from 1 to 15

# for x in range(1,16):
# 	if x%2==0:
# 		print(x)




# 4. print all odd number from  25 to 40.

# for x in range(25,41):
# 	if x%2!=0:
# 		print(x)



# 5. print all leap year from 1947 to 2024.

# for x in range(1947,2025):
# 	if x%4==0:
# 		print(x)
		



# print the sum of number from 1 to 100


# x = 1
# y = 100
# s = 0
# while x<=y:
# 	x+=1 print 




#print the sum of number from 1 to 100


# x = 1
# y = 100
# s = 0
# while x<=y:
# 	s+=x
# 	x+=1
# print(s)





# print the sum of number from 1 to 100 in which the number of 
# 60 to 70 is not included.

# x = 1
# y = 100
# s = 0
# while x<=y:
# 	x+=1
# 	if x<=70 and x>=60:
# 		continue
# 	else:
# 		s+=x
	
# print(f"the sum is {s}")















