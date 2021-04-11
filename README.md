### Mini-Project Risk Dice Roller

# Combat Rules
* There is an attacker and a defender
* The attacker rolls 3 dice if they hae 3 or more units, 2 dice if they have 2 units, and 1 die if they only have 1 unit
* The defender rolls 2 dice if they have t or mor eunits, and 1 die if they only have 1 unit
* All dice are standard 6-sided dice with an equal chance of rolling any number between 1 and 6, inclusive
* The attacker can choose to stop the battle any time
* Math the highest attacking die to the highest defending die - the side with the lower number loses a unit. The 
  defender always wins ties.
* If both sides rolled a second die, match the second-highest attacking die to the second-highest defending die - 
  the side with the lower number losses a unit. The defender always wins ties

# Expected Inputs and Outputs
### To resolve a battle, we need to know 3 things:
1. The number of attacking units
2. The number of defending units
3. The number of units the attacker is willing to lose before they call off the attack(this can be equal to or less 
   than the number of units they are attacking with)

### Expected output, we only need to know 2 things
1. The number of attackers remaining after the battle
2. The number of defenders remaining after the battle

