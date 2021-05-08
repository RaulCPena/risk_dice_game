import random

a = int(input("Enter number of attackers: "))
b = int(input("Enter number of defenders: "))
c = int(input("How many attackers are you willing to lose? "))

Attacker_Rolls = a
Defender_Rolls = b

if (a >= 3 and b >=2) and ((a-c) >= c):
    Attacker_Rolls = 3
    Defender_Rolls = 2
elif  (a == 2 and b >=2) and ((a-c) >= c):
    Attacker_Rolls = 2
    Defender_Rolls = 2
elif  (a == 1 and b >=2) and ((a-c) >= c):
    Attacker_Rolls = 1
    Defender_Rolls = 2
elif  (a >= 3 and b == 1 ) and ((a-c) >= c):
    Attacker_Rolls = 3
    Defender_Rolls = 1
elif  (a == 2 and b == 1 ) and ((a-c) >= c):
    Attacker_Rolls = 2
    Defender_Rolls = 1
elif  (a == 1 and b == 1 ) and ((a-c) >= c):
    Attacker_Rolls = 1
    Defender_Rolls = 1

num_of_attackers = [random.randint(1, 6) for i in range(Attacker_Rolls)]
num_of_attackers.sort(reverse=True)
num_of_defenders = [random.randint(1,6) for i in range(Defender_Rolls)]
num_of_defenders.sort(reverse=True)
print(num_of_attackers, num_of_defenders)

while len(num_of_attackers) > 0 and len(num_of_defenders) > 0:
    if num_of_attackers == c:
        print ("The attacker has ended the game!")
    elif  num_of_attackers.pop(0) > num_of_defenders.pop(0):
        Remaining_Attackers = a
        Remaining_Defenders = b - 1
        print("The attacker has won!")
        print(Remaining_Attackers, Remaining_Defenders)
    else:
            Remaining_Attackers = a - 1
            Remaining_Defenders = b
            print("The defender has won!")
            print(Remaining_Attackers, Remaining_Defenders)
