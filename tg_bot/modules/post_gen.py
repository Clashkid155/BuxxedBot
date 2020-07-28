from telegram import Update, Bot
from telegram.ext import run_async
from tg_bot.modules.disable import DisableAbleCommandHandler, CommandHandler, Filters
from tg_bot import dispatcher
from tg_bot import SUDO_USERS

@run_async
def post(bot: Bot, update: Update) -> str:

    message = update.effective_message
    text = message.text[6:]
    try:
        codename, fullname, size, link, mdsum, xda, date = text.split()
    except ValueError:
        message.reply_text("Please read help message\
                           to know list of commands", quote=True)
        exit(1)
    fullname = fullname.replace("-", "  ")

    template = f"\
        *ConquerOS for {fullname} ({codename}) is up!*\n\
        \n*ROM Version:* 3.4 BETA\
        \n*Build Date:* `{date}`\
        \n*ROM Size:*  `{size}`\
        \n*MD5SUM:* `{mdsum}`\
        \n[Download]({link})\
        \n[Official Community]({xda})"



    if message.reply_to_message and message.reply_to_message.photo != []:
        message.reply_photo(message.reply_to_message.photo[-1].file_id,
                            caption=template, parse_mode="Markdown")
    else:
        message.reply_text(template, parse_mode="Markdown")
    return ""

example = "*Example:*\n"\
    "` /post whyred Redmi-Note-5-Pro 1.2gb https://5y6.com  8u66vg777u75d6 http://5y6.com 2020-7-4 `"

__help__ = """
Only for *ConquerOS*
*Make sure you follow this  pattern else an error will arise.*\n
- /post device-codename device-fullname(use - instead of space)
size link mdsum xda-link date\n
{}
\nDon't give any extra word or space
""".format(example)

__mod_name__ = "Post"

#postgen = DisableAbleCommandHandler("post", post)
postgen = CommandHandler("post", post, filters=Filters.user(SUDO_USERS))
dispatcher.add_handler(postgen)
