


# =======================================================================
#                  ------------- SET ----------------
# =======================================================================




# SET:- SET is a collection of non-repitative elements.

# 1. Set is written in curly bracket.
# 2. Set dont allow duplicate value.
# 3. set are un-ordered.(when we take output , it will always be diffrent)
# 4. set are not indexed .
# 5. set are changable .
# 6. set allows multiple type of data.





# x = {"first","one","ten",10,45}
# print(x)



# x = {90,90,87,76,56,67,67,67,67}
# print(x)
# print(type(x))
# print(len(x))




# -------------------------

# How to delete the value from the set ?

# clear():- it is same as it works in list as it clear all value from the set.
# x.clear()

# pop():- it delete any one random value from the set.
# x.pop()

#remove():- it remove the named variable that we are giving in the formula.
# x.remove()


# -----------------------------------


# How to add data in set ?

# x = {"one","two","three","four"}
# print(x)



# add():- this function add the value in the end of set. 

# x.add("five")
# print(x)






# update():-

# x.update(["six"])
# print(x)









# union():= 

# x={56,12,454,67,88,66,12}
# y={34,234,4,5,6,7,6,5,12}

# x=x.union(y)
# print(x)








# x = {"Fruits","Animal","Birds","animal","birds","fruits"}
# print(x)


# 1. Delete the last value form the set

# x=list(x)
# x.pop()
# x=set(x)
# print(x)




# 2. add "tiger" in set

# x.add("tiger")
# print(x)


# 3. first five even Number in set

# y={2,4,6,8,10}
# x.update(y)
# print(x)








# 4. add your name with add  function . 


# x.add("love")
# print(x)








# 5. remove all duplicate value from set.

# y=set()
# for i in x:
# 	i = i.title()
# 	y.add(i)
# print(y)












# symmetric_difference()	Returns a set with the symmetric differences of two sets
                         # (we use this function when we want to extract the value frm two sets and seprate in both.)


# (here we have to take a variable in which we assign the function)




# x={1,2,3,4}
# y={3,4,5,6}


# z=x.symmetric_difference(y)
# print(z)








# symmetric_difference_update()	inserts the symmetric differences from this set and another

# (same as symmetric difference but here we will not take the variable )

# x={1,2,3,4}
# y={3,4,5,6}

# x.symmetric_difference_update(y)
# print(x)





# difference()	Returns a set containing the difference between two or more sets


# x={1,2,3,4}
# y={3,4,5,6}

# a=x.difference(y)
# print(a)





# difference_update()	Removes the items in this set that are also included in another, specified set

x={1,2,3,4}
y={3,4,5,6}

x.difference_update(y)
print(x)



# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
