## Тестовое задание для бэкенд разработчика на Python

1. Ответ на первое задание находится в папке `game/task1/models.py`  
или здесь:
<details><summary>Модели для первого задания</summary>

```python
from django.db import models


class Player(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    points = models.IntegerField(default=0)
    first_login = models.DateTimeField(auto_now_add=True)
    bonuses = models.ManyToManyField(
        "Boost", blank=True, related_name="bonuses"
    )


class BoostType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)


class Boost(models.Model):
    id = models.BigAutoField(primary_key=True)
    effect = models.ForeignKey(
        "BoostType", on_delete=models.PROTECT
    )
    duration = models.IntegerField()
    power = models.IntegerField()
```

</details>

2. Ответ на второе задание находится в папке `game/task2/functions.py`
или здесь:
<details><summary>Функции для присвоения игроку приза за прохождение уровня и выгрузки в csv данных</summary>

```python
import csv
from datetime import datetime, timezone

from task2.models import *


def give_prize(player_id, level_order):
    level_prize = LevelPrize.objects.filter(level__order=level_order).first()
    if level_prize.received is None:
        level_prize.received = datetime.now(timezone.utc)
        level_prize.save()

    print(f'Игрок {player_id} получил приз "{level_prize.prize.title}"')


def export_data_csv():
    with open("data.csv", mode="w", encoding='utf-8') as w_file:
        writer = csv.writer(w_file, delimiter=";", lineterminator="\n")
        data = PlayerLevel.objects.all().values_list('player__player_id', 'level__title', 'is_completed', 'level_id')
        for row in data:
            level_prize = LevelPrize.objects.filter(level_id=row[-1]).first()
            writer.writerow(row[:-1] + (level_prize.prize.title,))

```

</details>

*Примечание:* `LevelPrize.received` *- это дата первого получения приза.
Это сделано, так как в данных в задании моделях не возможно связать получение подарка с игроком*

<hr>

Для того, чтобы протестировать функции второго задания на своём компьютере выполните следующие команды в терминале:

1) Склонируйте репозиторий:
```commandline
git clone https://github.com/Tarasyonok/test-task-pusto-studio
```
2) Перейди в папку с проектом:
```commandline
cd test-task-pusto-studio
```

3) Создайте виртуальное окружение:
```commandline
python -m venv venv
```

4) Активируйте виртуальное окружение:
```commandline
./venv/Scripts/activate
```

5) Установите зависимости:
```commandline
pip install -r requirements.txt
```

6) Перейдите в папку с файлом `manage.py`:
```commandline
cd game
```

7) Запустите интерпретатор python:
```commandline
python manage.py shell  
```

8) Импортируйте функции:
```python
from task2.functions import * 
```

9) Пример вызова функции получения приза. Функция принимает `player_id` (ник игрока) и `level_order` (порядковый номер уровня):
```python
give_prize("bravekirty", 1)
```

10) Вторая функция сохраняет данные в `game/data.csv`:
```python
export_data_csv()
```

<hr>

В первой части второго задания некуда сохранять приз, ведь приз никак не связан с игроком в данной схеме бд, поэтому я только вывожу в консоль какая награда будет выдана.
