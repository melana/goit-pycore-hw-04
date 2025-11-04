
def total_salary(path: str):
    try:
        with open(path, "r", encoding='utf-8') as file:
            salary_info = [el.strip().split(",") for el in file.readlines()] # зчитуємо дані з файлу
            salary = [int(el[1]) for el in salary_info] # створюємо list, в якому лише інформація про зарплати
            
            total = sum(salary) # загальна сума заробітної плати
            average = int(sum(salary)/len(salary)) # cередня заробітна плата

            return total, average
    except:
        print("Перевірте, чи правиль вказаний шлях до файлу.")


total, average = total_salary("task-1/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")