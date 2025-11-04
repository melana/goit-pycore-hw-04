def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts): # функція, яка обробляє команду add
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts): # функція, яка обробляє команду change
    name, phone = args
    contacts[name] = phone
    return "Contact updated."

def show_phone(args, contacts): # функція, яка обробляє команду phone
    name = args[0]
    phone = contacts[name]
    return phone

def show_all(contacts): # функція, яка обробляє команду all
    return contacts

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]: # обробляє команди close, exit
            print("Good bye!")
            break
        elif command == "hello": # обробляє команду hello
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
