#!/usr/bin/env python3
"""Exibe relatorio de alunos por atividade

Imprimir a lista de alunos agrupados por sala
"""
__version__ = "0.1.0"

room_1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
room_2 = ["Joao", "Antonio", "Carlos"]


english_class = ["Erik", "Maia", "Carlos", "Manuel", "Sofia", "Joana"]
music_class = ["Erik", "Carlos", "Maria"]
dance_class = ["Gustavo", "Antonio", "Sofia", "Joana"]

activities = [
    ("English", english_class),
    ("Music", music_class),
    ("Dance", dance_class)]

for activity_name, activity in activities:
    # Starts with empty list for that activity
    activity_room1 = []
    activity_room2 = []

    for student in activity:
        if student in room_1:
            activity_room1.append(student)
        if student in room_2:
            activity_room2.append(student)

    print(f"Activity: {activity_name}")
    print()
    print(f"Room 1: {activity_room1}")
    print(f"Room 2: {activity_room2}")
    print()
    print("-" * 40)
    