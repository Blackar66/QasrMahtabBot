import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

TOKEN = os.getenv("BOT_TOKEN")  # توکن را بعداً در Render وارد می‌کنیم

bot = telebot.TeleBot(TOKEN)

MAIN_CHANNEL_ID = -1004297282062
MAIN_CHANNEL_LINK = "https://t.me/+eps7QA66F-Y3ZGM0"

NOVEL_CHANNEL_LINK = "https://t.me/+zYfSa9d95XtkZmZk"

def is_member(user_id):
    try:
        member = bot.get_chat_member(MAIN_CHANNEL_ID, user_id)
        return member.status in ["member", "administrator", "creator"]
    except:
        return False

def main_menu():
    keyboard = InlineKeyboardMarkup(row_width=2)

    keyboard.add(
        InlineKeyboardButton("📚 رمان‌ها", callback_data="novels"),
        InlineKeyboardButton("🆕 آخرین رمان‌ها", callback_data="latest")
    )

    keyboard.add(
        InlineKeyboardButton("🏷 ژانرها", callback_data="genres"),
        InlineKeyboardButton("👥 درباره ما", callback_data="about")
    )

    keyboard.add(
        InlineKeyboardButton("📜 قوانین", callback_data="rules"),
        InlineKeyboardButton("📩 ارتباط با ما", callback_data="contact")
    )

    return keyboard

@bot.message_handler(commands=['start'])
def start(message):

    text = """🌙 به قصر مهتاب خوش آمدید.

به دنیای رمان‌های اختصاصی ما قدم گذاشته‌اید.

از منوی زیر گزینه موردنظر خود را انتخاب کنید."""

    bot.send_message(
        message.chat.id,
        text,
        reply_markup=main_menu()
    )
