import socket

HOST = '127.0.0.1'
PORT = 9999


'''
cmd = ''

with open('./blender bpy/blender_rig_motion.py') as script:
    cmd = script.read()
    print(cmd)
    

with socket.create_connection((HOST, PORT)) as sock:
    sock.sendall(cmd.encode("utf-8"))
'''



class BlenderRig:

    def __init__(self):
        self.s = socket.create_connection((HOST, PORT))

        init_script = '''
            import bpy
            import math

            rig = bpy.data.objects['metarig']
            bpy.context.view_layer.objects.active = rig
            bpy.ops.object.mode_set(mode='POSE')
        '''
        self.execute(init_script)

    def close(self):
        self.s.close()

    def execute(self, script):
        self.sendall(script.encode("utf-8"))

    def rotate(self, bone, xAngle, yAngle, zAngle):
        script = '''
            bone = rig.pose.bones[\'''' + bone + '''\']
            bone.rotation_mode = 'XYZ'
            bone.rotation_euler = (math.radians(''' + xAngle + '''),
                            math.radians(''' + yAngle + '''),
                            math.radians(''' + zAngle + '''))
        '''
        self.execute(script)







        
