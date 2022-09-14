import pytest
import botometer
import twitter
from twitter import bot_check

def test_declaration():
    global clay 
    clay = bot_check.Bot('@clayadavis')
    assert clay.username == '@clayadavis'

def test_check_account():
    clay.check_account()
    rapidapi_key = "bf3e6ede39msh4cbeaff9746d9f9p153c59jsnf956fde60043" # now it's called rapidapi key
    twitter_app_auth = {
        'consumer_key': 'liEOkY8ipWk7KHV92pqsFbjr7',
        'consumer_secret': 'lQFPmXWg0GMOpiphBPeRSWgcAHMd21aZ4Afbowg9IPm0dWRTzF'
        }
    bom = botometer.Botometer(wait_on_ratelimit=True,
                            rapidapi_key=rapidapi_key,
                            **twitter_app_auth)
    assert clay.result == bom.check_account(clay.username)