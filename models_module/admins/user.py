from django.contrib import admin


class CustomUserAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'email', 'is_active',
                    'is_staff', 'is_superuser', 'last_login')
    list_display_links = ('email',)

    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'email', 'bio', 'password')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
    )
