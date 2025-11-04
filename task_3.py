
import sys
from pathlib import Path
from colorama import Fore


def tree_directory(directory, prefix=""): # функція для виведення дерева директорії
    directory = Path(directory)
    try:
        for el in directory.iterdir():
            if el.is_dir(): # виведення папок
                print(f"{Fore.BLUE}{prefix}{el.name}/")
                tree_directory(el, prefix + "    ") 
            else:  # виведення файлів
                 print(f"{Fore.GREEN}{prefix}{el.name}")
    except:
        print("Перевірте коректність введених даних")


def main():
    if len(sys.argv) != 2:
        print("Первірте коректність аргументів переданих в скрипт")
        sys.exit(1) # завершення програми, якщо передано невірну кількість аргументів в скрипт

    directory_path = sys.argv[1] # другим аргументом скрипту має бути директорія, яку необхідно відобразити
    tree_directory(directory_path)

if __name__ == "__main__":
    main()