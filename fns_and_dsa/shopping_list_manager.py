#!/usr/bin/python3

## Shopping List Manager

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                add = input("Enter the name of the item you want to add: ")
                shopping_list += add
            case "2":
                rmv = input("Enter the name of the item you want to remove: ")
                shopping_list.remove(rmv)
            case "3":
                for item in shopping_list:
                    print(item)
            case "4":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
        