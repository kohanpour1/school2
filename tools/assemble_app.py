#!/usr/bin/env python3
from pathlib import Path
import base64
root = Path(__file__).resolve().parents[1]
www = root / "app" / "src" / "main" / "assets" / "www"
www.mkdir(parents=True, exist_ok=True)
app = www / "app.js"
parts = [root / "tools" / f"app.js.b64.part{i}" for i in range(4)]
if all(p.exists() for p in parts):
    raw = base64.b64decode("".join(p.read_text().strip() for p in parts))
    app.write_bytes(raw)
    print("app.js from 4 b64 parts", app.stat().st_size)
elif (root / "tools" / "app.js.b64").exists():
    app.write_bytes(base64.b64decode((root / "tools" / "app.js.b64").read_text().strip()))
    print("app.js from b64", app.stat().st_size)
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
