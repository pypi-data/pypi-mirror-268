from django.apps import AppConfig


class SupportConfig(AppConfig):
    name = "zs_utils.support"
    label = "support"

    def ready(self) -> None:
        import zs_utils.support.signals  # noqa
