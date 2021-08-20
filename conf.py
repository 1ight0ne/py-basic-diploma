from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
    VK_TOKEN = os.getenv("VK_TOKEN")
    YA_TOKEN = os.getenv("YA_TOKEN")
    API_URL = "https://api.vk.com/method/"
    VK_USER_ID = os.getenv("USER_ID")
    VK_VERSON = os.getenv("VERSON_VK")
else:
    print('файл .env не найден')