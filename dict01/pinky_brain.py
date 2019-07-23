#!/usr/bin/python3
mice = {"number": 2, "names": [{"name": "Pinky", "tag": "the real genius"},{"name": "The Brain", "tag": "insane one"}], "world_domination_status": "pending"}
## print following
## Pinky is the real genius, and The Brain is the insane one

print(f'{mice["names"][0]["name"]} is {mice["names"][0]["tag"]}, and {mice["names"][1]["name"]} is the {mice["names"][1]["tag"]}.')
