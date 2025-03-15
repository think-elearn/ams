import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BlueprintConfig(AppConfig):
    name = "ams.apps.blueprint"
    verbose_name = _("Blueprint")

    def ready(self):
        with contextlib.suppress(ImportError):
            import ams.apps.blueprint.signals  # noqa: F401
