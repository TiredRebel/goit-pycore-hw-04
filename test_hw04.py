"""
Скрипт для тестування консольного бота hw04.py
"""
from hw04 import parse_input, add_contact, change_contact, show_phone, show_all


def test_bot() -> None:
    """Тестує всі функції бота."""
    print("=== Тестування консольного бота ===\n")
    
    # Тест 1: parse_input
    print("1. Тестування parse_input:")
    cmd, args = parse_input("add John 1234567890")
    print("   Input: 'add John 1234567890'")
    print(f"   Command: '{cmd}', Args: {args}")
    assert cmd == "add" and args == ["John", "1234567890"], "parse_input failed"
    print("   ✓ Пройдено\n")
    
    # Тест 2: add_contact
    print("2. Тестування add_contact:")
    contacts: dict[str, str] = {}
    result = add_contact(["John", "1234567890"], contacts)
    print(f"   add John 1234567890 -> {result}")
    assert result == "Contact added." and contacts["John"] == "1234567890", "add_contact failed"
    print("   ✓ Пройдено\n")
    
    # Тест 3: add_contact з неправильними аргументами
    print("3. Тестування add_contact з неправильними аргументами:")
    result = add_contact(["John"], contacts)
    print(f"   add John -> {result}")
    assert "Error" in result, "add_contact error handling failed"
    print("   ✓ Пройдено\n")
    
    # Тест 4: change_contact
    print("4. Тестування change_contact:")
    result = change_contact(["John", "0987654321"], contacts)
    print(f"   change John 0987654321 -> {result}")
    assert result == "Contact updated." and contacts["John"] == "0987654321", "change_contact failed"
    print("   ✓ Пройдено\n")
    
    # Тест 5: change_contact для неіснуючого контакту
    print("5. Тестування change_contact для неіснуючого контакту:")
    result = change_contact(["Alice", "1111111111"], contacts)
    print(f"   change Alice 1111111111 -> {result}")
    assert "not found" in result, "change_contact error handling failed"
    print("   ✓ Пройдено\n")
    
    # Тест 6: show_phone
    print("6. Тестування show_phone:")
    result = show_phone(["John"], contacts)
    print(f"   phone John -> {result}")
    assert result == "0987654321", "show_phone failed"
    print("   ✓ Пройдено\n")
    
    # Тест 7: show_phone для неіснуючого контакту
    print("7. Тестування show_phone для неіснуючого контакту:")
    result = show_phone(["Alice"], contacts)
    print(f"   phone Alice -> {result}")
    assert "not found" in result, "show_phone error handling failed"
    print("   ✓ Пройдено\n")
    
    # Тест 8: додавання кількох контактів
    print("8. Додавання кількох контактів:")
    add_contact(["Alice", "5555555555"], contacts)
    add_contact(["Bob", "6666666666"], contacts)
    print("   Додано Alice та Bob")
    print("   ✓ Пройдено\n")
    
    # Тест 9: show_all
    print("9. Тестування show_all:")
    result = show_all(contacts)
    print("   all ->")
    print(f"   {result}")
    assert "John" in result and "Alice" in result and "Bob" in result, "show_all failed"
    print("   ✓ Пройдено\n")
    
    # Тест 10: show_all для порожнього словника
    print("10. Тестування show_all для порожнього словника:")
    empty_contacts: dict[str, str] = {}
    result = show_all(empty_contacts)
    print(f"   all (порожній) -> {result}")
    assert result == "No contacts saved.", "show_all empty failed"
    print("   ✓ Пройдено\n")
    
    print("=== Всі тести пройдено успішно! ✓ ===")


if __name__ == "__main__":
    test_bot()
