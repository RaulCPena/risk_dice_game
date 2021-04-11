from random import randint

a = int(input("Enter number of attackers: "))
b = int(input("Enter number of defenders: "))
c = int(input("How many attackers are you willing to lose? "))

num_dice_a = a if a < 4 else 3
num_dice_b = b if b < 3 else 2
num_dice_c = c if c < a else 3

def main():
    playing = True
    while playing:
        attackers = [randint(1, 6) for i in range(num_dice_a)]
        attackers.sort(reverse = True)
        print(f"Attacker rolled: {attackers}")
        defenders = [randint(1, 6) for i in range(num_dice_b)]
        defenders.sort(reverse = True)
        print(f"Defender rolled: {defenders}")
        attack_units_lost = 0
        defend_units_lost = 0
        for atk, dfn in zip(attackers, defenders):
            if atk <= dfn:
                attack_units_lost += 1
            else:
                defend_units_lost += 1
        print(f"Lost {attack_units_lost} attackers")
        print(f"Lost {defend_units_lost} defenders")
        if attack_units_lost >= c:
            playing = False
            print("Game Ended Over! The attacker has reached their threshold!! The defender wins!")
        elif defend_units_lost == defenders:
            playing = False
            print("The defender has run out of defenders! The attacker wins!")
        else:
            print("You Win")

        while playing:
            # roll_dice()
            play_again = input("Do you want to play again? (yes?)\n")
            play_again = play_again.lower()
            if not play_again.startswith('y'):
                playing = False
                print("Thanks for playing!")
main()
# def roll_dice():
#     attackers = [randint(1, 6) for i in range(num_dice_a)]
#     attackers.sort(reverse = True)
#     print(f"Attacker rolled: {attackers}")
#
#     defenders = [randint(1, 6) for i in range(num_dice_b)]
#     defenders.sort(reverse = True)
#     print(f"Defender rolled: {defenders}")
#
#     attack_units_lost = 0
#     defend_units_lost = 0
#
#     for atk, dfn in zip(attackers, defenders):
#         if atk <= dfn:
#             attack_units_lost += 1
#         else:
#             defend_units_lost += 1
#
#
#
#     print(f"Lost {attack_units_lost} attackers")
#     print(f"Lost {defend_units_lost} defenders")
#
#     playing = True
#     while playing:
#         roll_dice()
#         play_again = input("Do you want to play again? (yes?)\n")
#         play_again = play_again.lower()
#         if not play_again.startswith('y'):
#             playing = False
#         print("Thanks for playing!")
#
# roll_dice()


