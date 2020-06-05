from django.contrib import admin

# local
from ..models import Team_Name


@admin.register(Team_Name)
class Team_NameAdmin(admin.ModelAdmin):
    '''Admin View for Team_Name'''

    list_display = ('name',)