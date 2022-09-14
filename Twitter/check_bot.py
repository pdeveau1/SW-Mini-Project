from decouple import config
from botometer import Botometer

class Bot:
    def __init__(self,account):
        self.account = account
        self.result = {}
        self.score = {}

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
    def get_score(self):
        self.score = self.result['cap']
        return(self.score)