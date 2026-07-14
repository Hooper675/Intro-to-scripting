abbreviation = { "LOL":"Laugh out loud",
                 "BFN":"Bye for now",
                 "FTW":"For the win",
                 "IRL":"In real life",
                 "JK" :"Just kidding",
                 "TTYL":"Talk to you later",
                 "LMK" : "Let me know",
                 "NKR" : "Not work related" }

user_input = input("Enter the abbreviation here:")

for abbr, value in abbreviation.items():
    if abbr in user_input:
        print(f"{abbr} : {value}")
    else:
        print("Unknown")


