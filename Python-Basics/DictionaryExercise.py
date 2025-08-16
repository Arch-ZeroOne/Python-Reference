import pprint
# TODO : Currently Doing the Practice Projects

message = "It was a bright cold day in April, and the clocks were striking thirteen."
count = {}

# Counts the occurences of character in a sentence
for ch in message:
    # Ensures that the character as a key is registered in the count dictionary
    count.setdefault(ch,0)
    # Stores each count to the designated key
    count[ch] = count[ch] + 1
    
# print(count)


# Pretty printing
"""
Makes the output much cleaner and organized usiing the pprint module
"""
# pprint.pprint(count)

spam = {'bar' : 100}
# Causes a key error
print(spam['foo'])