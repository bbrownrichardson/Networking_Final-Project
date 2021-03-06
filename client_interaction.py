"""
Brianna Brown Richardson, Sarah Padrutt
Dr. Visa
CS330 Computer Networking and Communications

Client_Interaction Module
Hangman Game
"""

from socket import *
import sys
import atexit

serverName = None #'140.103.35.132'  # put IP address
serverPort = 18000
clientSocket = socket(AF_INET, SOCK_DGRAM)


@atexit.register
def when_exit():
    print('Client closed')
    clientSocket.close()


class Client:
    def __init__(self):
        serverName = input(r'ENTER SERVER IP Address: ')

        print('\n\n'
              '______________________________________________\n\n'
              '              HANGMAN GAME                      \n'
              '______________________________________________'
              '\n\n'
              'Instructions: User must enter ONE character \n'
              'at a time to make guesses towards the given \n'
              'word. All hangman words will only contain \n'
              'letters in the alphabet, a - z. If user \n'
              'expresses desire to exit game at any point,\n'
              'the user MUST enter the phrase [quit] and the\n'
              'game will exit.\n\n'
              'CREATORS: BRIANNA AND SARAH\n'
  
              'TRY NOT TO LEAVE THE HOMIEEE HANGING LIKE THIS:')

        print(r""" 
                    ____
                   |    |
                   |    o
                   |   /|\
                   |    |
                   |   / \
                  _|_
                 |   |______
                 |          |
                 |__________|""" + \
            """\n\n\nSHOUTOUT TO DR.VISA!!\n\n\n""")

        while True:
            mssg = input('------------------------------\n'
                         'Enter a character to guess: ').lower().strip()

            if mssg == 'quit': # quit game
                clientSocket.sendto(mssg.encode('utf-8'),
                                    (serverName, serverPort))
                print("""\n\n\nDUECES\n\n
░░░░░░░░░░░░▄▀▀█▄░░░░░▄▀▀▄░░░░░░
░░░░░░░░░░░░█░░░█░░░░░█░░█░░░░░░
░░░░░░░░░░░░▀▄░░█░░░░█░░░█░░░░░░
░░░░░░░░░░░░░█░░█░░░░█░░░█░░░░░░
░░░░░░░░░░░░░█░░░▀▄▄█░░░█▀░░░░░░
░░░░░░░░░░░░░▀█▄░░░░░░░▄█░░░░░░░
░░░░░░░░░░▄▄▄▄████▄▄▄░░█░░░░░░░░
░░░░░░░░░░█░░█░░▀▄░░▀█▄█░░░░░░░░
░░░░░░░▄▄▄█▄░░█▄░░█░░▀███░░░░░░░
░░░░░░░█░░██░░░█░░█░░░▀██░░░░░░░
░░░░░░░██░░▀█░░░█▄▀░░░░▀█░░░░░░░
░░░░░░░███░░██▄▄▀░░░░░░▄█░░░░░░░
░░░░░░░█▄░▀▀▀░░░░░░░░░▄██░░░░░░░
░░░░░░░░█▄░░░░░░░░░░░░█▀░░░░░░░░
░░░░░░░░▀▀▄▄░░░░░░░░▄█░░░░░░░░░░
░░░░░░░░░░██░░░░░░░░██░░░░░░░░░░
                      """)
                sys.exit()

            elif len(mssg) == 1: #ensure one character is being sent at a time
                clientSocket.sendto(mssg.encode('utf-8'),
                                            (serverName, serverPort))

                # Set up a new connection from the client
                modified_messg, server = clientSocket.recvfrom(2048)

                # if client recieves "LOSS", user has lost the game
                if modified_messg.decode('UTF-8') == 'LOSS':
                    print(r""" 
                    ____
                   |    |
                   |    o
                   |   /|\
                   |    |
                   |   / \
                  _|_
                 |   |______
                 |          |
                 |__________|""")

                    print('\n\nALL OUT OF GUESSES! YOU LOSE!!')
                    print("""\n\n
░▄█▀░░░░░░░░▄▄▄▄▄▄░░░░░░▀▀▄░░░░░
██░░░░░░░░░▄▄▄▄▄▄▄░░░░░░░▄▄██▄░░
▀░░░░░░░░░░░░░░░░▄▄▄██████▀█▀█▄░
░░░▀▀████████████████░░███░█░░█▄
░░░░█░░▀███░░██░▀█░░██▄▄▄▄▄▀░░██
░░░░▀█▄▄░░░▄▄█░░░░█▄░░░▀▀░░░░░░█
░░░░░░░▀▀▀▀▀░░░░░▄▄█░░░░░░░░░░░█
░░░░░░░░░░░░░░░░░░░░░░░░░░█▀░░░█
░░░░░█▄░░░░░░▄██▀▀▀██▄░░░█░░░░░█
░░░░░░░█░░░░▀▀░░░░░░░░░░░░▀▄░░░█
░░░░░░░▀█░░░░░░░█▀░░░░░░░░░░░░░█
█▄░░░░░▀░░░░░░░░░░░░░░░░░░░░░░██
░▀▄░░░░░░░░░░░░░░░░░░░░░░░░░░░█░
░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░▄█░░
░░░░▀▄▄▄░░░░░░░░░░░░░░░░░░░██▀░░
░░░░░░▀▀▀█▄▄▄▄░░░░░░░░▄▄▄▄█▀▀░░░
                    """)
                    sys.exit()

                # if client recieves "WIN", user has WIN the game
                elif modified_messg.decode('UTF-8') == 'WIN':
                    print('\nCONGRATS YOU GUESSED IT!!')
                    print("""\n\n\n
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░████░░░░░░░░░░████░░░░░░░░░░
░░██░░░░██░░░░░░██░░░░██░░░░░░░░
██████░░░░██░░██████░░░░██░░░░░░
████████░░██░░████████░░██░░░░░░
████████████░░████████████░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
████████████████████████████░░░░
██░░░░░░░░░░░░░░░░░░░░░░██░░░░░░
██████░░░░░░░░░░░░░░░░░░██░░░░░░
████████░░░░░░░░░░░░░░████░░░░░░
░░██████░░░░░░░░░░░░██░░░░░░░░░░
░░░░████████████████░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░""")
                    sys.exit()

                else:
                    print(modified_messg.decode('UTF-8'))

            else:
                print('please enter one character \n')


def main():
    Client()


if __name__ == '__main__':
    main()
