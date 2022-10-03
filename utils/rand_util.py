import random
import os

class RandUtils():
    def __init__(self):
        self.__location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
    def rand_prompt(self):
        '''Takes a Prompt file and genertes one with random artists
        returns a dictionary with the selected artist and medium as such;

        {artist: <selection>, medium : <selection>}
        '''
        artists_list = []
        medium_list = []
        with open(f"{self.__location__}/artists.txt", 'r') as afile:
            for line in afile:
                line.rstrip("\n")
                artists_list.append(line)
        with open(f"{self.__location__}/medium.txt", 'r') as mfile:
            for line in mfile:
                line.rstrip("\n")
                medium_list.append(line)
        artists_selection = random.choice(artists_list)
        med_selection = random.choice(medium_list)
        return {
            'artist' : artists_selection,
            'medium' : med_selection
        }




