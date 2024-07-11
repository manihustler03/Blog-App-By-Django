from typing import Any
from myblog.models import Category
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "This Command use to insert category"

    def handle(self, *args: Any, **options: Any):
        Category.objects.all().delete()
        categories = ["Tech", "Cinema", "News", "Sports"]
        for category_name in categories:
            Category.objects.create(name=category_name)
            self.stdout.write(self.style.SUCCESS("Complted"))
