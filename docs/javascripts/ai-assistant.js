/**
 * AI Assistant — tro ly tra loi cau hoi ve tai lieu (goc duoi phai man hinh).
 *
 * Hoat dong hoan toan tren trinh duyet: tim trong search_index.json (cung
 * nguon voi o tim kiem san co cua site), xep hang cac muc lien quan nhat,
 * tra loi bang doan trich + danh sach lien ket click duoc di dung trang.
 * Khong can server, khong API key, khong ton phi.
 */
(function () {
  "use strict";

  if (window.__aiAssistantInit) return;
  window.__aiAssistantInit = true;

  /* ---------- Cau hinh ---------- */
  var TITLE = "AI Assistant";
  var SUBTITLE = "Hoi ve tai lieu Odoo 17";
  var GREETING =
    "Xin chao 👋 Mình là <b>AI Assistant</b> của Edupath. Hãy đặt câu hỏi về tài liệu " +
    "(báo giá, lead CRM, nhập kho, kế toán…). Mình sẽ tìm và dẫn bạn tới đúng trang.";
  var SUGGESTS = [
    "Làm sao tạo báo giá?",
    "Tạo lead trong CRM",
    "Quy trình nhập kho",
    "Ghi nhận doanh thu",
    "Email marketing",
  ];
  var MAX_RESULTS = 6;
  var STOP = {};
  (
    // Tu chuc nang (da bo dau) — khong xoa cac tu noi dung nhu 'tai', 'kho'…
    "va la cua cac cho duoc khi mot nhung de trong voi thi ma nhu do nay the nao" +
    " gi lam sao theo tu den ra vao hay hoac cung rat se da bi cai nguoi minh" +
    " a an of to in on and or how what is are do you it my we can with for by at as be this that"
  )
    .split(/\s+/)
    .forEach(function (w) {
      if (w) STOP[w] = 1;
    });

  /* ---------- Tien ich ---------- */
  function norm(s) {
    return (s || "")
      .toLowerCase()
      .replace(/đ/g, "d")
      .normalize("NFD")
      .replace(/[̀-ͯ]/g, "")
      .replace(/[^a-z0-9\s]/g, " ")
      .replace(/\s+/g, " ")
      .trim();
  }

  function stripHtml(html) {
    var tmp = document.createElement("div");
    tmp.innerHTML = html || "";
    return (tmp.textContent || tmp.innerText || "").replace(/\s+/g, " ").trim();
  }

  function esc(s) {
    return (s || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function baseUrl() {
    var s =
      document.currentScript ||
      (function () {
        var all = document.getElementsByTagName("script");
        for (var i = 0; i < all.length; i++) {
          if ((all[i].src || "").indexOf("ai-assistant.js") >= 0) return all[i];
        }
        return null;
      })();
    var src = s ? s.src : "";
    var marker = "javascripts/ai-assistant.js";
    var idx = src.indexOf(marker);
    if (idx >= 0) return src.substring(0, idx);
    return new URL(".", document.baseURI).href;
  }

  var BASE = baseUrl();

  /* ---------- Nap chi muc tim kiem ---------- */
  var DOCS = null;
  var loadingPromise = null;

  function loadIndex() {
    if (loadingPromise) return loadingPromise;
    // "no-cache": luôn hỏi lại server (kèm ETag) -> sau moi lan build+deploy,
    // chatbot tu dong lay search_index.json moi. Neu chua doi -> server tra 304 (rat nhe).
    loadingPromise = fetch(BASE + "search/search_index.json", {
      credentials: "same-origin",
      cache: "no-cache",
    })
      .then(function (r) {
        if (!r.ok) throw new Error("HTTP " + r.status);
        return r.json();
      })
      .then(function (data) {
        DOCS = (data.docs || [])
          .map(function (d) {
            var text = stripHtml(d.text);
            var title = stripHtml(d.title); // tieu de co the chua &amp; / <code> -> giai ma
            return {
              location: d.location,
              title: title,
              raw: text,
              lower: text.toLowerCase(),
              ntext: norm(text),
              ntitle: norm(title),
            };
          })
          .filter(function (d) {
            return d.location && (d.ntext.length > 0 || d.ntitle.length > 0);
          });
        return DOCS;
      });
    return loadingPromise;
  }

  /* ---------- Tim kiem & xep hang ---------- */
  function search(query) {
    var qn = norm(query);
    var nTerms = qn.split(/\s+/).filter(function (t) {
      return t.length >= 2 && !STOP[t];
    });
    if (!nTerms.length) {
      nTerms = qn.split(/\s+/).filter(Boolean);
    }
    if (!nTerms.length) return [];

    var rawTokens = query
      .toLowerCase()
      .split(/\s+/)
      .filter(function (t) {
        return t.length >= 2;
      });

    var scored = [];
    for (var i = 0; i < DOCS.length; i++) {
      var d = DOCS[i];
      var score = 0;
      var covered = 0;
      for (var j = 0; j < nTerms.length; j++) {
        var t = nTerms[j];
        var inTitle = d.ntitle.indexOf(t) >= 0;
        var occ = 0;
        var pos = d.ntext.indexOf(t);
        while (pos >= 0) {
          occ++;
          if (occ > 8) break;
          pos = d.ntext.indexOf(t, pos + t.length);
        }
        if (inTitle) score += 14;
        if (occ) score += Math.min(occ, 8);
        if (inTitle || occ) covered++;
      }
      if (!covered) continue;
      // Thuong khi khop cum tu / tieu de
      if (qn.length >= 4 && d.ntext.indexOf(qn) >= 0) score += 22;
      if (qn.length >= 4 && d.ntitle.indexOf(qn) >= 0) score += 55;
      // Thuong khi phu het cac tu
      score += covered * 4;
      if (nTerms.length > 1 && covered === nTerms.length) score += 12;
      // Uu tien muc goc trang (khong phai anchor phu) mot chut
      if (d.location.indexOf("#") < 0) score += 2;
      scored.push({ doc: d, score: score, covered: covered, tokens: rawTokens });
    }

    scored.sort(function (a, b) {
      return b.score - a.score;
    });

    // Loai bo trung trang gan giong (giu anchor dau tien diem cao nhat / trang)
    var seen = {};
    var out = [];
    for (var k = 0; k < scored.length && out.length < MAX_RESULTS; k++) {
      var loc = scored[k].doc.location;
      var page = loc.split("#")[0];
      var key = loc.indexOf("#") >= 0 ? loc : page;
      // Cho phep toi da 1 muc goc + cac anchor khac nhau, nhung tranh lap y het
      if (seen[key]) continue;
      seen[key] = 1;
      out.push(scored[k]);
    }
    return out;
  }

  function makeSnippet(result) {
    var raw = result.doc.raw;
    var lower = result.doc.lower;
    var pos = -1;
    for (var i = 0; i < result.tokens.length; i++) {
      var p = lower.indexOf(result.tokens[i]);
      if (p >= 0) {
        pos = p;
        break;
      }
    }
    if (pos < 0) pos = 0;
    var start = Math.max(0, pos - 70);
    var end = Math.min(raw.length, pos + 180);
    var snip = raw.slice(start, end).trim();
    return (start > 0 ? "… " : "") + snip + (end < raw.length ? " …" : "");
  }

  function highlight(text, tokens) {
    var out = esc(text);
    var uniq = tokens
      .slice()
      .sort(function (a, b) {
        return b.length - a.length;
      })
      .filter(function (t) {
        return t.length >= 2;
      });
    for (var i = 0; i < uniq.length; i++) {
      var safe = uniq[i].replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
      try {
        out = out.replace(new RegExp("(" + safe + ")", "gi"), "$1");
      } catch (e) {
        /* ignore */
      }
    }
    return out.replace(//g, "<mark>").replace(//g, "</mark>");
  }

  function crumb(location) {
    var path = location.split("#")[0].replace(/\.html?$/i, "");
    var parts = path.split("/").filter(Boolean);
    if (parts.length && /^index$/i.test(parts[parts.length - 1])) parts.pop();
    return parts
      .map(function (p) {
        return p.replace(/[-_]+/g, " ");
      })
      .join(" › ");
  }

  /* ---------- Soan cau tra loi ---------- */
  function answerHtml(query, results) {
    if (!results.length) {
      return (
        "<p>Mình chưa tìm thấy mục nào khớp với “<b>" +
        esc(query) +
        "</b>”. Bạn thử dùng từ khóa ngắn gọn hơn (ví dụ: <i>báo giá</i>, " +
        "<i>nhập kho</i>, <i>hóa đơn</i>) nhé.</p>"
      );
    }
    var top = results[0];
    var snippet = highlight(makeSnippet(top), top.tokens);
    var html =
      "<p>Mình tìm thấy nội dung liên quan. Đây là phần phù hợp nhất:</p>" +
      '<p style="opacity:.9">' +
      snippet +
      "</p>" +
      '<div class="ai-results">';
    for (var i = 0; i < results.length; i++) {
      var d = results[i].doc;
      var c = crumb(d.location);
      html +=
        '<a class="ai-result" href="' +
        esc(BASE + d.location) +
        '">' +
        '<span class="ai-result__title">' +
        esc(d.title || "Xem tài liệu") +
        "</span>" +
        (c ? '<span class="ai-result__crumb">' + esc(c) + "</span>" : "") +
        "</a>";
    }
    html += "</div>";
    return html;
  }

  /* ---------- Giao dien ---------- */
  var els = {};
  var history = [];

  function loadHistory() {
    try {
      history = JSON.parse(sessionStorage.getItem("ai-assistant-chat") || "[]");
    } catch (e) {
      history = [];
    }
  }

  function saveHistory() {
    try {
      sessionStorage.setItem("ai-assistant-chat", JSON.stringify(history.slice(-40)));
    } catch (e) {
      /* ignore */
    }
  }

  function scrollBottom() {
    els.body.scrollTop = els.body.scrollHeight;
  }

  function appendBubble(role, html, store) {
    var div = document.createElement("div");
    div.className = "ai-msg ai-msg--" + role;
    div.innerHTML = html;
    els.body.appendChild(div);
    scrollBottom();
    if (store) {
      history.push({ role: role, html: html });
      saveHistory();
    }
    return div;
  }

  function showTyping() {
    var div = document.createElement("div");
    div.className = "ai-msg ai-msg--bot";
    div.innerHTML =
      '<span class="ai-typing"><span></span><span></span><span></span></span>';
    els.body.appendChild(div);
    scrollBottom();
    return div;
  }

  function suggestsHtml() {
    var chips = SUGGESTS.map(function (q) {
      return '<button type="button" class="ai-chip" data-q="' + esc(q) + '">' + esc(q) + "</button>";
    }).join("");
    return '<div class="ai-suggests">' + chips + "</div>";
  }

  function ask(query) {
    query = (query || "").trim();
    if (!query) return;
    appendBubble("user", esc(query), true);
    els.textarea.value = "";
    autoGrow();
    var typing = showTyping();

    loadIndex()
      .then(function () {
        var results = search(query);
        var html = answerHtml(query, results);
        setTimeout(function () {
          typing.remove();
          appendBubble("bot", html, true);
        }, 250);
      })
      .catch(function (err) {
        typing.remove();
        appendBubble(
          "bot",
          "<p>Xin lỗi, mình chưa tải được dữ liệu tài liệu (" +
            esc(String(err && err.message ? err.message : err)) +
            "). Bạn có thể dùng ô <b>Tìm kiếm</b> ở đầu trang.</p>",
          false
        );
      });
  }

  function autoGrow() {
    els.textarea.style.height = "auto";
    els.textarea.style.height = Math.min(els.textarea.scrollHeight, 96) + "px";
  }

  function openPanel() {
    els.panel.hidden = false;
    els.fab.hidden = true;
    els.textarea.focus();
    scrollBottom();
  }

  function closePanel() {
    els.panel.hidden = true;
    els.fab.hidden = false;
  }

  function build() {
    // Nut noi (FAB)
    var fab = document.createElement("button");
    fab.type = "button";
    fab.className = "ai-fab";
    fab.setAttribute("aria-label", "Mở " + TITLE);
    fab.innerHTML =
      '<span class="ai-fab__badge"><img src="' +
      esc(BASE + "assets/edupath-mark.svg") +
      '" alt=""></span><span class="ai-fab__label">' +
      esc(TITLE) +
      "</span>";

    // Khung chat
    var panel = document.createElement("div");
    panel.className = "ai-panel";
    panel.setAttribute("role", "dialog");
    panel.setAttribute("aria-label", TITLE);
    panel.hidden = true;
    panel.innerHTML =
      '<div class="ai-header">' +
      '<span class="ai-header__logo"><img src="' +
      esc(BASE + "assets/edupath-logo.svg") +
      '" alt="EduPath"></span>' +
      '<span class="ai-header__titles">' +
      '<span class="ai-header__title">' +
      esc(TITLE) +
      "</span>" +
      '<span class="ai-header__subtitle">' +
      esc(SUBTITLE) +
      "</span>" +
      "</span>" +
      '<button type="button" class="ai-header__close" aria-label="Đóng">✕</button>' +
      "</div>" +
      '<div class="ai-body"></div>' +
      '<div class="ai-input">' +
      '<textarea rows="1" placeholder="Nhập câu hỏi của bạn…" aria-label="Câu hỏi"></textarea>' +
      '<button type="button" class="ai-send" aria-label="Gửi">' +
      '<svg viewBox="0 0 24 24"><path d="M3 20.5v-6l8-2.5-8-2.5v-6l19 8.5z"/></svg>' +
      "</button>" +
      "</div>" +
      '<div class="ai-footnote">Trả lời dựa trên nội dung tài liệu — bấm kết quả để mở đúng trang.</div>';

    document.body.appendChild(fab);
    document.body.appendChild(panel);

    els.fab = fab;
    els.panel = panel;
    els.body = panel.querySelector(".ai-body");
    els.textarea = panel.querySelector("textarea");
    els.send = panel.querySelector(".ai-send");
    els.close = panel.querySelector(".ai-header__close");

    // Khoi phuc lich su hoac chao mung
    loadHistory();
    if (history.length) {
      history.forEach(function (m) {
        appendBubble(m.role, m.html, false);
      });
    } else {
      appendBubble("bot", GREETING + suggestsHtml(), false);
    }

    // Su kien
    fab.addEventListener("click", openPanel);
    els.close.addEventListener("click", closePanel);
    els.send.addEventListener("click", function () {
      ask(els.textarea.value);
    });
    els.textarea.addEventListener("input", autoGrow);
    els.textarea.addEventListener("keydown", function (e) {
      if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        ask(els.textarea.value);
      }
    });
    els.body.addEventListener("click", function (e) {
      var chip = e.target.closest(".ai-chip");
      if (chip) {
        ask(chip.getAttribute("data-q"));
      }
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && !els.panel.hidden) closePanel();
    });

    // Nap truoc chi muc khi ranh de tra loi nhanh
    if ("requestIdleCallback" in window) {
      requestIdleCallback(function () {
        loadIndex().catch(function () {});
      });
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", build);
  } else {
    build();
  }
})();
