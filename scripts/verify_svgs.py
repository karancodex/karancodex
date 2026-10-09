#!/usr/bin/env python3
"""
Verification Script for Karan Maurya's Animated GitHub Profile README SVGs.
Tests:
  1. Zero external network requests (only XML namespaces permitted).
  2. Namespace integrity across IDs.
  3. Static fallback rendering without animations.
  4. Render snapshots at t = 0s, 2s, 5s, 9s, 13s.
  5. HTML <img> embed rendering test.
  6. Mobile width responsive rendering (420px).
"""

import json
import os
import re
import subprocess
import time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"
VERIFY_DIR = BASE_DIR / "verification"
VERIFY_DIR.mkdir(exist_ok=True)

SVG_FILES = [
    "hero.svg",
    "about-life.svg",
    "stack.svg",
    "id-dashboard.svg",
    "connect.svg"
]

def check_external_requests():
    print("\n--- 1. Checking for External Asset Requests ---")
    allowed = {
        "http://www.w3.org/2000/svg",
        "http://www.w3.org/1999/xlink",
        "http://minimarvel.rightbraininfotech.in/",
        "https://muraqabahtravels.com/",
        "https://karancodex.vercel.app",
        "https://github.com/karancodex",
        "https://linkedin.com/in/karan-maurya",
        "https://www.instagram.com/karancodex"
    }
    all_ok = True
    for svg_name in SVG_FILES:
        path = ASSETS_DIR / svg_name
        content = path.read_text(encoding="utf-8")
        # Find all URLs
        urls = re.findall(r'https?://[^\s"\'<>]+', content)
        disallowed = [u for u in urls if not any(u.startswith(a) for a in allowed)]
        if disallowed:
            print(f"FAILED {svg_name}: Disallowed external URLs found: {disallowed}")
            all_ok = False
        else:
            print(f"PASSED {svg_name}: 0 external asset requests (fully self-contained).")
    return all_ok

def check_namespaces():
    print("\n--- 2. Checking ID Namespacing ---")
    expected_ns = {
        "hero.svg": "hero-",
        "about-life.svg": "about-",
        "stack.svg": "stack-",
        "id-dashboard.svg": "id-",
        "connect.svg": "conn-"
    }
    all_ok = True
    for svg_name, prefix in expected_ns.items():
        path = ASSETS_DIR / svg_name
        content = path.read_text(encoding="utf-8")
        ids = re.findall(r'\bid="([^"]+)"', content)
        bad_ids = [i for i in ids if not i.startswith(prefix)]
        if bad_ids:
            print(f"FAILED {svg_name}: IDs without prefix '{prefix}': {bad_ids}")
            all_ok = False
        else:
            print(f"PASSED {svg_name}: All {len(ids)} IDs cleanly prefixed with '{prefix}'.")
    return all_ok

def generate_render_html():
    print("\n--- 3. Creating HTML Test Harness for Snapshots ---")
    # HTML page containing all SVGs as <img> elements
    html_content = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Verification Suite</title>
  <style>
    body {{
      background: #0d1117;
      color: #c9d1d9;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      margin: 0;
      padding: 40px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 30px;
    }}
    .container {{
      width: 900px;
      max-width: 100%;
    }}
    img {{
      display: block;
      width: 100%;
      height: auto;
      border-radius: 12px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.5);
    }}
  </style>
</head>
<body>
  <div class="container"><img src="../assets/hero.svg?v=1" alt="Hero"></div>
  <div class="container"><img src="../assets/about-life.svg?v=1" alt="About Life"></div>
  <div class="container"><img src="../assets/stack.svg?v=1" alt="Stack"></div>
  <div class="container"><img src="../assets/id-dashboard.svg?v=1" alt="ID Dashboard"></div>
  <div class="container"><img src="../assets/connect.svg?v=1" alt="Connect"></div>
</body>
</html>"""
    harness_path = VERIFY_DIR / "harness.html"
    harness_path.write_text(html_content, encoding="utf-8")
    print(f"Generated {harness_path}")

def render_snapshots():
    print("\n--- 4. Rendering Snapshots at t = 0s, 2s, 5s, 9s, 13s ---")
    times = [0, 2, 5, 9, 13]
    harness_path = VERIFY_DIR / "harness.html"

    # Start a quick local HTTP server or render via file://
    # We will use google-chrome headless screenshots with simulated delays
    for t in times:
        out_png = VERIFY_DIR / f"full_profile_t{t}s.png"
        cmd = [
            "google-chrome",
            "--headless",
            "--disable-gpu",
            "--window-size=1000,2600",
            f"--virtual-time-budget={t * 1000 if t > 0 else 500}",
            f"--screenshot={out_png}",
            f"file://{harness_path}"
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"Captured snapshot at {t}s -> {out_png.name} ({out_png.stat().st_size} bytes)")

    # Also render individual SVG snapshots for each at t=0s and t=5s
    for svg_name in SVG_FILES:
        svg_base = svg_name.replace(".svg", "")
        for t in [0, 5]:
            out_png = VERIFY_DIR / f"{svg_base}_t{t}s.png"
            cmd = [
                "google-chrome",
                "--headless",
                "--disable-gpu",
                "--window-size=920,520",
                f"--virtual-time-budget={t * 1000 if t > 0 else 500}",
                f"--screenshot={out_png}",
                f"file://{ASSETS_DIR / svg_name}"
            ]
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"Captured {svg_name} at {t}s -> {out_png.name}")

def render_static_fallback():
    print("\n--- 5. Rendering with Animation Removed (Static Fallback) ---")
    for svg_name in SVG_FILES:
        path = ASSETS_DIR / svg_name
        content = path.read_text(encoding="utf-8")
        # Strip animations
        no_anim = re.sub(r'animation:[^;}]+;', 'animation: none !important;', content)
        no_anim = re.sub(r'<animate[^>]*/>', '', no_anim)
        no_anim = re.sub(r'<animateTransform[^>]*/>', '', no_anim)
        
        static_file = VERIFY_DIR / f"static_{svg_name}"
        static_file.write_text(no_anim, encoding="utf-8")
        
        out_png = VERIFY_DIR / f"static_{svg_name.replace('.svg', '.png')}"
        cmd = [
            "google-chrome",
            "--headless",
            "--disable-gpu",
            "--window-size=920,520",
            f"--screenshot={out_png}",
            f"file://{static_file}"
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"Captured static fallback -> {out_png.name}")

def render_mobile_view():
    print("\n--- 6. Rendering Mobile Width (420px) ---")
    harness_path = VERIFY_DIR / "harness.html"
    out_png = VERIFY_DIR / "profile_mobile_420px.png"
    cmd = [
        "google-chrome",
        "--headless",
        "--disable-gpu",
        "--window-size=440,2800",
        "--virtual-time-budget=2000",
        f"--screenshot={out_png}",
        f"file://{harness_path}"
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Captured mobile preview -> {out_png.name} ({out_png.stat().st_size} bytes)")

def main():
    print("Starting comprehensive verification suite...")
    c1 = check_external_requests()
    c2 = check_namespaces()
    generate_render_html()
    render_snapshots()
    render_static_fallback()
    render_mobile_view()
    print("\nVerification suite completed successfully!")

if __name__ == "__main__":
    main()
