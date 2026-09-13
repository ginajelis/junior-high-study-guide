# 國一學習節奏指南

給國中一年級適應期的一份參考：週間作息安排、作業與複習的順序、
債務型與累積型科目的區辨，以及「一句話筆記」的用法。

靜態網站，沒有建置步驟。

## 線上版本

| 環境 | 網址 |
| --- | --- |
| GitHub Pages | https://ginajelis.github.io/junior-high-study-guide/ |
| Cloudflare Workers | 見 repo 的 Deployments |

## 結構

```
docs/
  index.html          # 全部內容在這裡
  assets/styles.css   # 設計 token、深淺色、列印樣式
  assets/app.js       # 深淺色切換、目錄高亮、今晚清單
wrangler.jsonc        # Cloudflare Workers 靜態資產設定
.github/workflows/    # push 到 main 就自動部署到 Cloudflare
```

## 本機預覽

```bash
python3 -m http.server 8000 --directory docs
```

然後開 http://localhost:8000

## 部署

- **GitHub Pages** — 設定為 `main` 分支的 `/docs` 目錄，push 後自動更新。
- **Cloudflare** — `.github/workflows/deploy-cloudflare.yml` 在 push 到 `main` 時
  用 wrangler 部署。需要兩個 repository secret：
  `CLOUDFLARE_API_TOKEN` 和 `CLOUDFLARE_ACCOUNT_ID`。

## 列印

網頁有專門的列印樣式（去掉目錄與按鈕、避免區塊跨頁）。
直接 Cmd／Ctrl + P 就能印出來貼在書桌前。
