import random

class RandUtils():
    def __init__(self):
        pass
    def rand_prompt(self):
        '''Takes a Prompt file and genertes one with random artists
        returns a dictionary with the selected artist and medium as such;

        {artist: <selection>, medium : <selection>}
        '''
        artists_list = []
        medium_list = []
        with open('./artists.txt', 'r') as afile:
            for line in afile:
                artists_list.append()
        with open('./medium.txt', 'r') as mfile:
            for line in mfile:
                medium_list.append(line)
        artists_selection = random.choice(artists_list)
        med_selection = random.choice(medium_list)
        return {
            'artist' : artists_selection,
            'medium' : med_selection
        }




