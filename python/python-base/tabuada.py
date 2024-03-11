#!/usr/bin/env python3

""" Retorna tabuada

"""

__version__ = "0.1.0"
__author__ = "Fabricio Nascimento"

# range is non inclusive for last argument
numbers = list(range(1, 11))

print(f"Programa de Tabuada \U0001F600") #printing an emoji

for base in numbers:
    title = f"Tabuada do {base}"
    print("{:-^20}".format(title))

    for multiplier in numbers:
        result = base * multiplier
        msg = f"{base} x {multiplier} = {result}"
        print(f"{msg:^20}")

    print("#"*20)
