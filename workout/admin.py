from django.contrib import admin
from django.utils.safestring import mark_safe
from workout.models import Workout, Exercise


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'difficulty', 'count_exercise', 'created_at', 'is_publish', 'get_images',)
    list_display_links = ('id', 'title',)
    ordering = ('-created_at',)
    filter_horizontal = ('exercises', )
    list_filter = ('is_publish', 'created_at', 'difficulty', 'favorites',)
    search_fields = ('title', 'difficulty',)
    readonly_fields = ('created_at', 'updated_at', 'get_big_images',)

    @admin.display(description='Изображение')
    def get_images(self, item):
        if item.images:
            return mark_safe(
                f'<img src="{item.images.url}" alt="{item.title}" width="100px" />')
        return '-'

    @admin.display(description='Изображение')
    def get_big_images(self, item):
        if item.images:
            return mark_safe(
                f'<img src="{item.images.url}" alt="{item.title}" width="100%" />')
        return '-'

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'repetition', 'exersice_cal', 'exersice_time', 'connection')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)

    @admin.display(description='Связь с тренировками (id)')
    def connection(self, obj):
        l = []
        for workout in obj.workouts.all():
            l.append(workout.id)
        return l

