from django.contrib import admin
from .models import File

class FileAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "position", "age"]
admin.site.register(File, FileAdmin)