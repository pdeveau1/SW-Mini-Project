import requests
import os
import json
from decouple import config
from botometer import Botometer

# Imports the Google Cloud client library
from google.cloud import language_v1

class User:
    def __init__(self,account):
        self.account = account
        self.id = None
        self.result = None
        self.score = None
        self.is_bot = False
        self.timeline = None
        self.sentiments = None

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

    def get_id(self):
        if(self.result is None):
            self.get_account()
        self.id = self.result['user']['user_data']['id_str']
        return self.id
    
    #Get the english and universal bot score of the user
    def get_score(self):
        if(self.result is None):
            self.get_account()
        self.score = self.result['cap']
        return(self.score)
    
    #Check if the bot is a user based off of the majority language score
    def get_bot(self):
        if(self.result is None):
            self.get_account()
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

    def create_url(self):
        if(self.id is None):
            self.get_id()
        return "https://api.twitter.com/2/users/{}/tweets".format(self.id)


    def get_params(self):
        # Tweet fields are adjustable.
        # Options include:
        # attachments, author_id, context_annotations,
        # conversation_id, created_at, entities, geo, id,
        # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
        # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
        # source, text, and withheld
        return {"tweet.fields": "created_at"}


    def bearer_oauth(self,r):
        """
        Method required by bearer token authentication.
        """

        r.headers["Authorization"] = f"Bearer {config('bearer',default='')}"
        r.headers["User-Agent"] = "v2UserTweetsPython"
        return r


    def connect_to_endpoint(self,url, params):
        response = requests.request("GET", url, auth=self.bearer_oauth, params=params)
        print(response.status_code)
        if response.status_code != 200:
            raise Exception(
                "Request returned an error: {} {}".format(
                    response.status_code, response.text
                )
            )
        return response.json()


    def get_timeline(self):
        url = self.create_url()
        params = self.get_params()
        json_response = self.connect_to_endpoint(url, params)
        self.timeline = json_response
        return self.timeline
        #print(json.dumps(json_response, indent=4, sort_keys=True))

    def get_sentiment(self):
        if(self.timeline is None):
            self.get_timeline()
        # Instantiates a client
        client = language_v1.LanguageServiceClient()

        # The text to analyze
        texts = []
        for item in self.timeline['data']:
            texts.append(item['text'])
        
        sentiments = []
        for text in texts:
            document = language_v1.Document(
                content=text, type_=language_v1.Document.Type.PLAIN_TEXT
            )
            # Detects the sentiment of the text
            sentiment = client.analyze_sentiment(
                request={"document": document}
            ).document_sentiment

            sentiments.append({'text': text, 'sentiment': {'score':sentiment.score, 'magnitude':sentiment.magnitude}})

        self.sentiments = sentiments
        return self.sentiments
        #print("Text: {}".format(text))
        #print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))
        
