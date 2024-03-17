from django.contrib import admin

from .models import Notes

class NotesAdmin(admin.ModelAdmin):
    list_display = ('title','description',)

admin.site.register(Notes, NotesAdmin)