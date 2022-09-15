import json
import user

username = input('Enter a username to check: ')
bot = user.User('@' + username)
print(bot.get_bot())
print(bot.calc_sentiment())