/**
 * Huy dang nhap muc bao ve (Ky thuat / Chuc nang) (Cancel) -> ve trang chu.
 * Bo sung nginx 401 redirect; xu ly tab Material / fetch 401.
 */
(function () {
  "use strict";

  function homeUrl() {
    var host = window.location.hostname || "";
    if (
      host === "docs.edupath.org.vn" ||
      /\.edupath\.org\.vn$/i.test(host)
    ) {
      return "https://docs.edupath.org.vn/";
    }
    return window.location.origin + "/index.html";
  }

  function goHome() {
    window.location.replace(homeUrl());
  }

  function isProtected(p) {
    return (
      p.indexOf("/technical/") !== -1 ||
      /\/technical(\/index)?\.html$/i.test(p) ||
      p.indexOf("/functional/") !== -1 ||
      /\/functional(\/index)?\.html$/i.test(p)
    );
  }

  var path = (window.location.pathname || "").replace(/\\/g, "/");

  if (isProtected(path)) {
    fetch(window.location.href, {
      method: "HEAD",
      credentials: "same-origin",
      cache: "no-store",
    })
      .then(function (response) {
        if (response.status === 401) {
          goHome();
        }
      })
      .catch(function () {
        /* ignore */
      });
  }

  document.addEventListener(
    "click",
    function (event) {
      var link = event.target.closest("a[href]");
      if (!link) {
        return;
      }
      var href = link.getAttribute("href") || "";
      if (href.indexOf("technical") === -1 && href.indexOf("functional") === -1) {
        return;
      }
      /* Cho trinh duyet mo hop dang nhap; neu 401 sau Cancel thi nginx/JS redirect */
    },
    true
  );

  if (typeof document$ !== "undefined" && document$.subscribe) {
    document$.subscribe(function () {
      var p = (window.location.pathname || "").replace(/\\/g, "/");
      if (!isProtected(p)) {
        return;
      }
      fetch(window.location.href, {
        method: "HEAD",
        credentials: "same-origin",
        cache: "no-store",
      }).then(function (response) {
        if (response.status === 401) {
          goHome();
        }
      });
    });
  }
})();
