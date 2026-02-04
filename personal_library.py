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

#User adds a new book to the library list
def addBook(library: list[str]):
    title = input("Enter book title: ").strip()
    library.append(title)
    print(f"Added: {title}")

def removeBook():
    pass

def listBooks(library: list[str]):
    if not library:
        print("The library is empty!")
        return
    print ("Book(s) in your library: ")
    for book in library:
        print(f' * {book}')

def searchBooks():
    pass

#Main program that loops showMenu() and lets user select an option
def main():
    library: list[str] = []

    while True:
        showMenu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            addBook(library)
        elif choice == "2":
            removeBook()
        elif choice == "3":
            listBooks(library)
        elif choice == "4":
            searchBooks()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, choose again")

if __name__ == "__main__":
    main()