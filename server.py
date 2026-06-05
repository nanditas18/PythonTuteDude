import socket
import threading

HOST = '127.0.0.1'  
PORT = 55555        

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

print(f"Server is running and listening on {HOST}:{PORT}...")

def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                raise Exception()
            broadcast(message)
        except:
            if client in clients:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                broadcast(f"⚡ {nickname} left the chat.".encode('utf-8'))
                nicknames.remove(nickname)
                print(f"[-] Connection closed for {nickname}")
            break

def receive_connections():
    while True:
        client, address = server.accept()
        print(f"[+] Connected with structural address: {str(address)}")

        client.send("NICKNAME_REQUEST".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        
        nicknames.append(nickname)
        clients.append(client)

        print(f"User identity registered as: {nickname}")
        broadcast(f"🎉 {nickname} joined the chatroom!".encode('utf-8'))
        client.send("Connected successfully to the server.".encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    receive_connections()