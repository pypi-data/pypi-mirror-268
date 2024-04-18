import os
import redis
import dotenv
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

from telegram import (
    Update,
    ReplyKeyboardMarkup,
    KeyboardButton)

PINDAO_TEXT = '📚频道列表'
XUEXI_TEXT = '🍿学习视频'
SHIYONG_TEXT = '🐝试用频道'
VIP_TEXT = '💎购买会员'
FANYONG_TEXT = '🍕返佣链接'
QUN_TEXT = '🙌社群链接'
FAQ_TEXT = '🤔疑问解答(FAQ❓)'
ENV_PREFIX = 'TG_KOLTIME_MENU_BOT_'

r: redis.client.Redis | None = None

score_dict: dict[float, str] = {
    1.0: '中文博主',
    2.0: '提阿非罗',
    3.0: '英文博主',
    4.0: 'koltime',
    5.0: '其他',
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [
            KeyboardButton(PINDAO_TEXT),
            KeyboardButton(XUEXI_TEXT),
        ],
        [
            KeyboardButton(SHIYONG_TEXT),
            KeyboardButton(VIP_TEXT),
        ],
        [
            KeyboardButton(FANYONG_TEXT),
            KeyboardButton(QUN_TEXT),
        ], [
            KeyboardButton(FAQ_TEXT)
        ]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard)

    description = r.hget('koltime_menu_bot', 'description')
    caption = 'welcome!'
    if isinstance(description, bytes):
        caption = description.decode()
    photo = r.hget('koltime_menu_bot', 'pic_url')
    if isinstance(photo, bytes):
        await update.message.reply_photo(
            photo=photo.decode(),
            caption=caption,
            reply_markup=reply_markup,
        )
    else:
        await update.message.reply_text(
            text=caption,
            reply_markup=reply_markup,
        )


async def pindao(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pindao_dict: dict[str, list[tuple[str]]] = {}
    channels = r.zrange("koltime_menu_bot_channels", 0, 1000, withscores=True)
    for item in channels:
        pindao_list = pindao_dict.setdefault(score_dict[item[1]], [])
        pindao_list.append(tuple(item[0].decode().split(',')))

    text = f"{PINDAO_TEXT}👇\n"
    for k, v in pindao_dict.items():
        text += f'【{k}】\n'
        for v_item in v:
            text += f'[{v_item[1]}]({v_item[2]})\n'

        text += '\n'

    text = text.replace('-', '\\-')
    await update.message.reply_text(
        text,
        parse_mode='MarkdownV2')


async def faq(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('🍄开发中...')


async def xuexi(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('🍄开发中...')


async def shiyong(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('🍄开发中...')


async def vip(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('🍄开发中...')


async def fanyong(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('🍄开发中...')


async def qun(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('🍄开发中...')


def koltime_menu_bot(env_path: str = '.env') -> None:
    dotenv.load_dotenv(env_path)
    global r
    if r is None:
        r = redis.Redis(
            host=os.getenv(f'{ENV_PREFIX}REDIS_HOST'),
            port=os.getenv(f'{ENV_PREFIX}REDIS_PORT'),
            password=os.getenv(f'{ENV_PREFIX}REDIS_PASSWORD'),
            db=0)

    proxy = os.getenv(f'{ENV_PREFIX}PROXY')
    token = os.getenv(f'{ENV_PREFIX}TOKEN')
    if proxy is None:
        application = (
            Application.builder()
            .token(token)
            .build()
        )
    else:
        application = (
            Application.builder()
            .proxy(proxy)
            .token(token)
            .build()
        )

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.Text(['?', FAQ_TEXT]), faq))
    application.add_handler(MessageHandler(filters.Text([PINDAO_TEXT]), pindao))
    application.add_handler(MessageHandler(filters.Text([XUEXI_TEXT]), xuexi))
    application.add_handler(MessageHandler(filters.Text([SHIYONG_TEXT]), shiyong))
    application.add_handler(MessageHandler(filters.Text([VIP_TEXT]), vip))
    application.add_handler(MessageHandler(filters.Text([FANYONG_TEXT]), fanyong))
    application.add_handler(MessageHandler(filters.Text([QUN_TEXT]), qun))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    koltime_menu_bot('d:/.env')
