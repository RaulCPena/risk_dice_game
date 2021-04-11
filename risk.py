from random import randint

#   takes in the user input
a = int(input("Enter number of attackers: "))
b = int(input("Enter number of defenders: "))
c = int(input("How many attackers are you willing to lose? "))

#   this does not allow the user to enter a higher number which would be outside the rules of the game
num_dice_a = a if (a < 4) and (a > 0) else 3
num_dice_b = b if (b < 3) and (b > 0) else 2
num_dice_c = c if c < a else 3

#   a loop that runs the while loop conditions
while (num_dice_a > 0 and num_dice_b > 0 and c > 0):
    num_dice_a = num_dice_a
    num_dice_b = num_dice_b

#   creates a random number from 1 to 6 for attackers
    attackers = [randint(1, 6) for i in range(num_dice_a)]
    attackers.sort(reverse = True)
    print(f"Attacker rolled: {attackers}")

#   creates a random number from 1 to 6 for defenders
    defenders = [randint(1, 6) for i in range(num_dice_b)]
    defenders.sort(reverse = True)
    print(f"Defender rolled: {defenders}")

#   var created and set to zero
    attack_units_lost = 0
    defend_units_lost = 0

#   takes the output from attackers and defenders and dcompairs them from highest to lowest integer
    for atk, dfn in zip(attackers, defenders):
        if atk <= dfn:
            attack_units_lost += 1
        else:
            defend_units_lost += 1

    print(f"Lost {attack_units_lost} attackers")
    print(f"Lost {defend_units_lost} defenders")

#   This is where the vars determine if the conditions have been met
    num_dice_a = num_dice_a - attack_units_lost
    num_dice_b = num_dice_b - defend_units_lost
    c = c = attack_units_lost

    print(f"Attackers remaining: {num_dice_a}")
    print(f"Defenders remaining: {num_dice_b}")