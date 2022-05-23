def try_me():
    answer = " "
    bad_teams = ["FC Barcelona", "Barcelona", "Atleti", "Atletico","Manchester United", "Manchester"]
    rm = ["Real Madrid", "Madrid", "RM"]
    while answer == " ":
        answer = input("best team?")
        if answer in bad_teams:
            return "LOL, don't even deserve another try"
        elif answer in rm:
            return "YES"
        else:
            answer = " "
            return "try again"

try_me()
