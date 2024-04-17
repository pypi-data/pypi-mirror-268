import json
from PIL import Image as ImageLoader
from PIL.Image import Image
from io import BytesIO
import requests

version = '14.7.1'
language = 'en_US'

class DdragonRequest():

    def __init__(self, **kwargs):
        self._get_version()



    def _get_version(self):
        path = 'https://ddragon.leagueoflegends.com/api/versions.json'
        response = requests.get(path)
        if response.status_code == 200:
            json = response.json()
        else:
            raise Exception ('CANT FIND VERSION')

        self.version = json[0];


    def _get_data(self, **kwargs):
        get_type = kwargs.get('get_type', None)

        match get_type:
            case 'champion':
                champ = kwargs.get('champion', None)
                path = f'https://ddragon.leagueoflegends.com/cdn/{self.version}/data/{language}/champion/{champ}.json'
                
            
            case 'item':
                path = f'https://ddragon.leagueoflegends.com/cdn/{self.version}/data/{language}/item.json'
                            
            case _:
                raise Exception ('Invalid data type')

        response = requests.get(path) 
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception (f'Invalid response code: {response.status_code}')


    def _get_champion_image(self, **kwargs):
        get_type = kwargs.get('get_type', 'splash')
        num = kwargs.get('num', 0)
        champ = kwargs.get('champion', 'Aatrox')
        wants_url = kwargs.get('return_url', False)
        path = f'https://ddragon.leagueoflegends.com/cdn/img/champion/{get_type}/{champ}_{num}.jpg'
        if wants_url == True:
            return path
        else:
            response = requests.get(path)
            return ImageLoader.open(BytesIO(response.content))
        # return data
    

class RiotJson():

    def __init__(self, Dto):
        self.type = Dto.get('type', None)
        self.format = Dto.get('format', None)
        self.version = Dto.get('version', None)
        self.data = Dto.get('data', None)


    



        
