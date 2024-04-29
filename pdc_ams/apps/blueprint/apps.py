import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BlueprintConfig(AppConfig):
    name = "pdc_ams.apps.blueprint"
    verbose_name = _("Blueprint")

    def ready(self):
        with contextlib.suppress(ImportError):
            import pdc_ams.apps.blueprint.signals  # noqa: F401
