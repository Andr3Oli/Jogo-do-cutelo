import math
import pygame

# from main import Example

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

def cameraMovement(self):
    cameraSpeed = 0.05
    if self.input.is_key_down('escape'):
        pygame.event.set_grab(not pygame.event.get_grab())
        pygame.mouse.set_visible(not pygame.mouse.get_visible())
    # if self.input.is_key_down('p'):
    #     print(self.mesh_blade._matrix[0][3], self.mesh_blade._matrix[1][3], self.mesh_blade._matrix[2][3])
    if self.input.is_key_pressed('r') and self.canReset:
        self.run()
        # reset(self)
        # self.pontuation = 0
        # self.nivel = 1
        # self.lifes = 3
        # self.canReset = False
        # for p in self.vidas:
        #     p._visible = True
        # self.game_over._visible = False
    # if self.input.is_key_pressed('w'):
    #     self.camera.translate(0, 0, -cameraSpeed)
    # if self.input.is_key_pressed('a'):
    #     self.camera.translate(-cameraSpeed, 0, 0)
    # if self.input.is_key_pressed('s'):
    #     self.camera.translate(0, 0, cameraSpeed)
    # if self.input.is_key_pressed('d'):
    #     self.camera.translate(cameraSpeed, 0, 0)
    # if self.input.is_key_pressed('left ctrl'):
    #     self.camera.translate(0, -cameraSpeed, 0, local=False)
    # if self.input.is_key_pressed('left shift'):
    #     self.camera.translate(0, cameraSpeed, 0, local=False)
    # if self.input.is_key_pressed('e'):
    #     self.camera.rotate_y(-cameraSpeed)
    # if self.input.is_key_pressed('q'):
    #     self.camera.rotate_y(cameraSpeed)

# def boxMovement(self):
#     box = self.box
#     speed = 0.001
#     if self.input.is_key_pressed('up'):
#         box.translate(0, 0, -speed, local=False)
#     if self.input.is_key_pressed('left'):
#         box.translate(-speed, 0, 0, local=False)
#     if self.input.is_key_pressed('down'):
#         box.translate(0, 0, speed, local=False)
#     if self.input.is_key_pressed('right'):
#         box.translate(speed, 0, 0, local=False)
#     if self.input.is_key_pressed('return'):
#         box.translate(0, speed, 0, local=False)
#     if self.input.is_key_pressed('right shift'):
#         box.translate(0, -speed, 0, local=False)
#     if self.input.is_key_pressed('[1]'):
#         box.rotate_x(-0.01)
#     if self.input.is_key_pressed('[2]'):
#         box.rotate_x(0.01)
#     if self.input.is_key_pressed('[4]'):
#         box.rotate_y(-0.01)
#     if self.input.is_key_pressed('[5]'):
#         box.rotate_y(0.01)
#     if self.input.is_key_pressed('[7]'):
#         box.rotate_z(-0.01)
#     if self.input.is_key_pressed('[8]'):
#         box.rotate_z(0.01)

# def cuteloMovement(self):
#     self.mesh_blade.translate(self.speed, self.speedy, 0, local=False)
#     self.mesh_handle.translate(self.speed, self.speedy, 0, local=False)
#     for box in self.cuteloBoxes: box.translate(self.speed, self.speedy, 0, local=False)
#     if self.input.is_key_pressed('l'):
#         self.speed = 0.05
#         # self.speedy = 0.005
#     if self.input.is_key_pressed('up'):
#         self.translated_z += -0.01 
#         self.mesh_blade.translate(0, 0, -0.01, local=False)
#         self.mesh_handle.translate(0, 0, -0.01, local=False)
#         for box in self.cuteloBoxes: box.translate(0, 0, -0.01, local=False)
#     if self.input.is_key_pressed('left'):
#         self.translated_x += -0.01 
#         self.mesh_blade.translate(-0.01, 0, 0, local=False)
#         self.mesh_handle.translate(-0.01, 0, 0, local=False)
#         for box in self.cuteloBoxes: box.translate(-0.01, 0, 0, local=False)

#     if self.input.is_key_pressed('down'):
#         self.translated_z += 0.01 
#         self.mesh_blade.translate(0, 0, 0.01, local=False)
#         self.mesh_handle.translate(0, 0, 0.01, local=False)
#         for box in self.cuteloBoxes: box.translate(0, 0, 0.01, local=False)

#     if self.input.is_key_pressed('right'):
#         self.translated_x += 0.01 
#         self.mesh_blade.translate(0.01, 0, 0, local=False)
#         self.mesh_handle.translate(0.01, 0, 0, local=False)
#         for box in self.cuteloBoxes: box.translate(0.01, 0, 0, local=False)

#     if self.input.is_key_pressed('return'):
#         self.translated_y += 0.01 
#         self.mesh_blade.translate(0, 0.01, 0, local=False)
#         self.mesh_handle.translate(0, 0.01, 0, local=False)
#         for box in self.cuteloBoxes: box.translate(0, 0.01, 0, local=False)
#     if self.input.is_key_pressed('right shift'):
#         self.translated_y += -0.01 
#         self.mesh_blade.translate(0, -0.01, 0, local=False)
#         self.mesh_handle.translate(0, -0.01, 0, local=False)
#         for box in self.cuteloBoxes: 
#             box.translate(0, -0.01, 0, local=False)
#     if self.input.is_key_pressed('[1]'):
#         self.mesh_blade.rotate_x(-0.01)
#         self.mesh_handle.rotate_x(-0.01)
#         for box in self.cuteloBoxes: 
#             box.translate(-self.translated_x, -self.translated_y, -self.translated_z, local=False)
#             box.rotate_x(-0.01, local=False)
#             box.translate(self.translated_x, self.translated_y, self.translated_z, local=False)
#     if self.input.is_key_pressed('[2]'):
#         self.mesh_blade.rotate_x(0.01)
#         self.mesh_handle.rotate_x(0.01)
#         for box in self.cuteloBoxes: 
#             box.translate(-self.translated_x, -self.translated_y, -self.translated_z, local=False)
#             box.rotate_x(0.01, local=False)
#             box.translate(self.translated_x, self.translated_y, self.translated_z, local=False)
#     if self.input.is_key_pressed('[4]'):
#         self.mesh_blade.rotate_y(-0.01)
#         self.mesh_handle.rotate_y(-0.01)
#         for box in self.cuteloBoxes: 
#             box.translate(-self.translated_x, -self.translated_y, -self.translated_z, local=False)
#             box.rotate_y(-0.01, local=False)
#             box.translate(self.translated_x, self.translated_y, self.translated_z, local=False)
#     if self.input.is_key_pressed('[5]'):
#         self.mesh_blade.rotate_y(0.01)
#         self.mesh_handle.rotate_y(0.01)
#         for box in self.cuteloBoxes:
#             box.translate(-self.translated_x, -self.translated_y, -self.translated_z, local=False) 
#             box.rotate_y(0.01, local=False)
#             box.translate(self.translated_x, self.translated_y, self.translated_z, local=False)
#     if self.input.is_key_pressed('7'):
#         self.mesh_blade.rotate_z(-0.03)
#         self.mesh_handle.rotate_z(-0.03)
#         for box in self.cuteloBoxes:
#             box.translate(-self.translated_x, -self.translated_y, -self.translated_z, local=False)
#             box.rotate_z(-0.03, local=False)
#             box.translate(self.translated_x, self.translated_y, self.translated_z, local=False)
#     if self.input.is_key_pressed('[8]'):
#         self.mesh_blade.rotate_z(0.01)
#         self.mesh_handle.rotate_z(0.01)
#         for box in self.cuteloBoxes: 
#             box.translate(-self.translated_x, -self.translated_y, -self.translated_z, local=False)
#             box.rotate_z(0.01, local=False)
#             box.translate(self.translated_x, self.translated_y, self.translated_z, local=False)
      
def cuteloPANMovement(self):
    if self.directionFRI == 'direita':
        if self.limitfri < 0.85:
            self.mesh_blade.translate(0, 0, self.valuefri)
            self.mesh_handle.translate(0, 0, self.valuefri)
        else:
            self.directionFRI = 'esquerda'
    else:
        if self.limitfri > -0.85:
            self.mesh_blade.translate(0, 0, -self.valuefri)
            self.mesh_handle.translate(0, 0, -self.valuefri)
        else:
            self.directionFRI = 'direita' 
     
def cuteloESPMovement(self):
    if self.directionESP == 'direita':
        if self.limitesp < 0.85:
            self.mesh_blade.translate(0, 0, self.valueesp)
            self.mesh_handle.translate(0, 0, self.valueesp)
        else:
            self.directionESP = 'esquerda'
    else:
        if self.limitesp > -0.85:
            self.mesh_blade.translate(0, 0, -self.valueesp)
            self.mesh_handle.translate(0, 0, -self.valueesp)
        else:
            self.directionESP = 'direita'

def cuteloROLLMovement(self):
    if self.directionROL == 'direita':
        if self.limitrol < 0.85 + 0.5:
            self.mesh_blade.translate(0, 0, self.valuerol)
            self.mesh_handle.translate(0, 0, self.valuerol)
        else:
            self.directionROL = 'esquerda'
    else:
        if self.limitrol > -0.85 + 0.5:
            self.mesh_blade.translate(0, 0, -self.valuerol)
            self.mesh_handle.translate(0, 0, -self.valuerol)
        else:
            self.directionROL = 'direita'
            
def cuteloAlvoMovement(self):
    if self.directionalvo == 'direita':
        if self.limitalvo < 1:
            self.mesh_blade.translate(0, 0, self.valuealvo)
            self.mesh_handle.translate(0, 0, self.valuealvo)
        else:
            self.directionalvo = 'esquerda'
    else:
        if self.limitalvo > -1:
            self.mesh_blade.translate(0, 0, -self.valuealvo)
            self.mesh_handle.translate(0, 0, -self.valuealvo)
        else:
            self.directionalvo = 'direita'

def alvoMovement(self):
    if self.directionalvo == 'direita':
        if self.limitalvo < 1:
            self.limitalvo = self.limitalvo + self.valuealvo
            self.mesh_alvo_feet.translate(0, 0, self.valuealvo)
            self.mesh_alvo_1.translate(0, 0, self.valuealvo)
            self.mesh_alvo_2.translate(0, 0, self.valuealvo)
            self.mesh_alvo_3.translate(0, 0, self.valuealvo)
            self.mesh_alvo_4.translate(0, 0, self.valuealvo)
            self.mesh_alvo_5.translate(0, 0, self.valuealvo)
            for box in self.targetBoxes1: box.translate(0,0, self.valuealvo, local=False)
            for box in self.targetBoxes2: box.translate(0,0, self.valuealvo, local=False)
            for box in self.targetBoxes3: box.translate(0,0, self.valuealvo, local=False)
            for box in self.targetBoxes4: box.translate(0,0, self.valuealvo, local=False)
            for box in self.targetBoxes5: box.translate(0,0, self.valuealvo, local=False)
        else:
            self.directionalvo = 'esquerda'
    else:
        if self.limitalvo > -1:
            self.limitalvo = self.limitalvo - self.valuealvo
            self.mesh_alvo_feet.translate(0, 0, -self.valuealvo)
            self.mesh_alvo_1.translate(0, 0, -self.valuealvo)
            self.mesh_alvo_2.translate(0, 0, -self.valuealvo)
            self.mesh_alvo_3.translate(0, 0, -self.valuealvo)
            self.mesh_alvo_4.translate(0, 0, -self.valuealvo)
            self.mesh_alvo_5.translate(0, 0, -self.valuealvo)
            for box in self.targetBoxes1: box.translate(0,0, -self.valuealvo, local=False)
            for box in self.targetBoxes2: box.translate(0,0, -self.valuealvo, local=False)
            for box in self.targetBoxes3: box.translate(0,0, -self.valuealvo, local=False)
            for box in self.targetBoxes4: box.translate(0,0, -self.valuealvo, local=False)
            for box in self.targetBoxes5: box.translate(0,0, -self.valuealvo, local=False)
        else:
            self.directionalvo = 'direita'

def espatulaMovement(self):
    if self.directionESP == 'direita':
        if self.limitesp < 0.85:
            self.limitesp = self.limitesp + self.valueesp
            self.mesh_base_2.translate(0, 0, self.valueesp)
            self.mesh_semPega.translate(0, 0, self.valueesp)
            self.mesh_pega.translate(0, 0, self.valueesp)
            self.base2_box.translate(0, 0, self.valueesp)
            for box in self.spatulaBoxes: box.translate(0,0, self.valueesp, local=False)
        else:
            self.directionESP = 'esquerda'
    else:
        if self.limitesp > -0.85:
            self.limitesp = self.limitesp - self.valueesp
            self.mesh_base_2.translate(0, 0, -self.valueesp)
            self.mesh_semPega.translate(0, 0, -self.valueesp)
            self.mesh_pega.translate(0, 0, -self.valueesp)
            self.base2_box.translate(0, 0, -self.valueesp)
            for box in self.spatulaBoxes: box.translate(0,0, -self.valueesp, local=False)
        else:
            self.directionESP = 'direita'
        
def frigideiraMovement(self):
    if self.directionFRI == 'direita':
        if self.limitfri < 0.85:
            self.limitfri = self.limitfri + self.valuefri
            self.mesh_base_1.translate(0, 0, self.valuefri)
            self.mesh_frigideira.translate(0, 0, self.valuefri)
            self.base1_box.translate(0, 0, self.valuefri)
            for box in self.panBoxes: box.translate(0,0, self.valuefri, local=False)
        else:
            self.directionFRI = 'esquerda'
    else:
        if self.limitfri > -0.85:
            self.limitfri = self.limitfri - self.valuefri
            self.mesh_base_1.translate(0, 0, -self.valuefri)
            self.mesh_frigideira.translate(0, 0, -self.valuefri)
            self.base1_box.translate(0, 0, -self.valuefri)
            for box in self.panBoxes: box.translate(0,0, -self.valuefri, local=False)
        else:
            self.directionFRI = 'direita'

def roloMovement(self):
    if self.directionROL == 'direita':
        if self.limitrol < 0.85 + 0.5:
            self.limitrol = self.limitrol + self.valuerol
            self.mesh_base_3.translate(0, 0, self.valuerol)
            self.mesh_rolo.translate(0, 0, self.valuerol)
            self.base3_box.translate(0, 0, self.valuerol)
            for box in self.rollBoxes: box.translate(0,0, self.valuerol, local=False)
        else:
            self.directionROL = 'esquerda'
    else:
        if self.limitrol > -0.85 + 0.5:
            self.limitrol = self.limitrol - self.valuerol
            self.mesh_base_3.translate(0, 0, -self.valuerol)
            self.mesh_rolo.translate(0, 0, -self.valuerol)
            self.base3_box.translate(0, 0, -self.valuerol)
            for box in self.rollBoxes: box.translate(0,0, -self.valuerol, local=False)
        else:
            self.directionROL = 'direita'
        

def cleaverMove(self):

    velocity = 0

    # impact moment
    if(self.cutelo_velocity[0] > 0 and (self.hit_pan or self.hit_handle)):
        self.cutelo_velocity[0]/=-3
        self.angle*=-1
        # print("impact handle/pan ")

    # process table rebound
    if(self.hit_tableHandle):
        self.cutelo_velocity[1]/=-2
        self.hit_tableHandle = False
        # self.angle*=-1
        # print("impact table with handle ")

    # aim cleaver
    # print(self.input.aim, (self.input.mouse_move_x != 0 or self.input.mouse_move_y != 0))
    if self.input.aim and (self.input.mouse_move_x != 0 or self.input.mouse_move_y != 0):

        mouseMoveX = 0
        mouseMoveY = 0
        bladeIntersection = False
        side = False
        timer = 30

        for box in self.bladeBoxes:
            # up box
            if intersect(box, self.verticalRestrictUp): 
                mouseMoveX = -abs(self.input.mouse_move_x)/1000
                bladeIntersection = True
                # print("colision up blade")
                self.timerVertical+=1
            elif self.timerVertical < timer and self.timerVertical != 0 and not intersect(box, self.verticalRestrictUp):
                mouseMoveX = -abs(self.input.mouse_move_x)/1000
                self.timerVertical+=1
            elif not intersect(box, self.verticalRestrictUp) and self.timerVertical == 0: mouseMoveX = -self.input.mouse_move_x/1000

            # left box
            if intersect(box, self.horizontalRestrictLeft): 
                mouseMoveY = abs(self.input.mouse_move_y)/500
                # print("colision sides")
                self.timerHorizontal+=1
                side = True
            elif self.timerHorizontal < timer and self.timerHorizontal != 0 and not intersect(box, self.horizontalRestrictLeft):
                mouseMoveY = abs(self.input.mouse_move_y)/500
                self.timerHorizontal+=1
            elif not intersect(box, self.horizontalRestrictLeft) and self.timerHorizontal == 0: mouseMoveY = self.input.mouse_move_y/500
        
            # right box
            if not side and intersect(box, self.horizontalRestrictRight): 
                mouseMoveY = -abs(self.input.mouse_move_y)/500
                # print("colision sides")
                self.timerHorizontal+=1
            elif not side and self.timerHorizontal < timer and self.timerHorizontal != 0 and not intersect(box, self.horizontalRestrictRight):
                mouseMoveY = -abs(self.input.mouse_move_y)/500
                self.timerHorizontal+=1
            elif not side and not intersect(box, self.horizontalRestrictRight) and self.timerHorizontal == 0: mouseMoveY = self.input.mouse_move_y/500
        
        for box in self.handleBoxes:
            # down box
            if intersect(box, self.verticalRestrictDown): 
                mouseMoveX = abs(self.input.mouse_move_x)/500
                # print("colision handle")
                self.timerVertical+=1
            elif not bladeIntersection and self.timerVertical < timer and self.timerVertical != 0 and not intersect(box, self.verticalRestrictDown):
                mouseMoveX = abs(self.input.mouse_move_x)/500
                self.timerVertical+=1
            elif not bladeIntersection and intersect(box, self.verticalRestrictDown) and self.timerVertical == 0:
                mouseMoveX = -self.input.mouse_move_x/500
         
        if(self.timerVertical >= timer): self.timerVertical = 0
        if(self.timerHorizontal >= timer): self.timerHorizontal = 0

        self.mesh_blade.translate(0, mouseMoveX, mouseMoveY, local = False)
        self.mesh_handle.translate(0, mouseMoveX, mouseMoveY, local = False)
        for box in self.cuteloBoxes: box.translate(0, mouseMoveX, mouseMoveY, local=False)
        self.translated_x += 0
        self.translated_y += mouseMoveX
        self.translated_z += mouseMoveY

        # self.test+=1
        # if(self.test > 10):
        #     self.test = 0
        #     print("y: ", -self.input.mouse_move_x)
        #     print("z: ", self.input.mouse_move_y)

        self.input.mouse_move_x = 0
        self.input.mouse_move_y = 0

    # charge cleaver
    if self.input.mouseDown and self.input.mousemotion:
        self.input.aim = False

        mouse_distance = math.sqrt(
            (self.input.line_end[0] - self.input.line_start[0])**2 + 
            (self.input.line_end[1] - self.input.line_start[1])**2
        )

        rotation_speed = 0.00008  
        max_rotation = 1
        rotation_angle = min(rotation_speed * mouse_distance, max_rotation)

        if self.total_rotation_angle + rotation_angle <= max_rotation:
            self.mesh_blade.rotate_z(rotation_angle)
            self.mesh_handle.rotate_z(rotation_angle)
            for box in self.cuteloBoxes: 
                box.translate(-self.translated_x, -self.translated_y, -self.translated_z, local=False)
                box.rotate_z(rotation_angle, local=False)
                box.translate(self.translated_x, self.translated_y, self.translated_z, local=False)
            self.total_rotation_angle += rotation_angle
        else:
            remaining_angle = max_rotation - self.total_rotation_angle
            if remaining_angle > 0:
                self.mesh_blade.rotate_z(remaining_angle)
                self.mesh_handle.rotate_z(remaining_angle)
                for box in self.cuteloBoxes: 
                    box.translate(-self.translated_x, -self.translated_y, -self.translated_z, local=False)
                    box.rotate_z(remaining_angle, local=False)
                    box.translate(self.translated_x, self.translated_y, self.translated_z, local=False)
                self.total_rotation_angle = max_rotation

    # initial speed
    if not self.input.mouseDown and self.input.afterLaunch:
        self.input.afterLaunch = False  
        self.cutelo_velocity = [
            min(abs(self.input.line_start[1] - self.input.line_end[1]) * 0.001, 0.240),
            min(abs(self.input.line_start[1] - self.input.line_end[1]) * 0.0002, 0.11),
            0
        ]
        # print(self.cutelo_velocity)
        
    # general movement of the cleaver
    if self.cutelo_velocity[0] != 0 or self.cutelo_velocity[1] != 0:

        if((self.cutelo_velocity[0] > 0 and self.hit_tableHandle) and not (self.hit_handle or self.hit_pan)):
            velocity = -0.016 
        # translation when it hits the pan or with the handle
        elif (self.cutelo_velocity[0] < -0.008 and (self.hit_handle or self.hit_pan or self.hit_tableHandle)):
            velocity = 0.008

        # x velocity
        self.cutelo_velocity[0] += velocity
        # y velocity
        if(self.cutelo_velocity[1] < 0 and min(self.cutelo_velocity[1], -0.12) == 0):
            self.cutelo_velocity[1] = -0.12
        elif(self.cutelo_velocity[1] < 0 and min(self.cutelo_velocity[1], -0.12) != 0):
            self.cutelo_velocity[1] += self.velocityY
        elif(self.cutelo_velocity[1] > 0): 
            self.cutelo_velocity[1] += self.velocityY

        # print("y vel: " ,self.cutelo_velocity[1])

        self.mesh_blade.translate(
        self.cutelo_velocity[0],
        self.cutelo_velocity[1],
        self.cutelo_velocity[2],
        local = False
        )
        self.mesh_handle.translate(
            self.cutelo_velocity[0],
            self.cutelo_velocity[1],
            self.cutelo_velocity[2],
            local = False
        )

        for box in self.cuteloBoxes: box.translate(
            self.cutelo_velocity[0],
            self.cutelo_velocity[1],
            self.cutelo_velocity[2], 
            local=False)
        self.translated_x += self.cutelo_velocity[0]
        self.translated_y += self.cutelo_velocity[1]
        self.translated_z += self.cutelo_velocity[2]
       
        for box in self.cuteloBoxes: 
            box.translate(-self.translated_x, -self.translated_y, -self.translated_z, local=False)
            box.rotate_z(self.angle, local=False)
            box.translate(self.translated_x, self.translated_y, self.translated_z, local=False)
        
        self.mesh_blade.rotate_z(self.angle)
        self.mesh_handle.rotate_z(self.angle)

        self.replay.append(self.cutelo_velocity)

    

def reset(self):
    self.checkAlvo = False
    self.past = False
    self.end_replay = False
    self.replay_frame = 0
    self.replay = []
    self.one._visible = False
    self.two._visible = False
    self.three._visible = False
    self.four._visible = False
    self.five._visible = False
    self.hit = False
    self.hit_handle = False
    self.miss._visible = False
    self.hit_pan = False
    self.hit_tableHandle = False
    self.velocityY = -0.003
    self.angle = -0.2
    self.speed = 0
    self.speedy = 0
    self.intersects = ""
    self.camera._matrix = self.initial_camera_state
    self.mesh_blade._matrix = self.initial_blade_state
    self.mesh_handle._matrix = self.initial_handle_state
    self.translated_x = -2.09
    self.translated_y =  0.6
    self.translated_z =  0.11

    for idx, box in enumerate(self.cuteloBoxes): box._matrix = self.initial_box_state[idx]
    
    self.mesh_blade.translate(0, 0.1, 0.1, local=False)
    self.mesh_handle.translate(0, 0.1, 0.1, local=False)
    for box in self.cuteloBoxes: box.translate(0, 0.1, 0.1, local=False)
    self.input.aim = True
    self.input.mouseDown = False
    pygame.mouse.set_pos(400, 300)
    self.cutelo_velocity = [0, 0, 0]
    self.total_rotation_angle = 0
    self.hit_timer = 0
