"""
Brianna Brown Richardson, Sarah Padrutt
Dr. Visa
CS330 Computer Networking and Communications

Server_Interaction Module
Hang Man Game
"""

from socket import *
import random

serverName = 'xxx.xxx.xxx.xxx'  # put IP address
serverPort = 10000

words_to_choose = ['fast', 'tiger', 'lounge', 'anxiety', 'notion', 'marathon',
                   'flood', 'load', 'cope', 'obscure', 'stress', 'silly',
                   'slippery', 'medieval', 'magazine', 'helmet', 'memory',
                   'pierce', 'old age', 'loot', 'scream', 'carrot', 'mile',
                   'sketch', 'systematic']

correct_selection = ' is a correct selection'

incorrect_selection = ' is not a correct selection'

current_standing = 'So far you have the letters '


class Server:
    def __init__(self):
        # Create a UDP server socket
        # (AF_INET is used for IPv4 protocols)
        # (SOCK_DGRAM is used for UDP)
        self.chosen_word = random.choice(words_to_choose)
        self.letters = list()
        self.selected_letters = list()

        for char in self.chosen_word:
            self.letters.append(char)
            self.selected_letters.append('_')

        serverSocket = socket(AF_INET, SOCK_DGRAM)

        # Bind the socket to server address and server port
        serverSocket.bind(("", serverPort))

        # Server should be up and running and listening to the incoming connections
        while True:
            print('Ready to serve...' + self.chosen_word)
            # Set up a new connection from the client
            character, clientAddress = serverSocket.recvfrom(2048)
            if character in self.letters:
                self.get_char_index(self.letters, character)
                # response = character.encode('UTF-8') + correct_selection
                # print(response)
                serverSocket.sendto(correct_selection.encode('UTF-8'), clientAddress)
                serverSocket.sendto(''.join(self.selected_letters) +
                                    correct_selection, clientAddress)

            # if len(self.letters) == 0:
            #     serverSocket.close()
            else:
                # response = character.encode('UTF-8') + incorrect_selection
                # print(response)
                serverSocket.sendto(correct_selection.encode('UTF-8'), clientAddress)

    def get_char_index(self, letter_list, character):
        for i in range(0, len(letter_list), 1):
            if letter_list[i] == character:
                self.selected_letters[i] = character
                self.letters.remove(self.letters[i])
            else:
                pass


def main():
    Server()

if __name__ == '__main__':
    main()
