import json
import copy

from little_croc.Stats import Stats

from little_croc.JsonHelper import write_json
from . import here

class Card:
    def __init__(self,
                 question: str,
                 answer: str,
                 topic: str,
                 tags: list,
                 box: int,
                 stats: Stats):
        self.question = question
        self.answer = answer
        self.topic = topic
        self.tags = tags
        self.box = box
        self.stats = stats

    def __str__(self):
        return self.to_dict().__str__()

    @classmethod
    def from_dict(cls, card: dict):
        return Card(
            question=card['question'],
            answer=card['answer'],
            topic=card['topic'],
            tags=card['tags'],
            box=int(card['box']),
            stats=Stats.from_dict(card['stats'])
        )

    def to_dict(self):
        return {
            'question': self.question,
            'answer': self.answer,
            'topic': self.topic,
            'tags': str(self.tags),
            'box': str(self.box),
            'stats': self.stats.to_dict()
        }

    def compare(self, other):
        return self.question == other.question

    def copy_to_box(self, to_box: int):
        to_box_file = here / f'resources/box_{to_box}.json'

        with open(to_box_file) as to_box_stream:
            print(f'Copy card to box {to_box}')
            cards_in_to_box = json.load(to_box_stream)

            new_card = copy.copy(self)
            new_card.box = to_box
            cards_in_to_box.append(new_card.to_dict())

            write_json(cards_in_to_box, to_box_file)

    def delete_from_box(self, from_box: int):
        from_box_file = here / f'resources/box_{from_box}.json'

        with open(from_box_file) as from_box_stream:
            print(f'Remove card from box {from_box}')
            cards_in_from_box = json.load(from_box_stream)

            filtered = [
                card
                for
                card
                in
                cards_in_from_box
                if not
                Card.from_dict(card).compare(self)
            ]

            write_json(filtered, from_box_file)

    def move_to_box(self, to_box: int):
        self.copy_to_box(to_box)
        self.delete_from_box(self.box)
