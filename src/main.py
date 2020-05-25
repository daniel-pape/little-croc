from typing import List, Optional
from colorama import init
from colorama import Fore, Style
import json

from little_croc.Card import Card


def load_cards(box: Optional[int] = None) -> List[Card]:
    assert box is None or box in [0, 1, 2, 3, 4]

    file = open("./src/little_croc/resources/box_1.json")
    cards: List[Card] = [Card.from_dict(card) for card in json.load(file)]
    file.close()

    return cards


def loop():
    cards = load_cards(1)

    for card in cards:
        print(card.question + ' = ', end='')
        try:
            answer = input()
            is_correct = (answer == card.answer)

            if is_correct:
                card.move_to_box(2)
            else:
                print(Fore.RED + f'''{card.question} = {card.answer}''' + Style.RESET_ALL)
        except EOFError:
            print("Exited")


def main():
    init()
    loop()


if __name__ == '__main__':
    main()
