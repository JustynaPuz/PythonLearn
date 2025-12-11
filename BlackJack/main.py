import random
from typing import List, Dict
from colorama import init, Fore, Style
import art


init(autoreset=True)

CARD_VALUES: Dict[str, int] = {
    "Ace": 11,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
}

COLOR_USER = Fore.GREEN
COLOR_DEALER = Fore.RED
COLOR_PROMPT = Fore.CYAN
COLOR_LOGO = Fore.YELLOW
COLOR_INFO = Fore.MAGENTA
RESET = Style.RESET_ALL

def draw_cards(card_count: int) -> List[str]:
    return random.sample(list(CARD_VALUES.keys()), card_count)


def calculate_score(hand: List[str]) -> int:
    score = 0
    aces = 0
    for card in hand:
        score += CARD_VALUES[card]
        if card == "Ace":
            aces += 1
    while score > 21 and aces > 0:
        score -= 10
        aces -= 1
    return score


def print_cards(hand: List[str], color: str = "") -> None:
    card_arts = [art.cards_ascii[card] for card in hand]
    split_cards = [card.lstrip("\n").splitlines() for card in card_arts]
    for lines in zip(*split_cards):
        print(color + "  ".join(lines) + RESET)


def get_yes_no(prompt: str) -> bool:
    while True:
        choice = input(COLOR_PROMPT + prompt + RESET).strip().lower()
        if choice in ("y", "yes"):
            return True
        if choice in ("n", "no"):
            return False
        print(Fore.RED + "Please type 'y' or 'n'." + RESET)


def play_round() -> None:
    print(COLOR_LOGO + art.logo + RESET)

    user_hand = draw_cards(2)
    computer_hand = draw_cards(2)

    user_score = calculate_score(user_hand)
    computer_score = calculate_score(computer_hand)

    while True:
        print_cards(user_hand, COLOR_USER)
        print(COLOR_USER + f"Your hand: {user_hand}, current score: {user_score}" + RESET)

        print_cards(computer_hand, COLOR_DEALER)
        print(COLOR_DEALER + f"Computer hand: {computer_hand}, computer score: {computer_score}" + RESET)

        if user_score >= 21:
            break

        if get_yes_no("Type 'y' to get another card, 'n' to pass: "):
            user_hand.extend(draw_cards(1))
            user_score = calculate_score(user_hand)
        else:
            break

    while computer_score < 17:
        computer_hand.extend(draw_cards(1))
        computer_score = calculate_score(computer_hand)

    print()
    print(COLOR_INFO + "Final hands:" + RESET)

    print_cards(user_hand, COLOR_USER)
    print(COLOR_USER + f"Your hand: {user_hand}, final score: {user_score}" + RESET)

    print_cards(computer_hand, COLOR_DEALER)
    print(COLOR_DEALER + f"Computer hand: {computer_hand}, final score: {computer_score}" + RESET)

    if user_score > 21 and computer_score > 21:
        print(COLOR_INFO + "Both busted. It's a draw." + RESET)
    elif user_score > 21:
        print(COLOR_DEALER + "You busted. Computer wins!" + RESET)
    elif computer_score > 21:
        print(COLOR_USER + "Computer busted. You win!" + RESET)
    elif user_score > computer_score:
        print(COLOR_USER + "You win!" + RESET)
    elif computer_score > user_score:
        print(COLOR_DEALER + "Computer wins!" + RESET)
    else:
        print(COLOR_INFO + "Draw!" + RESET)


def main() -> None:
    while get_yes_no("Do you want to play blackjack? (y/n): "):
        play_round()
        print()
    print(COLOR_INFO + "Goodbye!" + RESET)


if __name__ == "__main__":
    main()
