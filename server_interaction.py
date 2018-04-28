"""
Brianna Brown Richardson, Sarah Padrutt
Dr. Visa
CS330 Computer Networking and Communications

Server_Interaction Module
Hang Man Game
"""

from socket import *
import sys
import random
import atexit

serverPort = 18000
serverSocket = socket(AF_INET, SOCK_DGRAM)

words_to_choose = ['queue', 'protocols', 'datagram', 'boomboomboom', 'sommers',
                   'socket','flood', 'networking', 'bandwidth', 'frames',
                   'segment', 'handshake', 'acknowledgment', 'persistent',
                   'bynres', 'delay', 'memory','connectionless', 'congestion',
                   'dijkstra','pipeline', 'multiplexing', 'visa',
                   'fox', 'packet']

correct_selection = ' is a correct selection'
incorrect_selection = ' is not a correct selection'
current_standing = 'So far you have the letters '


@atexit.register
def when_exit():
    print('Server closed')
    serverSocket.close()


class Server:
    def __init__(self):
        # Create a UDP server socket
        # (AF_INET is used for IPv4 protocols)
        # (SOCK_DGRAM is used for UDP)
        self.chosen_word = random.choice(words_to_choose)
        self.letters = list()
        self.selected_letters = list()
        self.guesses = 0

        for char in self.chosen_word:
            self.letters.append(char)
            self.selected_letters.append('_')

        # Bind the socket to server address and server port
        serverSocket.bind(("", serverPort))

        print(self.letters)
        print('Ready to serve...' + self.chosen_word)

        while True:
            # Set up a new connection from the client
            character, client_address = serverSocket.recvfrom(2048)

            if character.decode('UTF-8') in self.letters:
                self.get_char_index(self.letters, character.decode('UTF-8'))

                # if there are no blanks in selected_letters user has
                # correctly guess all letter and win response will be sent
                # to client rendering a win and exit
                if '_' not in self.selected_letters:
                    response = 'WIN'
                    serverSocket.sendto(response.encode('UTF-8'),
                                        client_address)
                    sys.exit()

                else:
                    response = character.decode('UTF-8') + correct_selection + \
                    '\n\n' + ' '.join(self.selected_letters) + '\n'
                    serverSocket.sendto(response.encode('UTF-8'), client_address)

            elif character.decode('UTF-8') == 'quit':
                sys.exit()

            else:
                self.guesses += 1

                # if user runs out of guess a LOSS response will be sent to
                # client rendering a loss and exit
                if self.guesses == 5:
                    response = 'LOSS'
                    serverSocket.sendto(response.encode('UTF-8'),
                                        client_address)
                    sys.exit()

                else:
                    response = '\n' + character.decode('UTF-8') + \
                               incorrect_selection + '\n\n' + \
                               'You currently have ' + str(5 - self.guesses)\
                               + ' guesses left\n\n' + \
                               ' '.join(self.selected_letters) + '\n'

                    serverSocket.sendto(response.encode('UTF-8'),
                                        client_address)

    def get_char_index(self, letter_list, character):
        """
        function to replace blanks in selected_letters list with selected
        letters and replace selected letters with blanks in letter_list
        :param letter_list: list of letters of word being guessed
        :param character: selected character
        :return: None
        """
        for i in range(0, len(letter_list), 1):
            if letter_list[i] == character:
                self.selected_letters[i] = character
                self.letters[i] = '_'
            else:
                pass


def main():
    Server()


if __name__ == '__main__':
    main()
