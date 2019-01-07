import warnings
from django.core.management.base import LabelCommand


class Command(LabelCommand):
    args = '<clear | reload>'
    label = 'command'
    help = """clear: clear cached busters json
reload: reload cached busters json (DEPRECATED)"""

    def handle_label(self, label, **options):
        warnings.warn('The "buster" command is deprecated. Instead, set BUSTER_CACHE = True in settings.py to cache until server reload.') # noqa
