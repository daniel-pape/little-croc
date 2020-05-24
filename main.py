from typing import List, Set, Dict, Tuple, Optional
from colorama import init
from colorama import Fore, Back, Style
from Card import Card
import json


def move_to_next_box(card: Dict):
    pass


def check_answer(answer: str):
    return False


def load_cards(box: Optional[int] = None) -> Dict[str, str]:
    assert box is None or box in [0, 1, 2, 3, 4]

    file = open("./cards.json")
    cards: List[Dict] = json.load(file)
    file.close()

    data = [Card.from_dict(card) for card in cards]
    for x in data:
        print(x)

    for card in cards:
        for (k, v) in card.items():
            is_in_box = (box is None) or (card['box'] == box)
            if is_in_box:
                print(k, v)

    return [card for card in cards if (box is None) or (card['box'] == str(box))]


def loop():
    cards = load_cards(1)
    print(cards)

    for card in cards:
        print(card['question'] + ' = ', end='')
        try:
            answer = input()
            is_correct = (answer == card['answer'])

            if is_correct:
                move_to_next_box(card)
            else:
                print(Fore.RED + f'''{card['question']} = {card['answer']}''' + Style.RESET_ALL)
        except EOFError:
            print("Exited")


def main():
    init()
    loop()


if __name__ == '__main__':
    main()
