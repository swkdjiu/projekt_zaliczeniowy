from src.game import wyznacz_zwyciezce, WYBORY


def test_remis():
    assert wyznacz_zwyciezce("kamień", "kamień") == "remis"


def test_kamien_bije_nozyce():
    assert wyznacz_zwyciezce("kamień", "nożyce") == "gracz1"


def test_nozyce_bija_papier():
    assert wyznacz_zwyciezce("nożyce", "papier") == "gracz1"


def test_papier_bije_kamien():
    assert wyznacz_zwyciezce("papier", "kamień") == "gracz1"


def test_przegrany_zwraca_gracz2():
    assert wyznacz_zwyciezce("nożyce", "kamień") == "gracz2"