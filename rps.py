import re
import random

ROCK = "^1|a|(pedra)|(preda)$"
PAPER = "^2|b|(paper)$"
SCISSORS = "^3|c|((es)?tisor(a|es))$"
QUIT = "^4|d|sortir|surt|adéu|bye|quit|exit$"

# wins = 0 TODO
# losses = 0

def main():
    quit = False

    print("PEDRA - PAPER - ESTISORES")
    print()
    while True:
        try:
            option = menu()
            rps(option)
        except WrongChoice as e:
            print(f"ERROR: {e}")

def rps(player: str):
    # optimitzable TODO
    rockVSpaper = "Paper embolica la pedra"
    rockVSscissors = "Pedra romp les estisores"
    paperVSscissors = "Estisores tallen el paper"
    cpu = random.choice(["pedra", "paper", "estisores"]) ############## vaaaaars TODO
    print(f"Jo trii {cpu}")

    # optimitzable TODO
    if player == cpu:
        print("És un empat!!!")
    elif player == "pedra":
        if cpu == "paper":
            print(f"Ui! {rockVSpaper}, has perdut...")
            # losses += 1
        if cpu == "estisores":
            print(f"Molt bé!! {rockVSscissors}, has guanyat!!")
    elif player == "paper":
        if cpu == "pedra":
            print(f"Molt bé!! {rockVSpaper}, has guanyat!!")
        if cpu == "estisores":
            print(f"Ui! {paperVSscissors}, has perdut...")
    elif player == "estisores":
        if cpu == "pedra":
            print(f"Ui! {rockVSscissors}, has perdut...")
        if cpu == "paper":
            print(f"Molt bé!! {paperVSscissors}, has guanyat!!")

# Future class Weapon constructor
def getWeapon(text: str):
    text = text.lower()
    if re.match(ROCK, text):
        return "pedra"
    elif re.match(PAPER, text):
        return "paper"
    elif re.match(SCISSORS, text):
        return "estisores"
    elif re.match(QUIT, text):
        return "sortir"
    else:
        raise WrongChoice("Opció no vàlida!!!")

def menu(): # improvable
    menu = """
Tria una opció:
1 - Pedra
2 - Paper
3 - Estisores
4 - Sortir
"""
    print(menu)
    option = getWeapon(input("Opció? "))
    if option == "sortir":
        raise Terminate
    else:
        return option
    
class WrongChoice(Exception):
    pass

class Terminate(Exception):
    pass

if __name__ == "__main__":
    try:
        main()
    except (Terminate, KeyboardInterrupt) as e:
        print("Adéu!!!")
