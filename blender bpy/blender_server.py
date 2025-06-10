import bpy
import socket
import threading
import queue

command_queue = queue.Queue()
server = None


def handle_client(conn):
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            cmd = data.decode("utf-8")
            if cmd == "shutdown":
                stop_server()
                return
            command_queue.put(cmd)


def start_server(host='127.0.0.1', port=9999):
    global server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"Blender listening on {host}:{port}")
    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn,), daemon=True).start()


def stop_server():
    global server
    if server:
        try:
            server.close()
            print("Server socket closed.")
        except Exception as e:
            print(f"Error closing server: {e}")
        server = None


# server in background
threading.Thread(target=start_server, daemon=True).start()




def process_commands():
    while not command_queue.empty():
        cmd = command_queue.get()
        try:
            exec(cmd, {'bpy': bpy, '__builtins__': __builtins__})
            print(f"Executed: {command}")
        except Exception as e:
            print(f"Error executing command: {e}")
    return 0.5 # seconds

bpy.app.timers.register(process_commands)








