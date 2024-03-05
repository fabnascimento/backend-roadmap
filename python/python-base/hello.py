#!/usr/bin/env python3
"""Multi language hello world.

Based on the env language it will display
hello world based on that language.

This is an example of a Docstring
"""

__version__ = "0.0.1"
__author__ = "Fabricio Nascimento"
__license__ = "Unlicense"

import os

# Dunder __

msg = ''
# get default language on the system
# if LANG is not set, it will default to en_US
current_language = os.getenv("LANG", "en_US")[:5]

if current_language == "pt_BR":
    msg = "Nossa!!!"
elif current_language == "en_CA":
    msg = "Wow!!!"
elif current_language == "fr_FR":
    msg = "?"

print(msg)

