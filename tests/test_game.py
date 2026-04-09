import pytest
from src.game import wyznacz_zwyciezce, WYBORY, KTO_BIJE


def test_remis():
    assert wyznacz_zwyciezce("kamień", "kamień") == "remis"
    assert wyznacz_zwyciezce("nożyce", "nożyce") == "remis"
    assert wyznacz_zwyciezce("papier", "papier") == "remis"


def test_kamien_bije_nozyce():
    assert wyznacz_zwyciezce("kamień", "nożyce") == "gracz1"


def test_nozyce_biją_papier():
    assert wyznacz_zwyciezce("nożyce", "papier") == "gracz1"


def test_papier_bije_kamien():
    assert wyznacz_zwyciezce("papier", "kamień") == "gracz1"


def test_przegrany_zwraca_gracz2():
    """Sprawdzamy że porażka gracza 1 daje 'gracz2'."""
    assert wyznacz_zwyciezce("nożyce", "kamień") == "gracz2"


def test_wszystkie_wybory_sa_w_liscie():
    assert len(WYBORY) == 3
    assert "kamień" in WYBORY