


# Tuple :- Tuple are written in Round Bracket.
                     
#                   OR

# tuple are used to store the multiple value in a single Variable.




# 1. Tuple are written in round bracket ()
# 2. Tuple allow Duplicate values 
# 3. Tuple are unchangable or imutable 
# 4. Tuple are indexed .
# 5. We can insert multiple type of values .


# x = (45,78,89,56,50)

# print(x)
# print(type(x))
# print(len(x))




# How to create blank tuple?

# x=tuple()
# x=()



# x=(12,45,78,89,45,56)
# print(x)
# print(type(x))
# print(len(x))






# --------------------------------------------------------------

# Changing the value in tuple

# x = ("sun","mon","tue","wed","thu","fri","sat")
# print(x)
# print(type(x))

# -----------
# extract 
# 1. thu
# print(x[-3])


# 2. MON
# print(x[1].upper())



# 3. Sun
# print(x[0].title())



# 4. ("sat","fri")
# print(x[-1:-3:-1])


# 5. ("sun","tue","thu")
# print(x[0:5:2])


# 6. ("wed","tue","mon")
# print(x[3:0:-1])

# -------------------------------------------------------



# x = ("sun","mon","tue","wed","thu","fri","sat")


# 1 delete the first value from the tuple.

# x=list(x)
# x.pop(0)

# x=tuple(x)
# print(x)




# 2 delete the last value from the tuple.

# x=list(x)
# x.pop(-1)

# x=tuple(x)
# print(x)


# 3 delete "wed" from the tuple.

# x=list(x)
# x.remove("wed")

# x=tuple(x)
# print(x)





# 4 delete the first two value from tuple.

# x=list(x)
# del x[0:2]
# x=tuple(x)
# print(x)



# ----------------------------------------------------------




# x = ("sun","mon","tue","wed","thu","fri","sat")


# 1 add 500 on the 4th index of the tuple.

# x=list(x)
# x.insert(4,500)
# x=tuple(x)
# print(x)





# 2 add "science" in the last of the tuple.

# x=list(x)
# x.insert(-1,"science")
# x=tuple(x)
# print(x)





# 3 add three even numbers in tuple .

# x = list(x)
# x.extend([2,4,6])
# x = tuple(x)
# print(x)






# 4 arrange the tuple in descending order (z to a).

# x=list(x)
# x.sort(reverse=True)
# x=tuple(x)
# print(x)








# --------------------------------------------------------------------

# x = (12,78,12,8,12,45,89,56,12)



# a = x.index(12)
# print(a)




# find the  second index number of 12. 

# p = x.index(12,a+1)
# print(p)



# ========================================================================

                  # PACKING AND UNPACKING

# ========================================================================                  





# Packing:- with the help of this technique we divide the values of tuple 
#             in different variable.

# x=(12,45,78)
# a,b,c=x
# print(a)
# print(b)
# print(c)








# Unpacking:-with the help of this technique we divide the values of tuple 
#              but here number of variables are less than the number of values 
#              in tuple.
                 # here we use (*) to divide the rest value in a variable.

# x=(12,45,78,56)
# a,b,*c=x
# print(a)
# print(b)
# print(c)


# ---------

# x = (45,78,89,56,23,12,45)
# divide value in variable
# a = 45

# a,*b=x
# print(a)


# b = 45

# *a,b=x
# print(b)


# c = [89,56,23,12]

# a,p,*c,d=x
# print(c)



# d = 78

# a,d,*c=x
# print(d)




# --------------





x = (10,20,30,40,10,10,90,80,10)

# 1. show the index of all 10

# for i in range(len(x)):
# 	if x[i]==10:
# 		print(" Index of 10: ",i)




# 2. show the negative index number of all values.

# for i in range(len(x)):
# 	print(x[i],"negative: ",i-len(x))




# 3. delete all 10 from tuple.

# x=list(x)
# for i in x:
# 	if i==10:
# 		x.remove(i)
# x=tuple(x)
# print(x)




# 4. reverse this tuple.

# a= x[-1::-1]
# print(a)


# 5. show average of this number.

s = 0
for i in x:
	s+=i
print(s/len(x))

