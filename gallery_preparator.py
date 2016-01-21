#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os.path
import locale
import gettext

locale.setlocale(locale.LC_ALL, '')
_ = gettext.gettext
gettext.bindtextdomain('messages', 'locales')

script_name = os.path.basename(sys.argv[0])

if script_name == 'gallery_preparator_console.py':
    from ui.console import UI
else:
    # Fallback to console ui
    from ui.console import UI

app = UI()

try:
    app.galeries()
except KeyboardInterrupt:
    print(("\n\n" + _("Why so hurry? Goodbye.") + "\n"))
