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

版面結構參考 [blog.ichentsai.tw](https://blog.ichentsai.tw/)：單欄閱讀區（784px）、
Noto Serif TC 標題、寬鬆的段落節奏。首頁是卡片三欄網格，分類以顏色區分。

配色採**莫蘭迪色系**——低飽和、帶灰調，暖灰米色底配柔和的陶土／灰綠／灰藍／灰粉紫。
全站只有淺色一種主題，沒有深色模式。每個色相有兩階：`--x` 用於面／線，
`--x-deep` 用於需要對比的文字。

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

## 圖片

配圖透過 [Openverse](https://openverse.org/) 搜尋，**全部為 CC0 公眾領域授權**，
已下載到 `docs/assets/`：卡片封面統一為 1000×563（16:9），首頁 hero 為 960×540。
CC0 不要求標示出處，但每篇文章仍附上來源連結。

| 篇章 | 圖片 | 作者 | 來源 | 授權 |
| --- | --- | --- | --- | --- |
| 首頁 Hero | [Book Interior](https://stocksnap.io/photo/book-interior-KLXLJSBKJI) | Candace McDaniel | StockSnap | CC0 |
| 週間作息安排 | [Alarm Clock](https://stocksnap.io/photo/alarm-clock-VI3GY3LRD4) | Jessica Monte | StockSnap | CC0 |
| 作業就是複習 | [Writing Drawing](https://stocksnap.io/photo/writing-drawing-8Y0EDX4VP9) | Green Chameleon | StockSnap | CC0 |
| 作業很多又不會寫 | [Free stack spiral notebook image](https://www.rawpixel.com/image/5908233/image-paper-book-public-domain) | — | Rawpixel | CC0 |
| 債務型與累積型 | [Old stairs garden](https://www.rawpixel.com/image/3289030/free-photo-image-banister-best-stone-pictures-images-brick) | — | Rawpixel | CC0 |
| 一句話筆記 | [Sticky Notes](https://stocksnap.io/photo/sticky-notes-NCEC9BTO9Z) | Matt Moloney | StockSnap | CC0 |
| 頻繁小考的技巧 | [Pencil test paper](https://www.rawpixel.com/image/3338154/free-photo-image-exam-cc0-creative-commons) | — | Rawpixel | CC0 |
| 資源清單 | [Laptop Apple](https://stocksnap.io/photo/laptop-apple-DMY4V8V5W9) | Mateusz Dach | StockSnap | CC0 |
| 給家長：訊號判讀 | [Mother Daughter](https://stocksnap.io/photo/mother-daughter-FHQOAULEKZ) | Family First | StockSnap | CC0 |

## 列印

每一頁都有專門的列印樣式（去掉頁首、篩選列與按鈕，避免區塊跨頁）。
Cmd／Ctrl + P 就能單獨印出某一篇貼在書桌前。
