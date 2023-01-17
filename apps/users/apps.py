from django.apps import AppConfig
from django.conf import settings
from django.contrib.auth import get_user_model

from apps.utils.logger import logger


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.users"

    @classmethod
    def ready(cls):
        try:
            user_model = get_user_model()
            if user_model.objects.filter(is_superuser=True).exists():
                return
            logger.info("Creating default Superuser...")
            user_model.objects.create_superuser(
                email=settings.ENVS.get("DJANGO_SUPERUSER_EMAIL"),
                username=settings.ENVS.get("DJANGO_SUPERUSER_USERNAME"),
                password=settings.ENVS.get("DJANGO_SUPERUSER_PASSWORD"),
            )
            logger.info("Superuser created successfully")

        except Exception as err:
            logger.info(
                f"Found an error trying to create the superuser - {err}\n"
                "if you aren't running the user model migration yet, ignore this message."
            )
