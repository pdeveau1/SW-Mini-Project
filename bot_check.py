import botometer

rapidapi_key = "bf3e6ede39msh4cbeaff9746d9f9p153c59jsnf956fde60043" # now it's called rapidapi key
twitter_app_auth = {
    'consumer_key': 'liEOkY8ipWk7KHV92pqsFbjr7',
    'consumer_secret': 'lQFPmXWg0GMOpiphBPeRSWgcAHMd21aZ4Afbowg9IPm0dWRTzF'
    }
bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)

#bearer = 'AAAAAAAAAAAAAAAAAAAAABgwhAEAAAAAm%2FPuay9r8%2BLZ9%2Fio5DLOAMxoVS4%3DgClXcOmjXlMBgrBNmCofRbTH0vBmpHmaNxTgmEgkyHH7mtzVhZ'

# Check a single account by screen name
result = bom.check_account('@clayadavis')
print(result)

# Check a single account by id
result = bom.check_account(1548959833)

# Check a sequence of accounts
accounts = ['@clayadavis', '@onurvarol', '@jabawack']
for screen_name, result in bom.check_accounts_in(accounts):
    print('')
    # Do stuff with `screen_name` and `result`

"""
import botometer

rapidapi_key = "bf3e6ede39msh4cbeaff9746d9f9p153c59jsnf956fde60043"
twitter_app_auth = {
    'consumer_key': 'liEOkY8ipWk7KHV92pqsFbjr7',
    'consumer_secret': 'lQFPmXWg0GMOpiphBPeRSWgcAHMd21aZ4Afbowg9IPm0dWRTzF',
    'access_token': '1569361476795899907-avhB8Os4Mb1hVQKOxnqAwRmCR8GMTj',
    'access_token_secret': 'O9nyw0eUUITT5Hsg8cmaVy4FJeDCUHtpUdoBaypRnQj5y',
  }
  
blt_twitter = botometer.BotometerLite(rapidapi_key=rapidapi_key, **twitter_app_auth)

# Prepare a list of screen_names you want to check.
# The list should contain no more than 100 screen_names; please remove the @
screen_name_list = ['yang3kc', 'onurvarol', 'clayadavis']
blt_scores = blt_twitter.check_accounts_from_screen_names(screen_name_list)
"""