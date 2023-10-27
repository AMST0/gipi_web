from django.contrib import admin
from .models import Chat

# Register your models here.

class ChatAdmin(admin.ModelAdmin):
    list_display = ["user","created_date"]
    list_display_links = ["user","created_date"]
    search_fields = ["user","created_date"]
    list_filter = ["user","created_date"]

    class Meta:
        model = Chat

admin.site.register(Chat)