import tkinter as tk
import os
import asyncio
import subprocess
import winsound
from tkinter import messagebox
from dotenv import load_dotenv
from streampopup import twitch_example
from streampopup import get_category

exit_event = asyncio.Event()  # 終了イベントを作成
load_dotenv()  # 環境変数ロード
TARGET_CHANNEL = os.getenv("TARGET_CHANNEL")  # 対象チャンネルを定義

if not TARGET_CHANNEL:
    raise ValueError("TARGET_CHANNEL is not configured")

before_title = ""
after_title = ""

before_category = ""
after_category = ""

CHECK_INTERVAL_MS = 10000

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOUND_FILE = os.path.join(BASE_DIR, "tm2_hit005.wav")

async def show_popup():
    global before_title, after_title
    winsound.PlaySound(SOUND_FILE, winsound.SND_FILENAME)
    before_title = after_title
    messagebox.showinfo("ポップアップ通知", TARGET_CHANNEL + "のタイトルが変更されました")

async def changecomment():
    global before_category, after_category
    subprocess.run(["node", "categoryChat.js", after_category, TARGET_CHANNEL])
    before_category = after_category

async def check_condition():
    global before_title, after_title
    after_title = await get_title()
    return before_title != after_title

async def check_category():
    global before_category, after_category
    after_category = await get_category(TARGET_CHANNEL)
    return before_category != after_category

async def check_and_notify():
    # カテゴリ変更時の自動コメント機能
    # Twitchの利用状況によっては意図しない投稿となるため現在は無効化
    # if await check_category():
    #     await changecomment()
    if await check_condition():
      await show_popup()
    root.after(CHECK_INTERVAL_MS, lambda: asyncio.create_task(check_and_notify()))  # 10秒ごとにcheck_and_notifyを呼び出す

async def main():
    global root, before_title, before_category
    root = tk.Tk()
    root.title("ポップアップ通知アプリ")
    before_title = await get_title()
    before_category = await get_category(TARGET_CHANNEL)
    
    # 最初に一度だけ呼び出す
    asyncio.create_task(check_and_notify())
    
    # 終了ボタンを追加
    exit_button = tk.Button(root, text="終了", command=on_exit)
    exit_button.pack()

    # Tkinterのイベントループを制御可能な非同期ループ内で動作させる
    while not exit_event.is_set():  # 終了イベントがセットされるまで続ける
        root.update()
        await asyncio.sleep(0.01)

async def get_title():
    return await twitch_example(TARGET_CHANNEL)

def on_exit():
    exit_event.set()  # 終了イベントをセット
    root.destroy()

if __name__ == "__main__":
    asyncio.run(main())