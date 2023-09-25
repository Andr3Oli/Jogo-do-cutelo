import pygame, sys
from button import Button
from OpenGL.GL import *

import math
import numpy as np
import pygame
from core.base import Base
from core.input import Input
from core.matrix import Matrix
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer2 import Renderer
from core_ext.scene import Scene
from core_ext.texture import Texture
from extras.axes import AxesHelper
from extras.grid import GridHelper
from extras.text_texture import TextTexture
from geometry.box import BoxGeometry
from geometry.ellipsoid import EllipsoidGeometry
from light.ambient import AmbientLight
from geometry.model import Model
from geometry.rectangle2 import RectangleGeometry
from geometry.sphere import SphereGeometry
from geometry.uv_model import UVModel
from light.directional import DirectionalLight
from light.point import PointLight
from material.line import LineMaterial
from material.surface import SurfaceMaterial
from material.point import PointMaterial
from material.basic import BasicMaterial
from material.texture import TextureMaterial
from movement import *
from objects import generateHitboxes, generateObjects

pygame.init()

def intersect(sphere, box):
    box_x = box._matrix[0][3]
    box_y = box._matrix[1][3]
    box_z = box._matrix[2][3]

    box_minX = box_x - box._geometry.width/2
    box_minY = box_y - box._geometry.height/2
    box_minZ = box_z - box._geometry.depth/2

    box_maxX = box_x + box._geometry.width/2
    box_maxY = box_y + box._geometry.height/2
    box_maxZ = box_z + box._geometry.depth/2

    sphere_x = sphere._matrix[0][3]
    sphere_y = sphere._matrix[1][3]
    sphere_z = sphere._matrix[2][3]
    if sphere_z < box_minZ or sphere_z > box_maxZ: return False

    x = max(box_minX, min(sphere_x, box_maxX));
    y = max(box_minY, min(sphere_y, box_maxY));
    z = max(box_minZ, min(sphere_z, box_maxZ));

    distance = math.sqrt(
        (x - sphere_x) * (x - sphere_x) +
        (y - sphere_y) * (y - sphere_y) +
        (z - sphere_z) * (z - sphere_z)
    )
    
    return distance < sphere.radius

SCREEN = pygame.display.set_mode((640, 360))
pygame.display.set_caption("Menu")

BG = pygame.transform.scale(pygame.image.load("images/Background.jpg"), (640, 360))

def get_font(size):
    return pygame.font.Font("images/font.ttf", size)

class Example(Base):

    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)
        self.camera._matrix= [
            [ 0.01079612,  0.,         -0.99994172,  -2.5      ],
            [ 0.,          1.,          0.,          0.764     ],
            [ 0.99994172,  0.,          0.01079612, -0.01      ],
            [ 0.,          0.,          0.,          1.        ]
        ]
        self.initial_camera_state = self.camera.local_matrix

        ambient = AmbientLight(color=[0.2, 0.2, 0.2])
        self.scene.add(ambient)

        directional = DirectionalLight(color=[1, 1, 1], direction=[1, -0.5, -1])
        self.scene.add(directional)
        directional = DirectionalLight(color=[0.5, 0.5, 0.5], direction=[0, -1, 0])
        self.scene.add(directional)

        # point = PointLight(color=[0.35, 0.71, 0.9], position=[-1,2,0], attenuation=[0.1, 0.1, 0.1])
        # self.scene.add(point)
        # point.set_direction([0.5, 0.5, 0.5])

        self.hud_scene = Scene()
        self.hud_camera = Camera()
        self.hud_camera.set_orthographic(0, 800, 0, 600, 1, -1)

        self.cutelo_velocity = [0, 0, 0]

        self.nivel = 1
        generateObjects(self,self.nivel)
        generateHitboxes(self, self.nivel)
        
        pygame.event.set_grab(True)
        pygame.mouse.set_visible(False)


        self.test = 0
        self.speed = 0
        self.speedy = 0
        self.velocityY = -0.003
        self.intersects = ""
        self.angle = -0.2
        self.total_rotation_angle = 0
        self.hit = False
        self.hit_handle = False
        self.hit_pan = False
        self.hit_tableHandle = False
        self.timerVertical = 0
        self.timerHorizontal = 0
        pygame.mouse.set_pos(500, 300)
        self.pontuation = 0
        self.lifes = 3
        self.past = False
        self.canReset = False

        # ostacles movement variables
        self.valuefri = 0.01
        self.valueesp = 0.01
        self.valuerol = 0.01
        
        self.limitfri = 0
        self.limitesp = 0
        self.limitrol = 0
        
        self.directionFRI = 'direita'
        self.directionESP = 'esquerda'
        self.directionROL = 'direita'
        
        self.valuealvo = 0.008
        self.limitalvo = 0
        self.directionalvo = 'esquerda'

        self.replay = []
        self.replay_frame = 0
        self.end_replay = False
        self.start_replay = False
        
        self.checkAlvo = False

        self.mesh_blade.translate(0, 0.1, 0.1, local=False)
        self.mesh_handle.translate(0, 0.1, 0.1, local=False)
        for box in self.cuteloBoxes: box.translate(0, 0.1, 0.1, local=False)
        self.hit_timer = 0
        self.level_timer = 0
        self.level1_timer = 0
        self.freeze = True
        self.currentLevel = 1


    def update(self):  
        self.level_timer += 1
        if self.level_timer == 120: 
            self.freeze = False
            self.input.afterLaunch = False
            if self.currentLevel == 1: self.level1._visible = False
            if self.currentLevel == 2: self.level2._visible = False
            if self.currentLevel == 3: self.level3._visible = False
        
        if self.currentLevel == 4 and self.level_timer == 240: 
            self.win._visible = False
            self.currentLevel = 1
            reset(self)
            self.run()

        looseLife = False      
        if self.hit != False: self.hit_timer += 1; 
        if self.hit_timer >= 120 and self.currentLevel != 4: 
            reset(self)
            if self.pontuation >= 12: 
                if self.currentLevel == 1:
                    self.freeze = True 
                    self.level2._visible = True
                    self.level_timer = 0
                    for p in self.p_array:
                        if p._visible == True: p._visible = False
                    self.p_array[0]._visible = True
                if self.currentLevel == 2:
                    self.freeze = True  
                    self.level3._visible = True
                    self.level_timer = 0
                    for p in self.p_array:
                        if p._visible == True: p._visible = False
                    self.p_array[0]._visible = True
                if self.currentLevel == 3:
                    self.freeze = True  
                    self.win._visible = True
                    self.level_timer = 0
                self.currentLevel += 1
                self.nivel += 1
                self.pontuation = 0
                self.mesh_base_1._visible = True
                self.mesh_base_2._visible = True
                self.mesh_base_3._visible = True
                self.mesh_pega._visible = True
                self.mesh_semPega._visible = True
                self.mesh_rolo._visible = True
                self.mesh_frigideira._visible = True
        if not self.hit and not self.freeze: cleaverMove(self)
        if (self.intersects == "" or self.intersects == "pan" or self.intersects == "table_handle" or self.intersects == "handle"): # and not self.input.aim 
            self.intersects = self.intersections()
        # print(self.intersects)
        if self.intersects == "1":
            self.one._visible = True
            self.hit = "target"
            self.checkAlvo = True
            self.pontuation+=1
            self.intersects = "Nao passa porra nenhuma"
        if self.intersects == "2":
            self.two._visible = True
            self.hit = "target"
            self.checkAlvo = True
            self.pontuation+=2
            self.intersects = "Nao passa porra nenhuma"
        if self.intersects == "3":
            self.three._visible = True
            self.hit = "target"
            self.checkAlvo = True
            self.pontuation+=3
            self.intersects = "Nao passa porra nenhuma"
        if self.intersects == "4":
            self.four._visible = True
            self.hit = "target"
            self.checkAlvo = True
            self.pontuation+=4
            self.intersects = "Nao passa porra nenhuma"
        if self.intersects == "5":
            self.five._visible = True
            self.hit = "target"
            self.checkAlvo = True
            self.pontuation+=5
            self.intersects = "Nao passa porra nenhuma"
        if self.intersects == "pan":
            self.miss._visible = True
            self.hit_pan = True
            looseLife = True
        if self.intersects == "espatula":
            self.miss._visible = True
            self.hit = True
            looseLife = True
            cuteloESPMovement(self)
        if self.intersects == "roll":
            self.miss._visible = True
            self.hit = True
            looseLife = True
            cuteloROLLMovement(self)
        if self.intersects == "outside":
            self.miss._visible = True
            self.hit = True
            looseLife = True
        if self.intersects == "chao":
            self.miss._visible = True
            self.hit = True
            looseLife = True
        if self.intersects == "table":
            self.miss._visible = True
            self.hit = True
            looseLife = True
        if self.intersects == "handle":
            self.miss._visible = True
            self.hit_handle = True
            looseLife = True
        if self.intersects == "table_handle":
            self.miss._visible = True
            self.hit_tableHandle = True
            looseLife = True
        if self.hit == "target" and not self.end_replay:
            v = self.replay[self.replay_frame]
            self.replay_frame += 1
            for i in range(1,101):
                if self.replay_frame + i > len(self.replay): 
                    if i == 1: self.end_replay = True
                    self.camera.rotate_y(-0.05)
                    break
            self.camera.translate(v[0]-0.02, v[1]+0.001, v[2]-0.03, local=False)
        if(self.checkAlvo) and self.nivel == 3:
            cuteloAlvoMovement(self)

        if self.hit == "target":
            for p in self.p_array:
                if p._visible == True: p._visible = False   

            if self.pontuation < 16:
                self.p_array[self.pontuation]._visible = True
            else: self.p_array[15]._visible = True

        if looseLife and not self.past:
            self.past = True
            if self.lifes > 0:
                self.vidas[self.lifes-1]._visible = False
                self.lifes-=1

        if self.lifes == 0:
            self.freeze = True
            self.game_over._visible = True
            self.canReset = True
            
        if self.input.is_key_pressed('r') and self.canReset:
            reset(self)
            self.run()
        # cameraMovement(self)
        # cuteloMovement(self)
        if self.nivel != 1:
            frigideiraMovement(self)
            espatulaMovement(self)
            roloMovement(self)
        
        if self.nivel == 3:
            alvoMovement(self)

        

        # self.boxMovement(self)

        # self.camera.rotate_x(-self.input.get_mouse_move_x()/500)
        # self.camera.rotate_y(-self.input.get_mouse_move_y()/500)
    
        self.renderer.render(self.scene, self.camera)
        self.renderer.render(
            scene=self.hud_scene,
            camera=self.hud_camera,
            clear_color=False
        )

    def intersections(self):
        intersects = ""
        for box in self.bladeBoxes:
            if intersects != "": continue
            for target_box in self.targetBoxes1:
                if intersects != "": continue
                if intersect(box, target_box): intersects = "5"
        for box in self.bladeBoxes:
            if intersects != "": continue
            for target_box in self.targetBoxes2:
                if intersects != "": continue
                if intersect(box, target_box): intersects = "4"
        for box in self.bladeBoxes:
            if intersects != "": continue
            for target_box in self.targetBoxes3:
                if intersects != "": continue
                if intersect(box, target_box): intersects = "3"
        for box in self.bladeBoxes:
            if intersects != "": continue
            for target_box in self.targetBoxes4:
                if intersects != "": continue
                if intersect(box, target_box): intersects = "2"
        for box in self.bladeBoxes:
            if intersects != "": continue
            for target_box in self.targetBoxes5:
                if intersects != "": continue
                if intersect(box, target_box): intersects = "1"
        if self.nivel != 1:
            for box in self.bladeBoxes:
                if intersects != "": continue
                for target_box in self.panBoxes:
                    if intersects != "": continue
                    if intersect(box, target_box): intersects = "pan"
            for box in self.bladeBoxes:
                if intersects != "": continue
                for target_box in self.spatulaBoxes:
                    if intersects != "": continue
                    if intersect(box, target_box): intersects = "espatula"
            for box in self.bladeBoxes:
                if intersects != "": continue
                for target_box in self.rollBoxes:
                    if intersects != "": continue
                    if intersect(box, target_box): intersects = "roll"
            for box in self.bladeBoxes:
                if intersects != "": continue
                if intersect(box, self.base1_box): intersects = "espatula"
            for box in self.bladeBoxes:
                if intersects != "": continue
                if intersect(box, self.base2_box): intersects = "roll"
            for box in self.bladeBoxes:
                if intersects != "": continue
                if intersect(box, self.base3_box): intersects = "pan"
        for box in self.bladeBoxes:
            if intersects != "": continue
            if intersect(box, self.outside_box): intersects = "outside"
        for box in self.bladeBoxes:
            if intersects != "": continue
            if intersect(box, self.table_box): intersects = "table"
        for box in self.bladeBoxes:
            if intersects != "": continue
            if intersect(box, self.chao_box): intersects = "chao"
        
        for box in self.handleBoxes:
            if intersects != "": continue
            for target_box in self.targetBoxes1:
                if intersects != "": continue
                if intersect(box, target_box): intersects = "handle"
            for target_box in self.targetBoxes2:
                if intersects != "": continue
                if intersect(box, target_box): intersects = "handle"
            for target_box in self.targetBoxes3:
                if intersects != "": continue
                if intersect(box, target_box): intersects = "handle"
            for target_box in self.targetBoxes4:
                if intersects != "": continue
                if intersect(box, target_box): intersects = "handle"
            for target_box in self.targetBoxes5:
                if intersects != "": continue
                if intersect(box, target_box): intersects = "handle"
            if self.nivel != 1:
                for target_box in self.panBoxes:
                    if intersects != "": continue
                    if intersect(box, target_box): intersects = "handle"
                for target_box in self.spatulaBoxes:
                    if intersects != "": continue
                    if intersect(box, target_box): intersects = "handle"
                for target_box in self.rollBoxes:
                    if intersects != "": continue
                    if intersect(box, target_box): intersects = "handle"
            if intersect(box, self.outside_box): intersects = "handle"
            if self.nivel != 1:
                if intersect(box, self.base1_box): intersects = "handle"
                if intersect(box, self.base2_box): intersects = "handle"
                if intersect(box, self.base3_box): intersects = "handle"
            if intersect(box, self.table_box): intersects = "table_handle"
            if intersect(box, self.chao_box): intersects = "handle"
        return intersects
    
    
    
    def newCuteloHitbox(self, radius, x, y, z):
        box_geo = EllipsoidGeometry(radius, radius, 0)
        box_mat = LineMaterial()
        box = Mesh(box_geo, box_mat, visible=False)
        box.radius = radius/2
        self.scene.add(box)
        box._matrix = [     [ 1.,    0.,    0.,    x],
                            [ 0.,    1.,    0.,    y],
                            [ 0.,    0.,    1.,    z],
                            [ 0.,    0.,    0.,    1],]
        return box
    
    def newSquareHitbox(self, width, height, depth, x, y, z):
        box_geo = BoxGeometry(width, height, depth)
        box_mat = LineMaterial()
        box = Mesh(box_geo, box_mat, visible=False)
        self.scene.add(box)
        box.translate(x, y, z, local=False)
        return box
    

def play():
    # while True:
        Example(screen_size=[1280, 720]).run()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(315, 50))

        PLAY_BUTTON = Button(image= pygame.transform.scale(pygame.image.load("images/Play Rect.png"), (200, 70)), pos=(320, 175), 
                            text_input="START", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image= pygame.transform.scale(pygame.image.load("images/Quit Rect.png"), (200, 70)), pos=(320, 250), 
                            text_input="QUIT", font=get_font(60), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                    
        pygame.display.flip()

main_menu()