def total_salary(path: str) -> tuple[float, float]:
    """
    Аналізує файл із зарплатами розробників та повертає загальну та середню суму.
    
    Args:
        path: Шлях до текстового файлу з даними про зарплати
        
    Returns:
        tuple: Кортеж із двох чисел (загальна сума, середня зарплата)
        
    Raises:
        FileNotFoundError: Якщо файл не знайдено
        ValueError: Якщо дані у файлі мають некоректний формат
    """
    try:
        total: float = 0
        count: int = 0
        
        # Використовуємо менеджер контексту для читання файлу
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Видаляємо пробіли на початку та в кінці рядка
                line = line.strip()
                
                # Пропускаємо порожні рядки
                if not line:
                    continue
                
                try:
                    # Розділяємо рядок на ім'я та зарплату
                    parts: list[str] = line.split(',')
                    
                    if len(parts) != 2:
                        raise ValueError(f"Некоректний формат рядка: {line}")
                    
                    # Отримуємо зарплату та конвертуємо в число
                    salary: float = float(parts[1])
                    total += salary
                    count += 1
                    
                except ValueError as e:
                    print(f"Попередження: не вдалося обробити рядок '{line}': {e}")
                    continue
        
        # Перевіряємо, чи є дані у файлі
        if count == 0:
            return (0, 0)
        
        # Обчислюємо середню зарплату
        average: float = total / count
        
        return (total, average)
        
    except FileNotFoundError:
        print(f"Помилка: файл '{path}' не знайдено")
        raise
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
        raise


if __name__ == "__main__":
    # Приклад використання функції
    try:
        total, average = total_salary("salary_file.txt")
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    except Exception as e:
        print(f"Не вдалося виконати операцію: {e}")
