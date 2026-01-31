from django.contrib.auth.models import AbstractUser
from django.db import models
# noinspection PyUnresolvedReferences
from django_resized import ResizedImageField
from django.core.validators import MinValueValidator, MaxValueValidator
# noinspection PyUnresolvedReferences
from phonenumber_field.modelfields import PhoneNumberField
from account.manages import UserManager


class User(AbstractUser):

    class Meta:
        db_table = 'user_account'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-date_joined',)

    GENDER_CHOICES = [
        ('male', 'Муж.'),
        ('female', 'Жен.')
    ]

    GOAL_CHOICES = [
        ('lose weight', 'Похудет'),
        ('gain weight', 'Набрать вес'),
        ('muscle mass gain', 'Увеличать мышечную массу'),
        ('shape body', 'Форма тела'),
        ('others', 'Другое')
    ]

    PHYSICAL_ACTIVITY_CHOICES = [
        ('beginner', 'Начинающий'),
        ('intermediate', 'Средний'),
        ('advanced', 'Продвинутый')
    ]


    username = models.CharField(
        'Имя пользователя (никнейм)',
        max_length=50,
        unique=True,
        blank=True,
        null=True,
    )
    avatar = ResizedImageField('Аватарка', size=[500, 500], crop=['middle', 'center'],
                               upload_to='avatars/', force_format='WEBP', quality=90,
                               null=True, blank=True)
    gender = models.CharField('Пол', choices=GENDER_CHOICES, max_length=20, default='male')
    age = models.PositiveIntegerField('Возраст', blank=True, null=True, validators=[MinValueValidator(16, "Минимальный возраст: 14 лет"),
            MaxValueValidator(100, "Пожалуйста, проверьте возраст")]
    )
    growth = models.DecimalField('Рост', blank=True, null=True,
        max_digits=3,
        decimal_places=0,
        validators=[
            MinValueValidator(50, "Минимальный рост: 50 см"),
            MaxValueValidator(300, "Максимальный рост: 300 см")
        ]
    )
    goal = models.CharField('Цель', choices=GOAL_CHOICES, max_length=20, default='lose weight')
    physical_activity = models.CharField('Физицеский уровень', max_length=20, choices=PHYSICAL_ACTIVITY_CHOICES, default='beginner')
    weight_value = models.DecimalField('Вес', blank=True, null=True,
       max_digits=3,
       decimal_places=1,
       validators=[
           MinValueValidator(20.0, "Минимальный вес: 20 кг"),
           MaxValueValidator(300.0, "Максимальный вес: 300 кг")
       ]
    )
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    email = models.EmailField('Почта', unique=True)
    phone_number = PhoneNumberField('Номер телефона', region='KG', unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    @property
    def get_full_name(self):
        return f'{self.last_name} {self.first_name}'
    get_full_name.fget.short_description = 'Польное имя'

    def __str__(self):
        return self.get_full_name