import random

def choose_options():
    options = ('piedra', 'papel', 'tijera')
    user_option = input("Piedra, papel o tijera -> ")
    user_option = user_option.lower()

    if user_option not in options:
        print("!!! Esa opción no es válida")
        return None, None

    computer_option = random.choice(options)

    print("Tú elegiste =>", user_option)
    print("Oponente eligió =>", computer_option)
    return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print("¡Empate!")
    elif user_option == "piedra":
        if computer_option == "tijera":
            print("Piedra gana a tijera, ¡ganaste!")
            user_wins += 1
        else:
            print("Papel gana a piedra, perdiste")
            computer_wins += 1
    elif user_option == "papel":
        if computer_option == "piedra":
            print("Papel gana a piedra, ¡ganaste!")
            user_wins += 1
        else:
            print("Tijera gana a papel, perdiste")
            computer_wins += 1
    elif user_option == "tijera":
        if computer_option == "papel":
            print("Tijera gana a papel, ¡ganaste!")
            user_wins += 1
        else:
            print("Piedra gana a tijera, perdiste")
            computer_wins += 1

    return user_wins, computer_wins


def run_game():
    user_wins = 0
    computer_wins = 0
    rounds = 1

    while True:
        print("\n====================")
        print("ROUND", rounds)
        print("====================")

        print("Marcador => Tú:", user_wins, "Oponente:", computer_wins)

        user_option, computer_option = choose_options()
        if user_option is None:
            continue

        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

        if computer_wins == 2:
            print("------------------------")
            print("EL CAMPEON es el OPONENTE")
            print("------------------------\n")
            break

        if user_wins == 2:
            print("------------------------")
            print("EL CAMPEON es el USUARIO")
            print("------------------------\n")
            break

        rounds += 1


if __name__ == "__main__":
    run_game()
