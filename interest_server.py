
import socket
 
def calculate_interest(principal, rate, years):
    interest = (principal * rate * years) / 100
    return interest
 
def handle_client(client_socket):
    print("Client connected:", client_socket.getpeername())
 
    while True:
        data = client_socket.recv(1024).decode()
        if data == "exit":
            break
 
        try:
            principal, rate, years = map(float, data.split())
            interest = calculate_interest(principal, rate, years)
            client_socket.send(str(interest).encode())
        except ValueError:
            client_socket.send("Invalid input. Please enter principal, rate, and years.".encode())
 
    print("Client disconnected:", client_socket.getpeername())
    client_socket.close()
 
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 12345))
    server_socket.listen(5)
    print("Server is listening for incoming connections...")
 
    while True:
        client_socket, client_address = server_socket.accept()
        handle_client(client_socket)  # Corrected the function name
 
if __name__ == "__main__":
    main()
