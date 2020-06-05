from django.contrib import admin

# local
from ..models import Members


@admin.register(Members)
class MembersAdmin(admin.ModelAdmin):
    '''Admin View for Members'''

    list_display = ('team',)