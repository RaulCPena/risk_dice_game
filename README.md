#Mini-Project Risk Dice Roller

## Combat Rules

* There is an attacker and a defender.
* The attacker rolls three dice if they have three or more units, two dice if they have two units, and one die if they have 1 unit.
* The defender rolls two dice if they have two or more units and one die if they only have 1 unit.
* All dice are standard 6-sided with an equal chance of rolling any number between 1 and 6, inclusive.
* The attacker can choose to stop the battle at any time.
* Units are compared by the highest attacking die to the highest defending die - the side with the lower number loses a unit. 
* If both sides rolled a second die, we match the second-highest attacking die to the second-highest defending die - the side with the lower number losses a unit
* The defender always wins ties.

## Expected Inputs

To resolve a battle, we need to know three things:
* The number of attacking units.
* The number of defending units.
* The number of units the attacker is willing to lose before they call off the attack (this can be equal to or less than the number of units they are attacking with).


## Expected output

To end the battle, we need the following as outputs:

* The number of attackers remaining after the battle.
* The number of defenders remaining after the battle.
