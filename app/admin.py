from django.contrib import admin
from app.models import Card

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "description", "parameters"]