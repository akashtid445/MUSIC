from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_photo("https://telegra.ph/file/632730fba83716c858045.jpg")
    await message.reply_text(
        f"""**Hey, I'm MUSIC BOT🎵

I can play ꬺᶙȿᶖɕ  in your group's voice call. Developed by @MARATHAWARRIOR

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📠 Source Code 📠", url="https://github.com/tana9373/MARATHA_WARRIOR_MUSIC")
                  ],[
                    InlineKeyboardButton(
                        "📢 SUPPORT GROUP 📢", url="https://t.me/MARATHIWARRIORS"
                    ),
                    InlineKeyboardButton(
                        "🔰COMMAND 🔰", url="https://t.me/MARATH_IWARRIORS/18"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "⚜ DEVELOPER ⚜", url="https://t.me/XD_PERSON"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**#MARATHI_WARRIORS_ON_FIRE**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔰 COMMANDS 🔰", url="https://t.me/MARATH_IWARRIORS/18")
                ]
            ]
        )
   )


