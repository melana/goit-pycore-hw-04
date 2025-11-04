
def get_cats_info(path: str):
    try:
        key = {"id": None, "name": None, "age": None} # шаблон рядка
        cats_info = []
        with open(path, "r", encoding="utf-8") as file: 
            for line in file:
                values = line.strip().split(",") # зчитуємо дані з файлу
                record = dict(zip(key.keys(),values)) # розпаковуємо дані 
                cats_info.append(record)  
            
            return cats_info
    except:
        print("Перевірте, чи правиль вказаний шлях до файлу.")


cats_info = get_cats_info("task-2/cats_file.txt")
print(cats_info)
