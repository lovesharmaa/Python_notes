
# ------------------------------------------------------------------------
#                            LIST
# ----------------------------------------------------------------------


# list always written in square bracket.
               
#                or

# list are used to store the multiple values in a single variable .


# it came in the sequence data type .

# ------------------------------------------------- 

 #main uses of list

# 1. list are ordered 
# 2. list are changable or mutable
# 3. list are indexed 
# 4. list allow duplicate values
# 5. list written in square bracket
# 6. here you can show the multilple type of data



# -------------------------------------------------------

# storing the multiple data type of values 

# x = [100,"friday",78.23,45j,True,None,200,855]
# print("List: ",x)
# print("Data type: ",type(x))
# print("Length of list: ",len(x))


# --------------------------


# storing the duplicate values

# x = [45,45,45,45,45,45,45,45,54,54,45,45,4]
# print(x)


# -----------------------------

# List manipulation

# x = ["Sunday","Monday","Tueaday","Wednesday","Thrusday","Friday","Saturday"]
# print(x)



# --------functions used to delete data from list---------------------



# pop :- it is used to delete the value from the text with the help of indexing 
             # and by defalt delete the last value from the list

# x.pop()  #delete the last value
# print(x)

# x.pop(1)
# print(x)
# __________________

# remove:- it is used to delete the value from the list by giving the value .


# x.remove("Monday")  #delete the monday from the list
# print(x)
# ____________________

# clear:- it delete all values from the list
# x.clear()
# print(x)

# _____________________

# del:- del is a keyword which  is used to delete the values accourding to index and 
          # accourding to variable or we can say deleting by slicing  .

# del x[0:3]
# print(x)


# ---------------------------------------------------------------------




# x = [12,45,78,"fri",89,8,"thu",56,62,3,32,"sun"]


# 1. delete the last value with the help of pop

# x.pop()
# print(x)


# 2. delete "Fri" with remove

# x.remove("fri")
# print(x)



# 3. delete first three elements

# del x[0:3]
# print(x)




# 4. delete  all values from list

# x.clear()
# print(x)




# 5. delete variabel of list

# del x
# print(x)




# --------------------------------------------------------------------------------



# How to add the values in a list-------------------------------------



# 1. insert:- it is used  to insert the value accourding to index value

# 2. append :- it is used to insert the value at the end of the list.

# 3. extend:- it is used to insert the multiple value in a list or it is used to 
               # join or edit the list . 


# --------------------------

# x = [12,45,78,89,23,23]

# x.insert(2,"love")
# x.insert(0,250)
# print(x)




# x.append("ram")
# print(x)



# x = [1,2,3]
# y = [4,5,6]

# x.extend(y)
# print(x)

# x=[1,2,3]
# x.extend(["love"])
# print(x)




# ------------------------------------




# x = ["virat","rohit","anikul","rakesh"]

# create a new list and add all values of x and convert in capital letter .

# y=[]
# for i in x:
# 	i=i.upper()
# 	y.append(i)
# print(y)



# x = [45,78,89,56,12,25,47,69,10]


# delete third value

# x.pop(2)
# print(x)


# add 200 in 2nd index

# x.insert(2,200)
# print(x)




# add 500 in last of list

# x.append(500)
# print(x)






# delete 4th and 5th position of value

# del x[4:5]
# print(x)





# add [1,1,1] in the list

# x.extend([1,1,1])
# print(x)







# add "pyhton" in the last of the list.


# x.append("pyhton")
# print(x)




# delete 89 from the list.

# x.remove(89)
# print(x)




# delete all values from the list.


# del x
# print(x)





# show the lenght of the list

# print(len(x))





# show the data type of x


# y = type(x)
# print(y)







# ----------------------------------------------------------------------------------


# slicing and indexing in list


# x = [45,78,89,56,253,23]


# extract 253

# a = x[-2]
# print(a)




# [45,78]

# a = x[0:2]
# print(a)





# [89,78,45]
# a = x[-4::-1]
# print(a)





# --------------------------------






# sort():- it is used to arrange the data in ascending or descending ordered. This formula 
            # work only on the list.

# sorted:- it is used to arrange the data in ascending or descending ordered .This formula 
                # work everywhee.











# x = [45,78,89,56,253,23,20,100]

# ascending order___

# x.sort()
# print(x)



#descending order

# x.sort(reverse=True)
# print(x)








# ascending-


# y = sorted(x)
# print(y)
# print(x)


# descending_

# y = sorted(x,reverse=True)
# print(y)






# --------------------------------------------------------------------------------




# x = [45,89,56,25,41,10,96,35,78]

# 1. Arrange the data in ascending order.

# x.sort()
# print(x)


# 2. Extract the maximum value from the list.

# x.sort()
# y = x[-1]
# print(y)




# 3. Extract the minimum value from the list

# x.sort()
# y = x[0]
# print(y)


# 4. find the second highest value from the list.

# x.sort()
# y = x[-2]
# print(y)




# 5. Show the second lowest value from the list.

# x.sort()
# y = x[1]
# print(y)





# 6. show the top 3 number from the list

# x.sort()
# y = x[-1:-4:-1]
# print(y)




# 7. show the bottom 3 number form the list.

# x.sort()
# y = x[0:3]
# print(y)




# ------------------------------------------------------------------



# x = [45,89,56,25,41,10,96,35,78]

# print(max(x))   #max :- it shows the maximum value of the data 
# print(min(x))   #min:- it shows the minimum value from of the data 



# --------------------------------------------------------------------



# reverse:- it is used to reverse the list.

# x = [12,85,20,100]
# x.reverse()
# print(x)








# count:- it is used to count the values from the list .




# x = [12,45,78,89,56,12,45,12]

# 1. count the total number of 12.

# a = x.count(12)
# print(a)






#index:- it is used to show the index number of the value .

# b = x.index(78)
# print(b)







# x=[12,45,78,89,23]
# y = x
# x.clear()
# print(y)   #here the output will be empty list.


# copy:- This formula is used to copy the list.

# x=[12,45,78,89,23]
# y = x.copy()
# x.clear()
# print(y) 








# --------------------------------



# # 
# x = [12,45,78,89,65,23,10]


# 1. Extract all the even values from the list.

# for i in x:
# 	if i%2==0:
# 		print(i,end = " ")





# 2. Extract all the odd values from the list.


# for i in x:
# 	if i%2!=0:
# 		print(i,end = " ")



# 3. Create a blank list and add all even number from x.

# y = []
# for i in x:
# 	if i%2==0:
# 		y.append(i)
# print(y)



# 4. Create a blank list and add all odd numbers from x.

# y = []
# for i in x:
# 	if i%2!=0:
# 		y.append(i)
# print(y)











# x = [12,45,78,12,12,12]

# 1. delete 12 from the list.

# for i in x:
# 	if i==12:
# 		x.remove(i)
# print(x)
 
#            OR

# while 12 in x:
# 	x.remove(12)
# print(x)



# 2. delete even number from the list.

# for i in x :
# 	if i%2==0:
# 		x.remove(i)
# print(x)





# 3. delete odd number from the list.

# for i in x:
# 	if i%2!=0:
# 		x.remove(i)
# print(x)






# ------------------------------------------------------------


# Nested list:- When one list use another list inside it that is called Nested list.

# x=[[1,2,3],[4,5,6],[7,8,9]]

# print(len(x))









# x = [[12,45,78,[100,200,300]]]

#Extract

# 300

# print(x[0][3][-1])



# 78

# print(x[0][2])



# 12

# print(x[0][0])




# 45

# print(x[0][1])




# 200

# print(x[0][3][1])






# -----------------------------------------------------------------------------------------
# indexing in list
# -------------------------------------------------------


# x = [12,[120,89,56,[20,25]]]



# Extract :

# 89
# print(x[1][1])


# 25
# print(x[1][3][1])


# 120
# print(x[1][0])



# 12
# print(x[0])






# --------------------------------------------------------------------------------------
# slicing in list:
# ---------------------------------------------------------





# x = [[1,4,7,[9,8,6,10],[20,30,40]]]



# 1. [20,30]
# print(x[0][4][0:2])

# 2. [8,6]
# print(x[0][3][1:3])



# 3. [4,7]
# print(x[0][1:3])



# 4. [8,6,10]
# print(x[0][3][1:4])


# 5. [7,4,1]
# print(x[0][2::-1])


# 6. [40,30,20]
# print(x[0][4][2::-1])


# 7. [6,8,9]
# print(x[0][3][2::-1])


# 8. [10,6,8,9]
# print(x[0][3][-1::-1])






# -------------------------------------------------------------------------------------






x = ["DATA",34,22.3,89,12,"SCIENCE","PYTHON"]



# 1. Create a blank list and add all numerical data.

# y = []
# for i in x:
# 	if type(i)==int or type(i)==float:
# 		y.append(i)


# print(y)

# -----------------------------
# if i==x.isdigit()
# ----------------------------










# 2. Create a blcnk list and add all text data.

# y = []
# for i in x:
# 	if type(i)==str:
# 		y.insert(-1,i)
# print(y)






# 3. count total number of text in list.

# c=0
# for i in x:
# 	if type(i)==str:
# 		c+=1
# print(c)





# 4. Count total number decimal number in list

# c=0
# for i in x:
# 	if type(i)==float:
# 		c+=1
# print(c)









# 5. convert all text in small letter.

# for i in x:
# 	if type(i)==str:
# 		print(i.lower())







x = [12,45,78,89,5,6,23,23,12,45]




# 1. Create a  blank list and add all unique values.

# y = []
# for i in x:
# 	if i not in y:
# 		y.append(i)

# print(y)







# 2. Delete  first 23 from the list.

# y=x.remove(12)
# print(y)




# 3. Delete all 12 from the list.

# while 12 in x:
# 	x.remove(12)
# print(x)


# 4. Create a blank list and add all even number from x in the list .

y=[]
for i in x:
	if i%2==0:
		y.append(i)
print(y)