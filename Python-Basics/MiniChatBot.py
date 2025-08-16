responses = {
    "Who are you" : "I am Jarvis an AI Made by Windyl from scratch using python",
    "Who is your owner":"My Owner is Windyl P. Monton a BSIT Student",
    "Who is Windyl": "Windyl Is an Upcoming 3rd Year Student and is Passionate about learning and becoming a software engineer",
    "What is His Skills":"His skills revolves mostly in web development specifically: React,Html5, CSS, Javascript, PHP, Laravel, Mongo DB, MYsql",
    "What is your purpose": "My purpose is simple it is just to test if My owner understand the concept of dictionaries in Python",
    "What is your owner's goal why is he learning python?":"My Owner Is Aiming to build his first Machine Learning Project and enhanced his skill",
    "What does your owner love?":"My Owner loves to code all the time, but he also loves someone now who is Named Jellian a beautiful and kind girl who has done so much for him and the first one who treated him very well"
}


while True:
    print("----------------------------------------------------")
    print("(: Welcome to Jarvis AI :)")
    print("----------------------------------------------------")
    print("User:")
    response = input()
    
    if response in responses:
        print("")
        print("Chatbot:",responses[response])
        print("")
    elif response == "":
        break
    
    