import math
from core_ext.mesh import Mesh
from core_ext.texture import Texture
from geometry.normals_model import NormalsModel
from geometry.rectangle2 import RectangleGeometry
from geometry.sphere import SphereGeometry
from geometry.uv_model import UVModel
from material.flat import FlatMaterial
from material.texture import TextureMaterial

def generateObjects(self, nivel):
    textures = Texture(["images/blade.jpg", "images/handle.jpg", "images/table_top3.jpg", "images/table_feet.jpg", "images/pan.png", "images/alvo1.jpg", "images/alvo2.jpg", "images/alvo3.jpg", "images/alvo4.jpg", "images/alvo5.jpg", "images/metal.jpg", "images/borracha.jpg", "images/sky.jpg", "images/grass.jpg", "images/sky_new1.jpg", "images/cabin.png" , "images/chao.jpg", "images/quadro.png", "images/janela.jpg", "images/five.png", "images/four.png", "images/three.png", "images/two.png", "images/one.png", "images/p0.png", "images/p1.png", "images/p2.png", "images/p3.png", "images/p4.png", "images/p5.png", "images/p6.png", "images/p7.png", "images/p8.png", "images/p9.png", 
                        "images/p10.png", "images/p11.png", "images/p12.png", "images/p13.png", "images/p14.png", "images/p15.png", "images/miss.png",
                        "images/game_over.png", "images/level1.png", "images/level2.png", "images/level3.png", "images/cutelo_vida.png", "images/win.png", "images/vase.png", "images/planta.png", "images/arvore.jpg"]) #49
    label_material2 = TextureMaterial(texture=textures)
    label_geometry2 = RectangleGeometry(
            width=300, height=150,
            position=[290, -40],
            alignment=[1, 0]
        )
    
    label_geometry4 = RectangleGeometry(
        width=800, height=600,
        position=[800, 0],
        alignment=[1, 0]
    )
    
    self.game_over = Mesh(label_geometry4, label_material2, textures.texture_ref, 41, visible=False)
    self.hud_scene.add(self.game_over)

    self.level1 = Mesh(label_geometry4, label_material2, textures.texture_ref, 42, visible=True)
    self.hud_scene.add(self.level1)

    self.level2 = Mesh(label_geometry4, label_material2, textures.texture_ref, 43, visible=False)
    self.hud_scene.add(self.level2)

    self.level3 = Mesh(label_geometry4, label_material2, textures.texture_ref, 44, visible=False)
    self.hud_scene.add(self.level3)

    self.win = Mesh(label_geometry4, label_material2, textures.texture_ref, 46, visible=False)
    self.hud_scene.add(self.win)
    
    # p0
    self.p0 = Mesh(label_geometry2, label_material2, textures.texture_ref, 24, visible=True)
    # p1
    self.p1 = Mesh(label_geometry2, label_material2, textures.texture_ref, 25, visible=False)
    # p2
    self.p2 = Mesh(label_geometry2, label_material2, textures.texture_ref, 26, visible=False)
    # p3
    self.p3 = Mesh(label_geometry2, label_material2, textures.texture_ref, 27, visible=False)
    # p4
    self.p4 = Mesh(label_geometry2, label_material2, textures.texture_ref, 28, visible=False)
    # p5
    self.p5 = Mesh(label_geometry2, label_material2, textures.texture_ref, 29, visible=False)
    # p6
    self.p6 = Mesh(label_geometry2, label_material2, textures.texture_ref, 30, visible=False)
    # p7
    self.p7 = Mesh(label_geometry2, label_material2, textures.texture_ref, 31, visible=False)
    # p8
    self.p8 = Mesh(label_geometry2, label_material2, textures.texture_ref, 32, visible=False)
    # p9
    self.p9 = Mesh(label_geometry2, label_material2, textures.texture_ref, 33, visible=False)
    # p10
    self.p10 = Mesh(label_geometry2, label_material2, textures.texture_ref, 34, visible=False)
    # p11
    self.p11 = Mesh(label_geometry2, label_material2, textures.texture_ref, 35, visible=False)
    # p12
    self.p12 = Mesh(label_geometry2, label_material2, textures.texture_ref, 36, visible=False)
    # p13
    self.p13 = Mesh(label_geometry2, label_material2, textures.texture_ref, 37, visible=False)
    # p14
    self.p14 = Mesh(label_geometry2, label_material2, textures.texture_ref, 38, visible=False)
    # p15
    self.p15 = Mesh(label_geometry2, label_material2, textures.texture_ref, 39, visible=False)

    self.p_array = [self.p0, self.p1, self.p2, self.p3, self.p4, self.p5, self.p6, self.p7, self.p8, self.p9, self.p10, self.p11, self.p12, self.p13, self.p14, self.p15]
    for p in self.p_array:
        self.hud_scene.add(p)

    label_geometry2 = RectangleGeometry(
        width=100, height=100,
        position=[800, 500],
        alignment=[1, 0]
    )
    self.vida1 = Mesh(label_geometry2, label_material2, textures.texture_ref, 45, visible=True)

    # label_geometry2.position = [700, 500]
    label_geometry2 = RectangleGeometry(
        width=100, height=100,
        position=[725, 500],
        alignment=[1, 0]
    )
    self.vida2 = Mesh(label_geometry2, label_material2, textures.texture_ref, 45, visible=True)

    # label_geometry2.position = [600, 500] 
    label_geometry2 = RectangleGeometry(
        width=100, height=100,
        position=[650, 500],
        alignment=[1, 0]
    )
    self.vida3 = Mesh(label_geometry2, label_material2, textures.texture_ref, 45, visible=True)

    self.vidas = [self.vida1, self.vida2, self.vida3]
    for p in self.vidas:
        self.hud_scene.add(p)

    label_geometry2 = RectangleGeometry(
            width=100, height=100,
            position=[450, 450],
            alignment=[1, 0]
        )
    label_geometry3 = RectangleGeometry(
            width=323, height=100,
            position=[573, 450],
            alignment=[1, 0]
        )
    
    self.five = Mesh(label_geometry2, label_material2, textures.texture_ref, 19, visible=False)
    self.hud_scene.add(self.five)
    self.four = Mesh(label_geometry2, label_material2, textures.texture_ref, 20, visible=False)
    self.hud_scene.add(self.four)
    self.three = Mesh(label_geometry2, label_material2, textures.texture_ref, 21, visible=False)
    self.hud_scene.add(self.three)
    self.two = Mesh(label_geometry2, label_material2, textures.texture_ref, 22, visible=False)
    self.hud_scene.add(self.two)
    self.one = Mesh(label_geometry2, label_material2, textures.texture_ref, 23, visible=False)
    self.hud_scene.add(self.one)

    self.miss = Mesh(label_geometry3, label_material2, textures.texture_ref, 40, visible=False)
    self.hud_scene.add(self.miss)

    
    geometry_blade = UVModel('objects/CUTELO_BLADE.obj')
    blade_material = TextureMaterial(texture=textures)
    self.mesh_blade = Mesh(geometry_blade, blade_material, textures.texture_ref, 0)
    self.scene.add(self.mesh_blade)
    self.hud_scene.add(self.mesh_blade)
    self.mesh_blade.translate(-2.09, 0.5, -0.01, local=False)
    self.mesh_blade.rotate_z(-1)
    self.initial_blade_state = self.mesh_blade.local_matrix


    geometry_handle = NormalsModel('objects/HANDLE_NORMALS.obj')
    handle_material = FlatMaterial(texture=textures)
    self.mesh_handle = Mesh(geometry_handle, handle_material, textures.texture_ref, 1)
    self.scene.add(self.mesh_handle)
    self.mesh_handle.translate(-2.09, 0.5, -0.01, local=False)
    self.mesh_handle.rotate_z(-1)
    self.initial_handle_state = self.mesh_handle.local_matrix
    
    cabin_frente_geometry = RectangleGeometry(width=13, height=15)
    cabin_frente_material = FlatMaterial(texture=textures)
    cabin_frente = Mesh(cabin_frente_geometry, cabin_frente_material, textures.texture_ref, 15)
    self.scene.add(cabin_frente)
    cabin_frente.translate(4,-1,0)
    cabin_frente.rotate_y(-math.pi/2)
    
    cabin_lado_geometry = RectangleGeometry(width=13, height=15)
    cabin_lado_material = FlatMaterial(texture=textures)
    cabin_lado = Mesh(cabin_lado_geometry, cabin_lado_material, textures.texture_ref, 15)
    self.scene.add(cabin_lado)
    cabin_lado.translate(0,-1,4)
    
    quadro_geometry = RectangleGeometry(width=4, height=3)
    quadro_material = FlatMaterial(texture=textures)
    quadro = Mesh(quadro_geometry, quadro_material, textures.texture_ref, 17)
    self.scene.add(quadro)
    quadro.translate(3.98,3.8,1.8)
    quadro.rotate_y(-math.pi/2)
    
    janelaD_geometry = RectangleGeometry(width=3, height=3)
    janelaD_material = TextureMaterial(texture=textures)
    janelaD = Mesh(janelaD_geometry, janelaD_material, textures.texture_ref, 18)
    self.scene.add(janelaD)
    janelaD.rotate_y(-math.pi/2)
    janelaD.translate(-3,3.3,-3.80)
    
    chao_geometry = RectangleGeometry(width=100, height=100)
    chao_material = FlatMaterial(texture=textures, 
        property_dict={"repeatUV": [20, 20]})
    chao = Mesh(chao_geometry, chao_material,textures.texture_ref, 16)
    chao.rotate_x(-math.pi/2)
    chao.translate(0,0,-1)
    self.scene.add(chao)
    
    geometry_table_feet = NormalsModel('objects/TABLE_FEET.obj')
    table_feet_material = FlatMaterial(texture=textures)
    self.mesh_table_feet = Mesh(geometry_table_feet, table_feet_material, textures.texture_ref, 3)
    self.scene.add(self.mesh_table_feet)
    
    geometry_table_top = NormalsModel('objects/TABLE_TOP.obj')
    table_top_material = FlatMaterial(texture=textures)
    self.mesh_table_top = Mesh(geometry_table_top, table_top_material, textures.texture_ref, 2)
    self.scene.add(self.mesh_table_top)
    
    geometry_vase1 = NormalsModel('objects/vase.obj')
    vase1_material = FlatMaterial(texture=textures)
    self.mesh_vase1 = Mesh(geometry_vase1, vase1_material, textures.texture_ref, 47)
    self.scene.add(self.mesh_vase1)
    self.mesh_vase1.scale(0.3)
    self.mesh_vase1.translate(10,-2.5,-12)
    
    geometry_vase2 = NormalsModel('objects/vase.obj')
    vase2_material = FlatMaterial(texture=textures)
    self.mesh_vase2 = Mesh(geometry_vase2, vase2_material, textures.texture_ref, 47)
    self.scene.add(self.mesh_vase2)
    self.mesh_vase2.scale(0.3)
    self.mesh_vase2.translate(10,-2.5,9)
    
    geometry_plantaD = NormalsModel('objects/plant_leaves_2.obj')
    plantaD_material = FlatMaterial(texture=textures)
    self.mesh_plantaD = Mesh(geometry_plantaD, plantaD_material, textures.texture_ref, 48)
    self.scene.add(self.mesh_plantaD)
    self.mesh_plantaD.scale(0.3)
    self.mesh_plantaD.translate(10,-2.5,9)
    
    geometry_plantaA = NormalsModel('objects/plant_leaves_1_A.obj')
    plantaA_material = FlatMaterial(texture=textures)
    self.mesh_plantaA = Mesh(geometry_plantaA, plantaA_material, textures.texture_ref, 48)
    self.scene.add(self.mesh_plantaA)
    self.mesh_plantaA.scale(0.3)
    self.mesh_plantaA.translate(10,-2.5,-12)
    
    geometry_plantaB = NormalsModel('objects/plant_leaves_1_B.obj')
    plantaB_material = FlatMaterial(texture=textures)
    self.mesh_plantaB = Mesh(geometry_plantaB, plantaB_material, textures.texture_ref, 49)
    self.scene.add(self.mesh_plantaB)
    self.mesh_plantaB.scale(0.3)
    self.mesh_plantaB.translate(10,-2.5,-12)
    
    geometry_alvo_feet = NormalsModel('objects/ALVO_FEET.obj')
    alvo_feet_material = FlatMaterial(texture=textures)
    self.mesh_alvo_feet = Mesh(geometry_alvo_feet, alvo_feet_material, textures.texture_ref, 2)
    self.scene.add(self.mesh_alvo_feet)
    
    geometry_alvo_1 = NormalsModel('objects/ALVO_1.obj')
    alvo_1_material = FlatMaterial(texture=textures)
    self.mesh_alvo_1 = Mesh(geometry_alvo_1, alvo_1_material, textures.texture_ref, 5)
    self.scene.add(self.mesh_alvo_1)
    
    geometry_alvo_2 = NormalsModel('objects/ALVO_2.obj')
    alvo_2_material = FlatMaterial(texture=textures)
    self.mesh_alvo_2 = Mesh(geometry_alvo_2, alvo_2_material, textures.texture_ref, 6)
    self.scene.add(self.mesh_alvo_2)
    
    geometry_alvo_3 = NormalsModel('objects/ALVO_3.obj')
    alvo_3_material = FlatMaterial(texture=textures)
    self.mesh_alvo_3 = Mesh(geometry_alvo_3, alvo_3_material, textures.texture_ref, 7)
    self.scene.add(self.mesh_alvo_3)
    
    geometry_alvo_4 = NormalsModel('objects/ALVO_4.obj')
    alvo_4_material = FlatMaterial(texture=textures)
    self.mesh_alvo_4 = Mesh(geometry_alvo_4, alvo_4_material, textures.texture_ref, 8)
    self.scene.add(self.mesh_alvo_4)
    
    geometry_alvo_5 = NormalsModel('objects/ALVO_5.obj')
    alvo_5_material = FlatMaterial(texture=textures)
    self.mesh_alvo_5 = Mesh(geometry_alvo_5, alvo_5_material, textures.texture_ref, 9)
    self.scene.add(self.mesh_alvo_5)

    # if nivel != 1:
    geometry_base_1 = NormalsModel('objects/BASE_1.obj')
    base_1_material = FlatMaterial(texture=textures)
    self.mesh_base_1 = Mesh(geometry_base_1, base_1_material, textures.texture_ref, 10, visible = False)
    self.scene.add(self.mesh_base_1)
    
    geometry_base_2 = NormalsModel('objects/BASE_2.obj')
    base_2_material = FlatMaterial(texture=textures)
    self.mesh_base_2 = Mesh(geometry_base_2, base_2_material, textures.texture_ref, 10, visible = False)
    self.scene.add(self.mesh_base_2)
    
    geometry_base_3 = NormalsModel('objects/BASE_3.obj')
    base_3_material = FlatMaterial(texture=textures)
    self.mesh_base_3 = Mesh(geometry_base_3, base_3_material, textures.texture_ref, 10, visible = False)
    self.mesh_base_3.translate(0,0,-0.5)
    self.scene.add(self.mesh_base_3)
    
    geometry_pega = NormalsModel('objects/Pega.obj')
    pega_material = FlatMaterial(texture=textures)
    self.mesh_pega = Mesh(geometry_pega, pega_material, textures.texture_ref, 1, visible = False)
    self.scene.add(self.mesh_pega)
    
    geometry_semPega = NormalsModel('objects/semPega.obj')
    semPega_material = FlatMaterial(texture=textures)
    self.mesh_semPega = Mesh(geometry_semPega, semPega_material, textures.texture_ref, 11, visible = False)
    self.scene.add(self.mesh_semPega)
    
    geometry_rolo = NormalsModel('objects/ROLO_UV.obj')
    rolo_material = FlatMaterial(texture=textures)
    self.mesh_rolo = Mesh(geometry_rolo, rolo_material, textures.texture_ref, 1, visible = False)
    self.mesh_rolo.translate(0,0,-0.5)
    self.scene.add(self.mesh_rolo)
    
    geometry_frigideira = NormalsModel('objects/Frigideira.obj')
    frigideira_material = FlatMaterial(texture=textures)
    self.mesh_frigideira = Mesh(geometry_frigideira, frigideira_material, textures.texture_ref, 4, visible = False)
    self.scene.add(self.mesh_frigideira)

def generateHitboxes(self, nivel):
    #CUTELO HITBOXES
    self.cuteloBoxes = []
    self.handleBoxes = []
    box = self.newCuteloHitbox(0.030, 0.018, -0.04, 0)
    self.cuteloBoxes.append(box)
    self.handleBoxes.append(box)
    box = self.newCuteloHitbox(0.032, 0.018, -0.04, 0)
    self.cuteloBoxes.append(box)
    self.handleBoxes.append(box)
    box = self.newCuteloHitbox(0.032, 0.038, -0.04, 0)
    self.cuteloBoxes.append(box)
    self.handleBoxes.append(box)
    box = self.newCuteloHitbox(0.032, 0.058, -0.04, 0)
    self.cuteloBoxes.append(box)
    self.handleBoxes.append(box)
    box = self.newCuteloHitbox(0.032, 0.078, -0.04, 0)
    self.cuteloBoxes.append(box)
    self.handleBoxes.append(box)
    box = self.newCuteloHitbox(0.032, 0.098, -0.04, 0)
    self.cuteloBoxes.append(box)
    self.handleBoxes.append(box)
    box = self.newCuteloHitbox(0.032, 0.118, -0.04, 0)
    self.cuteloBoxes.append(box)
    self.handleBoxes.append(box)
    box = self.newCuteloHitbox(0.032, 0.138, -0.04, 0)
    self.cuteloBoxes.append(box)
    self.handleBoxes.append(box)
    box = self.newCuteloHitbox(0.032, 0.158, -0.04, 0)
    self.cuteloBoxes.append(box)
    self.handleBoxes.append(box)
    box = self.newCuteloHitbox(0.032, 0.178, -0.04, 0)
    self.cuteloBoxes.append(box)
    self.handleBoxes.append(box)
    box = self.newCuteloHitbox(0.030, 0.198, -0.04, 0)
    self.cuteloBoxes.append(box)
    self.handleBoxes.append(box)
    box = self.newCuteloHitbox(0.020, 0.218, -0.04, 0)
    self.cuteloBoxes.append(box)
    self.handleBoxes.append(box)
    box = self.newCuteloHitbox(0.013, 0.228, -0.04, 0)
    self.cuteloBoxes.append(box)
    self.handleBoxes.append(box)
    box = self.newCuteloHitbox(0.008, 0.238, -0.04, 0)
    self.cuteloBoxes.append(box)
    self.handleBoxes.append(box)

    self.bladeBoxes = []
    # box = self.newCuteloHitbox(0.15, -0.03, 0.04, 0)
    # self.cuteloBoxes.append(box)
    # self.bladeBoxes.append(box)
    # box = self.newCuteloHitbox(0.15, -0.17, 0.04, 0)
    # self.cuteloBoxes.append(box)
    # self.bladeBoxes.append(box)
    box = self.newCuteloHitbox(0.05, -0.248, 0.113, 0)
    self.cuteloBoxes.append(box)
    self.bladeBoxes.append(box)
    box = self.newCuteloHitbox(0.05, -0.248, -0.031, 0)
    self.cuteloBoxes.append(box)
    self.bladeBoxes.append(box)
    box = self.newCuteloHitbox(0.05, -0.101, 0.116, 0)
    self.cuteloBoxes.append(box)
    self.bladeBoxes.append(box)
    box = self.newCuteloHitbox(0.05, 0.047, 0.116, 0)
    self.cuteloBoxes.append(box)
    self.bladeBoxes.append(box)

    # box = self.newCuteloHitbox(0.05, -0.103, -0.035, 0)
    # self.cuteloBoxes.append(box)
    # self.bladeBoxes.append(box)
    self.initial_box_state = []
    for box in self.cuteloBoxes: 
        # box.translate(-self.translated_x, -self.translated_y, -self.translated_z, local=False)
        box.rotate_z(-1, local=False)
        # box.translate(self.translated_x, self.translated_y, self.translated_z, local=False)
        box.translate(-2.09, 0.5, -0.01, local=False)
        self.initial_box_state.append(box._matrix)
    self.translated_x = -2.09
    self.translated_y =  0.6
    self.translated_z =  0.11
    

    # TARGET HITBOXES
    self.targetBoxes1 = []
    box = self.newSquareHitbox(0.1, 0.135, 0.135, 2.151, 0.764, -0.005) #highest value
    self.targetBoxes1.append(box)
    box = self.newSquareHitbox(0.1, 0.1, 0.04, 2.151, 0.764, -0.073) #highest value
    self.targetBoxes1.append(box)
    box = self.newSquareHitbox(0.1, 0.1, 0.04, 2.151, 0.764, 0.059) #highest value
    self.targetBoxes1.append(box)
    box = self.newSquareHitbox(00.1, 0.04, 0.1, 2.151, 0.832, -0.005) #highest value
    self.targetBoxes1.append(box)
    box = self.newSquareHitbox(00.1, 0.04, 0.1, 2.151, 0.696, -0.005) #highest value
    self.targetBoxes1.append(box)

    self.targetBoxes2 = []
    box = self.newSquareHitbox(0.1, 0.28, 0.28, 2.151, 0.764, -0.005)
    self.targetBoxes2.append(box)
    box = self.newSquareHitbox(00.1, 0.1, 0.04, 2.151, 0.764, -0.165)
    self.targetBoxes2.append(box)
    box = self.newSquareHitbox(00.1, 0.04, 0.02, 2.151, 0.834, -0.155)
    self.targetBoxes2.append(box)
    box = self.newSquareHitbox(00.1, 0.04, 0.02, 2.151, 0.694, -0.155)
    self.targetBoxes2.append(box)
    box = self.newSquareHitbox(00.1, 0.04, 0.02, 2.151, 0.694, 0.145)
    self.targetBoxes2.append(box)
    box = self.newSquareHitbox(00.1, 0.04, 0.02, 2.151, 0.834, 0.145)
    self.targetBoxes2.append(box)
    box = self.newSquareHitbox(00.1, 0.1, 0.04, 2.151, 0.764, 0.155)
    self.targetBoxes2.append(box)
    box = self.newSquareHitbox(00.1, 0.04, 0.1, 2.151, 0.604, -0.005)
    self.targetBoxes2.append(box)
    box = self.newSquareHitbox(00.1, 0.04, 0.1, 2.151, 0.924, -0.005)
    self.targetBoxes2.append(box)
    box = self.newSquareHitbox(00.1, 0.02, 0.04, 2.151, 0.914, 0.0645)
    self.targetBoxes2.append(box)
    box = self.newSquareHitbox(00.1, 0.02, 0.04, 2.151, 0.914, -0.0755)
    self.targetBoxes2.append(box)
    box = self.newSquareHitbox(00.1, 0.02, 0.04, 2.151, 0.614, -0.0755)
    self.targetBoxes2.append(box)
    box = self.newSquareHitbox(00.1, 0.02, 0.04, 2.151, 0.614, 0.0655)

    self.targetBoxes3 = []
    box = self.newSquareHitbox(00.1, 0.44, 0.44, 2.151, 0.764, -0.005)
    self.targetBoxes3.append(box)

    box = self.newSquareHitbox(00.1, 0.07, 0.2, 2.151, 1.019, -0.005)
    self.targetBoxes3.append(box)
    box = self.newSquareHitbox(00.1, 0.07, 0.2, 2.151, 0.509, -0.005)
    self.targetBoxes3.append(box)
    box = self.newSquareHitbox(00.1, 0.2, 0.07, 2.151, 0.764, -0.260)
    self.targetBoxes3.append(box)
    box = self.newSquareHitbox(00.1, 0.2, 0.07, 2.151, 0.764, 0.249)
    self.targetBoxes3.append(box)

    box = self.newSquareHitbox(00.1, 0.07, 0.035, 2.151, 0.899, 0.233)
    self.targetBoxes3.append(box)
    box = self.newSquareHitbox(00.1, 0.07, 0.035, 2.151, 0.629, 0.233)
    self.targetBoxes3.append(box)
    box = self.newSquareHitbox(00.1, 0.07, 0.035, 2.151, 0.629, -0.242)
    self.targetBoxes3.append(box)
    box = self.newSquareHitbox(00.1, 0.07, 0.035, 2.151, 0.899, -0.242)
    self.targetBoxes3.append(box)

    box = self.newSquareHitbox(00.1, 0.035, 0.07, 2.151, 1.002, 0.13)
    self.targetBoxes3.append(box)
    box = self.newSquareHitbox(00.1, 0.035, 0.07, 2.151, 0.526, 0.13)
    self.targetBoxes3.append(box)
    box = self.newSquareHitbox(00.1, 0.035, 0.07, 2.151, 0.527, -0.140)
    self.targetBoxes3.append(box)
    box = self.newSquareHitbox(00.1, 0.035, 0.07, 2.151, 1.002, -0.140)

    self.targetBoxes4 = []
    box = self.newSquareHitbox(00.1, 0.65, 0.65, 2.151, 0.764, -0.005)
    self.targetBoxes4.append(box)

    box = self.newSquareHitbox(00.1, 0.1, 0.3, 2.151, 1.139, -0.005)
    self.targetBoxes4.append(box)
    box = self.newSquareHitbox(00.1, 0.1, 0.3, 2.151, 0.389, -0.005)
    self.targetBoxes4.append(box)
    box = self.newSquareHitbox(00.1, 0.3, 0.1, 2.151, 0.764, 0.37)
    self.targetBoxes4.append(box)
    box = self.newSquareHitbox(00.1, 0.3, 0.1, 2.151, 0.764, -0.38)
    self.targetBoxes4.append(box)

    box = self.newSquareHitbox(00.1, 0.06, 0.09, 2.151, 1.119, -0.2)
    self.targetBoxes4.append(box)
    box = self.newSquareHitbox(00.1, 0.06, 0.09, 2.151, 1.119, 0.19)
    self.targetBoxes4.append(box)
    box = self.newSquareHitbox(00.1, 0.06, 0.09, 2.151, 0.409, 0.19)
    self.targetBoxes4.append(box)
    box = self.newSquareHitbox(00.1, 0.06, 0.09, 2.151, 0.409, -0.2)
    self.targetBoxes4.append(box)

    box = self.newSquareHitbox(00.1, 0.09, 0.06, 2.151, 0.959, 0.35)
    self.targetBoxes4.append(box)
    box = self.newSquareHitbox(00.1, 0.09, 0.06, 2.151, 0.569, 0.35)
    self.targetBoxes4.append(box)
    box = self.newSquareHitbox(00.1, 0.09, 0.06, 2.151, 0.569, -0.36)
    self.targetBoxes4.append(box)
    box = self.newSquareHitbox(00.1, 0.09, 0.06, 2.151, 0.959, -0.36)
    self.targetBoxes4.append(box)

    self.targetBoxes5 = []
    box = self.newSquareHitbox(00.1, 0.85, 0.85, 2.151, 0.764, -0.005)
    self.targetBoxes5.append(box)

    box = self.newSquareHitbox(00.1, 0.14, 0.4, 2.151, 1.259, -0.005)
    self.targetBoxes5.append(box)
    box = self.newSquareHitbox(00.1, 0.14, 0.4, 2.151, 0.269, -0.005)
    self.targetBoxes5.append(box)
    box = self.newSquareHitbox(00.1, 0.4, 0.14, 2.151, 0.764, -0.5)
    self.targetBoxes5.append(box)
    box = self.newSquareHitbox(00.1, 0.4, 0.14, 2.151, 0.764, 0.49)
    self.targetBoxes5.append(box)

    box = self.newSquareHitbox(00.1, 0.09, 0.09, 2.151, 1.234, -0.25)
    self.targetBoxes5.append(box)
    box = self.newSquareHitbox(00.1, 0.09, 0.09, 2.151, 1.234, 0.24)
    self.targetBoxes5.append(box)
    box = self.newSquareHitbox(00.1, 0.09, 0.09, 2.151, 0.294, 0.24)
    self.targetBoxes5.append(box)
    box = self.newSquareHitbox(00.1, 0.09, 0.09, 2.151, 0.294, -0.25)
    self.targetBoxes5.append(box)
    box = self.newSquareHitbox(00.1, 0.09, 0.09, 2.151, 1.009, -0.475)
    self.targetBoxes5.append(box)
    box = self.newSquareHitbox(00.1, 0.09, 0.09, 2.151, 0.519, -0.475)
    self.targetBoxes5.append(box)
    box = self.newSquareHitbox(00.1, 0.09, 0.09, 2.151, 0.519, 0.465)
    self.targetBoxes5.append(box)
    box = self.newSquareHitbox(00.1, 0.09, 0.09, 2.151, 1.009, 0.465)
    self.targetBoxes5.append(box)

    box = self.newSquareHitbox(00.1, 0.06, 0.06, 2.151, 1.219, -0.325)
    self.targetBoxes5.append(box)
    box = self.newSquareHitbox(00.1, 0.06, 0.06, 2.151, 1.219, 0.315)
    self.targetBoxes5.append(box)
    box = self.newSquareHitbox(00.1, 0.06, 0.06, 2.151, 1.084, 0.45)
    self.targetBoxes5.append(box)
    box = self.newSquareHitbox(00.1, 0.06, 0.06, 2.151, 0.444, 0.45)
    self.targetBoxes5.append(box)
    box = self.newSquareHitbox(00.1, 0.06, 0.06, 2.151, 0.309, 0.315)
    self.targetBoxes5.append(box)
    box = self.newSquareHitbox(00.1, 0.06, 0.06, 2.151, 0.309, -0.325)
    self.targetBoxes5.append(box)
    box = self.newSquareHitbox(00.1, 0.06, 0.06, 2.151, 0.444, -0.46)
    self.targetBoxes5.append(box)
    box = self.newSquareHitbox(00.1, 0.06, 0.06, 2.151, 1.084, -0.46)
    self.targetBoxes5.append(box)

    # restrict boxes
    # left
    self.horizontalRestrictLeft  = self.newSquareHitbox(1, 0.4, 0.04, -2, 0.75, -0.3) 
    # right
    self.horizontalRestrictRight = self.newSquareHitbox(1, 0.4, 0.04, -2, 0.75, 0.3) 
    # up
    self.verticalRestrictUp = self.newSquareHitbox(1, 0, 0.6, -2, 1.1, 0) 
    # down
    self.verticalRestrictDown = self.newSquareHitbox(1, 0, 0.6, -2, 0.3, 0) 

    self.outside_box = self.newSquareHitbox(0.1, 100, 100, 3+0.9, 0.764, -0.005) 
    
    self.table_box = self.newSquareHitbox(3, 0.1, 2, -0.25, 0, -0.03) 
    
    self.base1_box = self.newSquareHitbox(0.2, 0.05, 0.2, -0.34, 0.08, -0.03) 
    self.base2_box = self.newSquareHitbox(0.2, 0.05, 0.2, 0.21, 0.08, -0.03) 
    self.base3_box = self.newSquareHitbox(0.2, 0.05, 0.2, 0.72, 0.08, -0.03-0.5) 
    
    self.chao_box = self.newSquareHitbox(10, 0, 10, 0, -1, 0) 
    
    # if nivel != 1:
    #PAN HITBOXES
    self.panBoxes = []
    box = self.newSquareHitbox(0.1, 0.4, 0.4, -0.299, 0.744, -0.03)
    self.panBoxes.append(box)

    box = self.newSquareHitbox(0.1, 0.1, 0.2, -0.299, 0.97, -0.03)
    self.panBoxes.append(box)
    box = self.newSquareHitbox(0.1, 0.1, 0.2, -0.299, 0.541, -0.03)
    self.panBoxes.append(box)
    box = self.newSquareHitbox(0.1, 0.2, 0.1, -0.299, 0.749, -0.241)
    self.panBoxes.append(box)
    box = self.newSquareHitbox(0.1, 0.2, 0.1, -0.299, 0.749, 0.186)
    self.panBoxes.append(box)

    box = self.newSquareHitbox(0.02, 0.4, 0.05, -0.324, 0.309, -0.035)
    self.panBoxes.append(box)

    #SPATULA HITBOXES
    self.spatulaBoxes = []
    box = self.newSquareHitbox(0.02, 0.8, 0.05, 0.202, 0.518, -0.035)
    self.spatulaBoxes.append(box)
    box = self.newSquareHitbox(0.05, 0.05, 0.24, 0.193, 0.944, -0.033)
    self.spatulaBoxes.append(box)
    box = self.newSquareHitbox(0.05, 0.05, 0.24, 0.17, 0.995, -0.034)
    self.spatulaBoxes.append(box)
    box = self.newSquareHitbox(0.05, 0.05, 0.24, 0.144, 1.045, -0.034)
    self.spatulaBoxes.append(box)
    box = self.newSquareHitbox(0.05, 0.05, 0.24, 0.103, 1.095, -0.035)
    self.spatulaBoxes.append(box)

    #ROLL HITBOXES
    self.rollBoxes = []
    box = self.newSquareHitbox(0.15, 0.7, 0.15, 0.717, 0.606, -0.011-0.5)
    self.rollBoxes.append(box)
    box = self.newSquareHitbox(0.08, 0.2, 0.08, 0.717, 1.017, -0.011-0.5)
    self.rollBoxes.append(box)
    box = self.newSquareHitbox(0.08, 0.2, 0.08, 0.717, 0.204, -0.018-0.5)
    self.rollBoxes.append(box)
