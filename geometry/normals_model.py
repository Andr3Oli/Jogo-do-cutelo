from core_ext.normals_obj_reader import my_obj_reader
from geometry.geometry import Geometry


class NormalsModel(Geometry):
    def __init__(self, file):
        super().__init__()
        result = my_obj_reader(file)
        position_data = result[0]
        uv_data = result[1]
        face_normal_data = result[2]
        # print(face_normal_data)
        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", uv_data)
        self.add_attribute("vec3", "faceNormal", face_normal_data)
        self.count_vertices()
