from telethon import events
import random, re
from userbot.utils import phantom_cmd, sudo_cmd

METOOSTR = [
    "`Me too thanks`",
    "`Haha yes, me too`",
    "`Same lol`",
    "`Me too`",
    "`Same here`",
    "`Haha yes`",
    "`Same pinch brp`",
]
RUNSREACTS = [
    "`Runs to Thanos`",
    "`Runs far, far away from earth`",
    "`Running faster than usian bolt coz I'mma Bot`",
    "`Runs to Marie`",
    "`This Group is too cancerous to deal with.`",
    "`Cya bois`",
    "`I am a mad person. Plox Ban me.`",
    "`I go away`",
    "`I am just walking off, coz me is too fat.`",
]

PRO_STRINGS = [
     "`Pros here -_- Time to Leave`",
]

@borg.on(phantom_cmd(pattern="run ?(.*)"))
@borg.on(sudo_cmd(pattern="run ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(RUNSREACTS) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = RUNSREACTS[bro]
    await event.edit(reply_text)


@borg.on(phantom_cmd(pattern="metoo ?(.*)"))
@borg.on(sudo_cmd(pattern="metoo ?(.*)"), allow_sudo=True)
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(METOOSTR) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = METOOSTR[bro]
    await event.edit(reply_text)
			  
			  
@borg.on(phantom_cmd(pattern="proo ?(.*)"))
@borg.on(sudo_cmd(pattern="proo ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(PRO_STRINGS) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = PRO_STRINGS[bro]
    await event.edit(reply_text)
			  
