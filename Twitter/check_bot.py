from decouple import config

rapidapi_key = config('rapidapi_key',default='')
twitter_app_auth = {
            'consumer_key': config('consumer_key',default=""),
            'consumer_secret': config('consumer_secret',default="")
            }

print(rapidapi_key)