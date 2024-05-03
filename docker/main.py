import asyncio
import logging
import sys

import aiogram.types
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
import BotClient

TOKEN = "---"
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await botclient.CommandStartHandler(message)


@dp.callback_query()
async def callback(callback: aiogram.types.CallbackQuery):
    await botclient.CallBackHandler(callback)

async def main() -> None:
    global bot
    global payer
    global botclient
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    botclient = BotClient.BotClient(bot, dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
