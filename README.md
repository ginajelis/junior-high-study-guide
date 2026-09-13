# 國一學習節奏指南

給國中一年級適應期的一份參考：週間作息安排、作業與複習的順序、
債務型與累積型科目的區辨，以及「一句話筆記」的用法。

八篇短文，首頁是卡片式索引，可依分類篩選。靜態網站，沒有建置步驟。

## 線上版本

| 環境 | 網址 |
| --- | --- |
| GitHub Pages | https://ginajelis.github.io/junior-high-study-guide/ |
| Cloudflare Workers | https://junior-high-study-guide.ginajelis.workers.dev |

兩邊都在 push 到 `main` 之後自動更新。

## 結構

```
docs/
  index.html                   # 卡片式文章索引 + 分類篩選
  posts/
    01-rhythm.html             # 週間作息安排        ★
    02-homework.html           # 作業就是複習        ★
    03-stuck.html              # 作業很多又不會寫
    04-types.html              # 債務型與累積型      ★
    05-onesentence.html        # 一句話筆記          ★
    06-quiz.html               # 頻繁小考的技巧
    07-resources.html          # 資源清單
    08-signals.html            # 給家長：訊號判讀
  assets/styles.css            # 設計 token、深淺色、列印樣式
  assets/app.js                # 深淺色、分類篩選、今晚清單、回頂端
wrangler.jsonc                 # Cloudflare Workers 靜態資產設定
.github/workflows/             # 備用的 Actions 部署路線
```

★ 標記的是核心篇章。

## 排版

版面語言參考 [blog.ichentsai.tw](https://blog.ichentsai.tw/)：深色外框配單欄白底內容
（784px）、Noto Serif TC 標題搭配磚橘色 H2、寬鬆的段落節奏。首頁則是白卡片的
三欄網格，分類以顏色區分。

新增一篇文章時，複製任一個 `docs/posts/*.html` 當範本，再到 `docs/index.html`
補一張卡片（`data-cat` 要對應篩選列的分類），並更新篩選列的篇數。

## 本機預覽

```bash
python3 -m http.server 8000 --directory docs
```

然後開 http://localhost:8000

## 部署

- **GitHub Pages** — 設定為 `main` 分支的 `/docs` 目錄。
- **Cloudflare** — 由 Workers Builds 監看這個 repo，push 後自行建置，不需要任何密鑰。
  `.github/workflows/deploy-cloudflare.yml` 是備用路線，設了
  `CLOUDFLARE_API_TOKEN` 和 `CLOUDFLARE_ACCOUNT_ID` 才會接手，否則自動跳過。

## 列印

每一頁都有專門的列印樣式（去掉頁首、篩選列與按鈕，避免區塊跨頁）。
Cmd／Ctrl + P 就能單獨印出某一篇貼在書桌前。
