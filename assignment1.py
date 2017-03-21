"""
Michael Fisher, 20/03/2017, CP1402 Assignment 1 - Reading List, https://github.com/CP1404-2017-1/a1-michaelfisher1
"""
VALID_CHOICES = ["R","r","C","c","A","a","M","m","Q","q"]
MENU_OPTIONS = "R - List Required books\nC - List completed books\nA - Add a book\nM - Mark a book as completed\n" \
               "Q - Quit"
BOOKS=[]

def get_menu_choice():
    print(MENU_OPTIONS)
    menu_choice = input(">")
    while menu_choice not in VALID_CHOICES:
        print("Invalid Menu Choice")
        print(MENU_OPTIONS)
        menu_choice = input(">")
    return menu_choice

def main():
    print("Reading List 1.0 - by <Michael Fisher>")
    user_menu_choice = get_menu_choice()
    in_file = open("temp.csv","r")
    for lines in in_file:
        details = lines.split(",")
        BOOKS.append(details)
    index = 0
    for i in BOOKS:
        if BOOKS[index][3] == "c\n":
            print("{:2}.{:36}{:15}{} pages".format(index,BOOKS[index][0], BOOKS[index][1], BOOKS[index][2]))
        index = index +1
if __name__ == '__main__':
    main()
