# Mobile-First Responsive Guide

## Strategy

Write base CSS for mobile (320px+), then add complexity at larger breakpoints using `min-width` queries.

## Breakpoints

```css
/* Tablet */
@media (min-width: 768px) { }
/* Desktop */
@media (min-width: 1024px) { }
/* Wide */
@media (min-width: 1280px) { }
```

## Layout Patterns

### Container

```css
.container {
  width: 100%;
  max-width: var(--max-width, 1200px);
  margin: 0 auto;
  padding: 0 1.25rem;
}
@media (min-width: 768px) {
  .container { padding: 0 2.5rem; }
}
@media (min-width: 1024px) {
  .container { padding: 0; }
}
```

### Responsive Grid

```css
.grid { display: grid; gap: 1.5rem; }
.grid-2 { grid-template-columns: 1fr; }
.grid-4 { grid-template-columns: 1fr; }

@media (min-width: 768px) {
  .grid-2 { grid-template-columns: repeat(2, 1fr); }
  .grid-4 { grid-template-columns: repeat(2, 1fr); }
}
@media (min-width: 1024px) {
  .grid-4 { grid-template-columns: repeat(4, 1fr); }
}
```

## Fluid Typography

Use `clamp()` for typography that scales smoothly:

```css
h1 { font-size: clamp(2rem, 5vw, 4.5rem); }
h2 { font-size: clamp(1.5rem, 3vw, 3rem); }
body { font-size: clamp(0.875rem, 1.5vw, 1rem); }
```

## Responsive Images

```html
<img
  src="image.jpg"
  alt="Description"
  loading="lazy"
  width="800"
  height="600"
  style="max-width: 100%; height: auto;"
>
```

## Common Patterns

- **Stack to row**: `flex-direction: column` on mobile, `row` on desktop
- **Show/hide**: `display: none` on mobile, `display: block` at breakpoint
- **Full-width to contained**: remove `max-width` on mobile, add at breakpoint
- **Single to multi-column**: CSS Grid `1fr` on mobile, `repeat(N, 1fr)` at breakpoint
