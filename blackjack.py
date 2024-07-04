import random
from blackjack_art import logo


def renew_deck():  # Function to renew the deck
    """Renew the deck of cards."""
    global cards
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6,
     7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # List of cards in the deck





def deal_card():  # Function to deal a card from the deck
    """Returns a random card from the deck."""
    print("The deck is: ", cards)
    #11 is the Ace card which can be 1 or 11, 10 is the face card which is 10. The rest three 10s
    #are for the three face cards: Jack, Queen, and King.
    my_card = random.choice(cards)  # Randomly choosing a card from the deck
    cards.remove(my_card)   # Removing the chosen card from the deck
    return my_card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards."""
    if sum(cards) == 21 and len(cards) == 2:    # Condition for Blackjack
        return 0
    if 11 in cards and sum(cards) > 21:     # Condition for Ace card
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):    # Function to compare the user_score and computer_score
    """Compare the user_score and computer_score and return the result."""
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose. 🥺"
    elif user_score == computer_score:
        return "It's a draw. 😇"
    elif computer_score == 0:
        return "Computer has Blackjack. You lose. 🥺"
    elif user_score == 0:
        return "You have Blackjack. You win. 😀"
    elif user_score > 21:
        return "You went over. You lose. 🥺"
    elif computer_score > 21:
        return "Computer went over. You win. 😀"
    elif user_score > computer_score:
        return "You win. 😀"
    else:
        return "You lose. 🥺"


def play_game():
    renew_deck()
    """Play the game of Blackjack."""
    print(logo)
    is_game_over = False
    user_cards = [deal_card(), deal_card()]     # Randomly dealing two cards to the user and computer
    computer_cards = [deal_card(), deal_card()]
    computer_score = calculate_score(computer_cards)
    while not is_game_over:     # Looping until the game is over
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:   # Checking for Blackjack or score > 21
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':    # Asking the user for another card
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:      # Computer will draw a card till its score < 17
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play_game()
