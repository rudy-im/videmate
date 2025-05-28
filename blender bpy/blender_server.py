import bpy
import socket
import threading

def handle_client(conn):
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            cmd = data.decode("utf-8")
            try:
                exec(cmd)
            except Exception as e:
                print(f"Error executing command: {e}")

def start_server(host='127.0.0.1', port=9999):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"Blender listening on {host}:{port}")
    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn,), daemon=True).start()

# server in background
threading.Thread(target=start_server, daemon=True).start()
