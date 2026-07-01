#!/usr/bin/env python3
"""Phục vụ site MkDocs với HTTP Basic Auth cho đường dẫn /technical/."""
from __future__ import annotations

import argparse
import base64
import sys
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE_DIR = ROOT / "site"
HTPASSWD = ROOT / "config" / "htpasswd"

sys.path.insert(0, str(ROOT / "scripts"))
from generate_htpasswd import check_credentials  # noqa: E402


class DocsHandler(SimpleHTTPRequestHandler):
    htpasswd_path: Path = HTPASSWD

    def log_message(self, format: str, *args) -> None:  # noqa: A003
        if args and str(args[0]).startswith("4"):
            super().log_message(format, *args)

    def _path_requires_auth(self) -> bool:
        path = self.path.split("?", 1)[0]
        return path == "/technical" or path.startswith("/technical/")

    def _home_url_html(self) -> str:
        return (
            "(location.hostname==='docs.edupath.org.vn'||/\\.edupath\\.org\\.vn$/i.test(location.hostname))"
            '? "https://docs.edupath.org.vn/"'
            ': (location.origin+"/index.html")'
        )

    def _unauthorized(self) -> None:
        home_js = self._home_url_html()
        body = (
            "<!DOCTYPE html><html><head><meta charset=utf-8>"
            "<title>Chuyen huong</title>"
            f"<script>location.replace({home_js});</script>"
            "</head><body><p>Dang chuyen ve trang chu...</p></body></html>"
        )
        self.send_response(401)
        self.send_header(
            "WWW-Authenticate",
            'Basic realm="Ky thuat - dang nhap de xem tai lieu"',
        )
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))

    def _check_auth(self) -> bool:
        header = self.headers.get("Authorization", "")
        if not header.startswith("Basic "):
            return False
        try:
            decoded = base64.b64decode(header[6:].strip()).decode("utf-8")
        except (ValueError, UnicodeDecodeError):
            return False
        if ":" not in decoded:
            return False
        user, password = decoded.split(":", 1)
        return check_credentials(user, password, self.htpasswd_path)

    def _gate(self) -> bool:
        if not self._path_requires_auth():
            return True
        if self._check_auth():
            return True
        self._unauthorized()
        return False

    def do_GET(self) -> None:  # noqa: N802
        if self._gate():
            super().do_GET()

    def do_HEAD(self) -> None:  # noqa: N802
        if self._gate():
            super().do_HEAD()


def main() -> None:
    parser = argparse.ArgumentParser(description="Serve MkDocs site with technical auth")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--bind", default="127.0.0.1")
    parser.add_argument("--htpasswd", type=Path, default=HTPASSWD)
    args = parser.parse_args()

    if not SITE_DIR.is_dir():
        raise SystemExit(f"Khong tim thay thu muc site: {SITE_DIR}")
    if not args.htpasswd.is_file():
        raise SystemExit(
            f"Chua co {args.htpasswd}. Chay: py -3 scripts/generate_htpasswd.py"
        )

    DocsHandler.htpasswd_path = args.htpasswd
    handler = partial(DocsHandler, directory=str(SITE_DIR))
    server = ThreadingHTTPServer((args.bind, args.port), handler)
    print(f"Serving site/ at http://{args.bind}:{args.port}/")
    print("Muc Ky thuat (/technical/) yeu cau dang nhap HTTP Basic Auth.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
