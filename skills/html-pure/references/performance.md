# Performance Optimization for Static HTML

## Target: Lighthouse > 95 on all metrics

### Performance
- No render-blocking JS
- Inline critical CSS or use `<link rel="preload">`
- `loading="lazy"` on below-fold images
- Serve images in WebP/AVIF when possible
- Set explicit `width`/`height` on images to prevent layout shift

### Accessibility
- Color contrast ratio >= 4.5:1 for normal text
- All interactive elements keyboard-accessible
- `aria-label` on icon-only buttons
- Skip-to-content link

### Best Practices
- HTTPS everywhere
- No mixed content
- No deprecated APIs

### SEO
- Valid meta tags on every page
- Structured data
- Mobile-friendly viewport

## Font Loading

```css
@font-face {
  font-family: 'Satoshi';
  src: url('/assets/fonts/Satoshi-Variable.woff2') format('woff2');
  font-weight: 200 700;
  font-display: swap;
}
```

## Image Optimization

- Use appropriate formats: SVG for icons/logos, WebP for photos
- Compress images (< 200KB for hero, < 100KB for thumbnails)
- Provide `width` and `height` attributes
- Use `loading="lazy"` for images below the fold
- Use `fetchpriority="high"` for hero/LCP images

## CSS Optimization

- Keep total CSS < 50KB
- Use CSS custom properties for theming (single source of truth)
- Avoid `@import` in CSS — use multiple `<link>` tags instead
- Order: reset → design-system → layout → components

## Minimal JS Guidelines

If JS is unavoidable (< 2KB budget):
- Place `<script>` before `</body>` with `defer`
- No external libraries
- Use event delegation for repeated elements
