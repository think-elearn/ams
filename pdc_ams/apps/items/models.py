from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from pdc_ams.apps.blueprint.models import LearningObjective
from pdc_ams.apps.core.models import BaseModel

from .validators import validate_p_value


class Question(BaseModel):
    class Type(models.TextChoices):
        STANDARD = "STANDARD", _("Standard")
        NEGATIVE = "NEGATIVE", _("Negative")
        LIST = "LIST", _("List")
        BLANK = "BLANK", _("Blank")

    text = models.TextField()
    type = models.CharField(max_length=8, choices=Type.choices, default=Type.STANDARD)

    def __str__(self):
        return self.text[:42]


class Choice(BaseModel):
    text = models.CharField(max_length=255)
    question = models.ForeignKey(
        Question,
        related_name="choices",
        on_delete=models.CASCADE,
    )
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text[:21]


class Item(BaseModel):
    class Status(models.TextChoices):
        DRAFT = "DRAFT", _("Draft")
        REVIEW = "REVIEW", _("Review")
        QA = "QA", _("QA")
        READY = "READY", _("Ready")
        PUBLISHED = "PUBLISHED", _("Published")
        SUSPENDED = "SUSPENDED", _("Suspended")
        RETIRED = "RETIRED", _("Retired")

    stem = models.OneToOneField(Question, on_delete=models.PROTECT)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.DRAFT,
    )
    rationale = models.TextField()
    enemy_items = models.ManyToManyField("self", blank=True)
    learning_objective = models.ForeignKey(LearningObjective, on_delete=models.PROTECT)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    estimated_p_value = models.FloatField(
        default=0.85,
        validators=[validate_p_value],
        help_text="Enter a value between 0 and 1",
    )
    p_value = models.FloatField(
        blank=True,
        null=True,
        validators=[validate_p_value],
    )

    def __str__(self):
        return self.stem.text[:42]
