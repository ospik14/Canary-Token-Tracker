import asyncio
import logging
import uvicorn
from backend.fastapi_loader import app
from bot.bot_loader import start_bot


def main():
    logging.basicConfig(level=logging.INFO)
    uvicorn.run(app, host='127.0.0.1', port=8000)

if __name__=='__main__':
    main()