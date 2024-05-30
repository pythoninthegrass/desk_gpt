#!/usr/bin/env python

import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatgpt_backend.settings')
from django.core.management import execute_from_command_line

execute_from_command_line([sys.argv[0], 'runserver', '127.0.0.1:8000'])
