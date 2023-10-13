
import socket
 
def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 12345))
 
    print("Connected to server. Type 'exit' to quit.")
 
    while True:
        operation = input("Enter operation (date/time/year): ")
        if operation == "exit":
            client_socket.send("exit".encode())
            break
 
        client_socket.send(operation.encode())
        result = client_socket.recv(1024).decode()
        print("Result: " + result)
 
    client_socket.close()
 
if __name__ == "__main__":
    main()
 
