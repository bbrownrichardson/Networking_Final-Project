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
serverPort = 18000
clientSocket = socket(AF_INET, SOCK_DGRAM)


@atexit.register
def when_exit():
    print('Client closed')
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

                print(modified_messg.decode('UTF-8'))

            else:
                print('please enter one character \n')
                clientSocket.close()


def main():
    Client()


if __name__ == '__main__':
    main()
