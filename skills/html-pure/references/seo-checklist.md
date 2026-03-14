# SEO Checklist for Static HTML Sites

## Required Meta Tags (every page)

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Page Title | Brand Name</title>
<meta name="description" content="150-160 char description">
<link rel="canonical" href="https://example.com/page">
```

## Open Graph (social sharing)

```html
<meta property="og:title" content="Page Title">
<meta property="og:description" content="Description">
<meta property="og:image" content="https://example.com/og-image.png">
<meta property="og:url" content="https://example.com/page">
<meta property="og:type" content="website">
```

## Twitter Card

```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Page Title">
<meta name="twitter:description" content="Description">
<meta name="twitter:image" content="https://example.com/og-image.png">
```

## Structured Data (JSON-LD)

### Organization

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Company Name",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png",
  "sameAs": ["https://linkedin.com/company/...", "https://facebook.com/..."]
}
</script>
```

### BreadcrumbList

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://example.com/"},
    {"@type": "ListItem", "position": 2, "name": "Services", "item": "https://example.com/services/"}
  ]
}
</script>
```

## Technical SEO

- One `<h1>` per page
- Logical heading hierarchy: h1 > h2 > h3
- All images have `alt` attributes
- Internal links use relative paths
- `robots.txt` at root
- `sitemap.xml` at root listing all pages
- Favicon: `<link rel="icon" href="/assets/images/favicon.png">`

## robots.txt Template

```
User-agent: *
Allow: /
Sitemap: https://example.com/sitemap.xml
```

## sitemap.xml Template

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://example.com/</loc></url>
  <url><loc>https://example.com/about-us.html</loc></url>
</urlset>
```
