from aiogram import Router, types, F
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Hello')