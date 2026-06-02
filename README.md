# Twitch Title Notifier

## 概要

Twitch配信者の配信タイトル変更を監視し、変更があった際にWindows上でポップアップ通知を表示するツールです。

普段視聴している配信者のタイトル変更や企画開始を見逃さないようにするために作成しました。

## 主な機能

- Twitch APIを利用した配信情報取得
- 配信タイトル変更の定期監視
- タイトル変更時のポップアップ通知
- 通知音の再生
- 環境変数による認証情報管理

## 使用技術

### Backend

- Python 3.11

### Libraries

- twitchAPI
- python-dotenv
- asyncio
- tkinter

## システム構成

```text
Twitch API
     ↓
streampopup.py
     ↓
main.py
     ↓
タイトル変更検知
     ↓
ポップアップ通知
```

## セットアップ

### 1. リポジトリを取得

```bash
git clone <repository-url>
cd twitch-title-notifier
```

### 2. Pythonライブラリをインストール

```bash
pip install -r requirements.txt
```

### 3. 環境変数設定

プロジェクト直下に `.env` を作成してください。

```env
TARGET_CHANNEL=channel_name
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
```

## 起動方法

```bash
python main.py
```

## 工夫した点

- Twitch APIを利用して配信タイトルを定期取得
- asyncioを利用した非同期処理による監視
- 認証情報を.envで管理し、GitHub公開時のセキュリティを向上
- API接続時にtry/finallyを利用してリソースを確実に解放
- 定数化や命名規則の見直しにより保守性を向上

## 学んだこと

本プロジェクトでは以下を学習しました。

- Twitch APIの利用方法
- 非同期処理（asyncio）
- 環境変数による認証情報管理
- Git/GitHubを利用したソースコード管理
- Pythonによるデスクトップアプリ開発
- API利用時の例外処理とリソース管理

## ライセンス

MIT License