# 生圖提示詞：國一學習節奏指南

十張插圖的生成提示詞。主角是**國中一年級男生**（閱讀對象就是他）。

英文段落是要**直接複製貼上**到生圖工具的；中文是說明，不要貼進去。

---

## 先做這一步：角色設定圖

**不要一張一張隨便生。** 九個場景如果各生各的，會變成九個不同的人。

正確順序：

1. 先用下面的 **STEP 1** 生出角色設定圖，反覆生到你滿意為止
2. 把那張設定圖當作**角色參考**，再生後面每一個場景
   - ChatGPT／Gemini：把設定圖上傳，然後說「用這個角色，畫出以下場景：⋯」
   - Midjourney：把設定圖的網址放在提示詞最前面，或用 `--cref <圖片網址> --cw 100`
   - 其他工具找「角色一致性 / character reference / 參考圖」功能
3. 每個場景都從**同一張**設定圖出發，不要用上一個場景的產出當參考（會越跑越歪）

### STEP 1 — 角色設定圖

```
Character reference sheet, Japanese anime style, cel shading.

A 13-year-old Taiwanese junior-high school boy. Short black hair, slightly
messy with a few strands sticking up, straight fringe above the eyebrows.
Large dark-brown anime eyes with soft highlights. Slim build, a little short
for his age, friendly and a bit unsure. Wearing a Taiwanese junior-high
summer uniform: plain white short-sleeved polo shirt, navy blue shorts,
white socks, navy school backpack.

Three views in one image: front, three-quarter, side. Neutral standing pose,
plain light warm-grey background, full body, consistent proportions.

Clean anime line art in dark brown (not pure black), flat cel shading with
one soft shadow tone, gentle natural lighting, muted warm palette.
No text, no logos, no watermark.
```

---

## 十張場景

生完設定圖之後，每一段都照這個格式：

> 用這個角色，畫出以下場景：〔貼上場景提示詞〕

所有場景都要保留這段**共用風格指令**（貼在每個場景提示詞後面）：

```
Japanese anime style, cel shading, clean dark-brown line art, one soft
shadow tone, gentle natural light, muted warm Morandi palette (warm greige,
soft clay, sage green, dusty blue). Wide 16:9 composition, simple uncluttered
background. No text, no letters, no numbers, no logos, no watermark.
```

> ⚠️ **一定要加「No text」。** AI 生成的中文字幾乎都是亂碼，網頁上的文字我會用真正的文字排上去，圖裡不需要。

---

### hero — 首頁主視覺 → 存成 `hero.png`

```
The boy sitting at a desk by a window in the late afternoon, seen from
behind and slightly to the side. Open notebook and pencil in front of him,
a stack of textbooks and a small potted plant on the windowsill. Warm
low-angle sunlight coming through the window, soft shadows across the desk.
Calm, focused, quiet mood.
```

### 01 週間作息安排 → `01-rhythm.png`

```
The boy has just got home from school, still holding his backpack strap,
about to put the bag down in the living room. A wall clock behind him shows
five o'clock. Warm afternoon light through the doorway. He looks tired but
relieved, the end of a school day.
```

### 02 作業就是複習 → `02-homework.png`

```
The boy at his desk in the evening, one hand flipping open a textbook, the
other holding a pencil above an open notebook. A mug beside him. Desk lamp
casting a warm pool of light. Calm and settled, just getting started.
```

### 03 作業很多又不會寫 → `03-stuck.png`

```
The boy surrounded by a tall leaning stack of textbooks and loose worksheets
that threatens to topple over. He is peeking out from behind it with a
worried face and one anime sweat-drop. Slightly comedic, not distressing.
```

### 04 債務型與累積型 → `04-types.png`

```
Split composition, two halves of one image. Left half: the boy climbing a
steep staircase where each step rests on the one below, looking up at how
far it goes, warm clay tones. Right half: the same boy reaching for square
blocks that float apart and fade away like leaves in the wind, cool dusty
blue tones. A clear vertical divide down the middle.
```

> 這張是概念圖，AI 比較難一次到位。多生幾次；真的不行就跟我說，我用現在的向量圖保留這一張。

### 05 一句話筆記 → `05-onesentence.png`

```
Classroom just after the bell. Other students are standing up and leaving in
the blurred background. The boy stays at his desk, leaning over his open
textbook, writing a single short line in the page margin. Focused, a small
private moment. Afternoon light through the classroom windows.
```

### 06 頻繁小考的技巧 → `06-quiz.png`

```
The boy taking a short quiz at his classroom desk, pencil in hand above an
answer sheet, brow slightly furrowed in concentration. A clock on the wall
behind him. Clean bright classroom light.
```

### 07 資源清單 → `07-resources.png`

```
The boy at his desk holding a tablet showing a paused video lesson, a small
sand timer standing beside it on the desk. He looks like he has just
understood something — eyes a little wider, a small nod. Warm evening lamp
light.
```

### 08 給家長：訊號判讀 → `08-signals.png`

```
The boy and his mother sitting at a dining table, talking. She is listening,
leaning in slightly, warm and unhurried — not scolding. He is mid-sentence,
relaxed. Two mugs on the table. Soft evening light, gentle and safe mood.
```

> 這張的重點是**大人在聽，不是在罵**。如果生出來像在訓話，加一句
> `The adult is listening calmly and warmly, absolutely not scolding.`

### 09 給國一生的自我判讀 → `09-quest.png`

```
The boy standing at the start of a winding path made of seven round stepping
stones leading into the distance, with a small flag at the far end, like an
RPG level map. He is looking ahead with determination, one fist lightly
clenched. Gentle rolling hills, warm sunset light, adventurous but calm.
```

---

## 技術規格

| 項目 | 要求 |
| --- | --- |
| 比例 | **16:9**（很重要，卡片和內頁都是這個比例） |
| 尺寸 | 至少 **1600 × 900**，越大越好，我會再壓縮 |
| 格式 | PNG 或 JPG 都可以 |
| 檔名 | 照上面每段標的名字（`hero.png`、`01-rhythm.png`⋯） |
| 張數 | 10 張 |

## 生完之後

把十張圖放進一個資料夾給我，我會處理：

- 統一裁切成 1000 × 563，壓到適當大小
- 換掉網站上的十張插圖（首頁卡片 + 九篇內頁）
- **重做十張臉書分享圖**（OG 圖也要跟著換）
- 更新每張圖的 alt 文字
- 部署到 GitHub Pages 和 Cloudflare

## 如果某幾張生不出來

不用勉強。跟我說是哪幾張，我把那幾張保留現在的向量插圖 —— 混用會有一點風格落差，但總比一張明顯畫壞的圖好。

特別容易失敗的是 **04**（概念分割圖）和 **09**（關卡路線圖），這兩張本來就不是 AI 擅長的題材。
