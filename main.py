from src.game import zagraj_runde

def main():
    print("Witaj w grze: Kamień, Nożyce, Papier!")

    imie1 = input("Podaj imię gracza 1: ")
    imie2 = input("Podaj imię gracza 2: ")

    while True:
        zagraj_runde(imie1, imie2)

        dalej = input("\nCzy chcecie zagrać jeszcze raz? (t/n): ").lower()

        if dalej != "t":
            print("👋 Koniec gry!")
            break  

if __name__ == "__main__":
    main()