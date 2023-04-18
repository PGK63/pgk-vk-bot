from vkbottle.bot import Message
from vkbottle.dispatch import rules


class BaseRule(rules.ABCRule[Message]):
    async def check(self, message: Message) -> dict:
        user_info = await message.ctx_api.users.get(message.from_id)
        return {"user": user_info[0]}
