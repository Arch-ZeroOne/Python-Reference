# a = int(input("Enter num1:"))
# b = int(input("Enter num2:"))
#
# # if statements relies on indentation , no indentation will cause an error
# if   a > b:
#     print(f"{a} is greater than {b}")
# elif a < b:
#     print(f"{a} is less than to {b}")
# else :
#     print(f"{b} is equal {a}")


hasConsent = False
print("+- Welcome To The Movie Theater -+")
age = int(input("What is your age: "))

if age < 13:
    print(f"You are underage you are {age} and not allowed to watch the movie")
elif age >= 13 and age <= 17:
    cons = input("Do you have a parental consent (yes/no):")
    if cons == "yes":
        print("Acces granted with parental consent")
    else:
        print("Access denied")
else :
    print("Access granted, enjoy the movie")


