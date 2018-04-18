"""
Brianna Brown Richardson, Sarah Padrutt
Dr. Visa
CS330 Computer Networking and Communications

Client_Interaction Module
Hangman Game
"""

from socket import *

serverName = 'localhost'  # put IP address
serverPort = 10000


class Client:
    def __init__(self):
        clientSocket = socket(AF_INET, SOCK_DGRAM)
        mssg = input('Enter a character to guess: ').lower().strip()

        if len(mssg) == 1:
            clientSocket.sendto(mssg.encode('utf-8'), (serverName, serverPort))

            # Set up a new connection from the client
            modified_messg, server = clientSocket.recvfrom(2048)

            print(modified_messg)
            clientSocket.close()

        # if modified_messg == 'Winner':
        #     pass
        else:
            print('please enter one character \n')


def main():
    Client()


if __name__ == '__main__':
    main()
