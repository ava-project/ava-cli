#!/usr/bin/env python
# -*- coding: utf-8 -*-

# EASY-INSTALL-ENTRY-SCRIPT: 'avacli','console_scripts','avacli'
__requires__ = 'avacli'

import re
import sys

from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('avacli', 'console_scripts', 'avacli')()
    )
