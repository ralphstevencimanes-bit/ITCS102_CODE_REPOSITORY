#anime concept
fantasy = []
adventure = []
isekai = []
korean = []
shonen = []

while True:
    ans = input("Do you watch or read any anime ---? yes / no ").lower()

    if ans == 'yes':
        print("what kind of anime do you watch or read ")
        print("1 fantasy \2 adventure \3 isekai \4 korean \5 shonen ")

        choice = int(input("Input --> "))
        if choice == 1:
            print("fantasy")
        title = input("input the title of anime --> ")
        fantasy.append("title")
        print(fantasy)
        con = input("Do you continue? ---> ")
        if con == 'yes':
            continue
        else:
            break

    else:
        print("Invalid Choice")