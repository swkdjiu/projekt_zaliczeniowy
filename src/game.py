# Podstawowa logika gry - wybory i zasady
WYBORY = ["kamień", "nożyce", "papier"]

# Słownik: kto kogo bije
KTO_BIJE = {
    "kamień": "nożyce",
    "nożyce": "papier",
    "papier": "kamień"
}


def wyznacz_zwyciezce(wybor1: str, wybor2: str) -> str:
    """Porównuje dwa wybory i zwraca wynik: gracz1, gracz2 lub remis."""
    if wybor1 == wybor2:
        return "remis"

    if KTO_BIJE[wybor1] == wybor2:
        return "gracz1"

    return "gracz2"