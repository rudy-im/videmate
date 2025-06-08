import bpy
import math

rig = bpy.data.objects['metarig']
bpy.context.view_layer.objects.active = rig
bpy.ops.object.mode_set(mode='POSE')

bone = rig.pose.bones['spine.006']
bone.rotation_mode = 'XYZ'
bone.rotation_euler = (0.0, math.radians(60), 0.0)

#bone.keyframe_insert(data_path="rotation_euler", frame=1)
