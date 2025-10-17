def parse_input(user_input: str) -> tuple[str, list[str]]:
    """
    Розбирає введений користувачем рядок на команду та аргументи.
    
    Args:
        user_input: Рядок введений користувачем
        
    Returns:
        tuple[str, list[str]]: Кортеж з команди та списку аргументів
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    """
    Додає новий контакт до словника контактів.
    
    Args:
        args: Список з ім'ям та номером телефону [name, phone]
        contacts: Словник контактів {name: phone}
        
    Returns:
        str: Повідомлення про результат операції
    """
    if len(args) != 2:
        return "Error: Invalid arguments. Usage: add [name] [phone]"
    
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    """
    Змінює номер телефону для існуючого контакту.
    
    Args:
        args: Список з ім'ям та новим номером телефону [name, phone]
        contacts: Словник контактів {name: phone}
        
    Returns:
        str: Повідомлення про результат операції
    """
    if len(args) != 2:
        return "Error: Invalid arguments. Usage: change [name] [new_phone]"
    
    name, phone = args
    
    if name not in contacts:
        return f"Error: Contact '{name}' not found."
    
    contacts[name] = phone
    return "Contact updated."


def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    """
    Показує номер телефону для вказаного контакту.
    
    Args:
        args: Список з ім'ям контакту [name]
        contacts: Словник контактів {name: phone}
        
    Returns:
        str: Номер телефону або повідомлення про помилку
    """
    if len(args) != 1:
        return "Error: Invalid arguments. Usage: phone [name]"
    
    name = args[0]
    
    if name not in contacts:
        return f"Error: Contact '{name}' not found."
    
    return contacts[name]


def show_all(contacts: dict[str, str]) -> str:
    """
    Показує всі збережені контакти.
    
    Args:
        contacts: Словник контактів {name: phone}
        
    Returns:
        str: Список всіх контактів або повідомлення про порожній список
    """
    if not contacts:
        return "No contacts saved."
    
    result: list[str] = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    
    return "\n".join(result)


def main() -> None:
    """
    Головна функція програми - управляє основним циклом обробки команд.
    
    Доступні команди:
        hello - Привітання бота
        add [name] [phone] - Додати новий контакт
        change [name] [phone] - Змінити номер телефону існуючого контакту
        phone [name] - Показати номер телефону контакту
        all - Показати всі збережені контакти
        close/exit - Вийти з програми
        
    Приклади використання:
        add John 1234567890
        change John 0987654321
        phone John
        all
    """
    contacts: dict[str, str] = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input: str = input("Enter a command: ")
        command, args = parse_input(user_input)
        
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        
        elif command == "hello":
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
