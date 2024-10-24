import os
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"  # Resetowanie koloru
YELLOW = "\033[93m"
# Inicjalizacja pustego słownika
result = {}

# Wczytanie istniejących UID z pliku
if os.path.exists('result.txt'):
    with open('result.txt', 'r') as file:
        for line in file:
            uid, url = line.strip().split(": ")
            result[uid.strip('"')] = url.strip('"')

# Wyświetlenie opcji
print("##################################################")
print("#                    1. 1A                       #")
print("#                    2. 2A                       #")
print("#                    3. 3B                       #")
print("#                    4. 3C                       #")
print("#                    5. 4A                       #")
print("##################################################")

# Pętla, aby umożliwić wybór URL
while True:
    # Pobranie numeru URL od użytkownika
    n = input("Podaj numer URL (1-5) lub 'q' aby zakończyć: ")
    if n.lower() == 'q':
        break  # Zakończ program, jeśli użytkownik wprowadzi 'q'

    # Sprawdzenie, czy numer URL jest poprawny
    if n not in ['1', '2', '3', '4', '5']:
        print(f" {RED}Nieprawidłowy numer URL. Spróbuj ponownie. {RESET}")
        continue

    # Wybór odpowiedniego URL-a na podstawie numeru
    url = f"{n}/index.html"

    # Wprowadzanie UID dla wybranego URL
    while True:
        u = input(f"{GREEN}Podaj numer UID dla URL{RESET}{YELLOW} (lub 'w'- wyniki,'q'- exit):{RESET}")
        if u.lower() == 'q':
            break  # Zakończ pętlę, aby wrócić do wyboru URL
        elif u.lower() == 'w':
            # Wyświetlenie wyników
            print("\nWyniki:")
            for uid, url in result.items():
                print(f'"{uid}": "{url}",')
            print()  # Pusta linia dla przejrzystości
            continue  # Kontynuuj, aby wprowadzać więcej UID

        # Sprawdzenie, czy UID już istnieje
        if u in result:
            print(f" {RED}Ten UID już istnieje. Wprowadź inny UID.{RESET}")
            continue

        # Dodanie do słownika
        result[u] = url
        print(f'Dodano: "{u}": "{url}",')  # Wyświetlenie bieżącego wpisu

# Zapisanie wyników do pliku
with open('result.txt', 'w') as file:
    for uid, url in result.items():
        file.write(f'   "{uid}": "{url}",\n')

# Wyświetlenie końcowego wyniku
print("\nKońcowy wynik:")
for uid, url in result.items():
    print(f'"{uid}": "{url}",')

# Opcjonalnie: czekanie na naciśnięcie klawisza przed zakończeniem programu
input("Naciśnij Enter, aby zakończyć...")
