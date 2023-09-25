from material.material import Material
from core.uniform import Uniform


class BasicMaterial(Material):
    def __init__(self, vertex_shader_code=None, fragment_shader_code=None, color=[1.0, 1.0, 1.0]):
        if vertex_shader_code is None:
            vertex_shader_code = """
            uniform mat4 projectionMatrix;
            uniform mat4 viewMatrix;
            uniform mat4 modelMatrix;
            in vec3 vertexPosition;
                    
            void main()
            {
                gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(vertexPosition, 1.0);
            }
            """
        if fragment_shader_code is None:
            fragment_shader_code = """
            uniform vec3 baseColor;
            out vec4 fragColor;
            
            void main()
            {
                fragColor = vec4(baseColor, 1.0);
            }
            """
        super().__init__(vertex_shader_code, fragment_shader_code)
        self.add_uniform("vec3", "baseColor", color)
        self.locate_uniforms()
