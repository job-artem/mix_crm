import datetime

from django.db import models

TIMES = [
    ('16:00', '16:00',),
    ('17:00', '17:00',),
    ('18:00', '18:00',),
    ('19:00', '19:00',),
    ('20:00', '20:00',),
]

LOCATIONS = [
    ('POZNYAKI', 'Позняки'),
    ('TROYESCHINA', 'Троещина'),
    ('DARNITSA', 'Дарница'),
    ('LESNAYA', 'Лесная'),
    ('PECHERSK', 'Печерск'),
    ('KLOVSKA', 'Кловская'),
    ('SHULYAVSKA', 'Шулявская'),
    ('OBOLON', 'Оболонь'),
]

TRAINERS = [
    ('Venger', 'Венгер'),
    ('Svistunov', 'Свистунов'),
    ('Kornev', 'Корнев'),
    ('Alekseyenko', 'Алексеенко'),
    ('Kovalevsky', 'Ковалевский'),
    ('Shoferenko', 'Шоференко'),
    ('Galitsky', 'Галицкий'),
    ('Vorontsov', 'Воронцов'),
    ('Karpenko', 'Карпенко'),
    ('Shkrob', 'Шкроб'),
    ('Sarkisyan', 'Саркисян'),
    ('Volskiy', 'Вольский'),
    ('Zaytsev', 'Зайцев'),
    ('Petrovskiy', 'Петровский'),
    ('Doroshenko', 'Дорошенко'),
    ('Ray', 'Рай'),
]

DAYS = [
    ('Monday', 'Понедельник'),
    ('Tuesday', 'Вторник'),
    ('Wednesday', 'Среда'),
    ('Thursday', 'Четверг'),
    ('Friday', 'Пятница'),
    ('Saturday', 'Суббота'),
    ('Sunday', 'Воскресенье'),
]

PAY_TYPES = [
    ('month', 'Месяц'),
    ('one_time', 'Разовый'),
    ('part_month', 'Часть месяца'),
    ('personal', 'Персональный'),
    ('personal_pakage', 'Персональный пакет'),
]


# Create your models here.
class Payment(models.Model):
    date = models.DateField(default=datetime.datetime.now())
    trainer = models.CharField(
        choices=TRAINERS,
        max_length=20,
        default='Not Set',
    )
    location = models.CharField(
        choices=LOCATIONS,
        max_length=20,
        default='Not Set',
    )
    name = models.CharField(max_length=50, null=True)
    surname = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=20, null=True)
    amount = models.IntegerField(default=0)
    payment_type = models.CharField(
        max_length=20,
        choices=PAY_TYPES,
        default='Not Set',
    )
    payment_date = models.DateField(default=datetime.datetime.now())


class Attendance(models.Model):
    date = models.DateField(default=datetime.date.today())
    location = models.CharField(
        choices=LOCATIONS,
        max_length=20,
        default='Not Set',
    )
    trainer = models.CharField(
        choices=TRAINERS,
        max_length=20,
        default='Not Set',
    )
    time = models.CharField(
        max_length=20,
        choices=TIMES,
        default='Not Set',
    )
    day = models.CharField(
        max_length=20,
        choices=DAYS,
        default='Not Set',
    )
    all_count = models.IntegerField(null=True)
    first_count = models.IntegerField(null=True)
    abonement_count = models.IntegerField(null=True)
