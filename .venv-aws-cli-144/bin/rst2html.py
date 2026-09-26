#!/home/yisenxu/rabeya/mini-swe-agent-ci-based/results/think_repair_deepseek/0e6f97d05d68c3d66d270865c31e9060c5a5b4de/testbed/.venv-aws-cli-144/bin/python3

# $Id: rst2html.py 8927 2022-01-03 23:50:05Z milde $
# Author: David Goodger <goodger@python.org>
# Copyright: This module has been placed in the public domain.

"""
A minimal front end to the Docutils Publisher, producing HTML.
"""

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_cmdline, default_description


description = ('Generates (X)HTML documents from standalone reStructuredText '
               'sources.  ' + default_description)

publish_cmdline(writer_name='html', description=description)
