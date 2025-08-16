import pprint
myCat = {
    'size' : 'fat',
    "color": "gray" , 
    "disposition" : 'loud'
}

myCat2 = {
    'color':"gray",
    'size' : "fat",
    'disposition':"loud"
}



# print("MyCat and MyCat2 is equal :",myCat == myCat2)


#Printing all values
# print(myCat)

#Printing a value using a specific key

# print("Size of the Cat:",myCat['size'])


# prints the  keys
# for keys in myCat:
#     print(keys)
    
# prints the values
# for index in myCat:
#     print(myCat[index])

# birthdays = {
#     'Alice':"Apr 1", 
#     'Bob':'Dec 12', 
#     'Carol': 'Mar 4' 
#     }

# while True:
#     print("Enter a name:(Blank to quit)")
#     name = input()
    
#     if name == "":
#         break
    
#     if name in birthdays:
#         print(birthdays[name], "is the birthday of ",name)
#     else:
#         print("I do not have birthday information for ",name)
#         print("What is their birthday?")
#         bday = input()
#         birthdays[name] = bday
#         print("Database has been updated !!")
#         print("Database Status:",birthdays)

#* Methods




spam = {"color":'red' , "age" : 42}

#? Values(values()) Method 
"""
This method prints the actual values of the dictionary
"""

# for x in spam.values():
#     print(x)

#? Keys(keys()) method
"""
This method prints the keys available in the dictionary
"""
# for x in spam.keys():
#     print(x)

#? Items(items()) method
"""
Returns a tuple of both key and values
"""
# for x in spam.items():
#     print(x)


#? List(list()) method
"""
Returns a list like value from a dictionary
"""

# keys = spam.keys()
# print(list(spam.keys()))


# Getting both key and value while iterating
# for x, y in spam.items():
#     print("Key: ", x , " Value:", str(y))
    



spam = {"name":'Zophie' , "age" : 7, "color":"brown"}

# Checking if a key or value exists in a Dictionary
# print('name' in spam.keys())
# print("color" in spam.keys())

# Checking if a key or value does not exists in a Dictionary
# print("age" not in spam.keys())
# print("gender" not in spam.keys())


#* The Get (get()) method
"""
- Takes two argument the key of the value you want to access and the fallback if the value does not exist
- This is important because it prevented specific errors when accessing a non existing value
"""
picnicItems = {"apples" : 5 , "cups" : 2}
# print(picnicItems.get("appless","Walay Value")) 

#? The Set Default(setDefault()) Method
"""
- This method will set a default value to a dictionary that has a value and a Key
- This method only works if the key doesn't exist
"""

spam = {"name": "Pooka", "age" : 5}

if 'color' not in spam:
    spam['color'] = 'black'
    
# print(spam)


# Doing the same with one life of code
spam.setdefault("color","red")
spam.setdefault('isMale',False)
# print(spam)



#? Nested Dictionaries and Lists

allGuests = {
    'Alice' : {"apples" : 5 , "pretzels": 12},
    'Bob' : {"ham sandwiches": 3, "apples" : 2 },
    'Carol' : {"cups" : 3 ,"apple pies" : 1 }
    }

pprint.pprint(allGuests)


for x in allGuests.values():
    if x == "apples":
        print(x)



def totalBrought(guest, item):
    numBrought = 0
    for key, value in guest.items():
        # Gets the actual value or the default value if the specific key is not present (0)
        
        numBrought = numBrought + value.get(item,0)
    return numBrought



print("Total Apples:",str(totalBrought(allGuests,"apples")))
# print(str(totalBrought(allGuests,"pretzels")))