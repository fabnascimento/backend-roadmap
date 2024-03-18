#!/usr/bin/env python3
"""Exibe relatorio de alunos por atividade

Imprimir a lista de alunos agrupados por sala
"""
__version__ = "0.2.0"

rooms = {
    "room_1": set(["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]),
    "room_2": set(["Joao", "Antonio", "Carlos"])
}

english_class = set(["Erik", "Maia", "Carlos", "Manuel", "Sofia", "Joana"])
music_class = set(["Erik", "Carlos", "Maria"])
dance_class = set(["Gustavo", "Antonio", "Sofia", "Joana"])

activities = {
    "english": {
        "name": "English",
        "students": english_class
    },
    "music": {
        "name": "Music",
        "students": music_class
    },
    "dance": {
        "name": "Dance",
        "students": dance_class
    }
}

for activity in activities:
    activity_name = activities[activity]["name"]
    print("_" * 40)
    print(f"Activity: {activity_name}\n")
    for room in rooms:
        students = activities[activity]["students"].intersection(rooms[room])
        print(f"{room} students: {students}")
    
    print()
    print("-" * 40)
