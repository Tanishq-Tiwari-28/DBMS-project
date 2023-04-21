#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from dashboard.globals import update_global, port_no


def main():
    # if(len(sys.argv == ))
    print(sys.argv)
    print(len(sys.argv))
    if(len(sys.argv) > 2):
        update_global(sys.argv[2])
    elif(len(sys.argv) == 2):
        update_global(8000)
    print(port_no)
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test1.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
