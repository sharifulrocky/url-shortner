from django.core.management.base import BaseCommand
from shortner.models import ShortUrl


class Command(BaseCommand):
    help = 'Refresh all shortcode'

    def handle(self, *args, **options):
        return ShortUrl.objects.refresh_shortcode()


