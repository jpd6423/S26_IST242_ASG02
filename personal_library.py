# Simple Personal Library
# Author: Joris Daub
# Version: 1

#Displays main menu options
def showMenu():
    print("\nPersonal Library Menu:")
    print("1. Add book")
    print("2. Remove book")
    print("3. List all books")
    print("4. Search for book")
    print("5. Exit")

def addBook():
    pass

def removeBook():
    pass

def listBooks():
    pass

def searchBooks():
    pass

#Main program that loops showMenu() and lets user select an option
def main():
    while True:
        showMenu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            addBook()
        elif choice == "2":
            removeBook()
        elif choice == "3":
            listBooks()
        elif choice == "4":
            searchBooks()
        elif choice == "5":
            break
        else:
            print("Invalid option, choose again")

if __name__ == "__main__":
    main()