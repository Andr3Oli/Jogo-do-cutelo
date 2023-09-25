import OpenGL.GL as GL

from core_ext.object3d import Object3D
from extras.text_texture import TextTexture
from material.texture import TextureMaterial


class Mesh(Object3D):
    """
    Contains geometric data that specifies vertex-related properties and material data
    that specifies the general appearance of the object
    """
    def __init__(self, geometry, material, texture_ref=None, texture_number=None, visible=True,):
        super().__init__()
        # if isinstance(material, TextureMaterial): breakpoint()
        self._geometry = geometry
        self._material = material
        self._textures = texture_ref
        self._texture_number = texture_number
        # self._texture = texture
        # Should this object be rendered?
        self._visible = visible
        # Set up associations between attributes stored in geometry
        # and shader program stored in material
        self._vao_ref = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self._vao_ref)
        for variable_name, attribute_object in geometry.attribute_dict.items():
            attribute_object.associate_variable(material.program_ref, variable_name)
        # Unbind this vertex array object
        GL.glBindVertexArray(0)

    @property
    def geometry(self):
        return self._geometry

    @property
    def material(self):
        return self._material

    @property
    def vao_ref(self):
        return self._vao_ref
    
    @property
    def textures(self):
        return self._textures

    @property
    def texture_number(self):
        return self._texture_number

    @property
    def visible(self):
        return self._visible
