from core_ext.uv_obj_reader import my_obj_reader
from geometry.geometry import Geometry


class UVModel(Geometry):
    def __init__(self, file):
        super().__init__()
        result = my_obj_reader(file)
        position_data = result[0]
        uv_data = result[1]
        # print(face_normal_data)
        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", uv_data)
        self.count_vertices()
