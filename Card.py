class Stats:
    def __init__(self,
                 date_created: str,
                 correct_answers_count: int,
                 incorrect_answers_count: int,
                 repetitions_count: int):
        self.date_created = date_created
        self.correct_answers_count = correct_answers_count
        self.incorrect_answers_count = incorrect_answers_count
        self.repetitions_count = repetitions_count

    @classmethod
    def from_dict(cls, stats_dict: dict):
        return Stats(
            stats_dict['date_created'],
            int(stats_dict['correct_answers_count']),
            int(stats_dict['incorrect_answers_count']),
            int(stats_dict['repetitions_count']),
        )


def to_dict(self):
    return {'x': ''}


class Card:
    def __init__(self,
                 question: str,
                 answer: str,
                 topic: str,
                 tags: object,
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
            'tags': self.tags,
            'box': self.box,
            'stats': self.stats
        }
