from datetime import datetime, timezone

from task2.models import *


def give_prize(player_id, level_order):
    level_prize = LevelPrize.objects.filter(level__order=level_order).first()
    if level_prize.received is None:
        level_prize.received = datetime.now(timezone.utc)
        level_prize.save()

    print(f'Игрок {player_id} получил приз "{level_prize.prize.title}"')
