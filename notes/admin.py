from django.contrib import admin

from .models import Notes

class NotesAdmin(admin.ModelAdmin):
    list_display = ('title','user','created_at',)

admin.site.register(Notes, NotesAdmin)