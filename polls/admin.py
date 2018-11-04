from django.contrib import admin

# Register your models here.

from .models import Positions,Candidate,Bucket

admin.site.register(Positions)
admin.site.register(Bucket)
@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    readonly_fields = ['votes']
    # exclude = ('votes',)

