import socket
import json

HOST = "0.0.0.0"
PORT = 8080
notes = {}
next_id = 1

def handle_request(data):
    global next_id
    try:
        request = json.loads(data)
        command = request.get("command")

        if command == "CREATE":
            note = request.get("note")
            if not note:
                return {"status": "error", "message": "Nota no proporcionada"}
            notes[next_id] = note
            response = {"status": "success", "id": next_id}
            next_id += 1
            return response

        elif command == "READ":
            return {"status": "success", "data": notes}

        elif command == "DELETE":
            note_id = request.get("id")
            if note_id in notes:
                del notes[note_id]
                return {"status": "success"}
            else:
                return {"status": "error", "message": "Nota no encontrada"}

        else:
            return {"status": "error", "message": "Comando desconocido"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# Iniciar servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Servidor escuchando en {HOST}:{PORT}")
    while True:
        client_socket, addr = server_socket.accept()
        with client_socket:
            print(f"Conexión establecida con {addr}")
            data = client_socket.recv(1024).decode("utf-8")
            if not data:
                continue
            response = handle_request(data)
            client_socket.send(json.dumps(response).encode("utf-8"))
