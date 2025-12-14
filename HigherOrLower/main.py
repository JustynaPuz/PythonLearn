import random
import sys
from typing import Any, Dict

from HigherOrLower import art
from game_data import data

Person = Dict[str, Any]
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


def draw_person() -> Person:
    return random.choice(data)


def draw_different_person(exclude: Person) -> Person:
    person = draw_person()
    while person == exclude:
        person = draw_person()
    return person


def format_person(label: str, person: Person) -> str:
    name = C.color(person["name"], C.BOLD)
    desc = C.color(person["description"], C.CYAN)
    country = C.color(person["country"], C.MAGENTA)
    return f"{C.color(label, C.YELLOW)}: {name}, {desc}, from {country}"


def correct_answer(a: Person, b: Person) -> str:
    return "A" if a["follower_count"] >= b["follower_count"] else "B"


def prompt_choice() -> str:
    while True:
        choice = input(
            f"Who has more followers? Type {C.color('A', C.BOLD)} or {C.color('B', C.BOLD)}: "
        ).strip().upper()
        if choice in {"A", "B"}:
            return choice
        print(C.color("Please type only 'A' or 'B'.", C.RED))


def reveal_counts(a: Person, b: Person) -> None:
    a_name = C.color(a["name"], C.BOLD)
    b_name = C.color(b["name"], C.BOLD)
    a_count = C.color(f"{a['follower_count']}M", C.CYAN)
    b_count = C.color(f"{b['follower_count']}M", C.CYAN)

    print(C.color("Follower counts:", C.DIM))
    print(f"  A ({a_name}): {a_count}")
    print(f"  B ({b_name}): {b_count}")
    print()


def play_round(a: Person, b: Person) -> bool:
    print(format_person("Compare A", a))
    print(art.vs)
    print(format_person("Against B", b))
    print()

    choice = prompt_choice()
    answer = correct_answer(a, b)

    reveal_counts(a, b)

    if choice == answer:
        print(C.color("✅ Correct!", C.GREEN))
        return True

    print(C.color("❌ Wrong!", C.RED))
    return False


def main() -> None:
    print(C.color(art.logo, C.CYAN))

    score = 0
    a = draw_person()

    while True:
        b = draw_different_person(a)

        if not play_round(a, b):
            print(C.color(f"Sorry, you lost! Final score: {score}", C.RED))
            break

        score += 1
        print(C.color(f"You're right! Current score: {score}\n", C.GREEN))
        a = b


if __name__ == "__main__":
    main()
