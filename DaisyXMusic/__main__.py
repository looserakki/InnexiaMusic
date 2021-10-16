# DaisyXMusic (Telegram bot project)
# Copyright (C) 2021  Inuka Asith & Rojserbest

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import requests
from pyrogram import Client as Bot
from pyrogram import idle

from DaisyXMusic.config import API_HASH1 as API_HASH
from DaisyXMusic.config import API_HASH2 as API_HASH1
from DaisyXMusic.config import API_ID1 as API_ID
from DaisyXMusic.config import API_ID2 as API_ID1
from DaisyXMusic.config import BG_IMAGE
from DaisyXMusic.config import BOT_TOKEN
from DaisyXMusic.services.callsmusic import run1
from DaisyXMusic.services.callsmusic import run2

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="DaisyXMusic.modules"),
)
bot = Bot(
    ":memory:",
    API_ID1,
    API_HASH1,
    bot_token=BOT_TOKEN,
    plugins=dict(root="DaisyXMusic.modules"),
)
bot.start()
run1()
run2()
idle()
