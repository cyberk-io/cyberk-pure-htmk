# CSS-Only Interaction Patterns

Patterns for building interactive UI without JavaScript.

## Accordion (details/summary)

```html
<details>
  <summary>Question text here</summary>
  <p>Answer content here.</p>
</details>
```

```css
details summary {
  cursor: pointer;
  padding: 1rem 0;
  border-bottom: 1px solid rgba(0,0,0,0.1);
  list-style: none;
}
details summary::marker { display: none; }
details summary::-webkit-details-marker { display: none; }
details[open] summary { border-bottom: none; }
details > :not(summary) {
  padding: 0 0 1rem;
  animation: slideDown 0.2s ease-out;
}
@keyframes slideDown {
  from { opacity: 0; transform: translateY(-8px); }
  to { opacity: 1; transform: translateY(0); }
}
```

## Mobile Hamburger Menu (checkbox hack)

```html
<input type="checkbox" id="nav-toggle" class="nav-toggle" hidden>
<label for="nav-toggle" class="nav-toggle-label" aria-label="Toggle menu">
  <span></span><span></span><span></span>
</label>
<nav class="nav-menu">
  <a href="/">Home</a>
  <a href="/services/">Services</a>
</nav>
```

```css
.nav-menu {
  display: none;
}
.nav-toggle:checked ~ .nav-menu {
  display: flex;
  flex-direction: column;
}
@media (min-width: 1024px) {
  .nav-toggle-label { display: none; }
  .nav-menu { display: flex; }
}
```

## Scroll-Snap Carousel

```html
<div class="carousel">
  <div class="carousel-item">Card 1</div>
  <div class="carousel-item">Card 2</div>
  <div class="carousel-item">Card 3</div>
</div>
```

```css
.carousel {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  gap: 1rem;
  scrollbar-width: none;
}
.carousel::-webkit-scrollbar { display: none; }
.carousel-item {
  flex-shrink: 0;
  scroll-snap-align: start;
}
```

## Infinite Marquee (CSS animation)

```html
<div class="marquee-container">
  <div class="marquee-track">
    <div class="marquee-item">Item 1</div>
    <div class="marquee-item">Item 2</div>
    <!-- Duplicate items for seamless loop -->
    <div class="marquee-item">Item 1</div>
    <div class="marquee-item">Item 2</div>
  </div>
</div>
```

```css
.marquee-container { overflow: hidden; }
.marquee-track {
  display: flex;
  animation: marquee 30s linear infinite;
  width: max-content;
}
@keyframes marquee {
  from { transform: translateX(0); }
  to { transform: translateX(-50%); }
}
```

## Tabs (radio button hack)

```html
<div class="tabs">
  <input type="radio" name="tab" id="tab1" checked hidden>
  <label for="tab1">Tab 1</label>
  <input type="radio" name="tab" id="tab2" hidden>
  <label for="tab2">Tab 2</label>
  <div class="tab-content" id="content1">Content 1</div>
  <div class="tab-content" id="content2">Content 2</div>
</div>
```

```css
.tab-content { display: none; }
#tab1:checked ~ #content1,
#tab2:checked ~ #content2 { display: block; }
```
