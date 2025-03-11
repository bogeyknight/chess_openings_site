import re

# Funkcja do wczytania zawartości pliku markdown
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()

# Funkcja do zapisania zmienionej zawartości do pliku markdown
def write_file(filename, lines):
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lines)

# Funkcja do pobrania mapy otwarć i ich ścieżek do obrazów z pierwszego pliku
def extract_images_from_first_file(lines):
    image_map = {}
    current_opening = None

    for line in lines:
        # Znajdź nazwę otwarcia
        if line.startswith("## "):
            current_opening = line[3:].strip()
        # Znajdź ścieżkę do obrazu i zapisz ją pod nazwą otwarcia
        elif line.startswith("!["):
            image_path = re.search(r'\(([^)]+)\)', line).group(1)
            if current_opening:
                image_map[current_opening] = image_path

    return image_map

# Funkcja do dodania obrazów do drugiego pliku
def add_images_to_second_file(lines, image_map):
    updated_lines = []
    current_opening = None

    for line in lines:
        updated_lines.append(line)

        # Znajdź nazwę otwarcia
        if line.startswith("## "):
            current_opening = line[3:].strip()

        # Dodaj obrazek po nazwie otwarcia
        if current_opening and current_opening in image_map and not line.startswith("!["):
            updated_lines.append(f"![{current_opening}]({image_map[current_opening]})\n\n")
            current_opening = None  # Reset po dodaniu obrazu

    return updated_lines

# Wczytanie plików markdown
first_file_lines = read_file('2025-03-05-chess-openings.md')
second_file_lines = read_file('2025-03-05-chess-openings-test.md')

# Pobranie mapy otwarć i obrazów z pierwszego pliku
image_map = extract_images_from_first_file(first_file_lines)

# Dodanie obrazów do drugiego pliku
updated_second_file_lines = add_images_to_second_file(second_file_lines, image_map)

# Zapisanie wyników do nowego pliku
write_file('2025-03-05-chess-openings-test-with-images.md', updated_second_file_lines)

print("Obrazy zostały dodane do drugiego pliku.")

