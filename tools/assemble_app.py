#!/usr/bin/env python3
from pathlib import Path
import base64
root = Path(__file__).resolve().parents[1]
www = root / "app" / "src" / "main" / "assets" / "www"
www.mkdir(parents=True, exist_ok=True)
app = www / "app.js"
# Prefer joining base64 halves
b1 = root / "tools" / "app.js.b64.part1"
b2 = root / "tools" / "app.js.b64.part2"
b64f = root / "tools" / "app.js.b64"
if b1.exists() and b2.exists():
    raw = base64.b64decode(b1.read_text().strip() + b2.read_text().strip())
    app.write_bytes(raw)
    print("app.js from b64 parts", app.stat().st_size)
elif b64f.exists():
    app.write_bytes(base64.b64decode(b64f.read_text().strip()))
    print("app.js from b64", app.stat().st_size)
elif (root / "tools" / "app_parts").exists():
    parts = sorted((root / "tools" / "app_parts").glob("p*.js.txt"))
    if parts:
        app.write_text("".join(p.read_text(encoding="utf-8") for p in parts), encoding="utf-8")
        print("app.js from text parts", app.stat().st_size)
elif app.exists():
    print("app.js OK", app.stat().st_size)
else:
    raise SystemExit("app.js missing")
logo = www / "logo.png"
lp1 = root / "tools" / "logo.b64.part1"
lp2 = root / "tools" / "logo.b64.part2"
lb = root / "tools" / "logo.b64"
if not logo.exists():
    if lp1.exists() and lp2.exists():
        logo.write_bytes(base64.b64decode(lp1.read_text().strip() + lp2.read_text().strip()))
        print("logo.png from parts", logo.stat().st_size)
    elif lb.exists():
        logo.write_bytes(base64.b64decode(lb.read_text().strip()))
        print("logo.png decoded", logo.stat().st_size)
    else:
        print("WARNING: no logo")
else:
    print("logo.png OK", logo.stat().st_size)
