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
        self.sentiment = None
        self.topics = None

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
        if(self.score is None):
            self.get_score()
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
        
    def calc_sentiment(self):
        if (self.sentiments is None):
            self.get_sentiment()

        score = 0
        for items in self.sentiments:
            #Use magnitude for weight of sentiment of each tweet
            score += items['sentiment']['score'] * items['sentiment']['magnitude']
        
        #score ranges from -inf to +inf once use magnitude as weight
        #negative score is a negative sentiment and positive score is positive sentiment
        if(score > 0):
            self.sentiment = 'Positive'
        elif(score < 0):
            self.sentiment = 'Negative'
        else:
            self.sentiment = 'Neutral'
        
        return self.sentiment


    def sample_analyze_entities(self):
        """
        Analyzing Entities in a String

        Args:
        text_content The text content to analyze
        """

        if(self.timeline is None):
            self.get_timeline()

        client = language_v1.LanguageServiceClient()

        # text_content = 'California is a state.'

        # Available types: PLAIN_TEXT, HTML
        type_ = language_v1.Document.Type.PLAIN_TEXT

        for item in self.timeline['data']:
            print(u'Text: {}'.format(item['text']))
            # Optional. If not specified, the language is automatically detected.
            # For list of supported languages:
            # https://cloud.google.com/natural-language/docs/languages
            document = {"content": item['text'], "type_": type_}

            # Available values: NONE, UTF8, UTF16, UTF32
            encoding_type = language_v1.EncodingType.UTF8

            response = client.analyze_entities(request = {'document': document, 'encoding_type': encoding_type})

            # Loop through entitites returned from the API
            for entity in response.entities:
                print(u"Representative name for the entity: {}".format(entity.name))

                # Get entity type, e.g. PERSON, LOCATION, ADDRESS, NUMBER, et al
                print(u"Entity type: {}".format(language_v1.Entity.Type(entity.type_).name))

                # Get the salience score associated with the entity in the [0, 1.0] range
                print(u"Salience score: {}".format(entity.salience))

                # Loop over the metadata associated with entity. For many known entities,
                # the metadata is a Wikipedia URL (wikipedia_url) and Knowledge Graph MID (mid).
                # Some entity types may have additional metadata, e.g. ADDRESS entities
                # may have metadata for the address street_name, postal_code, et al.
                for metadata_name, metadata_value in entity.metadata.items():
                    print(u"{}: {}".format(metadata_name, metadata_value))

                # Loop over the mentions of this entity in the input document.
                # The API currently supports proper noun mentions.
                for mention in entity.mentions:
                    print(u"Mention text: {}".format(mention.text.content))

                    # Get the mention type, e.g. PROPER for proper noun
                    print(
                        u"Mention type: {}".format(language_v1.EntityMention.Type(mention.type_).name)
                    )
            print('\n\n')
        # Get the language of the text, which will be the same as
        # the language specified in the request or, if not specified,
        # the automatically-detected language.
        print(u"Language of the text: {}".format(response.language))


    def calc_categories(self):
        if(self.timeline is None):
            self.get_timeline()
        """
        #Classifying Content in a String

        #Args:
        #text_content The text content to analyze. Must include at least 20 words.
        """

        topics = []

        client = language_v1.LanguageServiceClient()

        # text_content = 'That actor on TV makes movies in Hollywood and also stars in a variety of popular new TV shows.'

        # Available types: PLAIN_TEXT, HTML
        type_ = language_v1.Document.Type.PLAIN_TEXT

        # Optional. If not specified, the language is automatically detected.
        # For list of supported languages:
        # https://cloud.google.com/natural-language/docs/languages
        language = "en"
        for item in self.timeline['data']:
            tweet = item['text']
            #check that tweet has more then 20 tokens because that is how many classify text needs
            if(len(tweet.split()) > 20):
                document = {"content": tweet, "type_": type_, "language": language}
                response = client.classify_text(request = {'document': document})
                if(response):
                    # Loop through classified categories returned from the API
                    for category in response.categories:
                        if category.name not in topics:
                            topics.append(category.name)
        self.topics = topics
        return self.topics

