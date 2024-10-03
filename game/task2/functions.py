from datetime import datetime, timezone

from task2.models import *


def give_prize(player_id, level_order):
    level_prize = LevelPrize.objects.filter(level__order=level_order).first()
    if level_prize.received is None:
        level_prize.received = datetime.now(timezone.utc)
        level_prize.save()

    print(f'Игрок {player_id} получил приз "{level_prize.prize.title}"')


import csv


def export_data_csv():
    with open("data.csv", mode="w", encoding='utf-8') as w_file:
        writer = csv.writer(w_file, delimiter=";", lineterminator="\n")
        data = PlayerLevel.objects.all().values_list('player__player_id', 'level__title', 'is_completed', 'level_id')
        for row in data:
            level_prize = LevelPrize.objects.filter(level_id=row[-1]).first()
            writer.writerow(row[:-1] + (level_prize.prize.title,))
