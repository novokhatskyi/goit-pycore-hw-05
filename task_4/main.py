from parse_input import parse_input
from add_contacts import add_contacts, change_contacts, get_phone, get_all_contacts


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "пока"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print (add_contacts(args, contacts))
        elif command == "change":
            print (change_contacts(args, contacts))
        elif command == "phone":
            print(get_phone(args,contacts))
        elif command == "all":
            print (get_all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
