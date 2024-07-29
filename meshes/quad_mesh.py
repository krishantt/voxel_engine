from meshes.base_mesh import BaseMesh
import numpy as np
from settings import *


class QuadMesh(BaseMesh):
    def __init__(self, app):
        super().__init__()

        self.app = app
        self.ctx = self.app.ctx
        # self.program = self.app.shader_program.quad

        # self.vbo_format = '3f 3f'
        # self.attrs = ('in_position', 'in_color')

        self.program = self.app.shader_program.water

        self.vbo_format = '2u1 3u1'
        self.attrs = ('in_tex_coord', 'in_position')
        self.vao = self.get_vao()


    def get_vertex_data(self):
        vertices = np.array([
            (0, 0, 0), (1, 0, 1), (1, 0, 0),
            (0, 0, 0), (0, 0, 1), (1, 0, 1)
        ], dtype='uint8')

        tex_coords = np.array([
            (0, 0), (1, 1), (1, 0),
            (0, 0), (0, 1), (1, 1)
        ], dtype='uint8')

        vertex_data = np.hstack([tex_coords, vertices])
        return vertex_data











    # def get_vertex_data(self):
    #     vertices = [
    #         (0.5, 0.5, 0.0), (-0.5, 0.5, 0.0), (-0.5, -0.5, 0.0),
    #         (0.5, 0.5, 0.0), (-0.5, -0.5, 0.0), (0.5, -0.5, 0.0)
    #     ]
    #     colors = [
    #         (0, 1, 0), (1, 0, 0), (1, 1, 0),
    #         (0, 1, 0), (1, 1, 0), (0, 0, 1)
    #     ]
    #     vertex_data = np.hstack([vertices, colors], dtype=np.float32)
    #     return vertex_data
