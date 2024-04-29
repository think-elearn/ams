from django.db import models

from pdc_ams.apps.core.models import BaseModel


class Blueprint(BaseModel):
    version = models.CharField(max_length=255)

    def __str__(self):
        return self.version


class Category(BaseModel):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=30)
    blueprint = models.ForeignKey(Blueprint, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.short_name


class Subcategory(BaseModel):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    items_per_form = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = "Subcategories"

    def __str__(self):
        return self.name[:42]


class LearningObjective(BaseModel):
    class BloomLevel(models.IntegerChoices):
        REMEMBER = 1
        UNDERSTAND = 2
        APPLY = 3
        ANALYZE = 4
        EVALUATE = 5
        CREATE = 6

    reference = models.CharField(max_length=8, help_text="e.g., 1.1.1")
    text = models.CharField(max_length=255)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    bloom_level = models.IntegerField(choices=BloomLevel.choices)

    class Meta:
        verbose_name = "Learning Objective"
        verbose_name_plural = "Learning Objectives"

    def __str__(self):
        return self.text[:42]
