# はじめまして ろてんちゃんです

気象分野の「露点」を子ども向けに学ぶための絵本プロジェクトです。

## 開き方

ローカルサーバーを起動して、ブラウザで `index.html` を開きます。

```powershell
cd rotenchan_book
python -m http.server 8765 --bind 127.0.0.1
```

そのあと、以下を開きます。

```text
http://localhost:8765/index.html
```

## 内容

- `index.html`: ページ送りつき絵本ビューア
- `assets/`: 絵本に使う画像、タイトル文字、最終ページ文字
- `make_title_png.py`: 手書き風タイトルPNG生成用の補助スクリプト
- `page24_trial.html`: 文字配置試作用ページ
- `font_trial_11*.html`: フォント比較用ページ
