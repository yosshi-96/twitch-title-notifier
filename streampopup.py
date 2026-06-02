import os
import asyncio
from dotenv import load_dotenv
from twitchAPI.twitch import Twitch
from twitchAPI.helper import first

load_dotenv()  # 環境変数ロード
CLIENT_ID = os.getenv("CLIENT_ID")  # TwitchのクライントID
CLIENT_SECRET = os.getenv("CLIENT_SECRET")  # Twitchのクライントシークレット

if not CLIENT_ID:
    raise ValueError("CLIENT_ID is not configured")

if not CLIENT_SECRET:
    raise ValueError("CLIENT_SECRET is not configured")

async def twitch_example(target):
    twitch = await Twitch(CLIENT_ID, CLIENT_SECRET)

    try:
        user_info = await first(twitch.get_users(logins=target))
        ch_info = await twitch.get_channel_information(
            broadcaster_id=user_info.id
        )
        return ch_info[0].title

    finally:
        await twitch.close()

async def get_category(target):
    twitch = await Twitch(CLIENT_ID, CLIENT_SECRET)

    try:
        user_info = await first(twitch.get_users(logins=target))
        ch_info = await twitch.get_channel_information(
            broadcaster_id=user_info.id
        )
        return ch_info[0].game_name

    finally:
        await twitch.close()