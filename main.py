from src.game import zagraj_runde

def main():
    print("Witaj w grze: Kamień, Nożyce, Papier!")

    imie1 = input("Podaj imię gracza 1: ")
    imie2 = input("Podaj imię gracza 2: ")

    zagraj_runde(imie1, imie2)

if __name__ == "__main__":
    main()