#!/usr/bin/env python3
"""
Production Generator Script for Karan Maurya's Animated GitHub Profile SVGs.
Highlighting:
  - Frontend Developer (React / Next.js)
  - Mobile App Developer (React Native)
Creates:
  - assets/hero.svg
  - assets/about-life.svg
  - assets/stack.svg
  - assets/id-dashboard.svg
  - assets/connect.svg
"""

import base64
import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"
FONTS_DIR = BASE_DIR / "fonts"

ASSETS_DIR.mkdir(exist_ok=True)

# 1. Load Fonts
with open(FONTS_DIR / "Outfit-Bold.woff2", "rb") as f:
    outfit_b64 = base64.b64encode(f.read()).decode("ascii")

with open(FONTS_DIR / "JetBrainsMono-Medium.woff2", "rb") as f:
    jb_b64 = base64.b64encode(f.read()).decode("ascii")

# 2. Load Images (exact preservation)
with open(ASSETS_DIR / "id.png", "rb") as f:
    id_png_b64 = base64.b64encode(f.read()).decode("ascii")

with open(ASSETS_DIR / "right_pointing.png", "rb") as f:
    pointing_png_b64 = base64.b64encode(f.read()).decode("ascii")

# 3. Load Icons
with open(BASE_DIR / "icons.json", "r") as f:
    ICONS = json.load(f)

def get_font_css(ns):
    return f"""
    @font-face {{
      font-family: 'Outfit';
      font-style: normal;
      font-weight: 700 800;
      src: url('data:font/woff2;base64,{outfit_b64}') format('woff2');
    }}
    @font-face {{
      font-family: 'JetBrains Mono';
      font-style: normal;
      font-weight: 500 700;
      src: url('data:font/woff2;base64,{jb_b64}') format('woff2');
    }}
    .{ns}-display {{
      font-family: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }}
    .{ns}-mono {{
      font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
    }}
    @media (prefers-reduced-motion: reduce) {{
      *, *::before, *::after {{
        animation: none !important;
        transition: none !important;
      }}
    }}
    """

# ==============================================================================
# 1. HERO SVG
# ==============================================================================
def build_hero_svg():
    ns = "hero"
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 900 410" width="100%" height="100%">
  <defs>
    <style>
      {get_font_css(ns)}
      .{ns}-bg {{ fill: #070b16; }}
      .{ns}-text-primary {{ fill: #f8fafc; }}
      .{ns}-text-secondary {{ fill: #94a3b8; }}
      .{ns}-text-muted {{ fill: #64748b; }}
      .{ns}-accent-blue {{ fill: #247bff; }}
      .{ns}-accent-crimson {{ fill: #ff354f; }}
      
      /* Terminal Cursor */
      @keyframes {ns}-blink {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0; }}
      }}
      .{ns}-cursor {{
        animation: {ns}-blink 1s steps(2, start) infinite;
      }}
      
      /* Rising Mask Reveal */
      @keyframes {ns}-rise {{
        0% {{ transform: translateY(45px); opacity: 0.2; }}
        100% {{ transform: translateY(0); opacity: 1; }}
      }}
      .{ns}-name-anim {{
        animation: {ns}-rise 0.9s cubic-bezier(0.16, 1, 0.3, 1) both;
      }}
      
      /* Cycling Roles: Focused on Frontend (React) and Mobile (React Native) */
      @keyframes {ns}-cycle-1 {{
        0%, 22% {{ opacity: 1; transform: translateY(0); }}
        25%, 97% {{ opacity: 0; transform: translateY(-8px); }}
        100% {{ opacity: 1; transform: translateY(0); }}
      }}
      @keyframes {ns}-cycle-2 {{
        0%, 22% {{ opacity: 0; transform: translateY(8px); }}
        25%, 47% {{ opacity: 1; transform: translateY(0); }}
        50%, 100% {{ opacity: 0; transform: translateY(-8px); }}
      }}
      @keyframes {ns}-cycle-3 {{
        0%, 47% {{ opacity: 0; transform: translateY(8px); }}
        50%, 72% {{ opacity: 1; transform: translateY(0); }}
        75%, 100% {{ opacity: 0; transform: translateY(-8px); }}
      }}
      @keyframes {ns}-cycle-4 {{
        0%, 72% {{ opacity: 0; transform: translateY(8px); }}
        75%, 97% {{ opacity: 1; transform: translateY(0); }}
        100% {{ opacity: 0; transform: translateY(-8px); }}
      }}
      .{ns}-role-1 {{ animation: {ns}-cycle-1 12s infinite; }}
      .{ns}-role-2 {{ animation: {ns}-cycle-2 12s infinite; }}
      .{ns}-role-3 {{ animation: {ns}-cycle-3 12s infinite; }}
      .{ns}-role-4 {{ animation: {ns}-cycle-4 12s infinite; }}

      /* Status Dot Pulse */
      @keyframes {ns}-pulse {{
        0%, 100% {{ opacity: 1; transform: scale(1); }}
        50% {{ opacity: 0.4; transform: scale(0.85); }}
      }}
      .{ns}-dot-pulse {{
        animation: {ns}-pulse 2s ease-in-out infinite;
        transform-origin: 478px 342px;
      }}
    </style>

    <pattern id="{ns}-dots" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#247bff" fill-opacity="0.10" />
    </pattern>

    <linearGradient id="{ns}-border-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.6"/>
      <stop offset="50%" stop-color="#ff354f" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0.2"/>
    </linearGradient>

    <linearGradient id="{ns}-card-grad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#111b33" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#090f1d" stop-opacity="0.98"/>
    </linearGradient>

    <linearGradient id="{ns}-name-grad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="60%" stop-color="#e2e8f0"/>
      <stop offset="100%" stop-color="#60a5fa"/>
    </linearGradient>

    <filter id="{ns}-blur" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="30"/>
    </filter>

    <clipPath id="{ns}-name-clip">
      <rect x="40" y="72" width="560" height="75"/>
    </clipPath>

    <clipPath id="{ns}-portrait-clip">
      <rect x="635" y="42" width="225" height="295" rx="16"/>
    </clipPath>
  </defs>

  <!-- Canvas Background -->
  <rect width="900" height="410" fill="#070b16" rx="20"/>
  <rect width="900" height="410" fill="url(#{ns}-dots)" rx="20"/>
  <rect x="1" y="1" width="898" height="408" rx="19" fill="none" stroke="url(#{ns}-border-grad)" stroke-width="1.2"/>

  <!-- Ambient Glows -->
  <circle cx="160" cy="110" r="140" fill="#247bff" opacity="0.14" filter="url(#{ns}-blur)"/>
  <circle cx="750" cy="200" r="130" fill="#ff354f" opacity="0.10" filter="url(#{ns}-blur)"/>

  <!-- ================= LEFT COLUMN ================= -->
  <!-- 1. Typed Greeting Terminal Pill -->
  <g id="{ns}-greeting-pill" transform="translate(45, 42)">
    <rect width="320" height="28" rx="7" fill="#0d1527" stroke="#247bff" stroke-width="1" stroke-opacity="0.35"/>
    <circle cx="14" cy="14" r="3.5" fill="#ff354f"/>
    <circle cx="26" cy="14" r="3.5" fill="#f59e0b"/>
    <circle cx="38" cy="14" r="3.5" fill="#10b981"/>
    <text x="54" y="18.5" class="{ns}-mono" font-size="11" font-weight="500" fill="#93c5fd">&gt; const dev = &quot;React &amp; Mobile Engineer&quot;;</text>
    <rect x="295" y="7" width="6" height="14" rx="1" fill="#247bff" class="{ns}-cursor"/>
  </g>

  <!-- 2. Large Rising-Mask Name Reveal -->
  <g clip-path="url(#{ns}-name-clip)">
    <g class="{ns}-name-anim">
      <animateTransform attributeName="transform" type="translate" from="0 45" to="0 0" dur="0.9s" begin="0s" fill="freeze" keySplines="0.16 1 0.3 1" calcMode="spline"/>
      <animate attributeName="opacity" from="0.2" to="1" dur="0.7s" begin="0s" fill="freeze"/>
      <text x="45" y="130" class="{ns}-display" font-size="48" font-weight="800" fill="url(#{ns}-name-grad)" letter-spacing="1">KARAN <tspan fill="#247bff">MAURYA</tspan></text>
    </g>
  </g>

  <!-- 3. Four Cycling Roles (Frontend & Mobile Prominently Positioned) -->
  <g id="{ns}-roles-bar" transform="translate(45, 154)">
    <rect width="475" height="36" rx="8" fill="#0d1527" stroke="#247bff" stroke-width="1" stroke-opacity="0.3"/>
    
    <!-- Role Prefix Badge -->
    <rect x="6" y="5" width="84" height="26" rx="5" fill="#247bff" fill-opacity="0.18"/>
    <text x="14" y="22" class="{ns}-mono" font-size="10.5" font-weight="700" fill="#60a5fa">⚡ SPECIALTY</text>
    
    <!-- Cycling Roles Group -->
    <g transform="translate(104, 6)">
      <!-- Role 1: Frontend Developer (React / Next.js) -->
      <g class="{ns}-role-1" opacity="1">
        <text x="0" y="18" class="{ns}-display" font-size="15" font-weight="700" fill="#f8fafc">React / Next.js Frontend Developer</text>
      </g>
      <!-- Role 2: Mobile App Developer (React Native) -->
      <g class="{ns}-role-2" opacity="0">
        <text x="0" y="18" class="{ns}-display" font-size="15" font-weight="700" fill="#38bdf8">React Native Mobile App Developer</text>
      </g>
      <!-- Role 3: Full Stack & Component Architect -->
      <g class="{ns}-role-3" opacity="0">
        <text x="0" y="18" class="{ns}-display" font-size="15" font-weight="700" fill="#a78bfa">Full Stack Component Architect</text>
      </g>
      <!-- Role 4: Odoo ERP & Modern API Integrations -->
      <g class="{ns}-role-4" opacity="0">
        <text x="0" y="18" class="{ns}-display" font-size="15" font-weight="700" fill="#ff354f">Odoo ERP &amp; REST API Integrations</text>
      </g>
    </g>
  </g>

  <!-- 4. One-Line Pitch Focused on React & React Native -->
  <g transform="translate(45, 222)">
    <text class="{ns}-display" font-size="14.5" font-weight="400" fill="#cbd5e1">
      <tspan x="0" dy="0">Frontend &amp; Mobile Developer with 4+ years building high-performance web apps</tspan>
      <tspan x="0" dy="23">using React TS &amp; Next.js, and cross-platform mobile apps using React Native.</tspan>
    </text>
  </g>

  <!-- 5. Location / Company / Status Row -->
  <g id="{ns}-meta-row" transform="translate(45, 325)">
    <!-- Location Pill -->
    <g transform="translate(0, 0)">
      <rect width="180" height="34" rx="8" fill="#0d1527" stroke="#1e293b" stroke-width="1"/>
      <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z" transform="translate(10, 8) scale(0.7)" fill="#ff354f"/>
      <text x="32" y="21" class="{ns}-mono" font-size="11" font-weight="500" fill="#cbd5e1">Lucknow, UP, India</text>
    </g>

    <!-- Company Pill -->
    <g transform="translate(190, 0)">
      <rect width="215" height="34" rx="8" fill="#0d1527" stroke="#1e293b" stroke-width="1"/>
      <path d="M4 21V3h16v18h-4v-4h-8v4H4zm2-6h2v-2H6v2zm0-4h2V9H6v2zm0-4h2V5H6v2zm4 8h2v-2h-2v2zm0-4h2V9h-2v2zm0-4h2V5h-2v2zm4 8h2v-2h-2v2zm0-4h2V9h-2v2zm0-4h2V5h-2v2z" transform="translate(10, 8) scale(0.7)" fill="#38bdf8"/>
      <text x="32" y="21" class="{ns}-mono" font-size="11" font-weight="500" fill="#cbd5e1">Right Brain Infotech LLP</text>
    </g>

    <!-- Status Indicator Pill -->
    <g transform="translate(415, 0)">
      <rect width="155" height="34" rx="8" fill="#0d1527" stroke="#247bff" stroke-width="1" stroke-opacity="0.4"/>
      <circle cx="18" cy="17" r="4.5" fill="#10b981" class="{ns}-dot-pulse"/>
      <text x="31" y="21" class="{ns}-mono" font-size="11" font-weight="600" fill="#34d399">Open to Projects</text>
    </g>
  </g>

  <!-- ================= RIGHT COLUMN: PORTRAIT ================= -->
  <g id="{ns}-portrait-card">
    <rect x="635" y="42" width="225" height="295" rx="16" fill="url(#{ns}-card-grad)"/>
    
    <g clip-path="url(#{ns}-portrait-clip)">
      <image href="data:image/png;base64,{id_png_b64}" x="635" y="42" width="225" height="295" preserveAspectRatio="xMidYMid slice"/>
    </g>

    <rect x="635" y="42" width="225" height="295" rx="16" fill="none" stroke="url(#{ns}-border-grad)" stroke-width="1.5"/>

    <!-- Floating Badge: Top-Right -->
    <g transform="translate(735, 52)">
      <rect width="115" height="26" rx="6" fill="#070b16" fill-opacity="0.9" stroke="#247bff" stroke-width="1"/>
      <text x="57" y="17" text-anchor="middle" class="{ns}-mono" font-size="10.5" font-weight="700" fill="#60a5fa">★ 4+ YRS EXP</text>
    </g>

    <!-- Floating Chip: Bottom (Prominently React & React Native) -->
    <g transform="translate(642, 302)">
      <rect width="210" height="26" rx="6" fill="#070b16" fill-opacity="0.92" stroke="#247bff" stroke-width="1.2"/>
      <text x="105" y="17" text-anchor="middle" class="{ns}-mono" font-size="10" font-weight="700" fill="#61dafb">REACT • REACT NATIVE</text>
    </g>
  </g>
</svg>"""
    return svg

# ==============================================================================
# 2. ABOUT-LIFE SVG
# ==============================================================================
def build_about_life_svg():
    ns = "about"
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 900 420" width="100%" height="100%">
  <defs>
    <style>
      {get_font_css(ns)}
      .{ns}-bg {{ fill: #070b16; }}
      .{ns}-card {{ fill: #0d1527; }}
      .{ns}-text-primary {{ fill: #f8fafc; }}
      .{ns}-text-secondary {{ fill: #94a3b8; }}
      .{ns}-text-muted {{ fill: #64748b; }}
      
      /* Progress Bar Animations: 12s total (4s each) */
      @keyframes {ns}-prog-1 {{
        0% {{ width: 0px; }}
        33.33% {{ width: 105px; }}
        100% {{ width: 105px; }}
      }}
      @keyframes {ns}-prog-2 {{
        0%, 33.33% {{ width: 0px; }}
        66.66% {{ width: 105px; }}
        100% {{ width: 105px; }}
      }}
      @keyframes {ns}-prog-3 {{
        0%, 66.66% {{ width: 0px; }}
        100% {{ width: 105px; }}
      }}
      .{ns}-bar-1 {{ animation: {ns}-prog-1 12s linear infinite; }}
      .{ns}-bar-2 {{ animation: {ns}-prog-2 12s linear infinite; }}
      .{ns}-bar-3 {{ animation: {ns}-prog-3 12s linear infinite; }}

      /* Slide Visibility: 0-4s (Slide 1), 4-8s (Slide 2), 8-12s (Slide 3) */
      @keyframes {ns}-slide-1 {{
        0%, 28% {{ opacity: 1; transform: translateX(0); }}
        33.33%, 95% {{ opacity: 0; transform: translateX(-10px); }}
        98%, 100% {{ opacity: 1; transform: translateX(0); }}
      }}
      @keyframes {ns}-slide-2 {{
        0%, 28% {{ opacity: 0; transform: translateX(10px); }}
        33.33%, 61% {{ opacity: 1; transform: translateX(0); }}
        66.66%, 100% {{ opacity: 0; transform: translateX(-10px); }}
      }}
      @keyframes {ns}-slide-3 {{
        0%, 61% {{ opacity: 0; transform: translateX(10px); }}
        66.66%, 95% {{ opacity: 1; transform: translateX(0); }}
        100% {{ opacity: 0; transform: translateX(-10px); }}
      }}
      .{ns}-slide-item-1 {{ animation: {ns}-slide-1 12s infinite; }}
      .{ns}-slide-item-2 {{ animation: {ns}-slide-2 12s infinite; }}
      .{ns}-slide-item-3 {{ animation: {ns}-slide-3 12s infinite; }}
    </style>

    <pattern id="{ns}-dots" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#247bff" fill-opacity="0.10" />
    </pattern>

    <linearGradient id="{ns}-border-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.5"/>
      <stop offset="50%" stop-color="#ff354f" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0.2"/>
    </linearGradient>
  </defs>

  <!-- Background -->
  <rect width="900" height="420" fill="#070b16" rx="20"/>
  <rect width="900" height="420" fill="url(#{ns}-dots)" rx="20"/>
  <rect x="1" y="1" width="898" height="418" rx="19" fill="none" stroke="url(#{ns}-border-grad)" stroke-width="1.2"/>

  <!-- Section Title -->
  <g transform="translate(45, 45)">
    <text class="{ns}-display" font-size="22" font-weight="800" fill="#f8fafc">CAPABILITIES &amp; PURSUITS <tspan fill="#247bff">// FRONTEND &amp; MOBILE</tspan></text>
    <text x="0" y="22" class="{ns}-mono" font-size="11.5" fill="#94a3b8">React TS frontend excellence, cross-platform mobile &amp; genuine interests</text>
  </g>

  <!-- ================= LEFT COLUMN: CAPABILITIES ================= -->
  <g id="{ns}-capabilities-card" transform="translate(45, 88)">
    <rect width="385" height="295" rx="14" fill="#0d1527" stroke="#247bff" stroke-width="1" stroke-opacity="0.3"/>
    
    <!-- Header -->
    <g transform="translate(20, 24)">
      <text class="{ns}-mono" font-size="11" font-weight="700" fill="#38bdf8" letter-spacing="1">CORE ENGINEERING DOMAINS</text>
      <rect x="250" y="-12" width="95" height="20" rx="5" fill="#247bff" fill-opacity="0.15"/>
      <text x="297" y="1" text-anchor="middle" class="{ns}-mono" font-size="9.5" font-weight="700" fill="#60a5fa">4+ YRS EXP</text>
    </g>

    <!-- Capability 1: React & Next.js Frontend -->
    <g transform="translate(20, 52)">
      <circle cx="6" cy="10" r="4" fill="#61dafb"/>
      <text x="18" y="14" class="{ns}-display" font-size="14" font-weight="700" fill="#f8fafc">React TS &amp; Next.js Frontend Architecture</text>
      <text x="18" y="29" class="{ns}-mono" font-size="10.5" fill="#94a3b8">Reusable UI Components • SSR/SSG • SEO • Lighthouse 95+</text>
    </g>

    <!-- Capability 2: React Native Mobile Development -->
    <g transform="translate(20, 108)">
      <circle cx="6" cy="10" r="4" fill="#38bdf8"/>
      <text x="18" y="14" class="{ns}-display" font-size="14" font-weight="700" fill="#f8fafc">React Native Cross-Platform Mobile Apps</text>
      <text x="18" y="29" class="{ns}-mono" font-size="10.5" fill="#94a3b8">iOS &amp; Android Apps • Native Bridges • Capacitor &amp; Cordova</text>
    </g>

    <!-- Capability 3: Full Stack REST API & Integration -->
    <g transform="translate(20, 164)">
      <circle cx="6" cy="10" r="4" fill="#ff354f"/>
      <text x="18" y="14" class="{ns}-display" font-size="14" font-weight="700" fill="#f8fafc">REST API Integrations &amp; State Management</text>
      <text x="18" y="29" class="{ns}-mono" font-size="10.5" fill="#94a3b8">Odoo ERP Backend APIs • Node.js • Java Spring • Medusa</text>
    </g>

    <!-- Capability 4: Modern Web Standards & AI-Assisted Dev -->
    <g transform="translate(20, 220)">
      <circle cx="6" cy="10" r="4" fill="#a78bfa"/>
      <text x="18" y="14" class="{ns}-display" font-size="14" font-weight="700" fill="#f8fafc">Performance Optimization &amp; AI Workflows</text>
      <text x="18" y="29" class="{ns}-mono" font-size="10.5" fill="#94a3b8">TypeScript • Prompt Engineering • Docker • Vercel CI/CD</text>
    </g>
  </g>

  <!-- ================= RIGHT COLUMN: INTERESTS CAROUSEL ================= -->
  <g id="{ns}-carousel-card" transform="translate(450, 88)">
    <rect width="405" height="295" rx="14" fill="#0d1527" stroke="#ff354f" stroke-width="1" stroke-opacity="0.3"/>

    <!-- Header & Segment Progress Bars -->
    <g transform="translate(25, 24)">
      <text x="0" y="10" class="{ns}-mono" font-size="11" font-weight="700" fill="#ff354f" letter-spacing="1">INTERESTS CAROUSEL</text>
      <text x="355" y="10" text-anchor="end" class="{ns}-mono" font-size="10.5" font-weight="600" fill="#94a3b8">4s / SLIDE</text>

      <!-- 3 Progress Segments -->
      <g transform="translate(0, 24)">
        <rect x="0" y="0" width="105" height="4" rx="2" fill="#1e293b"/>
        <rect x="0" y="0" width="105" height="4" rx="2" fill="#247bff" class="{ns}-bar-1"/>
        
        <rect x="125" y="0" width="105" height="4" rx="2" fill="#1e293b"/>
        <rect x="125" y="0" width="105" height="4" rx="2" fill="#ff354f" class="{ns}-bar-2"/>
        
        <rect x="250" y="0" width="105" height="4" rx="2" fill="#1e293b"/>
        <rect x="250" y="0" width="105" height="4" rx="2" fill="#38bdf8" class="{ns}-bar-3"/>
      </g>
    </g>

    <!-- Slide 1: UI/UX Prototyping (Fallback: visible) -->
    <g transform="translate(25, 76)">
      <g id="{ns}-slide-1" class="{ns}-slide-item-1" opacity="1">
        <rect x="0" y="0" width="135" height="20" rx="4" fill="#247bff" fill-opacity="0.18"/>
        <text x="67.5" y="14" text-anchor="middle" class="{ns}-mono" font-size="9.5" font-weight="700" fill="#60a5fa">01 / 03 • PROTOTYPING</text>
        
        <text x="0" y="44" class="{ns}-display" font-size="20" font-weight="800" fill="#f8fafc">UI/UX Prototyping</text>
        <text x="0" y="64" class="{ns}-mono" font-size="11.5" font-weight="600" fill="#38bdf8">Design Systems &amp; Motion Architecture</text>
        
        <text class="{ns}-display" font-size="13" font-weight="400" fill="#94a3b8">
          <tspan x="0" y="92">Transforming complex product flows into intuitive, polished</tspan>
          <tspan x="0" y="112">digital experiences with responsive layouts and micro-interactions.</tspan>
        </text>

        <!-- Tags -->
        <g transform="translate(0, 150)">
          <rect x="0" y="0" width="60" height="22" rx="4" fill="#1e293b"/>
          <text x="30" y="15" text-anchor="middle" class="{ns}-mono" font-size="10" fill="#cbd5e1">Figma</text>

          <rect x="68" y="0" width="105" height="22" rx="4" fill="#1e293b"/>
          <text x="120.5" y="15" text-anchor="middle" class="{ns}-mono" font-size="10" fill="#cbd5e1">Design Systems</text>

          <rect x="181" y="0" width="80" height="22" rx="4" fill="#1e293b"/>
          <text x="221" y="15" text-anchor="middle" class="{ns}-mono" font-size="10" fill="#cbd5e1">Motion UX</text>

          <rect x="269" y="0" width="85" height="22" rx="4" fill="#1e293b"/>
          <text x="311.5" y="15" text-anchor="middle" class="{ns}-mono" font-size="10" fill="#cbd5e1">Wireframing</text>
        </g>
      </g>
    </g>

    <!-- Slide 2: Coffee Brewing & Cafe Hopping -->
    <g transform="translate(25, 76)">
      <g id="{ns}-slide-2" class="{ns}-slide-item-2" opacity="0">
        <rect x="0" y="0" width="135" height="20" rx="4" fill="#ff354f" fill-opacity="0.18"/>
        <text x="67.5" y="14" text-anchor="middle" class="{ns}-mono" font-size="9.5" font-weight="700" fill="#fb7185">02 / 03 • RITUAL</text>
        
        <text x="0" y="44" class="{ns}-display" font-size="20" font-weight="800" fill="#f8fafc">Coffee Brewing &amp; Cafe Hopping</text>
        <text x="0" y="64" class="{ns}-mono" font-size="11.5" font-weight="600" fill="#ff354f">Artisanal Roasts &amp; Creative Spaces</text>
        
        <text class="{ns}-display" font-size="13" font-weight="400" fill="#94a3b8">
          <tspan x="0" y="92">Dialing in manual pour-overs and discovering inspiring local cafe</tspan>
          <tspan x="0" y="112">spaces to architect complex software systems and brainstorm.</tspan>
        </text>

        <!-- Tags -->
        <g transform="translate(0, 150)">
          <rect x="0" y="0" width="85" height="22" rx="4" fill="#1e293b"/>
          <text x="42.5" y="15" text-anchor="middle" class="{ns}-mono" font-size="10" fill="#cbd5e1">Pour-Over</text>

          <rect x="93" y="0" width="100" height="22" rx="4" fill="#1e293b"/>
          <text x="143" y="15" text-anchor="middle" class="{ns}-mono" font-size="10" fill="#cbd5e1">Specialty Coffee</text>

          <rect x="201" y="0" width="80" height="22" rx="4" fill="#1e293b"/>
          <text x="241" y="15" text-anchor="middle" class="{ns}-mono" font-size="10" fill="#cbd5e1">Deep Focus</text>

          <rect x="289" y="0" width="65" height="22" rx="4" fill="#1e293b"/>
          <text x="321.5" y="15" text-anchor="middle" class="{ns}-mono" font-size="10" fill="#cbd5e1">Cafes</text>
        </g>
      </g>
    </g>

    <!-- Slide 3: Reading Tech Blogs -->
    <g transform="translate(25, 76)">
      <g id="{ns}-slide-3" class="{ns}-slide-item-3" opacity="0">
        <rect x="0" y="0" width="135" height="20" rx="4" fill="#38bdf8" fill-opacity="0.18"/>
        <text x="67.5" y="14" text-anchor="middle" class="{ns}-mono" font-size="9.5" font-weight="700" fill="#38bdf8">03 / 03 • MASTERY</text>
        
        <text x="0" y="44" class="{ns}-display" font-size="20" font-weight="800" fill="#f8fafc">Reading Tech Blogs</text>
        <text x="0" y="64" class="{ns}-mono" font-size="11.5" font-weight="600" fill="#38bdf8">Engineering Teardowns &amp; Systems Digests</text>
        
        <text class="{ns}-display" font-size="13" font-weight="400" fill="#94a3b8">
          <tspan x="0" y="92">Exploring architectural RFCs, web platform internals, high-scale</tspan>
          <tspan x="0" y="112">system design case studies, and modern open-source patterns.</tspan>
        </text>

        <!-- Tags -->
        <g transform="translate(0, 150)">
          <rect x="0" y="0" width="95" height="22" rx="4" fill="#1e293b"/>
          <text x="47.5" y="15" text-anchor="middle" class="{ns}-mono" font-size="10" fill="#cbd5e1">System Design</text>

          <rect x="103" y="0" width="100" height="22" rx="4" fill="#1e293b"/>
          <text x="153" y="15" text-anchor="middle" class="{ns}-mono" font-size="10" fill="#cbd5e1">Tech Digests</text>

          <rect x="211" y="0" width="70" height="22" rx="4" fill="#1e293b"/>
          <text x="246" y="15" text-anchor="middle" class="{ns}-mono" font-size="10" fill="#cbd5e1">RFCs</text>

          <rect x="289" y="0" width="65" height="22" rx="4" fill="#1e293b"/>
          <text x="321.5" y="15" text-anchor="middle" class="{ns}-mono" font-size="10" fill="#cbd5e1">Modern Web</text>
        </g>
      </g>
    </g>
  </g>
</svg>"""
    return svg

# ==============================================================================
# 3. STACK SVG
# ==============================================================================
def build_stack_svg():
    ns = "stack"
    
    def render_chip(icon_name, label, x, y, fill_color="#38bdf8", width=175):
        path_d = ICONS.get(icon_name, "")
        if not path_d:
            path_d = "M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"
        return f"""
        <g transform="translate({x}, {y})">
          <rect width="{width}" height="28" rx="6" fill="#0d1527" stroke="#1e293b" stroke-width="1"/>
          <g transform="translate(8, 6) scale(0.65)" fill="{fill_color}">
            <path d="{path_d}"/>
          </g>
          <text x="32" y="18" class="{ns}-mono" font-size="10.5" font-weight="600" fill="#cbd5e1">{label}</text>
        </g>
        """

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 900 500" width="100%" height="100%">
  <defs>
    <style>
      {get_font_css(ns)}
      .{ns}-bg {{ fill: #070b16; }}
      .{ns}-card {{ fill: #0d1527; }}
      .{ns}-text-primary {{ fill: #f8fafc; }}
      .{ns}-text-secondary {{ fill: #94a3b8; }}
      
      /* Orbit Pulse Animations */
      @keyframes {ns}-orbit-pulse-1 {{
        0%, 100% {{ stroke-dashoffset: 0; }}
        50% {{ stroke-dashoffset: 24; }}
      }}
      @keyframes {ns}-orbit-pulse-2 {{
        0%, 100% {{ stroke-dashoffset: 0; }}
        50% {{ stroke-dashoffset: -32; }}
      }}
      @keyframes {ns}-orbit-pulse-3 {{
        0%, 100% {{ stroke-dashoffset: 0; }}
        50% {{ stroke-dashoffset: 40; }}
      }}
      .{ns}-orbit-line-1 {{ animation: {ns}-orbit-pulse-1 14s linear infinite; }}
      .{ns}-orbit-line-2 {{ animation: {ns}-orbit-pulse-2 20s linear infinite; }}
      .{ns}-orbit-line-3 {{ animation: {ns}-orbit-pulse-3 26s linear infinite; }}

      /* Core Glow */
      @keyframes {ns}-core-glow {{
        0%, 100% {{ transform: scale(1); opacity: 0.8; }}
        50% {{ transform: scale(1.08); opacity: 1; }}
      }}
      .{ns}-core-pulse {{
        animation: {ns}-core-glow 3s ease-in-out infinite;
        transform-origin: 450px 145px;
      }}
    </style>

    <pattern id="{ns}-dots" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#247bff" fill-opacity="0.10" />
    </pattern>

    <linearGradient id="{ns}-border-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.5"/>
      <stop offset="50%" stop-color="#ff354f" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0.2"/>
    </linearGradient>

    <linearGradient id="{ns}-core-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#247bff"/>
      <stop offset="100%" stop-color="#61dafb"/>
    </linearGradient>

    <filter id="{ns}-glow-filter" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="900" height="500" fill="#070b16" rx="20"/>
  <rect width="900" height="500" fill="url(#{ns}-dots)" rx="20"/>
  <rect x="1" y="1" width="898" height="498" rx="19" fill="none" stroke="url(#{ns}-border-grad)" stroke-width="1.2"/>

  <!-- Title Focused on React & Mobile -->
  <g transform="translate(45, 40)">
    <text class="{ns}-display" font-size="22" font-weight="800" fill="#f8fafc">TECH STACK &amp; ORBITAL GALAXY <tspan fill="#247bff">// REACT &amp; MOBILE CORE</tspan></text>
    <text x="0" y="20" class="{ns}-mono" font-size="11.5" fill="#94a3b8">Interactive gravitational core highlighting React, Next.js &amp; React Native</text>
  </g>

  <!-- ================= THREE TILTED ELLIPTICAL ORBITS ================= -->
  <g id="{ns}-orbital-system" transform="translate(0, 10)">
    <!-- Orbit 3: Outer (Cloud, DevOps & ERP Backend) -->
    <ellipse cx="450" cy="145" rx="390" ry="78" fill="none" stroke="#247bff" stroke-width="1.2" stroke-opacity="0.2" stroke-dasharray="6,8" transform="rotate(-8 450 145)" class="{ns}-orbit-line-3"/>
    
    <!-- Orbit 2: Middle (Mobile, Language & Ecosystem) -->
    <ellipse cx="450" cy="145" rx="275" ry="58" fill="none" stroke="#ff354f" stroke-width="1.2" stroke-opacity="0.25" stroke-dasharray="5,7" transform="rotate(14 450 145)" class="{ns}-orbit-line-2"/>
    
    <!-- Orbit 1: Inner (Primary React & React Native Trinity) -->
    <ellipse cx="450" cy="145" rx="165" ry="40" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-opacity="0.5" stroke-dasharray="4,6" transform="rotate(-12 450 145)" class="{ns}-orbit-line-1"/>

    <!-- Center Core: React / Mobile Hub -->
    <g class="{ns}-core-pulse">
      <circle cx="450" cy="145" r="30" fill="url(#{ns}-core-grad)" filter="url(#{ns}-glow-filter)" opacity="0.9"/>
      <circle cx="450" cy="145" r="18" fill="#070b16"/>
      <path d="{ICONS['react']}" transform="translate(439, 134) scale(0.9)" fill="#61dafb"/>
    </g>

    <!-- Orbit 1 Satellites (Inner Core: React, React Native, Next.js, TypeScript) -->
    <!-- React (Top Left) -->
    <g transform="translate(295, 112)">
      <rect width="78" height="24" rx="12" fill="#0d1527" stroke="#61dafb" stroke-width="1.2"/>
      <path d="{ICONS['react']}" transform="translate(7, 5) scale(0.65)" fill="#61dafb"/>
      <text x="26" y="16" class="{ns}-mono" font-size="10" font-weight="700" fill="#f8fafc">React TS</text>
    </g>

    <!-- Next.js (Top Right) -->
    <g transform="translate(520, 112)">
      <rect width="80" height="24" rx="12" fill="#0d1527" stroke="#ffffff" stroke-width="1.2"/>
      <path d="{ICONS['nextdotjs']}" transform="translate(7, 5) scale(0.65)" fill="#ffffff"/>
      <text x="26" y="16" class="{ns}-mono" font-size="10" font-weight="700" fill="#f8fafc">Next.js</text>
    </g>

    <!-- React Native (Bottom Left) -->
    <g transform="translate(280, 165)">
      <rect width="112" height="24" rx="12" fill="#0d1527" stroke="#38bdf8" stroke-width="1.2"/>
      <path d="{ICONS['react']}" transform="translate(7, 5) scale(0.65)" fill="#38bdf8"/>
      <text x="26" y="16" class="{ns}-mono" font-size="10" font-weight="700" fill="#38bdf8">React Native</text>
    </g>

    <!-- TypeScript (Bottom Right) -->
    <g transform="translate(525, 165)">
      <rect width="98" height="24" rx="12" fill="#0d1527" stroke="#3178c6" stroke-width="1.2"/>
      <path d="{ICONS['typescript']}" transform="translate(7, 5) scale(0.65)" fill="#3178c6"/>
      <text x="26" y="16" class="{ns}-mono" font-size="10" font-weight="700" fill="#f8fafc">TypeScript</text>
    </g>

    <!-- Orbit 2 Satellites (Middle: JavaScript ES6+, Flutter, Ionic, Node.js) -->
    <!-- JavaScript (Far Left) -->
    <g transform="translate(170, 102)">
      <rect width="90" height="22" rx="11" fill="#0d1527" stroke="#f7df1e" stroke-width="1"/>
      <path d="{ICONS['javascript']}" transform="translate(6, 4) scale(0.6)" fill="#f7df1e"/>
      <text x="24" y="15" class="{ns}-mono" font-size="9.5" font-weight="700" fill="#f8fafc">JavaScript</text>
    </g>

    <!-- Flutter / Mobile (Far Right) -->
    <g transform="translate(635, 102)">
      <rect width="78" height="22" rx="11" fill="#0d1527" stroke="#02569b" stroke-width="1"/>
      <path d="{ICONS['flutter']}" transform="translate(6, 4) scale(0.6)" fill="#02569b"/>
      <text x="24" y="15" class="{ns}-mono" font-size="9.5" font-weight="700" fill="#f8fafc">Flutter</text>
    </g>

    <!-- Ionic / Capacitor (Far Right Bottom) -->
    <g transform="translate(640, 180)">
      <rect width="90" height="22" rx="11" fill="#0d1527" stroke="#3880ff" stroke-width="1"/>
      <path d="{ICONS['ionic']}" transform="translate(6, 4) scale(0.6)" fill="#3880ff"/>
      <text x="24" y="15" class="{ns}-mono" font-size="9.5" font-weight="700" fill="#f8fafc">Capacitor</text>
    </g>

    <!-- Node.js (Far Left Bottom) -->
    <g transform="translate(175, 180)">
      <rect width="80" height="22" rx="11" fill="#0d1527" stroke="#5fa04e" stroke-width="1"/>
      <path d="{ICONS['nodedotjs']}" transform="translate(6, 4) scale(0.6)" fill="#5fa04e"/>
      <text x="24" y="15" class="{ns}-mono" font-size="9.5" font-weight="700" fill="#f8fafc">Node.js</text>
    </g>

    <!-- Orbit 3 Satellites (Outer: Odoo ERP, Spring Boot, PostgreSQL, Docker, AWS, Git) -->
    <!-- Odoo ERP (Top Left) -->
    <g transform="translate(65, 85)">
      <rect width="85" height="22" rx="11" fill="#0d1527" stroke="#a24689" stroke-width="1"/>
      <path d="{ICONS['odoo']}" transform="translate(6, 4) scale(0.6)" fill="#a24689"/>
      <text x="24" y="15" class="{ns}-mono" font-size="9.5" font-weight="700" fill="#f8fafc">Odoo ERP</text>
    </g>

    <!-- Spring Boot (Top Right) -->
    <g transform="translate(735, 85)">
      <rect width="95" height="22" rx="11" fill="#0d1527" stroke="#6db33f" stroke-width="1"/>
      <path d="{ICONS['springboot']}" transform="translate(6, 4) scale(0.6)" fill="#6db33f"/>
      <text x="24" y="15" class="{ns}-mono" font-size="9.5" font-weight="700" fill="#f8fafc">Spring Boot</text>
    </g>

    <!-- Docker (Bottom Right) -->
    <g transform="translate(755, 195)">
      <rect width="75" height="22" rx="11" fill="#0d1527" stroke="#2496ed" stroke-width="1"/>
      <path d="{ICONS['docker']}" transform="translate(6, 4) scale(0.6)" fill="#2496ed"/>
      <text x="24" y="15" class="{ns}-mono" font-size="9.5" font-weight="700" fill="#f8fafc">Docker</text>
    </g>

    <!-- PostgreSQL / Git (Bottom Left) -->
    <g transform="translate(50, 195)">
      <rect width="102" height="22" rx="11" fill="#0d1527" stroke="#4169e1" stroke-width="1"/>
      <path d="{ICONS['postgresql']}" transform="translate(6, 4) scale(0.6)" fill="#4169e1"/>
      <text x="24" y="15" class="{ns}-mono" font-size="9.5" font-weight="700" fill="#f8fafc">PostgreSQL</text>
    </g>
  </g>

  <!-- ================= GROUPED STACK CHIPS (PROMINENT FRONTEND & MOBILE) ================= -->
  <g id="{ns}-grouped-chips" transform="translate(45, 275)">
    <!-- Category 1: React & Frontend Excellence -->
    <g transform="translate(0, 0)">
      <rect width="195" height="205" rx="12" fill="#0d1527" stroke="#61dafb" stroke-width="1.2" stroke-opacity="0.5"/>
      <text x="14" y="24" class="{ns}-mono" font-size="11" font-weight="700" fill="#61dafb">REACT &amp; FRONTEND</text>
      {render_chip("react", "React TS / React JS", 10, 36, "#61dafb", 175)}
      {render_chip("nextdotjs", "Next.js (SSR/SSG)", 10, 70, "#ffffff", 175)}
      {render_chip("typescript", "TypeScript / ES6+", 10, 104, "#3178c6", 175)}
      {render_chip("html5", "HTML5 &amp; CSS3 (SEO)", 10, 138, "#e34f26", 175)}
      {render_chip("odoo", "OWL UI Framework", 10, 170, "#a24689", 175)}
    </g>

    <!-- Category 2: React Native & Mobile App Dev -->
    <g transform="translate(210, 0)">
      <rect width="195" height="205" rx="12" fill="#0d1527" stroke="#38bdf8" stroke-width="1.2" stroke-opacity="0.5"/>
      <text x="14" y="24" class="{ns}-mono" font-size="11" font-weight="700" fill="#38bdf8">MOBILE APP DEV</text>
      {render_chip("react", "React Native (iOS/And)", 10, 36, "#38bdf8", 175)}
      {render_chip("flutter", "Flutter Cross-Plat", 10, 70, "#02569b", 175)}
      {render_chip("ionic", "Ionic Mobile", 10, 104, "#3880ff", 175)}
      {render_chip("capacitor", "Capacitor Plugins", 10, 138, "#119eff", 175)}
      {render_chip("ionic", "Apache Cordova", 10, 170, "#e8e8e8", 175)}
    </g>

    <!-- Category 3: Backend APIs & ERP -->
    <g transform="translate(420, 0)">
      <rect width="190" height="205" rx="12" fill="#0d1527" stroke="#ff354f" stroke-width="1" stroke-opacity="0.3"/>
      <text x="14" y="24" class="{ns}-mono" font-size="11" font-weight="700" fill="#ff354f">BACKEND &amp; APIS</text>
      {render_chip("nextdotjs", "REST APIs / JSON", 10, 36, "#38bdf8", 170)}
      {render_chip("nodedotjs", "Node.js / Express", 10, 70, "#5fa04e", 170)}
      {render_chip("openjdk", "Java &amp; Spring Boot", 10, 104, "#e76f00", 170)}
      {render_chip("odoo", "Odoo ERP APIs", 10, 138, "#a24689", 170)}
      {render_chip("python", "Python &amp; PHP", 10, 170, "#3776ab", 170)}
    </g>

    <!-- Category 4: Database & DevOps -->
    <g transform="translate(625, 0)">
      <rect width="185" height="205" rx="12" fill="#0d1527" stroke="#10b981" stroke-width="1" stroke-opacity="0.3"/>
      <text x="14" y="24" class="{ns}-mono" font-size="11" font-weight="700" fill="#34d399">DATABASE &amp; CLOUD</text>
      {render_chip("postgresql", "PostgreSQL / SQL", 10, 36, "#4169e1", 165)}
      {render_chip("docker", "Docker / Compose", 10, 70, "#2496ed", 165)}
      {render_chip("linux", "Linux &amp; Nginx", 10, 104, "#fcc624", 165)}
      {render_chip("aws", "AWS &amp; Vercel CI", 10, 138, "#ff9900", 165)}
      {render_chip("github", "Git, GitHub &amp; Jira", 10, 170, "#f8fafc", 165)}
    </g>
  </g>
</svg>"""
    return svg

# ==============================================================================
# 4. ID-DASHBOARD SVG
# ==============================================================================
def build_id_dashboard_svg():
    ns = "id"
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 900 480" width="100%" height="100%">
  <defs>
    <style>
      {get_font_css(ns)}
      .{ns}-bg {{ fill: #070b16; }}
      .{ns}-card {{ fill: #090f1d; }}
      .{ns}-text-primary {{ fill: #f8fafc; }}
      .{ns}-text-secondary {{ fill: #94a3b8; }}
      
      /* Lanyard Damped Pendulum Physics:
         Drop into place (0s-1.8s), then subtle +/-1.7 degree periodic swing! */
      @keyframes {ns}-drop-and-swing {{
        0% {{ transform: translateY(-50px) rotate(-8deg); }}
        15% {{ transform: translateY(0px) rotate(5deg); }}
        30% {{ transform: rotate(-3deg); }}
        45% {{ transform: rotate(2deg); }}
        60% {{ transform: rotate(-1.7deg); }}
        75% {{ transform: rotate(1.7deg); }}
        88% {{ transform: rotate(-1.7deg); }}
        100% {{ transform: rotate(1.7deg); }}
      }}
      @keyframes {ns}-perpetual-swing {{
        0%, 100% {{ transform: rotate(-1.7deg); }}
        50% {{ transform: rotate(1.7deg); }}
      }}
      .{ns}-assembly {{
        transform-origin: 450px 0px;
        animation: {ns}-drop-and-swing 3.2s cubic-bezier(0.25, 1, 0.5, 1) 1,
                   {ns}-perpetual-swing 3.2s ease-in-out 3.2s infinite;
      }}

      /* Foil Sweep Sheen */
      @keyframes {ns}-foil-anim {{
        0%, 25% {{ transform: translateX(-480px); }}
        55%, 100% {{ transform: translateX(520px); }}
      }}
      .{ns}-foil-layer {{
        animation: {ns}-foil-anim 4.5s ease-in-out infinite;
      }}
    </style>

    <pattern id="{ns}-dots" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#247bff" fill-opacity="0.10" />
    </pattern>

    <linearGradient id="{ns}-border-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.6"/>
      <stop offset="50%" stop-color="#ff354f" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0.3"/>
    </linearGradient>

    <!-- Metal Clasp Gradients -->
    <linearGradient id="{ns}-chrome-grad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#64748b"/>
      <stop offset="25%" stop-color="#cbd5e1"/>
      <stop offset="50%" stop-color="#f8fafc"/>
      <stop offset="75%" stop-color="#94a3b8"/>
      <stop offset="100%" stop-color="#475569"/>
    </linearGradient>

    <!-- Holographic Foil Sheen -->
    <linearGradient id="{ns}-foil-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0"/>
      <stop offset="35%" stop-color="#38bdf8" stop-opacity="0.08"/>
      <stop offset="50%" stop-color="#ff354f" stop-opacity="0.16"/>
      <stop offset="65%" stop-color="#38bdf8" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0"/>
    </linearGradient>

    <!-- Lanyard Fabric Pattern -->
    <linearGradient id="{ns}-strap-grad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#ff354f"/>
      <stop offset="10%" stop-color="#0a1228"/>
      <stop offset="90%" stop-color="#0a1228"/>
      <stop offset="100%" stop-color="#247bff"/>
    </linearGradient>

    <clipPath id="{ns}-card-clip">
      <rect x="220" y="85" width="460" height="375" rx="18"/>
    </clipPath>

    <clipPath id="{ns}-portrait-clip">
      <rect x="245" y="152" width="130" height="152" rx="10"/>
    </clipPath>
  </defs>

  <!-- Background -->
  <rect width="900" height="480" fill="#070b16" rx="20"/>
  <rect width="900" height="480" fill="url(#{ns}-dots)" rx="20"/>
  <rect x="1" y="1" width="898" height="478" rx="19" fill="none" stroke="url(#{ns}-border-grad)" stroke-width="1.2"/>

  <!-- ================= HANGING PENDULUM ASSEMBLY ================= -->
  <g id="{ns}-lanyard-assembly" class="{ns}-assembly">
    <!-- SMIL Fallback for Pendulum Motion -->
    <animateTransform attributeName="transform" type="rotate"
      values="-8 450 0; 5 450 0; -3 450 0; 2 450 0; -1.7 450 0; 1.7 450 0; -1.7 450 0"
      keyTimes="0; 0.15; 0.3; 0.45; 0.6; 0.8; 1"
      dur="3.2s" begin="0s" repeatCount="indefinite"/>

    <!-- 1. Lanyard Straps -->
    <polygon points="380,0 440,48 450,48 400,0" fill="url(#{ns}-strap-grad)"/>
    <polygon points="520,0 460,48 450,48 500,0" fill="url(#{ns}-strap-grad)"/>
    <rect x="442" y="32" width="16" height="18" rx="3" fill="#0d1527" stroke="#247bff" stroke-width="1"/>

    <!-- 2. Metallic Chrome Clasp & Swivel Hook -->
    <g transform="translate(450, 52)">
      <ellipse cx="0" cy="0" rx="9" ry="5" fill="url(#{ns}-chrome-grad)" stroke="#1e293b" stroke-width="0.8"/>
      <path d="M-5 2 L5 2 L7 18 L3 24 L-3 24 L-7 18 Z" fill="url(#{ns}-chrome-grad)"/>
      <ellipse cx="0" cy="12" rx="3" ry="5" fill="#1e293b"/>
      <rect x="-4" y="24" width="8" height="12" rx="2" fill="url(#{ns}-chrome-grad)" stroke="#334155" stroke-width="0.8"/>
      <path d="M-10 32 C-10 28 10 28 10 32 L8 44 C8 45 -8 45 -8 44 Z" fill="url(#{ns}-chrome-grad)" stroke="#1e293b" stroke-width="1"/>
    </g>

    <!-- 3. Frosted Badge Holder Shell -->
    <rect x="215" y="80" width="470" height="385" rx="20" fill="#0d1527" fill-opacity="0.8" stroke="url(#{ns}-border-grad)" stroke-width="1.2"/>
    <rect x="430" y="88" width="40" height="9" rx="4.5" fill="#070b16" stroke="#334155" stroke-width="1"/>

    <!-- 4. Inside ID Badge Card -->
    <g clip-path="url(#{ns}-card-clip)">
      <rect x="220" y="85" width="460" height="375" rx="18" fill="#090f1d"/>
      <rect x="220" y="85" width="460" height="375" rx="18" fill="url(#{ns}-dots)"/>

      <!-- Header Banner -->
      <g transform="translate(245, 115)">
        <rect width="410" height="28" rx="6" fill="#111c38" stroke="#247bff" stroke-width="0.8" stroke-opacity="0.4"/>
        <text x="12" y="18" class="{ns}-mono" font-size="10.5" font-weight="700" fill="#60a5fa" letter-spacing="1">DEV ID // REACT &amp; MOBILE SPECIALIST</text>
        <rect x="315" y="4" width="85" height="20" rx="4" fill="#10b981" fill-opacity="0.18"/>
        <circle cx="325" cy="14" r="3.5" fill="#10b981"/>
        <text x="334" y="17.5" class="{ns}-mono" font-size="9" font-weight="700" fill="#34d399">VERIFIED</text>
      </g>

      <!-- Left Column: Portrait -->
      <g transform="translate(0, 0)">
        <rect x="245" y="152" width="130" height="152" rx="10" fill="#070b16" stroke="#247bff" stroke-width="1.2"/>
        <g clip-path="url(#{ns}-portrait-clip)">
          <image href="data:image/png;base64,{id_png_b64}" x="245" y="152" width="130" height="152" preserveAspectRatio="xMidYMid slice"/>
        </g>
        <rect x="245" y="284" width="130" height="20" rx="4" fill="#070b16" fill-opacity="0.85"/>
        <text x="310" y="297" text-anchor="middle" class="{ns}-mono" font-size="9" font-weight="700" fill="#ff354f">KM-64181191-2020</text>
      </g>

      <!-- Right Column: Verified Dated Metrics (Frontend & Mobile Specialty) -->
      <g transform="translate(390, 160)">
        <text class="{ns}-display" font-size="20" font-weight="800" fill="#f8fafc">KARAN MAURYA</text>
        <text x="0" y="18" class="{ns}-mono" font-size="11.5" font-weight="600" fill="#38bdf8">Frontend &amp; React Native Developer</text>
        <text x="0" y="32" class="{ns}-mono" font-size="10.5" fill="#94a3b8">Right Brain Infotech LLP (May 2022 – Present)</text>

        <!-- Divider Line -->
        <line x1="0" y1="42" x2="265" y2="42" stroke="#1e293b" stroke-width="1"/>

        <!-- Metrics Grid -->
        <g transform="translate(0, 56)">
          <g transform="translate(0, 0)">
            <text class="{ns}-mono" font-size="9" font-weight="600" fill="#64748b">CORE SPECIALTY</text>
            <text x="0" y="16" class="{ns}-display" font-size="13" font-weight="700" fill="#f8fafc">React TS &amp; Mobile</text>
          </g>

          <g transform="translate(140, 0)">
            <text class="{ns}-mono" font-size="9" font-weight="600" fill="#64748b">PUBLIC REPOS</text>
            <text x="0" y="16" class="{ns}-display" font-size="13" font-weight="700" fill="#38bdf8">14 Repositories</text>
          </g>

          <g transform="translate(0, 44)">
            <text class="{ns}-mono" font-size="9" font-weight="600" fill="#64748b">PROFESSIONAL EXP</text>
            <text x="0" y="16" class="{ns}-display" font-size="13" font-weight="700" fill="#ff354f">4+ Years Pro</text>
          </g>

          <g transform="translate(140, 44)">
            <text class="{ns}-mono" font-size="9" font-weight="600" fill="#64748b">MEMBER SINCE</text>
            <text x="0" y="16" class="{ns}-display" font-size="13" font-weight="700" fill="#f8fafc">April 23, 2020</text>
          </g>
        </g>
      </g>

      <!-- Bottom Card Area: Barcode & Hologram -->
      <g transform="translate(245, 322)">
        <g transform="translate(18, 20)">
          <circle cx="0" cy="0" r="18" fill="#111c38" stroke="url(#{ns}-border-grad)" stroke-width="1.5"/>
          <circle cx="0" cy="0" r="12" fill="none" stroke="#38bdf8" stroke-width="1" stroke-dasharray="3,3"/>
          <text x="0" y="4" text-anchor="middle" class="{ns}-mono" font-size="8" font-weight="800" fill="#61dafb">REACT</text>
        </g>

        <!-- Vector Barcode -->
        <g transform="translate(56, 4)">
          <rect x="0" y="0" width="3" height="26" fill="#f8fafc"/>
          <rect x="5" y="0" width="1" height="26" fill="#f8fafc"/>
          <rect x="8" y="0" width="4" height="26" fill="#f8fafc"/>
          <rect x="15" y="0" width="2" height="26" fill="#f8fafc"/>
          <rect x="19" y="0" width="5" height="26" fill="#f8fafc"/>
          <rect x="27" y="0" width="1" height="26" fill="#f8fafc"/>
          <rect x="31" y="0" width="3" height="26" fill="#f8fafc"/>
          <rect x="36" y="0" width="6" height="26" fill="#f8fafc"/>
          <rect x="45" y="0" width="2" height="26" fill="#f8fafc"/>
          <rect x="50" y="0" width="4" height="26" fill="#f8fafc"/>
          <rect x="57" y="0" width="1" height="26" fill="#f8fafc"/>
          <rect x="61" y="0" width="5" height="26" fill="#f8fafc"/>
          <rect x="68" y="0" width="2" height="26" fill="#f8fafc"/>
          <rect x="73" y="0" width="4" height="26" fill="#f8fafc"/>
          <rect x="80" y="0" width="2" height="26" fill="#f8fafc"/>
          <rect x="85" y="0" width="6" height="26" fill="#f8fafc"/>
          <rect x="94" y="0" width="2" height="26" fill="#f8fafc"/>
          <rect x="99" y="0" width="4" height="26" fill="#f8fafc"/>
          <rect x="106" y="0" width="1" height="26" fill="#f8fafc"/>
          <rect x="110" y="0" width="5" height="26" fill="#f8fafc"/>
          <rect x="118" y="0" width="3" height="26" fill="#f8fafc"/>
          <rect x="124" y="0" width="2" height="26" fill="#f8fafc"/>
          <rect x="129" y="0" width="6" height="26" fill="#f8fafc"/>
          <rect x="138" y="0" width="2" height="26" fill="#f8fafc"/>
          <rect x="143" y="0" width="4" height="26" fill="#f8fafc"/>
          <rect x="150" y="0" width="1" height="26" fill="#f8fafc"/>
          <rect x="154" y="0" width="5" height="26" fill="#f8fafc"/>
          <rect x="162" y="0" width="3" height="26" fill="#f8fafc"/>
          <rect x="168" y="0" width="2" height="26" fill="#f8fafc"/>
          <rect x="173" y="0" width="6" height="26" fill="#f8fafc"/>
          <rect x="182" y="0" width="2" height="26" fill="#f8fafc"/>
          <rect x="187" y="0" width="4" height="26" fill="#f8fafc"/>
          <rect x="194" y="0" width="2" height="26" fill="#f8fafc"/>
          <rect x="199" y="0" width="5" height="26" fill="#f8fafc"/>
          <rect x="207" y="0" width="1" height="26" fill="#f8fafc"/>
          <rect x="211" y="0" width="3" height="26" fill="#f8fafc"/>
          <rect x="217" y="0" width="6" height="26" fill="#f8fafc"/>
          <rect x="226" y="0" width="2" height="26" fill="#f8fafc"/>
          <rect x="231" y="0" width="4" height="26" fill="#f8fafc"/>
          <rect x="238" y="0" width="2" height="26" fill="#f8fafc"/>
          <rect x="243" y="0" width="5" height="26" fill="#f8fafc"/>
          <rect x="251" y="0" width="1" height="26" fill="#f8fafc"/>
          <rect x="255" y="0" width="3" height="26" fill="#f8fafc"/>
          <rect x="260" y="0" width="4" height="26" fill="#f8fafc"/>
          <rect x="267" y="0" width="2" height="26" fill="#f8fafc"/>
          <rect x="272" y="0" width="3" height="26" fill="#f8fafc"/>

          <text x="137" y="38" text-anchor="middle" class="{ns}-mono" font-size="9" fill="#94a3b8" letter-spacing="2.5">*KM-64181191-2020-REACT*</text>
        </g>
      </g>

      <!-- 5. Holographic Foil Light Sweep Overlay -->
      <g class="{ns}-foil-layer">
        <rect x="100" y="80" width="220" height="400" transform="skewX(-25)" fill="url(#{ns}-foil-grad)"/>
      </g>
    </g>
  </g>
</svg>"""
    return svg

# ==============================================================================
# 5. CONNECT SVG
# ==============================================================================
def build_connect_svg():
    ns = "conn"
    
    def render_social_card(idx, icon_name, title, handle, desc, y_pos, accent_color="#247bff"):
        icon_path = ICONS.get(icon_name, "")
        return f"""
        <g id="{ns}-card-{idx}" transform="translate(420, {y_pos})">
          <rect width="435" height="72" rx="12" fill="#0d1527" stroke="{accent_color}" stroke-width="1" stroke-opacity="0.35"/>
          
          <!-- Icon Container -->
          <g transform="translate(16, 16)">
            <rect width="40" height="40" rx="8" fill="{accent_color}" fill-opacity="0.15"/>
            <path d="{icon_path}" transform="translate(10, 10) scale(0.85)" fill="{accent_color}"/>
          </g>

          <!-- Text -->
          <g transform="translate(72, 26)">
            <text class="{ns}-display" font-size="15" font-weight="700" fill="#f8fafc">{title} <tspan class="{ns}-mono" font-size="11" font-weight="500" fill="#94a3b8">({handle})</tspan></text>
            <text x="0" y="19" class="{ns}-mono" font-size="11" fill="#cbd5e1">{desc}</text>
          </g>

          <!-- Nudging Arrow -->
          <g class="{ns}-arrow-nudge" transform="translate(390, 36)">
            <path d="M0 0 L6 0 M3 -4 L7 0 L3 4" stroke="{accent_color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
          </g>
        </g>
        """

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 900 450" width="100%" height="100%">
  <defs>
    <style>
      {get_font_css(ns)}
      .{ns}-bg {{ fill: #070b16; }}
      .{ns}-card {{ fill: #0d1527; }}
      .{ns}-text-primary {{ fill: #f8fafc; }}
      .{ns}-text-secondary {{ fill: #94a3b8; }}

      /* Nudging Arrow Animation */
      @keyframes {ns}-nudge-anim {{
        0%, 100% {{ transform: translate(390px, 36px); }}
        50% {{ transform: translate(398px, 36px); }}
      }}
      .{ns}-arrow-nudge {{
        animation: {ns}-nudge-anim 1.8s ease-in-out infinite;
      }}
    </style>

    <pattern id="{ns}-dots" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#247bff" fill-opacity="0.10" />
    </pattern>

    <linearGradient id="{ns}-border-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.5"/>
      <stop offset="50%" stop-color="#ff354f" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0.2"/>
    </linearGradient>

    <filter id="{ns}-glow-filter" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="35"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="900" height="450" fill="#070b16" rx="20"/>
  <rect width="900" height="450" fill="url(#{ns}-dots)" rx="20"/>
  <rect x="1" y="1" width="898" height="448" rx="19" fill="none" stroke="url(#{ns}-border-grad)" stroke-width="1.2"/>

  <!-- Ambient Glows -->
  <circle cx="200" cy="220" r="160" fill="#247bff" opacity="0.14" filter="url(#{ns}-glow-filter)"/>
  <circle cx="700" cy="220" r="150" fill="#ff354f" opacity="0.10" filter="url(#{ns}-glow-filter)"/>

  <!-- Header Banner Focused on React & Mobile Collaboration -->
  <g transform="translate(45, 40)">
    <text class="{ns}-display" font-size="22" font-weight="800" fill="#f8fafc">LET&apos;S CONNECT &amp; COLLABORATE <tspan fill="#247bff">// FRONTEND &amp; MOBILE</tspan></text>
    <text x="0" y="20" class="{ns}-mono" font-size="11.5" fill="#94a3b8">React TS • Next.js • React Native • Open to high-impact projects</text>
  </g>

  <!-- ================= LEFT COLUMN: POINTING CHARACTER ================= -->
  <g id="{ns}-character" transform="translate(15, 60)">
    <image href="data:image/png;base64,{pointing_png_b64}" x="0" y="0" width="390" height="370" preserveAspectRatio="xMidYMid meet"/>
  </g>

  <!-- ================= RIGHT COLUMN: SOCIAL CARDS ================= -->
  {render_social_card(1, "linkedin", "LinkedIn", "karan-maurya", "React &amp; React Native engineering network", 75, "#247bff")}
  {render_social_card(2, "github", "GitHub", "karancodex", "14 public repos, frontend &amp; mobile codebases", 158, "#f8fafc")}
  {render_social_card(3, "nextdotjs", "Portfolio", "karancodex.vercel.app", "Interactive React web apps &amp; mobile case studies", 241, "#38bdf8")}
  {render_social_card(4, "instagram", "Instagram", "@karancodex", "Developer journey, tech builds &amp; behind-the-scenes", 324, "#e1306c")}

  <!-- Bottom Helper Text -->
  <g transform="translate(420, 416)">
    <rect width="435" height="24" rx="6" fill="#0d1527" stroke="#1e293b" stroke-width="1"/>
    <text x="217" y="16" text-anchor="middle" class="{ns}-mono" font-size="10" font-weight="600" fill="#94a3b8">👉 CLICK DIRECTLY ON THE REPOSITORY LINKS BELOW TO CONNECT</text>
  </g>
</svg>"""
    return svg

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================
def main():
    print("Regenerating SVGs emphasizing React Frontend and React Native Mobile...")
    
    hero_svg = build_hero_svg()
    with open(ASSETS_DIR / "hero.svg", "w", encoding="utf-8") as f:
        f.write(hero_svg)
    print("Generated assets/hero.svg")

    about_svg = build_about_life_svg()
    with open(ASSETS_DIR / "about-life.svg", "w", encoding="utf-8") as f:
        f.write(about_svg)
    print("Generated assets/about-life.svg")

    stack_svg = build_stack_svg()
    with open(ASSETS_DIR / "stack.svg", "w", encoding="utf-8") as f:
        f.write(stack_svg)
    print("Generated assets/stack.svg")

    id_svg = build_id_dashboard_svg()
    with open(ASSETS_DIR / "id-dashboard.svg", "w", encoding="utf-8") as f:
        f.write(id_svg)
    print("Generated assets/id-dashboard.svg")

    connect_svg = build_connect_svg()
    with open(ASSETS_DIR / "connect.svg", "w", encoding="utf-8") as f:
        f.write(connect_svg)
    print("Generated assets/connect.svg")

    print("All 5 SVGs successfully regenerated with Frontend & Mobile emphasis!")

if __name__ == "__main__":
    main()
