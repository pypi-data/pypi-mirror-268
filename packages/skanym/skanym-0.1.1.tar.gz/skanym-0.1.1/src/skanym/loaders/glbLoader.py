import struct
import warnings
from typing import List, Tuple
from pathlib import Path

import numpy as np

from skanym.utils.iFileLoader import IFileLoader
from skanym.core.model.skeleton import Skeleton
from skanym.core.model.joint import Joint
from skanym.core.animate.animation import Animation
from skanym.core.animate.curve.animationCurve import AnimationCurve
from skanym.core.animate.curve.positionCurve import PositionCurve
from skanym.core.animate.curve.quaternionCurve import QuaternionCurve
from skanym.core.animate.curve.key import Key
from skanym.core.math.transform import Transform


class GlbLoader(IFileLoader):
    def __init__(self, path: Path):
        super().__init__(path)
        try:
            import bpy
        except ImportError:
            warnings.warn("bpy module not found. Blender is not installed.")
            return
        
        try:
            from pygltflib import GLTF2
        except ImportError:
            warnings.warn("pygltflib module not found.")
            return
        
        self._GLTF2 = GLTF2
        
    
    def load_skeleton(self) -> Skeleton:
        return self._load_gltf()[0]
    
    def load_animation(self) -> Animation:
        return self._load_gltf()[1]
    
    def load_animations(self) -> List[Animation]:
        return NotImplementedError
    
    def _load_gltf(self) -> Tuple[Skeleton, Animation]:
        """TODO rewrite
        Creates an Animator object from a glTF 2.0 file.
        To create an Animator, we need the following piece of data:
            1. Skeleton Hierarchy
            2. Animator
                1. Joint Animations
                    1. Animation Curves

        glTF provides us two interesting lists: skins and animations
        We'll retrieve the Armature hierarchy from the skin list
        Then, we'll get the animation curves from the animation list

        We have to be careful Because the animation data contains
        final pos/rot and not the differences

        We can directly get the local_bind_transform from the metadata
        We need the accessor-buffer chain to get the time + TRS curves
        We are only interested in the translation and rotation though

        Same assumptions: one skin, one anim. No mesh yet.
        """
        
        def _array_from_accessor_id(accessor_i):
            accessor = gltf.accessors[accessor_i]
            buffer_view = gltf.bufferViews[accessor.bufferView]
            buffer = gltf.buffers[buffer_view.buffer]

            data = gltf.get_data_from_buffer_uri(buffer.uri)
            struct_size = buffer_view.byteLength // accessor.count
            output = []
            for i in range(accessor.count):
                index = buffer_view.byteOffset + accessor.byteOffset + i * struct_size
                d = data[index : index + struct_size]
                v = struct.unpack("<" + (struct_size // 4) * "f", d)
                if len(v) == 1:
                    v = v[0]
                output.append(v)

            return output

        gltf = self._GLTF2().load(self._path)

        skeleton_nodes = {}
        skeleton_root = None

        curves = {"translation": {}, "rotation": {}, "scale": {}, "weights": {}}
        anim_duration = 1.0

        # 1. Create a list of Joints from the file.
        for joint_i in gltf.skins[0].joints:
            skeleton_node = gltf.nodes[joint_i]

            joint_name = skeleton_node.name
            pos = skeleton_node.translation
            rot = skeleton_node.rotation

            if not pos:
                pos = [0.0, 0.0, 0.0]
            if not rot:
                rot = [0.0, 0.0, 0.0, 1.0]

            orient = np.quaternion(rot[3], rot[0], rot[1], rot[2])
            xform = Transform(pos, orient.normalized())
            joint = Joint(name=joint_name, local_bind_transform=xform)

            skeleton_nodes[joint_i] = joint
            curves["translation"][joint_i] = None
            curves["rotation"][joint_i] = None

        # 2. Create the skeleton hierarchy
        for joint_i in skeleton_nodes:
            skeleton_node = gltf.nodes[joint_i]
            children = [skeleton_nodes[child] for child in skeleton_node.children]
            skeleton_nodes[joint_i].add_children(children)

        armature_node = gltf.nodes[gltf.scenes[gltf.scene].nodes[0]]
        skeleton_root = skeleton_nodes[armature_node.children[0]]
        skeleton_name = armature_node.name
        
        output_skeleton = Skeleton(
            name=skeleton_name,
            root=skeleton_root,
        )

        # # 3. Create the animation curves from the file
        animation = gltf.animations[0]

        output_animation = Animation(
            name=self._path.stem,
            duration=0.0,
            shift=0.0,
            position_curves=[],
            rotation_curves=[],
        )
        
        for channel in animation.channels:
            target = channel.target
            joint_i = target.node

            sampler = animation.samplers[channel.sampler]
            key_times = _array_from_accessor_id(sampler.input)
            key_data = _array_from_accessor_id(sampler.output)
            keys = []

            key_len = len(key_times)
            duration = 1.0
            if key_len > 0:
                duration = key_times[-1]

                if key_len - 1 > anim_duration:
                    anim_duration = float(key_len - 1)

            for i in range(len(key_times)):
                t = float(int((key_times[i] / duration) * (key_len - 1)))
                v = key_data[i]
                if target.path == "translation":
                    p = skeleton_nodes[joint_i].local_bind_transform.getPosition()
                    if joint_i == armature_node.children[0]:
                        # Axis conversion for root joint
                        skeleton_nodes[joint_i].local_bind_transform.position = [p[0], -p[2], p[1]]
                        p = [0.0, 0.0, 0.0]
                        v = [v[0], -v[2], v[1]] 
                    keys.append(Key(t, np.array([v[0] - p[0], v[1] - p[1], v[2] - p[2]])))               
                
                elif target.path == "rotation":
                    q = skeleton_nodes[joint_i].local_bind_transform.getRotation()
                    Q1 = np.quaternion(v[3], v[0], v[1], v[2])
                    Q1 = Q1.normalized()
                    if joint_i == armature_node.children[0]:
                        keys.append(Key(t, Q1))
                    else:
                        keys.append(Key(t, q.conjugate() * Q1))
                else:
                    break

            for key in keys:
                key.time /= key_len - 1

            # if target.path == "translation":
            #     for key in keys:
            #         print(key.time, key.value)

            if target.path == "translation":
                curve = PositionCurve(keys)
                output_animation.position_curves.append(
                    AnimationCurve(curve, joint_i)
                )
            elif target.path == "rotation":
                curve = QuaternionCurve(keys)
                output_animation.rotation_curves.append(
                    AnimationCurve(curve, joint_i)
                )

        output_animation.duration /= IFileLoader.DEFAULT_FRAMERATE

        return output_skeleton, output_animation

if __name__ == "__main__":
    glb = GlbLoader(Path("C:\dev\MotionMachine\skanym\src\skanym\examples\input\walk_glb.glb"))
    # skeleton = glb.load_skeleton()
    animation = glb.load_animation()
    for curve in animation.position_curves[0:3]:
        for key in curve.curve.keys:
            pass
            # print(key)