import socket

HOST = '127.0.0.1'
PORT = 9999

cmd = """
import bpy
obj = bpy.data.objects["Armature"]
bone = obj.pose.bones["Bone"]
bone.location.x += 1.0
"""

with socket.create_connection((HOST, PORT)) as sock:
    sock.sendall(cmd.encode("utf-8"))
