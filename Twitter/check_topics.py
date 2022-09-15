import requests
import os
import json
from decouple import config
from user import User

class Topics(User):
    def __init__(self,account):
        self.timeline = None
        User.__init__(self, account)

        self.get_account()
        self.get_id()

    def create_url(self):
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
        