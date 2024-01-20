# Bluesky_Autopost

このリポジトリでは、[Nishiki-Hub](https://nishikiout.net)のRSSフィードを実行時に自動でBlueskyに投稿することができます。

[Bluesky]（https://bsky.app/）がとりあえずデフォルトになっていますが、post.pyに適切に設定すれば、他のAT Protocolのサービスでも利用可能なコードになっているはずです。

運用予定アカウントは[nishikiout.net](https://bsky.app/profile/nishikiout.net)です。

# 仕様

* 最大1日前のエントリーを取得して投稿します
* 私が使っているサーバーの関係上、'crontab'を使うことを前提にしています。つまり、1日以下の指定となります。
* もし使うなら、.envを使って、AT Protocolのアカウントを記述しておいてください。詳細はpost.pyを見ればわかります。
