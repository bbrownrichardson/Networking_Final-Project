"""
Brianna Brown Richardson, Sarah Padrutt
Dr. Visa
CS330 Computer Networking and Communications
Server_Interaction Module
Hang Man Game
"""

from socket import *
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

hang_man=[' 0 \n','-', '|', '-\n', '/', '|']



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

        #print(self.letters)
        print('Ready to serve...' + self.chosen_word)
    # Server should be up and running and listening to the incoming connections
        my_man=''
        while True:
            # Set up a new connection from the client
            character, client_address = serverSocket.recvfrom(2048)

            if character.decode('UTF-8') in self.letters:
                self.get_char_index(self.letters, character.decode('UTF-8'))

                response = character.decode('UTF-8') + correct_selection + \
                '\n\n' + ' '.join(self.selected_letters)
                serverSocket.sendto(response.encode('UTF-8'), client_address)

            else:
                # this condition is currently left broken as a quick way to
                # exit the program. The solution is currently in mind
                self.guesses += 1

                if self.guesses == 7:
                    pass
                else:
                    my_man = my_man + hang_man[self.guesses -1]
                    response = character + incorrect_selection + '\n\n' + \
                               'You Currently Have ' + str(7 - self.guesses)\
                               + 'Left' +'\n\n' + my_man
                    serverSocket.sendto(response.encode('UTF-8'),
                                        client_address)

    def get_char_index(self, letter_list, character):
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