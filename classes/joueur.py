import pygame
import socket

class Joueur:
    def __init__(self, nom: str, score: int, server : bool):
        self.nom = nom
        self.score = score
        self.server = server

    def augmenter_score(self, points: int):
        self.score += points

    def reset_score(self):
        self.score = 0

    def est_server(self):
        return self.server

    def set_join(self):
        if self.est_server():
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(("0.0.0.0", 5555))  # écoute sur le port 5555
            server.listen(1)

            print("En attente d'un joueur...")
            conn, addr = server.accept()
            print("Connecté à", addr)

            while True:
                data = conn.recv(1024).decode()
                if not data:
                    break
                print("Reçu:", data)
                conn.send("OK".encode())
        else:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            client.connect(("IP_DU_SERVEUR", 5555))

            while True:
                msg = input("Message: ")
                client.send(msg.encode())

                response = client.recv(1024).decode()
                print("Serveur:", response)     
