from colorama import Fore
from errors import input_error
@input_error
def add_contacts(args, contacts):
    # if len(args) !=2:
    #     return "Не правильно введено і\'я та номер телефону"
    name, phone = args
    contacts[name] = phone
    return f"Contact {Fore.BLUE}{name}{Fore.RESET} added!"
@input_error
def change_contacts(args,contacts):
    # if len(args) !=2:
    #     return "Не правильно введено і\'я та номер телефону"
    name, new_phone = args
    if name not in contacts:
        return f"Контакт {Fore.GREEN}{name}{Fore.RESET} не знайдено в списку контактів"
    else:
        contacts[name] = new_phone
    return f"Контакт {Fore.RED}{name}{Fore.RESET} оновлено"
@input_error
def get_phone (args, contacts):
    # if len(args) !=1:
    #     return "Помилка введення запиту. Потрібно ввести тільки ім\'я"
    name = args[0]
    if name in contacts:
        return f"Номер телефону контакту {Fore.YELLOW}{name}{Fore.RESET} - {contacts[name]}"
    else:
        return f"Контакт {args[0]} не знайдено в списку контактів"
@input_error    
def get_all_contacts (contacts):
    if not contacts:
        return f"Ваш списко пустий, додайте контакти"
    else:
        result = ""
        for name, phone in contacts.items():
            result += f"{Fore.RED}{name}{Fore.RESET}:{phone}\n"
        return result


if __name__== "__main__" :
    contacts = {}
    print(add_contacts(["Grisha", 50045476],contacts))
    print (contacts)