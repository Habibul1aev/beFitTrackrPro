from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from account.models import User


class TimeStampAbstractModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField('Дата добавление', auto_now_add=True)
    updated_at = models.DateTimeField('Дата добавление', auto_now=True)

class CookingTime(models.Model):

    class Meta:
        verbose_name = 'Время готовки'
        verbose_name_plural = 'Время готовки'

    duration_minutes = models.IntegerField(
        verbose_name='Длительность',
        default=0,
        help_text='от 5 минут до 45',
        validators=[MinValueValidator(5), MaxValueValidator(45)]
    )

    def __str__(self):
        return f'{self.duration_minutes}-минут'


class Ingredient(models.Model):

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    name = models.CharField('Название ингридиента', max_length=70, unique=True)

    def __str__(self):
        return self.name


class Nutrition(TimeStampAbstractModel):

    class Meta:
        db_table = 'nutrition'
        verbose_name = 'Питание'
        verbose_name_plural = 'Питание'

    MEAL_CHOICES = [
        ('breakfast', 'Завтрак'),
        ('lunch', 'Обед'),
        ('dinner', 'Ужин'),
    ]

    images = models.ImageField('Изображение', upload_to='nutrition_images')
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание', max_length=300)
    duration_minutes = models.ForeignKey(CookingTime, on_delete=models.CASCADE,
        verbose_name='Время приготовления'
    )
    estimated_calories = models.PositiveIntegerField("Калории",
        default=40,
        validators=[MinValueValidator(40), MaxValueValidator(1200)],
        help_text = 'от 40 минут до 1200'
    )
    ingredients = models.ManyToManyField(Ingredient,
        verbose_name='Ингредиенты',
        related_name='recipes'
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='nutritions'
    )
    favorites = models.ManyToManyField(User, related_name='favorite_nutrition', verbose_name='Избранное', blank=True)
    is_publish= models.BooleanField(
        default=False,
        verbose_name='Доступно всем'
    )

    def __str__(self):
        return self.title

class PhotoAI(TimeStampAbstractModel):
    class Meta:
        verbose_name = 'Изоброжение ИИ'
        verbose_name_plural = 'Изоброжения ИИ'

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    image = models.ImageField('Изоброжение', upload_to='food_photo_ai')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    ai_result = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f'{self.pk-1}  {str(self.image)}'
