from file_comparator import main

if __name__ == "__main__":
    # Вказуємо шляхи до наших тестових файлів
    file1_path = "file1.txt"
    file2_path = "file2.txt"

    print(f"Порівнюємо файли: {file1_path} та {file2_path}")
    main(file1_path, file2_path)

    # Виводимо результати для перевірки
    print("\nРезультати порівняння:")

    print("\nСпільні рядки (same.txt):")
    with open('same.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    print("\nУнікальні рядки (diff.txt):")
    with open('diff.txt', 'r', encoding='utf-8') as f:
        print(f.read())