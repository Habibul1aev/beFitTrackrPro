from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Nutrition, Ingredient, CookingTime, PhotoAI


@admin.register(Nutrition)
class NutritionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'estimated_calories', 'created_at', 'get_images',)
    list_display_links = ('id', 'title',)
    ordering = ('-created_at', )
    list_filter = ('favorites', 'created_at', 'ingredients',)
    search_fields = ('title', 'description',)
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


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('name', )


@admin.register(CookingTime)
class CookingTimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'duration_minutes_format')
    list_display_links = ('duration_minutes_format',)
    search_fields = ('duration_minutes', )
    list_filter = ('duration_minutes', )

    @admin.display(description='Длительность')
    def duration_minutes_format(self, item):
        return f'{item.duration_minutes}-минут'


admin.site.register(PhotoAI)
