import json
import user

username = input('Enter a username to check: ')
bot = user.User('@' + username)
print(bot.get_account())
print(bot.get_score())
print(bot.get_bot())
print(bot.get_id())
bot.get_timeline()
print(json.dumps(bot.timeline, indent=4, sort_keys=True))
bot.get_sentiment()