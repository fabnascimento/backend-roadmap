#!/usr/bin/env python3
"""Exibe relatorio de alunos por atividade

Imprimir a lista de alunos agrupados por sala
"""
__version__ = "0.2.0"

room_1 = set(["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"])
room_2 = set(["Joao", "Antonio", "Carlos"])


english_class = ["Erik", "Maia", "Carlos", "Manuel", "Sofia", "Joana"]
music_class = ["Erik", "Carlos", "Maria"]
dance_class = ["Gustavo", "Antonio", "Sofia", "Joana"]

activities = [
    ("English", set(english_class)),
    ("Music", set(music_class)),
    ("Dance", set(dance_class))]

for activity_name, activity in activities:
    activity_room1 = activity.intersection(room_1)
    activity_room2 = activity.intersection(room_2)

    print(f"Activity: {activity_name}")
    print()
    print(f"Room 1: {activity_room1}")
    print(f"Room 2: {activity_room2}")
    print()
    print("-" * 40)
    