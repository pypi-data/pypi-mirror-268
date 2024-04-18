"""
    Rendering 3D mashes via PyRender auxiliary functions.
"""

__all__ = ['FaceVideoPyrenderer']

import numpy as np
import trimesh
import pyrender
from typing import Optional


class FaceVideoPyrenderer(object):
    """
    Face video renderer based on pyrender.

    Parameters
    ----------
    faces : np.ndarray
        Mesh facets.
    viewport_width : int
        The width of the main viewport, in pixels.
    viewport_height : int
        The height of the main viewport, in pixels.
    """
    def __init__(self,
                 faces: np.ndarray,
                 viewport_width,
                 viewport_height):
        super(FaceVideoPyrenderer, self).__init__()
        self.faces = faces

        self.renderer = pyrender.OffscreenRenderer(
            viewport_width=viewport_width,
            viewport_height=viewport_height)

        self.scene = pyrender.Scene()

        camera = pyrender.PerspectiveCamera(
            yfov=np.pi / 4.0,
            aspectRatio=1.0)
        camera_pose = np.array([
            [1.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.02],
            [0.0, 0.0, 1.0, 0.45],
            [0.0, 0.0, 0.0, 1.0],
        ])
        self.scene.add(obj=camera, pose=camera_pose)

        light = pyrender.SpotLight(
            color=np.ones(3),
            intensity=0.5,
            innerConeAngle=np.pi / 16.0,
            outerConeAngle=np.pi / 6.0)
        self.scene.add(obj=light, pose=camera_pose)

    def __call__(self,
                 vertices: np.ndarray,
                 vertex_colors: Optional[np.ndarray]) -> np.ndarray:
        """
        Process render request.

        Parameters
        ----------
        vertices : np.ndarray
            Vertices.
        vertex_colors : np.ndarray or None
            Vertex colors.

        Returns
        -------
        np.ndarray
            Color render (image).
        """
        vertices0 = vertices - vertices.mean(axis=0)

        tm = trimesh.Trimesh(
            vertices=vertices0,
            faces=self.faces,
            vertex_colors=vertex_colors)
        mesh = pyrender.Mesh.from_trimesh(tm)
        mesh_node = self.scene.add(mesh)
        # self.pyrender.Viewer(self.scene, use_raymond_lighting=True)

        color_img, _ = self.renderer.render(scene=self.scene)

        self.scene.remove_node(mesh_node)

        return color_img
