import pygame
import random

class Survivor:
    def __init__(self, name:str = '', pos:list, size:list, sexe:bool, ):
        self.position = pos
        self.size = size
        self.velocity = 30
        images = []
        self.image = random.choice([images])
        if sexe == None: self.sexe = random.choice([True, False])
        if name == '':
            if sexe : names = ['Albert', 'Giles', 'Arthur', 'Jeremy']
            else : names = ['Louise', 'Jeanne', 'Marie', 'N0Nam€']
            self.name = random.choice([names])
        else: self.name = name
        self.objectif = None
        self.do = ''
        pass

    def __repr__(self):
        return

    def move(self):
        pass

    def changePos(self):
        pass

