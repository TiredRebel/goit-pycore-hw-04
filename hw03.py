import sys
from pathlib import Path
from colorama import Fore, Style, init

# Ініціалізація colorama для підтримки кольорів в Windows
init(autoreset=True)


def visualize_directory_structure(directory_path: Path, indent: str = "", is_last: bool = True) -> None:
    """
    Рекурсивно візуалізує структуру директорії з кольоровим виведенням.
    
    Args:
        directory_path: Шлях до директорії для візуалізації
        indent: Рядок для відступу (використовується для рекурсії)
        is_last: Чи є це останній елемент у поточному рівні
    """
    try:
        # Визначаємо символи для відображення структури
        connector: str = "┗ " if is_last else "┣ "
        
        # Виводимо ім'я поточної директорії
        if indent == "":
            # Це корінь - виводимо повний шлях
            print(f"{Fore.BLUE}📦 {directory_path.name or directory_path}{Style.RESET_ALL}")
        
        # Отримуємо список всіх елементів у директорії
        try:
            items: list[Path] = sorted(directory_path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
        except PermissionError:
            print(f"{indent}{connector}{Fore.RED}[Доступ заборонено]{Style.RESET_ALL}")
            return
        
        # Обробляємо кожен елемент
        for index, item in enumerate(items):
            is_last_item: bool = index == len(items) - 1
            
            if item.is_dir():
                # Це директорія - виводимо синім кольором з іконкою папки
                print(f"{indent}{connector}{Fore.BLUE}📂 {item.name}{Style.RESET_ALL}")
                
                # Рекурсивно обробляємо піддиректорію
                new_indent: str = indent + ("   " if is_last else " ┃ ")
                visualize_directory_structure(item, new_indent, is_last_item)
            else:
                # Це файл - виводимо зеленим кольором з іконкою файлу
                print(f"{indent}{connector}{Fore.GREEN}📜 {item.name}{Style.RESET_ALL}")
    
    except Exception as e:
        print(f"{Fore.RED}Помилка при обробці директорії: {e}{Style.RESET_ALL}")


def main() -> None:
    """
    Головна функція програми.
    Отримує шлях до директорії з аргументів командного рядка та візуалізує її структуру.
    """
    # Перевіряємо, чи передано аргумент командного рядка
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Помилка: Не вказано шлях до директорії{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Використання: python hw03.py <шлях_до_директорії>{Style.RESET_ALL}")
        sys.exit(1)
    
    # Отримуємо шлях до директорії
    directory_path_str: str = sys.argv[1]
    directory_path: Path = Path(directory_path_str)
    
    # Перевіряємо, чи існує шлях
    if not directory_path.exists():
        print(f"{Fore.RED}Помилка: Шлях '{directory_path}' не існує{Style.RESET_ALL}")
        sys.exit(1)
    
    # Перевіряємо, чи це директорія
    if not directory_path.is_dir():
        print(f"{Fore.RED}Помилка: '{directory_path}' не є директорією{Style.RESET_ALL}")
        sys.exit(1)
    
    # Візуалізуємо структуру директорії
    print(f"\n{Fore.CYAN}Структура директорії:{Style.RESET_ALL}\n")
    visualize_directory_structure(directory_path)
    print()  # Додаємо порожній рядок в кінці


if __name__ == "__main__":
    main()
