from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import requests
import logging

# 配置日志
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# DeepSeek-V3 API 的 URL 和 API 密钥
DEEPSEEK_API_URL = "https://api.deepseek.com/chat/completions"
DEEPSEEK_API_KEY = "sk-8dc4deadabdc4352aa1881f501436ca0"

# Telegram Bot Token
TELEGRAM_BOT_TOKEN = "7653536587:AAG7Tskt2zfDrRcLNMFjKi33pWGSa51QqSE"

# 调用 DeepSeek-V3 API 的函数
def get_deepseek_response(prompt):
    """
    调用 DeepSeek-V3 API 生成回复
    :param prompt: 用户输入的文本
    :return: DeepSeek-V3 生成的回复内容
    """
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "你是一个19岁的大学生，你需要和一个19岁的同龄人对话，请用朋友的语气和他对话"},
            {"role": "user", "content": prompt}
        ],
    }
    try:
        response = requests.post(DEEPSEEK_API_URL, json=data, headers=headers)
        print(response.status_code);
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return "抱歉，我暂时无法处理这个消息。"
    except Exception as e:
        logging.error(f"调用 DeepSeek-V3 API 失败: {e}")
        return "抱歉，出错了，请稍后再试。"

# 处理 /start 命令
async def start(update: Update, context):
    await update.message.reply_text("你好！我是你的 AI 助手，随时可以和我聊天。")

# 处理用户消息
async def chat(update: Update, context):
    user_message = update.message.text
    logging.info(f"收到消息: {user_message}")

    # 调用 DeepSeek-V3 API 生成回复
    ai_reply = get_deepseek_response(user_message)
    logging.info(f"回复消息: {ai_reply}")

    # 发送回复给用户
    await update.message.reply_text(ai_reply)

# 启动机器人
if __name__ == "__main__":
    # 创建应用
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    # 注册命令处理器
    application.add_handler(CommandHandler("start", start))

    # 注册消息处理器
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    # 启动机器人
    logging.info("机器人已启动...")
    application.run_polling()
