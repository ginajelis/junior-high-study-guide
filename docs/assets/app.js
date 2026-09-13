(function () {
  "use strict";

  /* ── Theme toggle ──────────────────────────────────────── */
  var THEME_KEY = "study-guide-theme";
  var root = document.documentElement;
  var toggle = document.getElementById("themeToggle");

  function storage(fn, fallback) {
    try { return fn(); } catch (e) { return fallback; }
  }

  var saved = storage(function () { return localStorage.getItem(THEME_KEY); }, null);
  if (saved === "light" || saved === "dark") root.setAttribute("data-theme", saved);

  if (toggle) {
    toggle.addEventListener("click", function () {
      var current = root.getAttribute("data-theme");
      if (!current) {
        var prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
        current = prefersDark ? "dark" : "light";
      }
      var next = current === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      storage(function () { return localStorage.setItem(THEME_KEY, next); });
    });
  }

  /* ── Print ─────────────────────────────────────────────── */
  var printBtn = document.getElementById("printBtn");
  if (printBtn) printBtn.addEventListener("click", function () { window.print(); });

  /* ── Back to top ───────────────────────────────────────── */
  var toTop = document.getElementById("toTop");
  if (toTop) {
    toTop.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });

    var onScroll = function () {
      toTop.classList.toggle("is-visible", window.scrollY > 600);
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  /* ── Category filter (index page) ──────────────────────── */
  var filters = Array.prototype.slice.call(
    document.querySelectorAll("#filters .filter")
  );
  var cards = Array.prototype.slice.call(
    document.querySelectorAll("#cards > li")
  );

  if (filters.length && cards.length) {
    filters.forEach(function (button) {
      button.addEventListener("click", function () {
        var cat = button.dataset.cat;

        filters.forEach(function (b) {
          b.setAttribute("aria-pressed", String(b === button));
        });

        cards.forEach(function (card) {
          card.hidden = cat !== "all" && card.dataset.cat !== cat;
        });
      });
    });
  }

  /* ── Tonight checklist ─────────────────────────────────── */
  var CHECK_KEY = "study-guide-tonight";
  var boxes = Array.prototype.slice.call(
    document.querySelectorAll("#tonight input[type=checkbox]")
  );

  if (boxes.length) {
    var state = storage(function () {
      return JSON.parse(localStorage.getItem(CHECK_KEY) || "{}");
    }, {}) || {};

    boxes.forEach(function (box) {
      box.checked = state[box.dataset.task] === true;
      box.addEventListener("change", function () {
        state[box.dataset.task] = box.checked;
        storage(function () {
          return localStorage.setItem(CHECK_KEY, JSON.stringify(state));
        });
      });
    });

    var reset = document.getElementById("resetChecks");
    if (reset) {
      reset.addEventListener("click", function () {
        boxes.forEach(function (box) { box.checked = false; });
        state = {};
        storage(function () { return localStorage.removeItem(CHECK_KEY); });
      });
    }
  }
})();
