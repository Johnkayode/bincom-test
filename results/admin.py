from django.contrib import admin
from .models import *


@admin.register(AnnouncedLgaResults)
class AnnouncedLgaResultsAdmin(admin.ModelAdmin):
    search_fields = ['lga_name', 'party_score' ]


admin.site.register(Agentname)
admin.site.register(AnnouncedPuResults)
admin.site.register(AnnouncedStateResults)
admin.site.register(AnnouncedWardResults)
admin.site.register(Lga)
admin.site.register(Party)
admin.site.register(PollingUnit)
admin.site.register(States)
admin.site.register(Ward)