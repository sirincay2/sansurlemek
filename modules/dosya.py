import os
from pyrogram import Client, filters
from pyrogram.types import Message
import random


@Client.on_message(filters.document)
async def dosya(bot: Client, msg: Message):
    file_name = msg.document.file_name
    if not msg.document.file_name.endswith(".txt"):
        return await msg.reply("Bu bir txt dosyası değil.")
    else:
        file = await msg.download()
        metin = open(f"downloads/{file_name}").read()
        ana_kelime_listesi = metin.split("\n")
        print(f"ana_kelime_listesi: {ana_kelime_listesi}")
        bbb = "BasicBots.txt"
        for bir_kelime in ana_kelime_listesi:
            kelimedeki_harf_listesi = list(bir_kelime)
            print(f"bir_kelime: {bir_kelime}")
            print(f"kelimedeki_harf_listesi: {kelimedeki_harf_listesi}")
            a = sayy(bir_kelime)
            print(f"a: {a}")
            if a is None:
                pass
            else:
                secilen_harfler = random.sample(set(kelimedeki_harf_listesi), a)
                print(f"secilen_harfler: {secilen_harfler}")
                for secilen_harf in secilen_harfler:
                    bir_kelime = bir_kelime.replace(secilen_harf, "*", 1)
                
            with open(bbb, "w") as f:
                f.write(f"{bir_kelime}")
                f.close()
        await bot.send_document(msg.chat.id, document="BasicBots.txt")
        #os.remove("BasicBots.txt")



def say(metin):
    sayi = int(len(set(list(metin))))
    print(f"metin: {metin}")
    print(f"sayi: {sayi}")
    if sayi == 0:
        return None
    if sayi == 3:
        return 1
    elif sayi == 4:
        return random.randint(1, 2)
    elif sayi == 5:
        return 2
    elif sayi == 6:
        return 3
    elif sayi == 7:
        return random.randint(3,4)
    elif sayi == 8:
        return 4
    elif sayi == 9:
        return 5
    elif sayi == 10:
        return random.randint(5,6)
    elif sayi == 11:
        return random.randint(6,7)
    elif sayi == 12:
        return random.randint(6,8)
    elif sayi > 12:
        return random.randint(7,9)
    else:
        if sayi < 6:
            return 2
        else:
            return 3

def sayy(metin):
    sayi = int(len(set(list(metin))))
    print(f"metin: {metin}")
    print(f"sayi: {sayi}")
    if sayi == 0:
        return None
    if sayi == 3:
        return 1
    elif sayi == 4:
        return random.randint(1,2)
    elif sayi == 5:
        return 2
    elif sayi == 6:
        return 3
    elif sayi == 7:
        return 3
    elif sayi == 8:
        return 3
    elif sayi == 9:
        return 4
    elif sayi == 10:
        return 4
    elif sayi == 11:
        return 5
    elif sayi == 12:
        return 5
    elif sayi > 12:
        return 6
    else:
        if sayi < 6:
            return 2
        else:
            return 3