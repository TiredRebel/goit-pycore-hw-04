def get_cats_info(path: str) -> list[dict[str, str]]:
    """
    Читає файл з інформацією про котів та повертає список словників.
    
    Args:
        path: Шлях до текстового файлу з даними про котів
        
    Returns:
        list[dict[str, str]]: Список словників з інформацією про кожного кота.
                              Кожен словник містить ключі: "id", "name", "age"
        
    Raises:
        FileNotFoundError: Якщо файл не знайдено
        ValueError: Якщо дані у файлі мають некоректний формат
    """
    cats: list[dict[str, str]] = []
    
    try:
        # Використовуємо менеджер контексту для читання файлу
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Видаляємо пробіли на початку та в кінці рядка
                line = line.strip()
                
                # Пропускаємо порожні рядки
                if not line:
                    continue
                
                try:
                    # Розділяємо рядок на id, ім'я та вік
                    parts: list[str] = line.split(',')
                    
                    if len(parts) != 3:
                        raise ValueError(f"Некоректний формат рядка: {line}")
                    
                    # Створюємо словник з інформацією про кота
                    cat_id: str = parts[0].strip()
                    cat_name: str = parts[1].strip()
                    cat_age: str = parts[2].strip()
                    
                    cat_info: dict[str, str] = {
                        "id": cat_id,
                        "name": cat_name,
                        "age": cat_age
                    }
                    
                    cats.append(cat_info)
                    
                except ValueError as e:
                    print(f"Попередження: не вдалося обробити рядок '{line}': {e}")
                    continue
        
        return cats
        
    except FileNotFoundError:
        print(f"Помилка: файл '{path}' не знайдено")
        raise
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
        raise


if __name__ == "__main__":
    # Приклад використання функції
    try:
        cats_info: list[dict[str, str]] = get_cats_info("cats_file.txt")
        print(cats_info)
    except Exception as e:
        print(f"Не вдалося виконати операцію: {e}")
