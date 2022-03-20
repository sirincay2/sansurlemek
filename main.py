# @G4rip - < https://t.me/G4rip >
# Copyright (C) 2022
# Tüm hakları saklıdır.
#
# Bu dosya, < https://github.com/aylak-github/CallTone > parçasıdır.
# Lütfen GNU Affero Genel Kamu Lisansını okuyun;
# < https://www.github.com/aylak-github/CallTone/blob/master/LICENSE/ >
# ================================================================


from logging import INFO, basicConfig, getLogger
from operator import imod

from pyrogram import Client, idle, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

basicConfig(
    level=INFO,
    format="[%(levelname)s - %(asctime)s] - %(name)s - %(message)s",
    datefmt="%H:%M:%S",
)
getLogger("pyrogram").setLevel(INFO)


app = Client(
    "KelimeDüzenleme",
    api_id=8365793,
    api_hash="53ea88aba8b6f1a2fcd4f17252aaad78",
    bot_token="5278187676:AAEHKSS5Cj5SsZtLc462npaOXavAruk_ZFY",
    plugins=dict(root="modules"),
)




app.storage.SESSION_STRING_FORMAT = ">B?256sQ?"


if __name__ == "__main__":
    app.start()
    print("Başltıldı.")
    idle()

    app.stop()
