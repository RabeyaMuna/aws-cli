#!/home/yisenxu/rabeya/mini-swe-agent-ci-based/results/think_repair_deepseek/0e6f97d05d68c3d66d270865c31e9060c5a5b4de/testbed/.venv-aws-cli-144/bin/python3

# $Id: rst2latex.py 8956 2022-01-20 10:11:44Z milde $
# Author: David Goodger <goodger@python.org>
# Copyright: This module has been placed in the public domain.

"""
A minimal front end to the Docutils Publisher, producing LaTeX.
"""

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_cmdline

description = ('Generates LaTeX documents from standalone reStructuredText '
               'sources. '
               'Reads from <source> (default is stdin) and writes to '
               '<destination> (default is stdout).  See '
               '<https://docutils.sourceforge.io/docs/user/latex.html> for '
               'the full reference.')

publish_cmdline(writer_name='latex', description=description)
