from django.contrib import admin

from .models import Blueprint
from .models import Category
from .models import LearningObjective
from .models import Subcategory


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1


class SubcategoryInline(admin.TabularInline):
    model = Subcategory
    extra = 1


class LearningObjectiveInline(admin.TabularInline):
    model = LearningObjective
    extra = 1


@admin.register(Blueprint)
class BlueprintAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubcategoryInline]


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    inlines = [LearningObjectiveInline]


admin.site.register(LearningObjective)
