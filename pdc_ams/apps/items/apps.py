import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ItemsConfig(AppConfig):
    name = "pdc_ams.apps.items"
    verbose_name = _("Items")

    def ready(self):
        with contextlib.suppress(ImportError):
            import pdc_ams.apps.items.signals  # noqa: F401
