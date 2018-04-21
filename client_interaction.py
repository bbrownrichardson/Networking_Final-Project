"""
Brianna Brown Richardson, Sarah Padrutt
Dr. Visa
CS330 Computer Networking and Communications

Client_Interaction Module
Hangman Game
"""

from socket import *
import atexit

serverName = 'localhost'  # put IP address
serverPort = 28000
clientSocket = socket(AF_INET, SOCK_DGRAM)


def when_exit():
    clientSocket.close()

class Client:
    def __init__(self):
        # mssg = input('Enter a character to guess: ').lower().strip()

        while True:
            mssg = input('Enter a character to guess: ').lower().strip()

            if mssg == 'quit':
               clientSocket.close()

            elif len(mssg) == 1:
                clientSocket.sendto(mssg.encode('utf-8'),
                                            (serverName, serverPort))

                # Set up a new connection from the client
                modified_messg, server = clientSocket.recvfrom(2048)

                print(modified_messg)

            # if modified_messg == 'Winner':
            #     pass
            else:
                print('please enter one character \n')
                clientSocket.close()


def main():
    atexit.register(clientSocket.close())
    Client()


if __name__ == '__main__':
    main()
