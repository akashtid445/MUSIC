from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_photo("https://telegra.ph/file/bfc82f0de5ea1d35830f5.jpg")
    await message.reply_text(
        f"""**Hey, I'm PRINSECC MUSIC BOT🎵

I can play ꬺᶙȿᶖɕ  in your group's voice CHAT Powered by [PRINSECC-NETWORK](https://t.me/PRINCESS_NETWORK)

Add me to your group and play music freely❣️!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📢𝙋𝙊𝙒𝙀𝙍𝙀𝘿 𝘽𝙔", url="https://t.me/PRINCESS_NETWORK")
                  ],[
                    InlineKeyboardButton(
                        "⚜ SUPPORT GROUP ⚜", url="https://t.me/BESTU_1"
                    ),
                    InlineKeyboardButton(
                        "🔷️ UPDATE CHANNEL 🔷️", url="https://t.me/PRIN_CESS"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "ADD TO GROUP 🥺", url="https://t.me/PRINSECC_VC_ROBOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**PRINSECC-NETWORK**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "SUPPORT ♻️", url="https://t.me/PRINCESS_NETWORK")
                ]
            ]
        )
   )


