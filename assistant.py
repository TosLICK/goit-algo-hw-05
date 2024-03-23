def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command."
        except KeyError:
            return no_contact()

    return inner

@input_error
def parse_input(user_input): # парсимо ввод користувача
    cmd, *args = user_input.split() # розбиваємо ввод на команду (перший аргумент) і інші аргументи
    cmd = cmd.strip().lower() # команду приводимо до нижнього регістру
    return cmd, *args

@input_error
def add_contact(args: list, contacts: dict): # якщо введеного контакту в словнику немає, тоді додаємо контакт
    name, phone = args
    if name not in contacts:
        contacts[name] = phone
        return "Contact added."
    else:
        return "Contact already exists." # якщо введений контакт вже є в словнику, тоді виводимо відповідне повідомлення

@input_error
def change_contact(args: list, contacts: dict): # змінюємо номер телефону, якщо контакт присутній у словнику
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return no_contact() # якщо контакту немає, виводимо відповідне повідомлення

@input_error
def show_phone(args: list, contacts: dict): # виводимо номер телефону за заданим ім'ям контакту
        name = str(args[0])
        # if name in contacts:
        return f"{contacts[name]}"
        # else:
            # return no_contact() # якщо контакту немає, виводимо відповідне повідомлення

@input_error
def show_all(contacts: dict): # виводимо усі контакти з номерами телефонів
    if contacts:
        string = ''
        for name, phone in contacts.items():
            string += f"{name} {phone}\n"
        return string
    else:
        return "There are no contacts." # якщо контактів немає, виводимо відповідне повідомлення
    
def usage():
    return "Invalid command. Usage: 'hello'\n'close'\n'exit'\n'all'\n'add name phone_number'\n"\
            "'change name phone_number'\n'phone name'"

def no_contact():
    return "Contact does not exist."

@input_error
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        try:
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "phone": # and len(args) == 1:
                print(show_phone(args, contacts))
            elif command == "all":
                print(show_all(contacts))
            else:
                print(usage())
        except ValueError:
            print(usage())

if __name__ == "__main__":
    main()