import socket
import threading
import tkinter as tk
from tkinter import simpledialog, scrolledtext

class ChatClient:
    def __init__(self, host, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))

        root_login = tk.Tk()
        root_login.withdraw()
        self.nickname = simpledialog.askstring("Nickname Selection", "Please choose a chat name:", parent=root_login)
        
        if not self.nickname:
            self.nickname = "Anonymous"
        root_login.destroy()

        self.win = tk.Tk()
        self.win.title(f"Chatroom - Logged in as: {self.nickname}")
        self.win.configure(bg="#2c3e50")
        self.win.geometry("450x600")

        self.chat_label = tk.Label(self.win, text="Global Live Feed", bg="#2c3e50", fg="white", font=("Helvetica", 12, "bold"))
        self.chat_label.pack(padx=10, pady=5)

        self.text_area = scrolledtext.ScrolledText(self.win, wrap=tk.WORD, font=("Helvetica", 10), bg="#ecf0f1")
        self.text_area.pack(padx=20, pady=5, fill=tk.BOTH, expand=True)
        self.text_area.config(state='disabled') 

        self.msg_label = tk.Label(self.win, text="Type your message below:", bg="#2c3e50", fg="white", font=("Helvetica", 10))
        self.msg_label.pack(padx=10, pady=5)

        self.input_area = tk.Entry(self.win, font=("Helvetica", 11), bg="#ffffff")
        self.input_area.pack(padx=20, pady=5, fill=tk.X)
        self.input_area.bind("<Return>", self.send_message) 

        self.send_button = tk.Button(self.win, text="Send Message", command=self.send_message, bg="#2ecc71", fg="white", font=("Helvetica", 10, "bold"))
        self.send_button.pack(padx=20, pady=10)

        self.running = True
        gui_thread = threading.Thread(target=self.receive_messages)
        gui_thread.start()

        self.win.protocol("WM_DELETE_WINDOW", self.stop_app)
        self.win.mainloop()

    def send_message(self, event=None):
        message = self.input_area.get().strip()
        if message:
            formatted_message = f"{self.nickname}: {message}"
            self.client_socket.send(formatted_message.encode('utf-8'))
            self.input_area.delete(0, tk.END) 

    def receive_messages(self):
        while self.running:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message == 'NICKNAME_REQUEST':
                    self.client_socket.send(self.nickname.encode('utf-8'))
                else:
                    self.text_area.config(state='normal')
                    self.text_area.insert(tk.END, message + "\n")
                    self.text_area.yview(tk.END) 
                    self.text_area.config(state='disabled')
            except:
                print("An error occurred or connection closed.")
                self.client_socket.close()
                break

    def stop_app(self):
        self.running = False
        self.win.destroy()
        self.client_socket.close()

if __name__ == "__main__":
    ChatClient('127.0.0.1', 55555)