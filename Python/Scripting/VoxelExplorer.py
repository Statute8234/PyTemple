import random
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()

class Voxel(Entity):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            texture = 'white_cube',
            collider = 'box',
        )


for z in range(60 // 2):
    for x in range(60 // 2):
        voxel = Voxel(position=(x, 0, z))
        #----------------------------------------------
        if (x % 2) == 0 and (z % 2) == 0:
            voxel.color = color.black
        if (x % 2) != 0 and (z % 2) != 0:
            voxel.color = color.black



player = FirstPersonController()
app.run()
