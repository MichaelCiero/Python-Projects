import random
import string
possible_values = 10
total_card_value = random.randint(1,11) + random.randint(1,11)
dealers_card_value = random.randint(1,11) + random.randint(1,11)

while True:
    if int(total_card_value) > 21:
        print(f"Dealer's total: {dealers_card_value}")
        print(f"Player's total: {total_card_value}")
        print("Bust!")
    elif dealers_card_value == 21:
        print(f"Dealer's total: {dealers_card_value}")
        print(f"Player's total: {total_card_value}")
        print("Dealer Wins!")
    elif dealers_card_value > 21:
        print(f"Dealer's total: {dealers_card_value}")
        print(f"Player's total: {total_card_value}")
        print("Player Wins!")
    else:
        print("Current total: " + str(total_card_value))    
        dealers_quest = input("Hit or Stay?: ")
        if dealers_quest.lower() == "hit":
            total_card_value = total_card_value + random.randint(1,10)
            print(f"Total: {total_card_value}")
            if total_card_value > 21:
                print("Bust!")
                break
            else:
                continue
            continue
        else:
            if dealers_card_value >= total_card_value:
                print(f"Dealer's total: {dealers_card_value}")
                print(f"Player's total: {total_card_value}")
                print("Dealer Wins!")
                break
            else:
                print(f"Dealer's total: {dealers_card_value}")
                print(f"Player's total: {total_card_value}")
                print("Player Wins!")
                break


