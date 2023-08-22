#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self,name="",breed="pug") :
        if not(type(name)in (str,)) and (1<=len(name)<=25):
            print(f"Name must be string between 1 and 25 characters.")
        elif breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.") 
        else:
            self.name=name
            self.breed=breed
               
    