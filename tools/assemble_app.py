#!/usr/bin/env python3
from pathlib import Path
import base64
root = Path(__file__).resolve().parents[1]
www = root / "app" / "src" / "main" / "assets" / "www"
www.mkdir(parents=True, exist_ok=True)
app = www / "app.js"
if not app.exists():
    raise SystemExit("app.js missing")
print("app.js OK", app.stat().st_size)
logo = www / "logo.png"
b64f = root / "tools" / "logo.b64"
if not logo.exists() and b64f.exists():
    logo.write_bytes(base64.b64decode(b64f.read_text().strip()))
    print("logo.png decoded", logo.stat().st_size)
elif logo.exists():
    print("logo.png OK", logo.stat().st_size)
else:
    print("WARNING: no logo")
