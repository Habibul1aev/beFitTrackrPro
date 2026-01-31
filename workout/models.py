from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from account.models import User

class TimeStampAbstractModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField('Дата добавление', auto_now_add=True)
    updated_at = models.DateTimeField('Дата добавление', auto_now=True)

class Workout(TimeStampAbstractModel):

    class Meta:
        db_table = 'workout'
        verbose_name = 'Тренировку'
        verbose_name_plural = 'Тренировки'

    DIFFICULTY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    title = models.CharField('Название', max_length=50)
    difficulty = models.CharField('Сложность', choices=DIFFICULTY_CHOICES, max_length=20, default='biginner')
    images = models.ImageField('Изоброжение', upload_to='workout_images')
    exercises = models.ManyToManyField(
        'Exercise',
        related_name='workouts',
        verbose_name='Упражнения',
        blank=True
    )
    favorites = models.ManyToManyField(User, related_name='favorites_workout', verbose_name='Избранное', blank=True)
    is_publish = models.BooleanField('Публикация', default=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def count_exercise(self):
        return self.exercises.count()

    count_exercise.fget.short_description = 'Количество упражнений'

    @property
    def calorie_count(self):
        total = 0
        for exercise in self.exercises.all():
            if exercise.cal:
                total += exercise.cal * int(exercise.repetition)
        return total

    calorie_count.fget.short_description = 'Количество калории'


    @property
    def finish_time(self):
        seconds = 0
        for exercise in self.exercises.all():
            if exercise.repetition:
                seconds += exercise.time * int(exercise.repetition)

        minutes = seconds // 60
        secs = seconds % 60
        return f"{minutes:02d}:{secs:02d}"

    finish_time.fget.short_description = 'Длительность тренировки'



class Exercise(models.Model):

    class Meta:
        verbose_name = 'Упражнения'
        verbose_name_plural = 'Упражнения'

    name = models.CharField('Название', max_length=50)
    video = models.FileField('Видео', upload_to='videos/', blank=True, null=True)
    description = models.TextField('Описание', max_length=150)
    repetition = models.DecimalField('Повторение', max_digits=1, decimal_places=0, default=3)
    time = models.PositiveIntegerField('Длительность (сек.)', help_text='Укажите длительность в секундах', default=20)
    cal = models.PositiveIntegerField("Калории", help_text="Сжигаемовый калории",
        validators=[MinValueValidator(1), MaxValueValidator(200)], default=20
    )

    def __str__(self):
        return self.name

    def exersice_time(self):
        seconds = 0
        seconds += self.time * int(self.repetition)
        minutes = seconds // 60
        secs = seconds % 60
        return f"{minutes:02d}:{secs:02d}"

    exersice_time.short_description = 'Длительность тренировки'


    def exersice_cal(self):
        total = 0
        total += self.cal * int(self.repetition)
        return f"{total} ккал"

    exersice_cal.short_description = 'Количество калории'



