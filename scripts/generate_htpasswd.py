#!/usr/bin/env python3
"""Tạo hoặc cập nhật config/htpasswd (Apache apr1-md5) cho phần Kỹ thuật."""
from __future__ import annotations

import argparse
import getpass
import hashlib
import secrets
import string
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTPASSWD = ROOT / "config" / "htpasswd"

ITOA64 = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def _to64(value: int, count: int) -> str:
    out = []
    while count > 0:
        out.append(ITOA64[value & 0x3F])
        value >>= 6
        count -= 1
    return "".join(out)


def apr1_md5(password: str, salt: str) -> str:
    pw = password.encode("utf-8")
    sl = salt.encode("utf-8")
    ctx = hashlib.md5(pw + b"$apr1$" + sl)
    final = hashlib.md5(pw + sl + pw).digest()
    for i in range(len(pw)):
        ctx.update(bytes([final[i % 16]]))
    i = len(pw)
    while i:
        ctx.update(b"\x00" if i & 1 else pw[:1])
        i >>= 1
    digest = ctx.digest()
    for i in range(1000):
        ctx1 = hashlib.md5()
        ctx1.update(pw if i & 1 else digest)
        if i % 3:
            ctx1.update(sl)
        if i % 7:
            ctx1.update(pw)
        ctx1.update(digest if i & 1 else pw)
        digest = ctx1.digest()
    order = [0, 6, 12, 1, 7, 13, 2, 8, 14, 3, 9, 15, 4, 10, 5, 11]
    perm = b"".join(digest[i : i + 1] for i in order)
    hashstr = (
        _to64((perm[0] << 16) | (perm[1] << 8) | perm[2], 4)
        + _to64((perm[3] << 16) | (perm[4] << 8) | perm[5], 4)
        + _to64((perm[6] << 16) | (perm[7] << 8) | perm[8], 4)
        + _to64((perm[9] << 16) | (perm[10] << 8) | perm[11], 4)
        + _to64((perm[12] << 16) | (perm[13] << 8) | perm[14], 4)
        + _to64(perm[15], 2)
    )
    return f"$apr1${salt}${hashstr}"


def verify_apr1(password: str, stored: str) -> bool:
    if not stored.startswith("$apr1$"):
        return False
    parts = stored.split("$")
    if len(parts) != 4:
        return False
    salt = parts[2]
    return apr1_md5(password, salt) == stored


def random_salt(length: int = 8) -> str:
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))


def load_htpasswd(path: Path | None = None) -> dict[str, str]:
    path = path or HTPASSWD
    users: dict[str, str] = {}
    if not path.is_file():
        return users
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        user, hashed = line.split(":", 1)
        users[user] = hashed
    return users


def check_credentials(user: str, password: str, path: Path | None = None) -> bool:
    stored = load_htpasswd(path).get(user)
    if not stored:
        return False
    return verify_apr1(password, stored)


def write_auth(user: str, password: str) -> None:
    HTPASSWD.parent.mkdir(parents=True, exist_ok=True)
    salt = random_salt()
    hashed = apr1_md5(password, salt)
    HTPASSWD.write_text(f"{user}:{hashed}\n", encoding="utf-8")
    print("OK:", HTPASSWD.name)
    print("User:", user)


def main() -> None:
    parser = argparse.ArgumentParser(description="Tao htpasswd cho muc Ky thuat")
    parser.add_argument("-u", "--user", default="technical", help="Ten dang nhap")
    parser.add_argument("-p", "--password", help="Mat khau (neu bo trong se hoi)")
    args = parser.parse_args()
    password = args.password or getpass.getpass("Mat khau Ky thuat: ")
    if len(password) < 8:
        raise SystemExit("Mat khau can it nhat 8 ky tu.")
    write_auth(args.user, password)


if __name__ == "__main__":
    main()
