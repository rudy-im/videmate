import socket

HOST = '127.0.0.1'
PORT = 9999

cmd = ''

with open('./blender bpy/blender_rig_motion.py') as script:
    cmd = script.read()
    print(cmd)
    

with socket.create_connection((HOST, PORT)) as sock:
    sock.sendall(cmd.encode("utf-8"))

