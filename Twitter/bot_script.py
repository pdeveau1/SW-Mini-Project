import check_bot

username = input('Enter a username to check: ')
bot = check_bot.Bot('@' + username)
print(bot.get_account())
print(bot.get_score())
print(bot.get_bot())