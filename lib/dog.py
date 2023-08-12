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
    def __init__(self, name = 'Fido', breed = 'Mastiff'):
        self.name = name
        if (type(name) == str and len(name) > 1 and len(name) < 25):
            pass
        else:
            print('Name must be string between 1 and 25 characters.')
        
        self.breed = breed
        if (len(breed) > 0 and breed not in APPROVED_BREEDS):
            print('Breed must be in list of approved breeds.')