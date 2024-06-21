


# loop:- loop are used to run the set of statement.
             #or
#         block of code  



# type of loop :-

# 1. while loop 
# 2. for loop
# 3. nested loop 



# while loop :- it is used to iterate the set of statement for 
#                infinite time . 


# print hello world 10 times 


# x = 20
# while x>1:
# 	print("hello world")
# 	print(x)
# 	x-=1




# print your name 10 times

# x = 10
# while x>0:
# 	print("love sharama")
# 	x-=1



# print the counting from 1 to 50 


# x = 1
# y = 51
# while x<y:
# 	print(x)
# 	x+=1




# print counting from 10 to 40 

# x = 10
# y = 41

# while x<y:
# 	print(x)
# 	x+=1





# print backward counting from 30 to 1 

# x = 30
# y = 0
# while x>y:
# 	print(x)
# 	x-=1




# print counting with the help of user input.


# y = 0
# x=int(input("enter the number:- "))

# while x>y:
# 	print(y)
# 	y+=1



# print the table of 5 .

# x = 5
# y = 100
# while x<y:
# 	print(x)
# 	x+=5



# By using user input write a code by which the tables can be coded.

# x=int(input("enter the table name:- "))
# y=1
# while y<11:
# 	print(x*y)
# 	y+=1






# print hello world 15 times.

# x = 15
# while x>1:
# 	print("hello world",x)
# 	x-=1






# print the counting between 40 to 50

# x = 40
# y = 51
# while x<y:
# 	print(x)
# 	x+=1





# print backward counting from 60 to 40 

# x=60
# y=39
# while x>y:
# 	print(x)
# 	x-=1






# print the table by using user input .

# u = int(input("enter the table name:- "))
# x = 1

# while x<11:
# 	print(x*u)
# 	x+=1







# print all even number between 31 to 50 

# x = 31
# y = 50 

# while x<=y:
# 	if x%2==0:
# 		print("Even number:",x)
# 	x+=1




# print all the odd number between 1 to 30 

# x = 1
# y = 31

# while x<y:
# 	if x%2!=0:
# 		print("odd number",x)
# 	x+=1







# print all number from 58 to 89 which is divisible by 7.


# x = 58
# y = 89

# while x<y:
# 	if x%7==0:
# 		print(x,"divisible by 7")
# 	x+=1





# print all number form 1 to 100 which is divisible by 5 and 8

# x = 1
# y = 100

# while x<y:
# 	if x%5==0 and x%8==0:
# 		print(x,"are divisible by both 5 and 8")
# 	x+=1







# print all number from 100 to 200 which is divisible by 10 or 5


# x = 100
# y = 200
# while x<y:
# 	if x%10==0 or x%5==0:
# 		print(x)
# 	x+=1










# print all even number from 340 to 300 

# x = 340
# y = 300

# while x>=y:
# 	if x%2==0:
# 		print(x)
# 	x-=1








# print square value from 1 to 10 

# x = 1 
# y = 10

# while x<=10:
# 	print(x**2)
# 	x+=1







# -------------------------------------------------------------------






















# ---------------------------------------------------------------------


# 1. find the sum of first 10 number 1 to 10

# x = 1
# y = 10
# s = 0

# while y>=x:
# 	print("counting :- ",x)
# 	s+=x
# 	x+=1


# print("sum of first 10 numbers:-",s)





# 2. Find the average of first 5 number

# x = 5
# y = 1
# add = 0

# while x>=y:
# 	add+=y
# 	y+=1

# avg = add/x
# print("average of first 5 numbers :- ",avg)





# 3. Count total Number of even Number from 1 to 25

# x = 25
# y = 1
# c = 0

# while x>=y:
# 	if y%2==0:
# 		 print("even number: ",y)
# 		c+=1
# 	y+=1
# print("Number of even number:-",c)







# 4. Count total Number of odd Number from 20 to 36


# x = 20 
# y = 36
# c = 0
# while x<=y:
# 	if x%2!=0:
# 		c+=1
# 	x+=1
# print("odd number from 20 to 36: ",c)







# 5. Count total number who is divisible of 7 from 1 to 80.

# x = 1
# y = 80
# c = 0

# while x<=y:
# 	if x%7==0:
# 		c+=1
# 	x+=1

# print(c)



# ------------------------------------------------------



#statement

# Break:- Break statement are used to break the loop accourding 
#          to the condition .


# x = 10
# y = 1

# while x>=y:
# 	if y==5:
# 		break
# 	else:
# 		print(y)
# 	y+=1


# --------


# Continue :- Continue statement is used to skip the text 
#               accourding to the  condition.



# x = 10
# y = 0

# while x>y:
# 	y+=1
# 	if y==4 or y==7:
# 		continue
# 	else:
# 		print(y)





# print number from 50 to 80 and skip the numbers 60 to 70. 

# x = 50
# y = 80

# while x<=y:
# 	x+=1
# 	if x<=70 and x>=60:
# 		continue
# 	else:
# 		print(x)






# ------------------------------------------------------------
# ------------------------------------------------------------

# for loop :- it is used to run the set of statement .
              #  or
              # it is used to iterate the block of code






# print the counting from 1 to 10 using for loop ,


# for a in range(1,11):
# 	print(a)




# for a in range(100,141):
# 	print(a)


# for x in range(20,10,-1):
# 	print(x)


# for x in range(1,16):
# 	if x%2==0:
# 		print(x)


# for x in range(25,41):
# 	if x%2!=0:
# 		print(x)


# for x in range(1947,2024):
# 	if x%4==0:
# 		print(x)




# for x in range(10,80,5):
# 	print(x)



# count total number of odd number from 1 to 15 

# c=0
# for i in range(1,16):
# 	if i%2!=0:
# 		#print(i)
# 		c+=1
# print("total odd number:- ",c)




# write a pyhton program to print the number from 100 to 50 who is
# divisible by 3 or 7 and also even
# c=0
# for i in range(100,49,-1):
# 	if (i%3==0 or i%7==0) and i%2==0:
# 		# print(i)
# 		c+=1
# print(c)



# -------------------------------------------------------------------


# -----------------------------------------------
# text in loop
# -----------------------------------------------
# import time

# x = "Love"
# for y in x:
# 	print(y)

# 	time.sleep(1)









# pritnt the text by using their index numbers .


# x = "Love sharma"

# y = len(x)

# for i in range(y):
# 	print(x[i])

# --------------------------------------------------
# extract the text using the while loop.

# x = "kunal"
# y = len(x)
# z = 0

# while y>z:
# 	print(x[z])
# 	z+=1






# print the number from 20 to 40 and break the number when the number is 30

# for i in range(20,40):
# 	if i==30:
# 		break
# 	print(i)










# print counting from 1 to 10 but print the numbers horizontaly .

# for i in range(1,11):
# 	print(i,end="--")



# show the index number of each alphabet from the text. 

# x = "rohit sharma"
# y = len(x)
# for i in range(y):
# 	print(x[i],"index number :-",i)








# show the index number of each alphabet from the text in negative index.


# x = "rohit sharma"
# y = len(x)
# for i in range(y):
# 	print(x[i],"negative index",i-y)





# Extract the numerial value from the text.

x = "pr8oga5rmming123"
for i in x :
	if i.isdigit():
		print(i)
 		




# print(y)
# print(type(y))
# y = int(y)
# print(type(y))


# c=0
# for i in x:
# 	if i.isdigit():

# 		c+=1
# print(c)









# x = "lovesharma171017@gmail.com"

# count total number of alohabet 

# c = 0
# for i in x:
# 	if i.isalpha():
# 		c+=1
# print(c)  







# print all special character


# for i in x:
# 	if i.isalnum():
# 		continue
# 	else:
# 		print(i)





# extract all alphabet from the test.

# for i in x:
# 	if i.isalpha():
# 		print(i)



# print all alphabet before g

# for i in x:
# 	if i=="g":
# 		break
# 	else:
# 		print(i)



# count all special character














# x = "ramayan"


# print all a from the text

# for i in x:
# 	if i=="a":
# 		print(i)





# count total number of a

# print(x.count("a"))





# print a and r from the text.

# for i in x:
# 	if i=="a" or i=="r":
# 		print(i)








# ------------------------------------------------------------------
# ------------------------------------------------------------------




# for i in range(10,4,-1):
# 	print(i,end=" ")



# print odd number from 1 to 20

# for i in range(1,21):
# 	if i%2==1:
# 		print(i)







# print backward counting from 20 to 10.

# for i in range(20,9,-1):
# 	print(i)



# x = "programming"


#extract all vowel  alphabet.

# a = ["a","e","i","o","u"]

# for i in x:
# 	if i in a:
# 		print(i)




# print the alphabet who is repeted more then one time 

# for i in x:
# 	if x.count(i)>1:
# 		print(i)

		


#print all even index of value from text

# y = len(x)
# for i in range(y):
# 	if i%2==0:
# 		print(x[i],end=" ")





# x = "princeKR"

# for i in x:
# 	if i==i.upper():
# 		print(i)



# 1 to 20 square value 

# for i in range(1,21):
# 	print(i**2)
  

  # or



# x = 1
# y = 21
# while x<y:
# 	x+=1
# 	print(x**2)





# x = "p34ert345j4j34534j"




#extract all number

# for i in x:
# 	if i.isdigit():
# 		print(i)




# count how many numbers are there in the string

# c = 0
# for i in x:
# 	if i.isdigit():
# 		c+=1
# print(c)






# find the average of first 10 numbers .

# s = 0
# for i in range(1,11):
# 	s=s+i
# avg=s/i
# print(avg)




# x = "p34ert345j4j34534j"

# find the sum of number.
# s=0
# for i in x:
# 	if i.isdigit():
# 		y=int(i)
# 		s=s+y
# print(s)






# find the average of first 10 number .

# s = 0
# for i in range(1,11):
# 	s=s+i
# avg=s/i
# print(avg)







# x = "p34ert345j4j34534j"

# 1. find the sum of the numbers

# s = 0
# for i in x:
# 	if i.isdigit():
# 		y = int(i)
# 		s=s+y
# print(s)
 





