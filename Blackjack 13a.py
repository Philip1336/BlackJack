import random

dealer_karten = []

spieler_karten = []


while sum(dealer_karten) <= 16:
    dealer_karten.append(random.randint(1, 11))
    if sum(dealer_karten) >= 17:
        print("Dealer has %d, %d" % (dealer_karten[1], dealer_karten[0]))
    
while sum(dealer_karten) >= 17:
	if sum(dealer_karten) == 21:
		print("Dealer has BLACKJACK and wins!")
	elif sum(dealer_karten) > 21:
		print("Dealer has busted!")
		break

while len(spieler_karten) != 2:
    spieler_karten.append(random.randint(1, 11))
    if len(spieler_karten) == 2:
        print("You have ", spieler_karten)

while sum(spieler_karten) < 21:
    action_taken = str(input("Do you want to stay or hit?  "))
    if action_taken == "hit":
        spieler_karten.append(random.randint(1, 11))
        print("You now have a total of " + str(sum(spieler_karten)) + " from these cards ", spieler_karten)
    else:
        print("The dealer has a total of " + str(sum(dealer_karten)) + " with ", dealer_karten)
        print("You have a total of " + str(sum(spieler_karten)) + " with ", spieler_karten)
        
        if sum(dealer_karten) > sum(spieler_karten):
            print("Dealer wins!")
            break
        elif sum(dealer_karten) < sum(spieler_karten):
        	print("You win!")
        	break
        elif sum(dealer_karten) == sum(spieler_karten):
            print("PUSH")
            break

if sum(spieler_karten) > 21:
    print("You BUSTED! Dealer wins.")
elif sum(spieler_karten) == 21:
    print("You have BLACKJACK! You Win!! 21")
    
    
    
#Dealer busted schon manchmal am Anfang, dann ist das restliche Spiel unnötig
#Dealer nimmt am Anfang, kommt aber bei dieser Blackjack Version nicht drauf an, da nicht mit ganzen Decks, sonder mit zufälligen Zahlen von 1-11 gespielt wird.
