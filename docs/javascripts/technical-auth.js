/**
 * Lớp bổ sung: che nội dung mục bảo vệ (Kỹ thuật, Chức năng) khi mở file
 * trực tiếp (file://) hoặc server không có Basic Auth.
 * Không thay thế xác thực phía server (nginx Basic Auth mới là khóa thật).
 */
(function () {
  "use strict";

  var path = (window.location.pathname || "").replace(/\\/g, "/");

  var SECTIONS = [
    {
      match: function (p) {
        return p.indexOf("/technical/") !== -1 || /\/technical\.html$/i.test(p);
      },
      title: "Kỹ thuật (Technical)",
      message:
        "Mục kỹ thuật yêu cầu đăng nhập. Dùng tài khoản được cấp bởi quản trị viên.",
    },
    {
      match: function (p) {
        return p.indexOf("/functional/") !== -1 || /\/functional\.html$/i.test(p);
      },
      title: "Chức năng (Functional)",
      message:
        "Mục chức năng yêu cầu đăng nhập. Dùng tài khoản được cấp bởi quản trị viên.",
    },
  ];

  var section = null;
  for (var i = 0; i < SECTIONS.length; i++) {
    if (SECTIONS[i].match(path)) {
      section = SECTIONS[i];
      break;
    }
  }

  if (!section) {
    return;
  }

  var overlayId = "technical-auth-overlay";

  function showOverlay(message) {
    if (document.getElementById(overlayId)) {
      return;
    }
    var overlay = document.createElement("div");
    overlay.id = overlayId;
    overlay.innerHTML =
      '<div class="technical-auth-box">' +
      "<h2>" +
      section.title +
      "</h2>" +
      "<p>" +
      (message || section.message) +
      "</p>" +
      "<p class=\"technical-auth-hint\">Nếu trình duyệt chưa hiện hộp đăng nhập, tải lại trang hoặc mở qua server nội bộ (Docker / MoTaiLieu).</p>" +
      "</div>";
    document.body.appendChild(overlay);
    document.body.classList.add("technical-locked");
  }

  function hideOverlay() {
    var overlay = document.getElementById(overlayId);
    if (overlay) {
      overlay.remove();
    }
    document.body.classList.remove("technical-locked");
  }

  /* Server Basic Auth: trình duyệt gửi Authorization — không cần overlay */
  if (window.location.protocol === "http:" || window.location.protocol === "https:") {
    fetch(window.location.href, {
      method: "HEAD",
      credentials: "same-origin",
      cache: "no-store",
    })
      .then(function (response) {
        if (response.status === 401) {
          showOverlay("Vui lòng đăng nhập qua hộp thoại của trình duyệt.");
        } else {
          hideOverlay();
        }
      })
      .catch(function () {
        /* offline / CORS — giữ nội dung */
        hideOverlay();
      });
    return;
  }

  /* file:// — không có auth server */
  showOverlay(
    "Bạn đang mở file trực tiếp. Mục này chỉ xem qua server có đăng nhập."
  );
})();
