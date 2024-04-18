import sys
import warnings
from typing import List
from pathlib import Path

import numpy as np

from skanym.loaders.iFileLoader import IFileLoader
from skanym.structures.character.skeleton import Skeleton
from skanym.structures.character.joint import Joint
from skanym.structures.animation.animation import Animation
from skanym.structures.animation.animationCurve import AnimationCurve
from skanym.structures.animation.positionCurve import PositionCurve
from skanym.structures.animation.quaternionCurve import QuaternionCurve
from skanym.structures.animation.key import Key
from skanym.structures.data.transform import Transform


class FbxLoader(IFileLoader):
    def __init__(self, path: Path):
        super().__init__(path)
        try:
            import fbx
        except ImportError:
            import platform

            sys.path.append("C:/dev/MotionMachine/skanym/src/skanym/utils/fbx_bindings")

            # Second try:
            try:
                import fbx
            except ImportError:
                raise

        self._fbx = fbx

    def load_skeleton(self) -> Skeleton:
        fbx_scene = self._load_fbx_scene(self._path)

        root_node = fbx_scene.GetRootNode()
        skeleton_node_list = []

        self._load_skeleton_nodes(skeleton_node_list, root_node)

        skeleton_root = None

        joint_hierarchy = []

        for skeleton_node in skeleton_node_list:
            # Creating joints
            joint_name = skeleton_node.GetName()

            pos = np.array([float(val) for val in skeleton_node.LclTranslation.Get()])

            rotation = skeleton_node.PreRotation.Get()

            v = self._fbx.FbxVector4(rotation)

            m = self._fbx.FbxAMatrix()
            m.SetR(v)
            q = m.GetQ()
            orient = np.quaternion(q.GetAt(3), q.GetAt(0), q.GetAt(1), q.GetAt(2))
            # if orient.w < 0:
            #     print(f"NEGATIVE QUATERNION for {joint_name} in {fbx_file_path.split('/')[-1]}, {orient}")

            joint = Joint(name=joint_name, local_bind_transform=Transform(pos, orient))

            children = []
            for i in range(skeleton_node.GetChildCount()):
                child_node = skeleton_node.GetChild(i)
                children.append(child_node.GetName())

            joint_hierarchy.append((joint, children))

            if skeleton_root is None:
                skeleton_root = joint

        # Building joint hierarchy
        joint_list = [relation[0] for relation in joint_hierarchy]

        for relation in joint_hierarchy:
            children = [joint for joint in joint_list if joint.name in relation[1]]
            relation[0].add_children(children)

        # Creating skeleton
        skeleton_root.local_bind_transform = Transform()
        skeleton = Skeleton(skeleton_root)

        return skeleton

    def load_animation(self) -> Animation:
        fbx_scene = self._load_fbx_scene(self._path)

        root_node = fbx_scene.GetRootNode()
        skeleton_node_list = []

        self._load_skeleton_nodes(skeleton_node_list, root_node)

        anim_layer = self._get_anim_layer(fbx_scene)

        animation = Animation(
            name=self._path.stem,
            duration=0.0,
            shift=0.0,
            position_curves=[],
            rotation_curves=[],
        )

        node_id = 0
        for skeleton_node in skeleton_node_list:
            # Creating joint animations
            if anim_layer:
                translation_curve, rotation_curve, duration = self._load_curves(
                    skeleton_node, anim_layer
                )
                if duration > animation.duration:
                    animation.duration = duration
                animation.position_curves.append(
                    AnimationCurve(translation_curve, node_id)
                )
                animation.rotation_curves.append(
                    AnimationCurve(rotation_curve, node_id)
                )

            node_id += 1

        animation.duration /= IFileLoader.DEFAULT_FRAMERATE

        return animation

    def load_animations(self) -> List[Animation]:
        return NotImplementedError

    def _load_fbx_scene(self, fbx_file_path: Path):
        sdk_manager = self._fbx.FbxManager.Create()

        ios = self._fbx.FbxIOSettings.Create(sdk_manager, self._fbx.IOSROOT)
        sdk_manager.SetIOSettings(ios)

        importer = self._fbx.FbxImporter.Create(sdk_manager, "")

        if not importer.Initialize(str(fbx_file_path), -1, sdk_manager.GetIOSettings()):
            print("Call to FbxImporter::Initialize() failed.")
            raise ImportError(
                "Error importing file %s file not found or %s"
                % (
                    str(fbx_file_path),
                    importer.GetStatus().GetErrorString(),
                )
            )

        scene = self._fbx.FbxScene.Create(sdk_manager, "myScene")
        importer.Import(scene)
        importer.Destroy()

        return scene

    def _load_skeleton_nodes(self, skeleton_node_list, root_node):
        for i in range(root_node.GetChildCount()):
            child_node = root_node.GetChild(i)
            for i in range(child_node.GetNodeAttributeCount()):
                attribute = child_node.GetNodeAttributeByIndex(i)
                if type(attribute) == self._fbx.FbxSkeleton:
                    skeleton_node_list.append(child_node)
            self._load_skeleton_nodes(skeleton_node_list, child_node)

    def _get_anim_layer(self, scene):
        nb_anim_stack = scene.GetSrcObjectCount(
            self._fbx.FbxCriteria.ObjectType(self._fbx.FbxAnimStack.ClassId)
        )

        if nb_anim_stack == 0:
            raise ValueError("No animation stack found in fbx file.")
        elif nb_anim_stack > 1:
            warnings.warn(
                "Multiple anim stacks found in fbx file, only the first one is treated",
                stacklevel=2,
            )

        anim_stack = scene.GetSrcObject(
            self._fbx.FbxCriteria.ObjectType(self._fbx.FbxAnimStack.ClassId), 0
        )

        nb_anim_layers = anim_stack.GetSrcObjectCount(
            self._fbx.FbxCriteria.ObjectType(self._fbx.FbxAnimLayer.ClassId)
        )

        if nb_anim_layers == 0:
            raise ValueError("No animation layer found in anim stack.")
        elif nb_anim_layers > 1:
            warnings.warn(
                "Multiple anim layers found in anim stack, only the first one is treated",
                stacklevel=2,
            )

        anim_layer = anim_stack.GetSrcObject(
            self._fbx.FbxCriteria.ObjectType(self._fbx.FbxAnimLayer.ClassId), 0
        )

        return anim_layer

    def _load_curves(self, skeleton_node, anim_layer):
        # Assumes that when a change to the position/orientation of a joint is made,
        # the translation/rotation values for each axis are given in the keyframe.

        tX_curve = skeleton_node.LclTranslation.GetCurve(anim_layer, "X")
        tY_curve = skeleton_node.LclTranslation.GetCurve(anim_layer, "Y")
        tZ_curve = skeleton_node.LclTranslation.GetCurve(anim_layer, "Z")
        rX_curve = skeleton_node.LclRotation.GetCurve(anim_layer, "X")
        rY_curve = skeleton_node.LclRotation.GetCurve(anim_layer, "Y")
        rZ_curve = skeleton_node.LclRotation.GetCurve(anim_layer, "Z")

        translation_keys = []
        rotation_keys = []

        duration = 1.0

        if tX_curve is not None and tY_curve is not None and tZ_curve is not None:
            for key_id in range(tX_curve.KeyGetCount()):
                key_time = tX_curve.KeyGetTime(key_id).GetTimeString("")

                t = np.array(
                    [
                        tX_curve.KeyGetValue(key_id),
                        tY_curve.KeyGetValue(key_id),
                        tZ_curve.KeyGetValue(key_id),
                    ]
                )

                if "*" in key_time:
                    # Keys whose time is marked with "*" are not used in the animation.
                    # They are probably used to improve interpolation quality in between keyframes.
                    pass
                else:
                    key_time = float(key_time)
                    if key_time > duration:
                        duration = key_time

                    translation_keys.append(Key(key_time, t))

        if rX_curve is not None and rY_curve is not None and rZ_curve is not None:
            for key_id in range(rX_curve.KeyGetCount()):
                key_time = rX_curve.KeyGetTime(key_id).GetTimeString("")

                v = self._fbx.FbxVector4(
                    rX_curve.KeyGetValue(key_id),
                    rY_curve.KeyGetValue(key_id),
                    rZ_curve.KeyGetValue(key_id),
                )

                m = self._fbx.FbxAMatrix()
                m.SetR(v)
                q = m.GetQ()
                q = np.array([q.GetAt(3), q.GetAt(0), q.GetAt(1), q.GetAt(2)])

                # if q.w < 0:
                #     print(f"NEGATIVE QUATERNION for {skeleton_node.GetName()} in {fbx_file_path.split('/')[-1]} at time {key_time}, {q}")

                if "*" in key_time:
                    # Keys whose time is marked with "*" are not used in the animation.
                    # They are probably used to improve interpolation quality in between keyframes.
                    pass
                else:
                    key_time = float(key_time)
                    if key_time > duration:
                        duration = key_time

                    rotation_keys.append(Key(key_time, q))

        for key in translation_keys:
            key.time /= duration
        for key in rotation_keys:
            key.time /= duration

        translation_curve = PositionCurve(translation_keys)
        rotation_curve = QuaternionCurve(rotation_keys)
        return translation_curve, rotation_curve, duration

if __name__ == "__main__":
    fbx = FbxLoader(Path("C:\dev\MotionMachine\skanym\src\skanym\examples\input\walk.fbx"))
    skeleton = fbx.load_skeleton()
    for joint in skeleton.as_joint_list()[0:3]:
        print(type(joint.local_bind_transform.position))

    animation = fbx.load_animation()
    for curve in animation.position_curves[0:3]:
        for key in curve.curve.keys[0:3]:
            print(type(key.value))