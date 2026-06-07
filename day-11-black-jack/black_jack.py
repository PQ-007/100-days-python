import random
print(r'''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      '------'                           |__/   
''')

def deal_card():
    return random.randint(1, 11)


def calculate_score(hand):
    return sum(hand)


running = True
while running:
    print("Do you want to play a game of Blackjack? Type 'y' or 'n'")
    if input().lower() == 'y':
        player_hand = [deal_card(), deal_card()]
        computer_hand = [deal_card(), deal_card()]

        print(f"Your cards: {player_hand}, current score: {calculate_score(player_hand)}")
        print(f"Computer's first card: {computer_hand[0]}")
        player_score = calculate_score(player_hand)
        while player_score < 21:
            print("Type 'y' to get another card, type 'n' to pass.")
            if input().lower() == 'y':
                player_hand.append(deal_card())
                player_score = calculate_score(player_hand)
                print(f"Your cards: {player_hand}, current score: {player_score}")
                if player_score > 21:
                    break
            else:
                break

        computer_score = calculate_score(computer_hand)
        while player_score <= 21 and computer_score < 17:
            computer_hand.append(deal_card())
            computer_score = calculate_score(computer_hand)

        computer_score = calculate_score(computer_hand)

        print(f"Your final hand: {player_hand}, final score: {player_score}")
        print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")

        if player_score > 21:
            print("You went over. You lose 😭")
        elif computer_score > 21:
            print("Computer went over. You win 😁")
        elif player_score > computer_score:
            print("You win 😁")
        elif player_score < computer_score:
            print("You lose 😭")
        else:
            print("It's a draw 🙃")
    else:
        print("Exiting the game. Goodbye!")
        running = False