import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 12345))

    print("Connected to server. Type 'exit' to quit.")

    while True:
        data = input("Enter principal, rate, and years (e.g., 1000 5 2): ")
        client_socket.send(data.encode())

        if data.lower() == "exit":
            break

        interest = client_socket.recv(1024).decode()
        print("Interest calculated by server: " + interest)

    client_socket.close()

if __name__ == "__main__":
    main()
