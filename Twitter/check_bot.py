from decouple import config
from botometer import Botometer
from user import User

class Bot(User):
    def __init__(self, account):
        self.score = {}
        self.is_bot = False
        
        User.__init__(self, account)

        self.get_account()

    #Get the english and universal bot score of the user
    def get_score(self):
        self.score = self.result['cap']
        return(self.score)
    
    #Check if the bot is a user based off of the majority language score
    def get_bot(self):
        #get majority language to determine what score to use for bot check
        if self.result['user']['majority_lang'] == 'en':
            score = self.score['english']
        else:
            score = self.score['universal']

        #Assume score of more than 0.6 is an indication that an account is a bot
        if score > 0.6:
            self.is_bot = True
        else:
            self.is_bot = False

        return self.is_bot