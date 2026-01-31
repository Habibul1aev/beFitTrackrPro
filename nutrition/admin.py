from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Nutrition, Ingredient, CookingTime, PhotoAI
from django.utils.translation import gettext_lazy as _


@admin.register(Nutrition)
class NutritionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'estimated_calories', 'created_at', 'get_images',)
    list_display_links = ('id', 'title',)
    ordering = ('-created_at', )
    list_filter = ('favorites', 'created_at', 'ingredients',)
    search_fields = ('title', 'description',)
    readonly_fields = ('created_at', 'updated_at', 'get_big_images', 'created_by', )

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

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


@admin.register(PhotoAI)
class PhotoAIAdmin(admin.ModelAdmin):
    list_display = ('id', 'parse_ai_json', 'uploaded_at', 'get_ai_photo', )
    list_display_links = ('id', 'parse_ai_json', )
    readonly_fields = ('user', 'image', 'get_big_ai_photo', 'ai_result', )

    def parse_ai_json(self, items):
        return items.ai_result.get('name')

    @admin.display(description=_('Изображение'))
    def get_ai_photo(self, items):
        if items.image:
            return mark_safe(
                f'<img src="{items.image.url}" alt="{self.parse_ai_json}" width="100px" />')
        return '-'

    @admin.display(description=_('Изображение'))
    def get_big_ai_photo(self, items):
        if items.image:
            return mark_safe(
                f'<img src="{items.image.url}" alt="{self.parse_ai_json}" width="100%" />')
        return '-'