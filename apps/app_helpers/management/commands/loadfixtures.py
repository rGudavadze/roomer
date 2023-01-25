from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Load initial data into database"

    def handle(self, *args, **options):

        base_dir = settings.BASE_DIR
        fixture_dirs = settings.FIXTURE_DIRS

        for fixture_dir in fixture_dirs:
            fixture_dir_path = base_dir / fixture_dir
            fixture_files = fixture_dir_path.glob("**/*.json")

            for file in fixture_files:
                call_command("loaddata", file)
