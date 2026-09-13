/* 給國一生的自我判讀 — a seven-stage walkthrough of chapters 01–07.
   Every stage is a decision the reader actually faces on a weekday
   evening; the feedback is the principle from the matching chapter. */

(function () {
  "use strict";

  var mount = document.getElementById("quest");
  if (!mount) return;

  var STAGES = [
    {
      icon: "🏠",
      tag: "關卡一 · 放學回到家",
      from: "01",
      link: "01-rhythm.html",
      scene: "四點半，你剛進門，書包還在肩上。第一件事要做什麼？",
      options: [
        {
          text: "馬上進房間開始寫作業，早點寫完早點輕鬆",
          ok: false,
          say: "聽起來很認真，但你的腦袋還停在學校模式。更麻煩的是，休息被擠到最後，通常會變成「邊寫邊滑手機」——兩件事都做不好。"
        },
        {
          text: "先休息一小時，而且是「動」的休息：洗澡、散步、打球",
          ok: true,
          say: "放學後那一小時是你一天裡<strong>唯一不受作業量影響的時段</strong>，所以它是保底的休息，不管今天作業多少都有。而且「動」的休息比躺著更能把腦袋切換回來。"
        },
        {
          text: "先躺著滑手機放鬆一下，有精神再開始",
          ok: false,
          say: "滑手機的問題不是浪費時間，是它很難停，而且停下來之後你會更難開機。同樣一小時，換成洗澡或走一走，效果完全不同。"
        }
      ]
    },
    {
      icon: "📚",
      tag: "關卡二 · 坐到書桌前",
      from: "02",
      link: "02-homework.html",
      scene: "晚上六點四十，桌上有數學習作、英文單字抄寫、還有明天要考的理化。先動哪一個？",
      options: [
        {
          text: "先翻兩分鐘今天的課本，再開始寫作業",
          ok: true,
          say: "這兩分鐘不是複習，是<strong>開機</strong>。翻過今天上的內容，作業會寫得更順——它其實是在替你省時間，不是多花時間。"
        },
        {
          text: "先做最快做完的英文單字抄寫，拿一點成就感",
          ok: false,
          say: "抄寫是手工，不是複習。而且它是少數可以隔天早自習或下課補的作業——留到腦袋累的時候做就好。"
        },
        {
          text: "先讀明天要考的理化，考試最重要",
          ok: false,
          say: "小考靠的是記憶的即時提取，排在<strong>睡前</strong>效果最好。太早讀，睡前那一段反而空掉了。"
        }
      ]
    },
    {
      icon: "✏️",
      tag: "關卡三 · 卡住了",
      from: "02",
      link: "02-homework.html",
      scene: "數學寫到一題卡住，你已經盯著它想了五分鐘，還是沒有頭緒。",
      options: [
        {
          text: "再想想看，想不出來不甘心",
          ok: false,
          say: "卡死在一題上，是晚上整個失控的頭號原因。一題花掉四十分鐘，其他六科就沒了。"
        },
        {
          text: "畫個記號、跳過，先把會寫的全部寫完",
          ok: true,
          say: "五分鐘是停損點。等會寫的都清掉之後再回頭處理有記號的地方——<strong>那一步才是真正的複習</strong>，也是唯一不能省的。"
        },
        {
          text: "翻到解答抄下來，至少作業是完整的",
          ok: false,
          say: "抄答案會讓這個洞隱形：老師以為你懂了，你自己也以為懂了，然後它一路累積到段考。"
        }
      ]
    },
    {
      icon: "🔍",
      tag: "關卡四 · 上網查",
      from: "03",
      link: "03-stuck.html",
      scene: "回頭處理有記號的題目。有一題你看得懂它在問什麼，只是不會算。你決定上網查。",
      options: [
        {
          text: "把題目原文貼進搜尋，找一模一樣的解答",
          ok: false,
          say: "那是查答案，不是查觀念。下次數字一換，你還是不會。"
        },
        {
          text: "搜「一元一次方程式 移項」，看十分鐘，看完關掉自己重寫一次",
          ok: true,
          say: "查<strong>觀念</strong>不查「這一題」，限時十分鐘，而且看完立刻關掉自己重寫。邊看邊抄是最常見的假學習——當下覺得懂了，隔天完全不會。"
        },
        {
          text: "開一套影片課程，從第一章開始重新複習",
          ok: false,
          say: "那會變成第二個課程、新的壓力來源。當天卡住、當天晚上看十分鐘那一個觀念就好。"
        }
      ]
    },
    {
      icon: "⚖️",
      tag: "關卡五 · 只剩四十分鐘",
      from: "04",
      link: "04-types.html",
      scene: "今天留下三個洞：數學的移項還不熟、歷史第三課沒讀、英文單字沒背。時間只夠處理一個。",
      options: [
        {
          text: "歷史，因為完全沒讀過，最心虛",
          ok: false,
          say: "歷史是<strong>累積型</strong>：今天沒讀，損失就是今天那一點，不會變大。心虛歸心虛，它晚一週讀真的沒事。"
        },
        {
          text: "數學，因為明天的課會用到今天的東西",
          ok: true,
          say: "問一句就能判斷：<strong>這科今天不懂，會不會害到下個月？</strong>數學會——它是債務型，有複利，一週的洞兩週後要花三倍時間補。債務型永遠優先。"
        },
        {
          text: "英文單字，因為背起來最快",
          ok: false,
          say: "單字也是累積型，可以欠但不能斷。而且它最好的時段是睡前那一小段，不用占用這四十分鐘。"
        }
      ]
    },
    {
      icon: "📝",
      tag: "關卡六 · 下課鐘響",
      from: "05",
      link: "05-onesentence.html",
      scene: "回到今天的理化課。老師講得很快，你有點跟不上。下課鐘響了，你有三十秒。",
      options: [
        {
          text: "趕快把黑板剩下的抄完",
          ok: false,
          say: "抄完不等於懂。筆記很完整但沒印象，是最常見的狀況。"
        },
        {
          text: "翻開剛上完那一頁，用自己的話寫一句「這節在講什麼」",
          ok: true,
          say: "<strong>寫不出來的那一節，就是今天的洞</strong>——這個發現本身就是全部的價值。這三十秒是在幫你存檔；沒存檔，晚上寫作業等於從頭再讀一次。"
        },
        {
          text: "先去福利社，回家再整理",
          ok: false,
          say: "回家就忘光了。同樣的內容，晚上要花十倍時間才想得起來。"
        }
      ]
    },
    {
      icon: "🎯",
      tag: "關卡七 · 睡前二十分鐘",
      from: "06",
      link: "06-quiz.html",
      scene: "明天第一節考英文單字二十個。你還有二十分鐘。",
      options: [
        {
          text: "從頭到尾讀三遍，讀熟一點",
          ok: false,
          say: "讀的時候很順，考的時候提取不出來——那是<strong>重複閱讀造成的熟悉感錯覺</strong>，是累積型科目最危險的陷阱。"
        },
        {
          text: "蓋住中文自己默寫一次，然後只看剛剛錯的",
          ok: true,
          say: "主動回想勝過重複閱讀，這是差距最大的一點。再加一招：單字分兩批，睡前一次、早上到校再一次，間隔重複的效果差很多。"
        },
        {
          text: "把整課課本都複習一遍比較保險",
          ok: false,
          say: "小考<strong>範圍小是優勢，不是壓力</strong>。只讀考試範圍就好，多讀的部分是拿睡眠換來的。"
        }
      ]
    }
  ];

  var RECAP = [
    { t: "放學後那一小時是保底的休息，不因作業多寡被犧牲。", n: "01", href: "01-rhythm.html" },
    { t: "先翻兩分鐘課本再寫作業，那是開機，不是複習。", n: "02", href: "02-homework.html" },
    { t: "卡超過五分鐘就畫記號跳過，回頭處理才是真複習。", n: "02", href: "02-homework.html" },
    { t: "查觀念不查答案，限時十分鐘，看完自己重寫一次。", n: "03", href: "03-stuck.html" },
    { t: "債務型（數學、理化、英文文法）永遠優先，當天清零。", n: "04", href: "04-types.html" },
    { t: "每節課三十秒寫一句話，寫不出來的就是今天的洞。", n: "05", href: "05-onesentence.html" },
    { t: "小考靠主動回想，蓋起來默寫一次勝過讀三遍。", n: "06", href: "06-quiz.html" }
  ];

  var RANKS = [
    { min: 7, name: "節奏大師", say: "七關全部一次過。你已經抓到整套邏輯了——接下來要練的不是判斷，是讓它變成習慣。" },
    { min: 5, name: "穩定上手", say: "大部分的判斷都對。剩下那一兩關值得回去看一下，通常就是目前最容易卡住的地方。" },
    { min: 3, name: "正在抓到手感", say: "一半左右答對，代表方向是通的。挑一關你最有感覺的開始做，一次一件就好。" },
    { min: 0, name: "剛開始，這很正常", say: "第一次玩幾乎沒有人會全對——這些選擇本來就違反直覺。你現在知道哪裡不一樣了，這就是收穫。" }
  ];

  var stage = 0;       // current stage index
  var firstTry = 0;    // stages cleared without a wrong pick
  var wrongHere = false;
  var focus = 100;     // 專注力

  function el(tag, cls, html) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (html != null) n.innerHTML = html;
    return n;
  }

  function renderHud() {
    var hud = el("div", "quest-hud");

    var track = el("div", "quest-track");
    for (var i = 0; i < STAGES.length; i++) {
      var dot = el("span", "quest-dot" + (i < stage ? " is-done" : i === stage ? " is-now" : ""));
      track.appendChild(dot);
    }

    var meter = el("div", "quest-meter");
    meter.innerHTML =
      '<span class="quest-meter-label">專注力</span>' +
      '<span class="quest-meter-bar"><span class="quest-meter-fill" style="width:' + focus + '%"></span></span>' +
      '<span class="quest-meter-num">' + focus + '</span>';

    hud.appendChild(track);
    hud.appendChild(meter);
    return hud;
  }

  function renderStage() {
    var s = STAGES[stage];
    wrongHere = false;

    mount.innerHTML = "";
    mount.appendChild(renderHud());

    var head = el("div", "quest-head");
    head.appendChild(el("span", "quest-icon", s.icon));
    head.appendChild(el("span", "quest-tag", s.tag));
    mount.appendChild(head);

    mount.appendChild(el("p", "quest-scene", s.scene));

    var list = el("div", "quest-options");
    s.options.forEach(function (opt, i) {
      var b = el("button", "quest-option");
      b.type = "button";
      b.innerHTML = '<span class="quest-key">' + "ABC".charAt(i) + "</span><span>" + opt.text + "</span>";
      b.addEventListener("click", function () { choose(opt, b, list); });
      list.appendChild(b);
    });
    mount.appendChild(list);
  }

  function choose(opt, button, list) {
    var buttons = list.querySelectorAll(".quest-option");
    var s = STAGES[stage];

    if (opt.ok) {
      button.classList.add("is-right");
      for (var i = 0; i < buttons.length; i++) buttons[i].disabled = true;
      if (!wrongHere) firstTry++;
      showFeedback(true, opt.say, s);
    } else {
      button.classList.add("is-wrong");
      button.disabled = true;
      wrongHere = true;
      focus = Math.max(0, focus - 8);
      var fill = mount.querySelector(".quest-meter-fill");
      var num = mount.querySelector(".quest-meter-num");
      if (fill) fill.style.width = focus + "%";
      if (num) num.textContent = focus;
      showFeedback(false, opt.say, s);
    }
  }

  function showFeedback(ok, say, s) {
    var old = mount.querySelector(".quest-feedback");
    if (old) old.remove();

    var fb = el("div", "quest-feedback " + (ok ? "is-right" : "is-wrong"));
    fb.appendChild(el("div", "quest-verdict", ok ? "✓ 過關" : "✗ 再想一下"));
    fb.appendChild(el("p", null, say));

    if (ok) {
      fb.appendChild(el("p", "quest-source",
        '出自〈<a href="' + s.link + '">第 ' + s.from + ' 篇</a>〉'));
      var next = el("button", "quest-next");
      next.type = "button";
      next.textContent = stage === STAGES.length - 1 ? "看結果 →" : "下一關 →";
      next.addEventListener("click", function () {
        stage++;
        if (stage >= STAGES.length) renderEnd();
        else renderStage();
        mount.scrollIntoView({ block: "start", behavior: "smooth" });
      });
      fb.appendChild(next);
    }

    mount.appendChild(fb);
  }

  function renderEnd() {
    var rank = RANKS.filter(function (r) { return firstTry >= r.min; })[0];

    mount.innerHTML = "";
    var end = el("div", "quest-end");

    end.appendChild(el("div", "quest-rank-label", "自我判讀結果"));
    end.appendChild(el("div", "quest-rank", rank.name));
    end.appendChild(el("p", "quest-rank-say", rank.say));

    var score = el("div", "quest-score");
    score.innerHTML =
      '<div><span class="v">' + firstTry + ' / 7</span><span class="l">一次過關</span></div>' +
      '<div><span class="v">' + focus + '</span><span class="l">剩餘專注力</span></div>';
    end.appendChild(score);

    end.appendChild(el("h3", "quest-recap-title", "七句話帶走"));
    var ul = el("ul", "quest-recap");
    RECAP.forEach(function (r) {
      var li = document.createElement("li");
      li.innerHTML = '<span class="n">' + r.n + "</span>" + r.t +
        ' <a href="' + r.href + '">看該篇 →</a>';
      ul.appendChild(li);
    });
    end.appendChild(ul);

    var again = el("button", "quest-next");
    again.type = "button";
    again.textContent = "↻ 再挑戰一次";
    again.addEventListener("click", function () {
      stage = 0; firstTry = 0; focus = 100;
      renderStage();
      mount.scrollIntoView({ block: "start", behavior: "smooth" });
    });
    end.appendChild(again);

    mount.appendChild(end);
  }

  renderStage();
})();
