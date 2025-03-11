import os
import re

# Przygotowanie katalogu na podstrony, jeśli jeszcze nie istnieje
output_dir = "openings"
os.makedirs(output_dir, exist_ok=True)

# Odczytanie pełnych danych wejściowych
with open("2025-03-05-chess-openings-test-with-images.md", "r", encoding="utf-8") as file:
    content = file.read()

# Regex do znalezienia wszystkich otwarć szachowych
opening_pattern = r'(.*?)(?:\n{3,}|\Z)'

# Zastosowanie regexa na treści
matches = re.findall(opening_pattern, content, re.DOTALL)

# Zmienna na plik lista.md, który będzie zawierał linki do podstron
with open("lista.md", "w", encoding="utf-8") as lista_file:
    lista_file.write("# Lista Otwarć Szachowych\n\n")

    # Iteracja po wszystkich matchach
    for match in matches:
        # Pobranie nazwy otwarcia (pierwszy nagłówek, np. "Wing Gambit")
        opening_name_match = re.search(r"## (.*?)\n", match)
        if opening_name_match:
            opening_name = opening_name_match.group(1)
            # Dodanie linku do podstrony w pliku lista.md
            opening_link = f"openings/{opening_name.lower().replace(' ', '_')}.md"
            lista_file.write(f"- [{opening_name}]({opening_link})\n")

            # Tworzenie pliku .md dla danego otwarcia
            opening_file_name = os.path.join(output_dir, opening_link)
            with open(opening_file_name, "w", encoding="utf-8") as opening_file:
                opening_file.write(f"---\nlayout: post\ntitle: \"{opening_name}\"\n---\n\n")
                opening_file.write(match)  # Zapisanie pełnego matcha do pliku

print("Pliki zostały wygenerowane.")

