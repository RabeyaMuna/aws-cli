#!/home/yisenxu/rabeya/mini-swe-agent-ci-based/results/think_repair_deepseek/0e6f97d05d68c3d66d270865c31e9060c5a5b4de/testbed/.venv-aws-cli-144/bin/python3

# Author:
# Contact: grubert@users.sf.net
# Copyright: This module has been placed in the public domain.

"""
man.py
======

This module provides a simple command line interface that uses the
man page writer to output from ReStructuredText source.
"""

import locale
try:
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_cmdline, default_description
from docutils.writers import manpage

description = ("Generates plain unix manual documents.  "
               + default_description)

publish_cmdline(writer=manpage.Writer(), description=description)
