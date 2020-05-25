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
        return {
            "date_created": self.date_created,
            "correct_answers_count": str(self.correct_answers_count),
            "incorrect_answers_count": str(self.incorrect_answers_count),
            "repetitions_count": str(self.repetitions_count)
        }