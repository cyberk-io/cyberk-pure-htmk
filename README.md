# Cyberk.io — Pure Static HTML Website

Pure HTML/CSS static website for [cyberk.io](https://cyberk.io). Zero JavaScript frameworks, zero build tools, zero runtime dependencies.

## Stack

- **HTML5** — Semantic markup
- **CSS3** — Custom properties, Grid, Flexbox, scroll-snap, keyframe animations
- **Vanilla JS** — < 1KB, only for header scroll behavior and How We Work step switcher
- **Font** — Satoshi Variable (self-hosted)

## Structure

```
├── index.html                     # Home
├── about-us.html                  # About Us
├── services/
│   ├── index.html                 # Services overview
│   ├── mvp-development.html
│   ├── smart-contract-development.html
│   ├── mvp-agent-development.html
│   └── dedicated-lab.html
├── case-studies/
│   ├── index.html                 # Case studies listing
│   ├── aethir.html
│   ├── coinseeker.html
│   ├── helix.html
│   └── oracler.html
├── blog/
│   └── index.html                 # Blog (placeholder for Phase 2)
├── css/
│   ├── design-system.css          # Variables, typography, reset
│   ├── layout.css                 # Grid, containers, responsive
│   └── components.css             # All component styles
├── assets/
│   ├── images/                    # PNG images
│   ├── icons/                     # SVG icons
│   └── fonts/                     # Satoshi-Variable.ttf
├── js/
│   └── main.js                    # Minimal vanilla JS
├── robots.txt
├── sitemap.xml
└── README.md
```

## Development

No build step needed. Open any HTML file directly in a browser, or serve with any static file server:

```bash
# Python
python3 -m http.server 8000

# Node.js
npx serve .

# PHP
php -S localhost:8000
```

## Deployment

Deploy to any static hosting:
- **GitHub Pages** — push to `gh-pages` branch
- **Cloudflare Pages** — connect repo, no build command needed
- **Netlify** — drag and drop the folder
- **Vercel** — import as static site

## Design Tokens

| Token | Value |
|-------|-------|
| Primary Red | `#EC2B39` |
| Text | `#212121` |
| Font | Satoshi Variable |
| Max Width | `1200px` |
| Breakpoints | 768px, 1024px, 1280px |

## Related

- IP-015: Automated Content Distribution System
- Phase 2 will add: Static Site Generator, Content Engine, Analytics
