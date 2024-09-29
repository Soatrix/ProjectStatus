from django.core.management.base import BaseCommand
from django.conf import settings
from utils import compile_directory

if __name__ == "__main__":
    exclude_dirs = ["django_compiler", "env"]
    directory = settings.BASE_DIR
    compile_directory(directory, exclude_dirs=exclude_dirs)