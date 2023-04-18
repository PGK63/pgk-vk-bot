from vkbottle import BaseStateGroup
from vkbottle.bot import Message, BotLabeler

from bot.utils.base_rule import BaseRule

auth_labeler = BotLabeler()

auth_labeler.vbml_ignore_case = True
auth_labeler.auto_rules = [BaseRule()]


class AuthState(BaseStateGroup):
    TOKEN = 0


@auth_labeler.private_message(text='/start')
async def auth_handler(message: Message):
    await message.answer('Введите токен')
