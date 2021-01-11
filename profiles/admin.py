from django.contrib import admin
from .models import Profile, Relationship
# Register your models here.
from django.contrib.auth.models import Group


class ProfileAdmin(admin.ModelAdmin):
    class Media:
        js = (
            'main.js',
        )

    def has_add_permission(self, request):
        return False

    actions = ['Block_Profile', 'Unblock_Profile']

    def Block_Profile(self, request, queryset):
        queryset.update(is_block=True)

    def Unblock_Profile(self, request, queryset):

        queryset.update(is_block=False)

    list_display = ('first_name', 'last_name', 'user', 'email', 'country', 'created', 'is_block',)


admin.site.register(Profile, ProfileAdmin)
admin.site.unregister(Group)
