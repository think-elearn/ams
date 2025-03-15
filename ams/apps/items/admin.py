from django.contrib import admin

from .models import Choice
from .models import Item
from .models import Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("stem", "status")
