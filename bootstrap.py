if __name__ == "__main__":
    from application.bot import bot
    from application.settings import TOKEN as token

    bot.run(token=token)
