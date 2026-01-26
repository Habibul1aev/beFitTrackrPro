from django.contrib import admin
from account.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'username', 'email', 'get_full_name', 'phone_number', 'get_favorites', 'get_avatar',)
    list_display_links = ('id', 'username',)
    ordering = ('-date_joined',)
    search_fields = ('first_name', 'last_name', 'email', 'phone_number',)
    filter_horizontal = ('groups', 'user_permissions',)
    list_filter = ('is_staff', 'is_superuser', 'is_active',)
    fieldsets = (
        (None,
         {'fields':
             (
                 'username',
                 'email',
                 'phone_number',
                 'password',
             )
         }
         ),
        (_('Personal info'),
         {'fields':
             (
                 'avatar',
                 'get_big_avatar',
                 'first_name',
                 'last_name',
             )
         }
         ),
        (_('Permissions'), {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )}),
        (_('Профиль пользователя'), {'fields': (
            'gender',
            'age',
            'weight_value',
            'growth',
            'goal',
            'physical_activity',
        )}),
        (_('Important dates'), {'fields': (
            'date_joined',
            'last_login',
        )}),
    )
    readonly_fields = (
        'date_joined',
        'last_login',
        'get_big_avatar',
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'email',
                'phone_number',
                'password1',
                'password2',
            ),
        }),
    )

    @admin.display(description=_('Аватарка'))
    def get_avatar(self, user):
        if user.avatar:
            return mark_safe(
                f'<img src="{user.avatar.url}" alt="{user.username}" width="50px" />')
        return '-'

    @admin.display(description=_('Аватарка'))
    def get_big_avatar(self, user):
        if user.avatar:
            return mark_safe(
                f'<img src="{user.avatar.url}" alt="{user.username}" width="100%" />')
        return '-'

    @admin.display(description=_('В Избранных'))
    def get_favorites(self, user):
        favorites = 0
        favorites += user.favorites_workout.count()
        favorites += user.favorite_nutrition.count()
        return favorites
