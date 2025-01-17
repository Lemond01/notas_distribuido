import socket
import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Configuración del cliente
HOST = "servidor"
PORT = 8080

# Función para enviar comandos al servidor
def send_request(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        client_socket.send(json.dumps(command).encode("utf-8"))
        response = client_socket.recv(1024).decode("utf-8")
        return json.loads(response)

# Función para guardar las notas en un archivo .txt
def guardar_notas_txt(notas):
    with open("notas.txt", "w") as file:
        for nota in notas:
            file.write(nota + "\n")
    print("Notas guardadas en notas.txt")

# Función para guardar las notas en un archivo PDF
def guardar_notas_pdf(notas):
    c = canvas.Canvas("notas.pdf", pagesize=letter)
    width, height = letter
    y_position = height - 40  # Espacio inicial en la página

    c.setFont("Helvetica", 12)
    
    for nota in notas:
        c.drawString(40, y_position, nota)
        y_position -= 20  # Mover hacia abajo para la siguiente nota
        if y_position < 40:
            c.showPage()  # Crear una nueva página si se llena
            c.setFont("Helvetica", 12)
            y_position = height - 40

    c.save()
    print("Notas guardadas en notas.pdf")

# Interfaz del cliente
notas = []  # Lista de notas en el cliente

while True:
    print("\nOpciones:")
    print("------------------")
    print("1. Crear nota")
    print("2. Leer notas")
    print("3. Eliminar nota")
    print(".")
    print(".")
    print("4. Guardar notas en \033[92m.txt\033[0m")
    print("5. Guardar notas en \033[92mPDF\033[0m")
    print("------------------")
    print("\033[91m6. Salir\033[0m")

    option = input("Selecciona una opción: ")

    if option == "1":
        note = input("Escribe la nota: ")
        response = send_request({"command": "CREATE", "note": note})
        print(response)
        notas.append(note)  # Agregar la nueva nota a la lista local

    elif option == "2":
        response = send_request({"command": "READ"})
        print(response)

    elif option == "3":
        note_id = int(input("Escribe el ID de la nota a eliminar: "))
        response = send_request({"command": "DELETE", "id": note_id})
        print(response)

    elif option == "4":
        guardar_notas_txt(notas)

    elif option == "5":
        guardar_notas_pdf(notas)

    elif option == "6":
        break

    else:
        print("Opción inválida.")

