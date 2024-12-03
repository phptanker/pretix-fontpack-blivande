from django.apps import AppConfig

from . import __version__


class PluginApp(AppConfig):
    name = "pretix_fontpackblivande"
    verbose_name = "Fontpack: Blivande"

    class PretixPluginMeta:
        name = "Fontpack: Blivande fonts"
        author = "Philip Shevin"
        description = "Pack of fonts for Blivande"
        visible = False
        version = __version__
        compatibility = "pretix>=4.16.0"

    def ready(self):
        from . import signals  # NOQA
