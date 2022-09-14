from decouple import config
from botometer import Botometer

class Bot:
    def __init__(self,account):
        self.account = account
        self.result = {}
        self.score = {}
        self.is_bot = False

    #Get the account information of the user
    def get_account(self):
        rapidapi_key = config('rapidapi_key',default='')
        twitter_app_auth = {
                    'consumer_key': config('consumer_key',default=""),
                    'consumer_secret': config('consumer_secret',default=""),
                    'access_token': config('access_token',default=""),
                    'access_token_secret': config('access_token_secret',default="")
                    }

        botometer = Botometer(wait_on_ratelimit=True,
                                rapidapi_key=rapidapi_key,
                                **twitter_app_auth)

        self.result = botometer.check_account(self.account)
        return(self.result)
    """
    def check_accounts(self):
        rapidapi_key = config('rapidapi_key',default='')
        twitter_app_auth = {
                    'consumer_key': config('consumer_key',default=""),
                    'consumer_secret': config('consumer_secret',default=""),
                    'access_token': config('access_token',default=""),
                    'access_token_secret': config('access_token_secret',default="")
                    }

        botometer = Botometer(wait_on_ratelimit=True,
                                rapidapi_key=rapidapi_key,
                                **twitter_app_auth)

        for screen_name, result in bom.check_accounts_in(self.accounts):
            self.results[screen_name] = botometer.check_account(screen_name)
    """

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