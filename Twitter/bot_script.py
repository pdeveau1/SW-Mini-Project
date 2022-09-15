import json
import check_bot
import check_topics

username = input('Enter a username to check: ')
bot = check_bot.Bot('@' + username)
print(bot.get_account())
print(bot.get_score())
print(bot.get_bot())

topics = check_topics.Topics('@' + username)
topics.get_timeline()
print(json.dumps(topics.timeline, indent=4, sort_keys=True))