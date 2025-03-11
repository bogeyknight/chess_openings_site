def remove_posts_prefix(file_path):
    # Otwieramy plik w trybie odczytu
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Przetwarzamy linie, usuwając "/_posts" z każdej
    updated_lines = [line.replace(')', '.html)') for line in lines]

    # Zapisujemy zmieniony tekst do tego samego pliku
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(updated_lines)

    print("Gotowe! Fragment '/_posts' został usunięty ze wszystkich linii.")

# Wywołanie funkcji z nazwą pliku
file_path = '2025-03-06-chess-openings-list.md'
remove_posts_prefix(file_path)

