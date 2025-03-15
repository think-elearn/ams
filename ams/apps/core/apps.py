import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CoreConfig(AppConfig):
    name = "ams.apps.core"
    verbose_name = _("Core")

    def ready(self):
        with contextlib.suppress(ImportError):
            import ams.apps.core.signals  # noqa: F401
