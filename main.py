import aiogram
import json
import requests

from aiogram.dispatcher.filters import Command

bot = aiogram.Bot(token="")
dp = aiogram.Dispatcher(bot)

async def search_picture(query: str):
    api_key = ""
    url = f"http://api.giphy.com/v1/gifs/search?q={query}&api_key={api_key}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data["data"][0]["images"]["original"]["url"]

@dp.message_handler(Command("find_picture"))
async def find_picture(message: aiogram.types.Message):
    query = message.text.split()[1]
    picture_url = await search_picture(query)
    await bot.send_photo(chat_id=message.chat.id, photo=picture_url)

if __name__ == "__main__":
    aiogram.executor.start_polling(dp)
