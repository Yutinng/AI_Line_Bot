from linebot.v3 import WebhookHandler
from linebot.v3.messaging import MessagingApi, Configuration
from linebot.v3.webhooks import ApiClient  


user_state = {}  # 共享用戶狀態，避免 Circular Import 問題


# 官方帳號資訊放置區：設定 Line Bot API 的 Access Token & Secret
ACCESS_TOKEN = '65nN+KPiWewuFsWcM6qeDxYvVlJAvUQo7sOtXFWsj7XZkmMSRq0TFzod+weRYuzXbQPr9eDtyD23VjAWgk6Nc9639NJRww/PTNeBrx4GhKIQnhlEZVuNVXmnbwV8sr+bFFpvsBKHSLoNULAlRBtnLAdB04t89/1O/w1cDnyilFU='
CHANNEL_SECRET = '2d5eaa1e69a05a761337495df4fedf2e'

# ✅ 初始化 WebhookHandler
line_handler = WebhookHandler(CHANNEL_SECRET)

# ✅ 建立 Line API 配置
configuration = Configuration(access_token=ACCESS_TOKEN)
api_client = ApiClient(configuration)  # ✅ 確保 api_client 是全域變數
line_bot_api = MessagingApi(api_client)  # ✅ 這樣 `line_bot_api` 不會因為 with 區塊結束而無法使用

# ✅ 天氣 API Token
CWA_TOKEN = "CWA-A27AB7D0-2B62-4EEA-84DF-9CD035E693D6"
MOENV_API_KEY = "eb163e20-cd60-462f-b678-e947ec9c4fc8"  

# ✅ MySQL 資訊(地端)
MYSQL_HOST = 'localhost'
MYSQL_PORT = '3307'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '@j23h36ajh4y'
MYSQL_DATABASE = "expense_db"
