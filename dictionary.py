

print("-" *70)

# ----------------------------------------------------------------------------
# ------------------------------ DICTIONARY ----------------------------------
# ----------------------------------------------------------------------------

# Dictionary are written with curly brackets and have keys and values.
# Dictionary is a collection of Non-Repitative keys. 


# 1. Dictionary are written in Curly bracket and have key and value pair.
# 2. Dict do not allow duplicate keys.
# 3. Dict are changable.
# 5. Dict are un-indexed .
# 6. store multiple type of data.




# Dictionary are odered , changable , and does not allow the duplicate values

# dictionary item are presented in keys : values pairs, and can be refferd to by using




# -------------------------------------

# How to create a blank dictionary ? 
# x = dict()
    # or
# y = {}

# print(type(x))
# print(type(y))





# x = {1:"one",2:"Two",3:"Three"}
# print(x)
# print(len(x))
# print(type(x))





# mobile={
# 	"Brand":["Realme","Apple","MI"],
# 	"Model":["3-pro","6x","I7"],
# 	"Colour":["Black","White","Green"],
# 	"Year":[2015,2016,2019]
# }
# print(mobile["Brand"])
# print(mobile["Year"])







# x = {"Name":"Love sharma",
# 	"Age":23,
# 	"City":"Delhi",
# 	"Job role":"Data Analyst"
	
# }
# print(x)
# print(len(x))





# ----------------------------------------------------


# Show the keys from the dictionary.

# keys() :- it extract all the keys from dictionary. 
# values() :- it exttract the total values from the dictionary.






# x = {"Name":"Love sharma",
# 	"Age":23,
# 	"City":"Delhi",
# 	"Job role":"Data Analyst"
	
# }

# a = x.keys()
# print(a)

# v = x.values()
# print(v)



# -------------------------------------------------------


# dic = {"Haryana":"Chandigarh",		
# 	"Bihar":"Patna",
# 	"Uttar pradesh":"Lucknow",
# 	"Assam":"Dispur",
# 	"Goa":"Panji"	
# }

# x = str(input("Enter the name of the sate :-  ")).title()
# y = dic[x]

# print(f"The capital of {x} is : {y}")





# ----------------------------------
# dic = {"Haryana":"Chandigarh",		
# 	"Bihar":"Patna",
# 	"Uttar pradesh":"Lucknow",
# 	"Assam":"Dispur",
# 	"Goa":"Panji"	
# }




# How to add the key and values in the Dictionary ?

#  1. update :- With the help of this function we can add single or multiple 
#             keys and values in dictionary.


# Adding single key and variable in the dictionary 

# dic.update({"Punjab":"Chandigarh"})
# print(dic)






# Adding multiple key and vlaue .

# y = {1:"one",2:"two",3:"three"}

# dic.update(y)
# print(dic)





# Adding the keys and values in dictionary using without formula . 

# x = {1:"one",2:"Two",3:"Three",4:"four"}

# 2. without:- 


# x[5]="five"
# x[6]="six"
# x[10]="one"

# print(x)




# ---------------------------------------------------------





# Create a Dictionary with the help of user input

# dic = {}
# x = int(input("Enter the length of  dictionary :- "))
# for i in range(x):
# 	key = input("Enter key :- ")
# 	val = input("Enter values :- ")
# 	dic[key] = val

# print(dic)







# Create a list with the help of user input

# l = []
# x = int(input("Enter the length of list :- "))
# for i in range(x):
# 	v = eval(input("Enter the data :- "))
# 	l.append(v)

# print(l)





# Create a tuple with the help of user input

# t = []
# x = int(input("Enter the length of the tuple:- "))
# for i in range(x):
# 	v = eval(input("Enter the data :- "))
# 	t.append(v)
# f=tuple(t)
# print(f)




# Create a set with the help of user input

# s = set()
# x = int(input("enter the length of set:- "))

# for i in range(x):
# 	v = eval(input("Enter the data:- "))
# 	s.add(v)

# print(s)

 # or


# x = set()
# for i in range(int(input("Enter the length:- "))):
# 	el = eval(input(f"Enter {i+1} value :- "))
# 	x.add(el)

# print(x)





# ------------------------------------------------------






             # ------------------
# Convert all keys to values and all values to keys.
# sort the dictionary by values 
# ----------------------------------------------------------






# Convert all keys to values and all values to keys.

# x = {2:"Two",1:"One",4:"Four",3:"Three"}
# y = {}
# for i,j in x.items():
	# y[j] = i
# 	y.update({j:i})
	
# print(y)



# sort the dictionary by values 


# x = {2:"Two",1:"One",4:"Four",3:"Three"}
# print(x)

# y = sorted(x.items(),key=lambda a:a[0])
# print(y) 
# x = dict(y)
# print(x)




# x = {2:"two",1:"One",4:"Four",3:"Three",7:"seven",9:"nine",10:"ten"}

# 1. Create a new dictionary and add all keys and values whose name startswith
#     t and s .

# y={}
# for i,j in x.items():
# 	if j.startswith("t") or j.startswith("s"):
# 		y[i]=j

# print(y)






# 2. print the keys and values whose number is less than 6.

# y={}
# for i,j in x.items():
# 	if i<6:
# 		x.update({i:j})

# print(y)









# 3. Print dictionary whose value does not contain "o"

# y={}
# for i,j in x.items():
# 	if "o" not in j:
# 		print(i,":",j)







# convert all values into capital letter.

# for i,j in x.items():
# 	j.upper()
# 	print(i,"--",j)








# -----------------------------------------------------------------------



















# --------------------------------------------------------------



# Dictionary

# dictionary are written in curly brackets, and have keys and values
# dictionary is a collection of non repitative keys.

# 1. dic are written in curly bracket and have key and value pair
# 2. dic do not allow duplicate keys.
# 3. dic are ordered.
# 4. dic are changeable
# 5. dic are unindexed
# 6. store multiple type of data.

# ----------------------------------------------------

# how to create a blank dictionary

# x = dict()
# y = {}
# z = set()
# print(type(x))
# print(type(y))
# print(type(z))


# -------------------------------------------------------

# x = {1:"ONE",2:"TWO",3:"THREE"}

# print(x)
# print(len(x))
# print(type(x))

# mob = {
# 	"Brand" : ["Realme","Apple","MI"],
# 	"Model" : ["3-pro","6x","I7"],
# 	"Color"	: ["Black","White","Green"],
# 	"Year"	: [2015,2016,2017]
	
# }

# print(mobile)
# print(mobile["Brand"])
# print(mobile["Year"])

# Show the keys from dictionary

# keys() :- it returns the total keys from the dict.
# values() :- it returns the total values from the dict


# a = mob.keys()
# print(a)

# b = mob.values()
# print(b)


# create a dictionary name of students and add students name,roll no,city and marks

# s = {
# 	"Name": ["Ram","Shyam","Rohan"],
# 	"Roll No" : [1,2,3],
# 	"City" : ["Delhi","Punjab","UP"],
# 	"Marks" : [54,84,45]

# }

# print(s)
# print(s["Name"])
# print(s["Roll No"])
# print(s["City"])
# print(s["Marks"])


# ----------------------------------------------------------------

# dic = {
# 	"Delhi" : "New Delhi",
# 	"Bihar" : "Patna",
# 	"Uttar Pardesh" : "Lucknow",
# 	"Haryana" : "Chandigarh",
# 	"Assam" : "Dispur"
	
# }

# print(dic)

# x = str(input("Enter the Name of State :- ")).title()

# y = dic[x]

# print(f"The Capital of {x} is : {y}")


# -----------------------------------------------------------------------

# how to add key and values in dictionary

# update :- with the help of thiss function we can add single or multiple keys
# and values in dictionary 


# adding single key and value

# dic.update({"Chennai" : "Tamil Nadu"})

# print(dic)


# # adding multiple key and value

# dic.update({1:"one",2:"two",3:"three"})
# print(dic)

# # adding the key and value without formula

# dic["Gujrat"] = "Ahemdabad"
# dic[4] = "four"
# print(dic)



# # create the dict with the help of user input

# x = int(input("enter length of dict :- "))
# dic = {}
# for i in range(x):
# 	key = input("Enter key :- ")
# 	val = input("Enter value :-")
# 	dic[key] = val
# print(dic)







# create a list with the help of user input
# x = []
# for i in range(int(input("Enter Length of list :- "))):
# 	val = eval(input(f"Enter {i + 1} value :- "))
# 	x.append(val)
# print(x)




# create a tuple with the help of user input
# x = []
# for i in range(int(input("enter length of tuple :- "))):
# 	v = eval(input(f"enter {i+1} value :- "))
# 	x.append(v)
# x = tuple(x)
# print(x)






# create a set with the help of user input
# x = set()
# for i in range(int(input("enter length of set:- "))):
# 	v = eval(input(f"enter {i+1} value :-"))
# 	x.add(v)
# print(x)

# ------------------------------------------------------------------

# dictionary functions

# key() :- it shows total keys
# value() :- it shows total values
# get() :- it shows value according to keys
# items() :- it shows keys and values list of tuple
# update () :- add keys and values in dict
# x[key] = values


# car = {"Brand" : "BMW",
# 	"Model" : "tr34",
# 	"Fuel" : ["Petrol","CNG"],
# 	"Year" : 2017,
# 	"Color" : "White"
# }

# print(car)

# # 1. show the all key from dict.
# a = car.keys()
# print(a)



# # 2. Show fuel type of car.
# print(car["Fuel"])



# # 3. show the brand of car.
# print(car["Brand"])
# print(car.get("Brand"))

# # 4. Add high speed feature in Car.
# car["High Speed"] = 450

# print(car)

# # 5. Add price of car
# car.update({"Price" : "Rs.50Lakh"})

# print(car)


# car = {"Brand" : "BMW",
# 	"Model" : "tr34",
# 	"Fuel" : ["Petrol","CNG"],
# 	"Year" : 2017,
# 	"Color" : "White"
# }


# how to delete functions in dictionary

# clear():- it delete all keys and values from dict
# car.clear()
# print(car)


# pop() :- it delete keys and values according to mentioned item
# car.pop("Brand")
# print(car)


# popitem():- it delete the last value from dictionary by default
# car.popitem()
# print(car)


# del :- delete the values according to keys or dict
# del car["Model"]
# print(car)


# Items :- it shows the list and value in list of tuple

# print(car.items())

# for i in car.items():
# 	print(i)


# x = {2:"Two",3:"Three",5:"Five",4:"Four"}

# a = sorted(x.items())

# x = dict(a)

# print(x)
# print(type(x))


# convert all keys to values  and values to keys
# y = x.copy()
# x.clear()

# for i,j in y.items():
# 	x[j] = i
# print(x)

# sort the dictionary by values

# a = sorted(x.items(),key=lambda b:b[0]) #sorting the value 
# 										#if we use 0 then sorting aaccording to keys

# x = dict(a)

# print(x)


# -------------------------------------------------------------------------

# x = {2:"Two",1:"one",4:"Four",3:"three",6:"six",
# 		5:"five",9:"nine",8:"eigth",10:"ten",7:"seven"}



# ------------------------------------------------------------------------

# Nested Dictionary

# st1 = {"Name":"raghav","marks":456,"city":"Delhi"}

# st2 = {"Name":"paras","marks":356,"city":"noida"}

# st3 = {"Name":"ruhi","marks":466,"city":"haryana"}

# st4 = {"Name":"harsh","marks":436,"city":"new delhi"}



# student = {1:st1,2:st2,3:st3,4:st4}


#print(student[4]["marks"])


# d = {
# 				"car":{"Brand":"TATA","Model":"Nexon","Year":2015},
# 				"Bike":{"Brand":"RE","Model":"Standard","Year":2019}
	
# }


# print(len(d))


# # 1. show the details of bike
# print(d["Bike"])



# # 2. show the model of car
# print(d["car"]["Model"])


# # 3. sort the dict of car
# a = sorted(d["car"].items())
# d = dict(d)

# d["car"] = a

# print(d)

# # 4. change the model of bike

# d["Bike"]["Model"] = "Classic"
# print(d)













x = {"suraj singh":{"suraj singh":1,"maths":45,"eng":56,"sst":87,"science":89,"hindi":76},
	"Raghav sharma":{"maths":49,"eng":86,"sst":67,"science":87,"hindi":16},
	"manish yadav":{"maths":95,"eng":66,"sst":77,"science":49,"hindi":16},
	"priyanshu raj":{"maths":85,"eng":78,"sst":76,"science":59,"hindi":36}
}

# print(x)

# show the maths marks of suraj kumar

# a = x["suraj singh"]["maths"]
# print(a)




# show the maths of hindi of priyanshu raj 

# a = x["priyanshu raj"]["hindi"]
# print(a)


name = input("enter the name of student:- ")
y = x[name]
z = y.value()
marks = sum(z)

per = marks/5

if per>=60:
	div="First division"
elif per>=45:
	div="second division"
elif per>=33:
	div="third division"
else:
	div="fail"




print(marks)
print(per)
print(div)
