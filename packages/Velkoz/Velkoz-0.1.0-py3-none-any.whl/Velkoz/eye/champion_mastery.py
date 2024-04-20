
#useless?
class ChampionMastery():
    

    def __init__(self, kwargs):
        if kwargs != None:
            
            self.ChampionMasteryDto = kwargs
            self.chestGranted = kwargs.get('chestGranted' ,False)
            self.championId = kwargs.get('championId' ,None)
            self.lastPlayTime = kwargs.get('lastPlayTime', 0)
            self.championLevel = kwargs.get('championLevel', 0)
            self.championPoints = kwargs.get('championPoints', 0)
            self.tokensEarned = kwargs.get('tokensEarned', None)
        else:
            self.ChampionMasteryDto = kwargs
            self.chestGranted = False
            self.championId = None
            self.lastPlayTime = 0
            self.championLevel = 0
            self.championPoints = 0
            self.tokensEarned = 0
    def get(self, parameter):
        got = self.ChampionMasteryDto.get(parameter, None)

