import os
from dotenv import load_dotenv

# 环境变量
load_dotenv()
DASH_SCOPE_API_KEY = os.getenv('DASH_SCOPE_API_KEY')