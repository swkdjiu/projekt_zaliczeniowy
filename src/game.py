import os

# Podstawowa logika gry - wybory i zasady
WYBORY = ["kamień", "nożyce", "papier"]

# Słownik: kto kogo bije
KTO_BIJE = {
    "kamień": "nożyce",
    "nożyce": "papier",
    "papier": "kamień"
}

def wyczysc_ekran():
    """Czyści terminal - gracz 1 nie zobaczy wyboru gracza 2."""
    os.system('cls' if os.name == 'nt' else 'clear')


def wyznacz_zwyciezce(wybor1: str, wybor2: str) -> str:
    """Porównuje dwa wybory i zwraca wynik: gracz1, gracz2 lub remis."""
    if wybor1 == wybor2:
        return "remis"

    if KTO_BIJE[wybor1] == wybor2:
        return "gracz1"

    return "gracz2"

def pobierz_wybor(nazwa_gracza: str) -> str:
    """Pyta gracza o wybór."""
    while True:
        print(f"\n{nazwa_gracza}, wybierz:")
        for numer, wybor in enumerate(WYBORY, start=1):
            print(f"  {numer}. {wybor}")

        odpowiedz = input("Twój wybór (1/2/3): ").strip()

        if odpowiedz in ("1", "2", "3"):
            wyczysc_ekran()  # czyścimy ekran po wyborze
            print(f"✅ {nazwa_gracza} wybrał(a). Teraz kolej na drugiego gracza!")
        return WYBORY[int(odpowiedz) - 1]

        print("Zły wybór! Wpisz 1, 2 lub 3.")


def zagraj_runde(imie1: str, imie2: str) -> str:
    """Przeprowadza jedną rundę i zwraca wynik."""
    wybor1 = pobierz_wybor(imie1)
    wybor2 = pobierz_wybor(imie2)

    print(f"\n--- Wyniki rundy ---")
    print(f"  {imie1}: {wybor1}")
    print(f"  {imie2}: {wybor2}")

    wynik = wyznacz_zwyciezce(wybor1, wybor2)

    if wynik == "remis":
        print("🤝 Remis!")
    elif wynik == "gracz1":
        print(f"🏆 Wygrywa {imie1}!")
    else:
        print(f"🏆 Wygrywa {imie2}!")

    return wynik