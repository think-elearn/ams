import uuid

from django.db import models


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.
    """

    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class UUIDModel(models.Model):
    """
    An abstract base class model that provides an UUIDField.
    """

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True


class BaseModel(TimeStampedModel, UUIDModel):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields and an UUIDField.
    """

    class Meta:
        abstract = True
