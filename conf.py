import os
import logging

from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
    VK_TOKEN = os.getenv("VK_TOKEN")
    YA_TOKEN = os.getenv("YA_TOKEN")
    VK_USER_ID = os.getenv("VK_USER_ID")
    VK_VERSON = os.getenv("VK_VERSON")
    VK_API_URL = os.getenv("VK_API_URL")
else:
    logging.error('файл .env не найден')
