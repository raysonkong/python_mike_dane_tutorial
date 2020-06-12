# 1:10:51 
# List Functions
lucky_number = [100, 4,8,15,16,23,42]
friends = ["Kevin", "Karen","Jim", "Jim", "Jim", "Oscar", "Toby", "Jim", "Jim"]


# extend a list by another list
friends.extend(lucky_number)
print(friends)


# Add a single element to a list
friends.append("Creed")
print(friends)


# insert an element into a certain positon in the list
friends.insert(1, "Kelly")
print(friends)


# remove a particular element
friends.remove("Jim")
print(friends)


# clear list
#friends.clear()

# remove last element and return the last element
print(friends.pop())  # returns popped element(last element)
print(friends)  # last element removed


# check if certain element is in the list
# if not in list => error
print(friends.index("Kevin"))



# count elements
print(friends.count("Jim"))



# sort a list in ascending order
lucky_number.sort()
print(lucky_number)

new_friends = ["Kevin", "Karen", "Jim"]
new_friends.sort()
print(new_friends)




# sort in descending order (reverse)
print(lucky_number.reverse())

print(lucky_number)



# copy a list
# copy is pass by value (sort of)
# if you just do list1 = list2, then it is pass by reference (both variables pointing at the same object)
numbers1 = [1,2,3,4,5]
numbers2 = numbers1.copy()

numbers1.pop()
print(f"numbers1 after pop: {numbers1}")
print(f"numbers2 after ... {numbers2}")



# more shallow copy
# it means (my own words, need to confirm later)
# the array itself is pass-by-value
# but the elements are pass-by-reference
# how do you visualize it?
# a copied array here is just a different catalogue pointing to the same products in the warehouse

guitars1 = ["Ibanez", ["Fender"], "Schecter", "Shur"]
guitars2 = guitars1.copy()
guitars1[1][0] = "Whatever"

print(guitars1) # [ibanez, [whatever], schecter, shur]
print(guitars2) # [ibanez, [whatever], schecter, shur]


guitars3 = ["Ibanez", "Fender", "Schecter", "Shur"]
guitars4 = guitars3.copy()

guitars3[1] = "whatever"
print(guitars3) # [ibanez, whatever, schecter, shur]
print(guitars4) #[ibanez, fender, schecter, shur]

