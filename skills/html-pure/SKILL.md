---
name: html-pure
description: |
  Build static websites with pure HTML/CSS — no frameworks, no build steps.
  Use when: creating landing pages, marketing sites, company websites, or any static content site.
  Skip for: web apps needing client-side state, SPAs, dashboards with real-time data.
version: 1.0.0
---

# HTML Pure — Static Website Builder

Build fast, accessible, SEO-optimized static websites using only HTML5, CSS3, and minimal vanilla JS. Zero frameworks, zero build tools, zero runtime dependencies.

## When to Use

- Company/marketing websites
- Landing pages and product pages
- Portfolio and case study pages
- Blog with pre-generated static HTML
- Any site where content changes infrequently

## Core Rules (MANDATORY)

1. **Zero framework, zero build step** — no React, Vue, Tailwind, Webpack, or any toolchain. Ship raw HTML/CSS files directly.
2. **CSS-first interactions** — use `<details>/<summary>` for accordions, CSS `:target` for modals, `checkbox` hack for toggles, `scroll-snap` for carousels. Only fall back to vanilla JS when CSS truly cannot solve the interaction.
3. **Vanilla JS budget: < 2KB minified** — if JS is needed (e.g., mobile hamburger menu with complex animation), keep total JS under 2KB. No libraries.
4. **Mobile-first responsive** — write base styles for mobile, use `min-width` media queries to scale up: `768px` (tablet), `1024px` (desktop), `1280px` (wide).
5. **Semantic HTML5** — use `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`. Never use divs where semantic elements apply.
6. **SEO metadata on every page** — `<title>`, `<meta name="description">`, Open Graph tags, canonical URL, structured data (JSON-LD).
7. **Performance targets** — Lighthouse > 95 on all 4 metrics. Use `loading="lazy"` on images, `font-display: swap`, minimal CSS.
8. **Accessibility** — proper heading hierarchy (one `<h1>` per page), alt text on all images, sufficient color contrast, keyboard navigation support.

## File Structure Convention

```
project/
├── index.html
├── [page].html
├── css/
│   ├── design-system.css    # Variables, typography, reset
│   ├── layout.css           # Grid, containers, responsive
│   └── components.css       # Reusable component styles
├── assets/
│   ├── images/
│   ├── icons/
│   └── fonts/
├── js/
│   └── main.js              # Only if CSS cannot solve it
├── robots.txt
└── sitemap.xml
```

## CSS Architecture

Use CSS custom properties for the design system. Keep specificity flat — prefer class selectors, avoid nesting beyond 2 levels.

```css
:root {
  --color-primary: #EC2B39;
  --color-text: #212121;
  --font-sans: 'Satoshi', sans-serif;
  --max-width: 1200px;
}
```

## Responsive Breakpoints

| Name    | Min-width | Usage                  |
|---------|-----------|------------------------|
| mobile  | 0         | Base styles (default)  |
| tablet  | 768px     | 2-column layouts       |
| desktop | 1024px    | Full navigation, grids |
| wide    | 1280px    | Max-width containers   |

## CSS-Only Interaction Patterns

| Pattern           | HTML/CSS Approach                          |
|-------------------|--------------------------------------------|
| Accordion/FAQ     | `<details>` + `<summary>` elements         |
| Mobile menu       | Checkbox hack + `~` sibling combinator     |
| Carousel/slider   | `scroll-snap-type` + `overflow-x: auto`    |
| Tabs              | Radio buttons + `:checked` + `~`           |
| Modal             | `:target` pseudo-class                     |
| Marquee/scroll    | `@keyframes` with `translateX`             |
| Hover effects     | `:hover`, `:focus-within` pseudo-classes   |

## References

| Topic | File |
|-------|------|
| CSS-only patterns | [references/css-only-patterns.md](references/css-only-patterns.md) |
| Responsive guide | [references/responsive-guide.md](references/responsive-guide.md) |
| SEO checklist | [references/seo-checklist.md](references/seo-checklist.md) |
| Performance tips | [references/performance.md](references/performance.md) |

## Templates

| Template | File |
|----------|------|
| Base page | [templates/page.html](templates/page.html) |
| Design system CSS | [templates/design-system.css](templates/design-system.css) |
