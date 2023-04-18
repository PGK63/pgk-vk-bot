from vkbottle import Bot

from bot.utils.config import BOT_TOKEN, labelers

bot = Bot(token=BOT_TOKEN)


def main():
    for custom_labeler in labelers:
        bot.labeler.load(custom_labeler)

    bot.run_forever()


if __name__ == '__main__':
    main()
