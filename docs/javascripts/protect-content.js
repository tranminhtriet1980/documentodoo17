/**
 * Bảo vệ hình ảnh trong tài liệu: chặn tải/kéo/chuột phải, hạn chế in ấn.
 * Lưu ý: không thể chặn hoàn toàn chụp màn hình ở cấp hệ điều hành.
 */
(function () {
  "use strict";

  var WATERMARK = "Edupath - Noi bo";

  function wrapImages() {
    var images = document.querySelectorAll(".md-typeset img:not(.img-guard img)");
    images.forEach(function (img) {
      if (img.closest(".img-guard")) {
        return;
      }
      var guard = document.createElement("div");
      guard.className = "img-guard";
      guard.setAttribute("data-doc-watermark", WATERMARK);
      guard.setAttribute("aria-hidden", "true");
      img.parentNode.insertBefore(guard, img);
      guard.appendChild(img);
    });
  }

  function blockImageContextMenu(event) {
    var target = event.target;
    if (target && target.tagName === "IMG") {
      event.preventDefault();
    }
  }

  function blockDrag(event) {
    var target = event.target;
    if (target && target.tagName === "IMG") {
      event.preventDefault();
    }
  }

  function blockSaveShortcut(event) {
    var key = (event.key || "").toLowerCase();
    if ((event.ctrlKey || event.metaKey) && (key === "s" || key === "p")) {
      event.preventDefault();
    }
  }

  function blurOnCaptureAttempt() {
    document.body.classList.add("doc-anti-capture");
    window.setTimeout(function () {
      document.body.classList.remove("doc-anti-capture");
    }, 1800);
  }

  function onVisibilityChange() {
    if (document.hidden) {
      document.body.classList.add("doc-hidden-blur");
    } else {
      document.body.classList.remove("doc-hidden-blur");
    }
  }

  document.addEventListener("contextmenu", blockImageContextMenu);
  document.addEventListener("dragstart", blockDrag);
  document.addEventListener("keydown", blockSaveShortcut);
  document.addEventListener("keyup", function (event) {
    if (event.key === "PrintScreen") {
      blurOnCaptureAttempt();
      try {
        navigator.clipboard.writeText("");
      } catch (e) {
        /* ignore */
      }
    }
  });
  document.addEventListener("visibilitychange", onVisibilityChange);

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", wrapImages);
  } else {
    wrapImages();
  }

  /* MkDocs Material instant navigation */
  if (typeof document$ !== "undefined" && document$.subscribe) {
    document$.subscribe(function () {
      wrapImages();
    });
  }

  document.body.setAttribute("data-doc-watermark", WATERMARK);
})();
