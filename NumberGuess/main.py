import random
import sys

from NumberGuess import art

MIN_NUMBER = 1
MAX_NUMBER = 100

ATTEMPTS_BY_DIFFICULTY = {
    "easy": 10,
    "hard": 5,
}

ANSI_SUPPORTED = sys.stdout.isatty()


class C:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    CYAN = "\033[36m"
    MAGENTA = "\033[35m"

    @staticmethod
    def color(text: str, code: str) -> str:
        if not ANSI_SUPPORTED:
            return text
        return f"{code}{text}{C.RESET}"


def prompt_difficulty() -> int:
    while True:
        level = input("Choose a difficulty level. Type 'easy' or 'hard': ").strip().lower()
        if level in ATTEMPTS_BY_DIFFICULTY:
            return ATTEMPTS_BY_DIFFICULTY[level]
        print(C.color("Invalid choice. Please type 'easy' or 'hard'.", C.RED))


def prompt_int(prompt: str, min_value: int, max_value: int) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print(C.color("Please enter a whole number.", C.RED))
            continue

        if not (min_value <= value <= max_value):
            print(C.color(f"Please enter a number between {min_value} and {max_value}.", C.RED))
            continue

        return value


def temperature_hint(distance: int) -> str:
    if distance == 0:
        return C.color("Perfect!", C.GREEN)
    if distance <= 3:
        return C.color("🔥 Boiling hot!", C.RED)
    if distance <= 8:
        return C.color("🌶️ Hot!", C.YELLOW)
    if distance <= 15:
        return C.color("🙂 Warm.", C.CYAN)
    if distance <= 25:
        return C.color("🧊 Cold.", C.MAGENTA)
    return C.color("❄️ Freezing.", C.DIM)


def attempts_bar(left: int, total: int) -> str:
    filled = "█" * left
    empty = "░" * (total - left)
    return f"[{filled}{empty}] {left}/{total}"


def play_round(number_to_guess: int, total_attempts: int) -> bool:
    attempts_left = total_attempts
    previous_distance = None

    while attempts_left > 0:
        print(C.color(attempts_bar(attempts_left, total_attempts), C.BOLD))

        guess = prompt_int("Guess a number: ", MIN_NUMBER, MAX_NUMBER)

        distance = abs(guess - number_to_guess)

        if guess == number_to_guess:
            print(C.color("✅ You got it!", C.GREEN))
            return True

        direction = "Too high!" if guess > number_to_guess else "Too low!"
        print(C.color(direction, C.YELLOW))

        print(temperature_hint(distance))

        if previous_distance is not None:
            if distance < previous_distance:
                print(C.color("↗️ Getting closer!", C.GREEN))
            elif distance > previous_distance:
                print(C.color("↘️ Getting farther!", C.RED))
            else:
                print(C.color("→ Same distance as last time.", C.CYAN))

        previous_distance = distance
        attempts_left -= 1
        print()

    print(C.color("💀 Game Over!", C.RED))
    print(f"The number was {C.color(str(number_to_guess), C.BOLD)}.")
    return False


def main() -> None:
    while True:
        print(art.logo)
        print(C.color("Welcome to the Number Guessing Game!", C.BOLD))
        print(f"I am thinking of a number between {MIN_NUMBER} and {MAX_NUMBER}.")

        attempts = prompt_difficulty()
        number_to_guess = random.randint(MIN_NUMBER, MAX_NUMBER)

        play_round(number_to_guess, attempts)

        again = input("Play again? Type 'yes' or 'no': ").strip().lower()
        if again not in {"yes", "y"}:
            print(C.color("Bye! 👋", C.CYAN))
            break
        print()


if __name__ == "__main__":
    main()
