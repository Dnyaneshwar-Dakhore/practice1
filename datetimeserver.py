import threading
import socket
import datetime
 
def handle_client(client_socket):
    print("Client connected:", client_socket.getpeername())
 
    while True:
        operation = client_socket.recv(1024).decode()
        if operation == "exit":
            break
 
        if operation == "date":
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            client_socket.send(current_date.encode())
        elif operation == "time":
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            client_socket.send(current_time.encode())
        elif operation == "year":
            current_year = datetime.datetime.now().year
            client_socket.send(str(current_year).encode())
 
    print("Client disconnected:", client_socket.getpeername())
    client_socket.close()
 
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 12345))
    server_socket.listen(5)
    print("Server is listening for incoming connections...")
 
    while True:
        client_socket, client_address = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()
 
if __name__ == "__main__":
    main()
