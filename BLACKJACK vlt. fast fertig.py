# BlackJack or 21 game

import random

total_money = 100

while True:
    print("\n\n")
    print("Restarting the game with " + str(total_money) + " dollars left")
    current_money = int(input("How much money are you willing to bet? "))
    total_money -= current_money
    print("\n\n")
    # THE PLANNING PHASE
    dealer_cards = []
    player_cards = []
    # Deal the cards
    # Display the cards
    # Dealer Cards
    game_finished = False
    while sum(dealer_cards) <= 16:
        dealer_cards.append(random.randint(1, 11))
        if sum(dealer_cards) >= 17:
            print("Dealer has X &", dealer_cards[0])
        
     	# Sum of the Dealer cards
        if sum(dealer_cards) == 21:
            print("Dealer has 21 and wins!")
            current_money = 0
            game_finished = True
            print(dealer_cards)
        elif sum(dealer_cards) > 21:
            print("Dealer has busted!")
            current_money *= 2
            game_finished = True
            print(dealer_cards)

    if not game_finished:
        # Player Cards
        while len(player_cards) != 2:
            player_cards.append(random.randint(1, 11))
            if len(player_cards) == 2:
                print("You have ", player_cards)
 


    

        # Sum of the Player cards
        while sum(player_cards) < 21:
            action_taken = str(input("Do you want to stay or hit?  "))
            if action_taken == "hit":
                player_cards.append(random.randint(1, 11))
                print("You now have a total of " + str(sum(player_cards)) + " from these cards ", player_cards)
            else:
                print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
                print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)
                if sum(dealer_cards) > sum(player_cards):
                    print("Dealer wins!")
                    current_money = 0
                    break
                elif sum(dealer_cards) < sum(player_cards):
                    print("You win!")
                    current_money *= 2
                    break
                elif sum(dealer_cards) == sum(player_cards):
                	print("PUSH")
                	break

        if sum(player_cards) > 21:
            print("You BUSTED! Dealer wins.")
            current_money = 0
        elif sum(player_cards) == 21:
            print("You have BLACKJACK! You Win!! 21")
            current_money *= 2.5
            
    total_money += current_money
    
