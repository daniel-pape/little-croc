from typing import List, Set, Dict, Tuple, Optional

import json


def check_answer(answer: str):
    return False


def load_cards(box: Optional[int] = None) -> Dict[str, str]:
    assert box is None or box in [0, 1, 2, 3, 4]

    file = open("./cards.json")
    cards: List[Dict] = json.load(file)
    file.close()

    for card in cards:
        print(card)
        for (k, v) in card.items():
            is_in_box = (box is None) or (card['box'] == box)
            if is_in_box:
                print(k, v)

    return [card for card in cards if (box is None) or (card['box'] == str(box))]

def loop():
    questions = ["5 x 7"]

    cards = load_cards(1)
    print(cards)

    for card in cards:
        print(card['question'])
        print("Answer:")
        try:
            answer = input()
            check = (answer == card['answer'])

            if check:
                print('Correct')
            else:
                print('Incorrect')
        except EOFError:
            print("Exited")


def main():
    loop()


if __name__ == '__main__':
    main()
