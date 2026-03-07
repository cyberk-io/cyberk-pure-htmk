#!/usr/bin/env python3
"""
Blog generator for cyberk-io-static.
Fetches blog posts from cyberk.io, extracts article content, generates static HTML.
"""
import urllib.request
import re
import os
import html as html_module
import time

BLOG_DIR = "/Users/anderson/Desktop/works/cyberk-io-static/blog"
POSTS_DIR = os.path.join(BLOG_DIR, "posts")
CDN = "https://d2l5jmy01h5jfp.cloudfront.net"

BLOGS = [
    {
        "slug": "ai-agents-are-making-millions-on-polymarket",
        "title": "AI Agents Are Making Millions on Polymarket",
        "description": "An AI agent can turn Polymarket inefficiencies into repeatable profit.",
        "author": "Jon Ren",
        "date": "January 29, 2026",
        "readTime": "5 min read",
        "category": "AI & Agent Systems",
        "coverImg": f"{CDN}/Polymarket_3a6e168564.png",
    },
    {
        "slug": "nft-strategy-a-new-nft-fi-paradigm",
        "title": "NFT Strategy: A New NFTFi Paradigm from DLMM and Uniswap Hooks",
        "description": "NFT Strategy is poised to create a new revolution for NFTs.",
        "author": "Anderson",
        "date": "January 29, 2026",
        "readTime": "5 min read",
        "category": "Architecture & Build",
        "coverImg": f"{CDN}/Banner_7_25446a9129.png",
    },
    {
        "slug": "if-2026-is-a-bear-market-de-fi-will-split-in-two",
        "title": "If 2026 Is a Bear Market, DeFi Will Split in Two",
        "description": "Which form of DeFi will endure and thrive, especially in a potential bear market scenario in 2026.",
        "author": "Jon Ren",
        "date": "January 29, 2026",
        "readTime": "6 min read",
        "category": "Industry Insights & Research",
        "coverImg": f"{CDN}/Banner_12_04ed6c4f25.png",
    },
    {
        "slug": "why-are-proprietary-am-ms-is-dominating-solana",
        "title": "Why Are Proprietary AMMs Is Dominating Solana?",
        "description": "Solana's liquidity structure is being rebuilt around a new model - Proprietary AMMs.",
        "author": "Anderson",
        "date": "January 29, 2026",
        "readTime": "12 min read",
        "category": "Industry Insights & Research",
        "coverImg": f"{CDN}/Banner_116f3ab4b3.png",
    },
    {
        "slug": "stablecoin-playbook-for-ct-os-choosing-an-issuance-model-and-an-operating-architecture",
        "title": "Stablecoin Playbook for CTOs: Choosing an Issuance Model and an Operating Architecture",
        "description": "Stablecoin in nature is a financial product with a balance sheet and an on-chain interface.",
        "author": "Anderson",
        "date": "January 29, 2026",
        "readTime": "10 min read",
        "category": "Stablecoin",
        "coverImg": f"{CDN}/Banner_2_190faeba26.png",
    },
    {
        "slug": "how-cyberk-build-a-indexer-with-million-qps-in-30-days",
        "title": "How Cyberk Build an Indexer with Million QPS in 30 Days",
        "description": "Let's explore how such an architecture is built to make million-QPS indexing possible.",
        "author": "Anderson",
        "date": "January 8, 2026",
        "readTime": "9 min read",
        "category": "Architecture & Build",
        "coverImg": f"{CDN}/How_to_build_an_Indexer_999b85a978.png",
    },
    {
        "slug": "cyberk-audit-readiness-guide",
        "title": "Cyberk Audit Readiness Procedure",
        "description": "We will provide a comprehensive guidance on the smart contract security audit process.",
        "author": "Anderson",
        "date": "January 26, 2026",
        "readTime": "11 min read",
        "category": "Blockchain Development",
        "coverImg": f"{CDN}/Audit_guide_f4735dbb8a.png",
    },
    {
        "slug": "from-kyc-to-zkp-de-pin",
        "title": "From KYC to ZKP: DePIN's Next Frontier in Self-Custodial Biometric Authentication",
        "description": "Biometric verification built on the Blockchain significantly helps mitigate DePIN risk factors.",
        "author": "Anderson",
        "date": "January 29, 2026",
        "readTime": "6 min read",
        "category": "Blockchain Development",
        "coverImg": f"{CDN}/Biometrics_72e09089ed.png",
    },
    {
        "slug": "trad-fi-x-de-fi-unifying-to-shape-the-rwa-market",
        "title": "TradFi x DeFi: Unifying to Shape the RWA Market",
        "description": "Let's find out a CTO viewpoint about the relations between TradFi x DeFi in RWA Markets.",
        "author": "Anderson",
        "date": "January 29, 2026",
        "readTime": "7 min read",
        "category": "RWA",
        "coverImg": f"{CDN}/Banner_1_b54fbf030d.png",
    },
    {
        "slug": "kohaku-the-new-sdk-frameworks-that-bring-real-privacy-to-ethereum",
        "title": "Kohaku: The New SDK Frameworks that Bring Real Privacy to Ethereum",
        "description": "Cyberk explores how Kohaku SDK framework brings default privacy and ZK security to every wallet.",
        "author": "Anderson",
        "date": "January 29, 2026",
        "readTime": "7 min read",
        "category": "Blockchain Development",
        "coverImg": f"{CDN}/Banner_10_3434bcd9b4.png",
    },
    {
        "slug": "what-we-can-learn-from-the-128-m-balancer-attack",
        "title": "What We Can Learn from the $128M Balancer Attack",
        "description": "This exploit is a wake-up call for every project writing economic logic in Solidity.",
        "author": "Anderson",
        "date": "January 29, 2026",
        "readTime": "6 min read",
        "category": "Blockchain Development",
        "coverImg": f"{CDN}/Banner_8_909c979504.png",
    },
    {
        "slug": "turnning-a-redemption-queue-into-a-numeric-comparison-with-mathematical-accumulation-in-a-stablecoin-project",
        "title": "Turning a Redemption Queue into a Numeric Comparison with Mathematical Accumulation",
        "description": "Today, we want to share how we optimized the redemption process for a Stablecoin project.",
        "author": "Kanz",
        "date": "January 29, 2026",
        "readTime": "5 min read",
        "category": "Stablecoin",
        "coverImg": f"{CDN}/Banner_3_f7913173fa.png",
    },
    {
        "slug": "designing-a-stablecoin-protocol-with-mathematical-accumulation-on-evm",
        "title": "Designing a Stablecoin Protocol with Mathematical Accumulation on EVM",
        "description": "In this article, Cyberk will outline a practical design for a stablecoin backed by USDC/USDT.",
        "author": "Kanz",
        "date": "January 29, 2026",
        "readTime": "5 min read",
        "category": "Architecture & Build",
        "coverImg": f"{CDN}/Banner_6_7bf0b1ec1b.png",
    },
    {
        "slug": "top-blockchain-development-services-for-startups-choosing-the-best-providers-for-acceleration",
        "title": "Top Blockchain Development Services for Startups",
        "description": "The fast, scalable blockchain development services for startups and enterprises.",
        "author": "Anderson",
        "date": "March 5, 2026",
        "readTime": "7 min read",
        "category": "Web3 & Startup",
        "coverImg": f"{CDN}/Top_blockchain_services_for_startups_c38b7a6672.png",
    },
    {
        "slug": "realistic-and-sustainable-apr-in-de-fi-in-2026",
        "title": "What's a Realistic & Sustainable APR in DeFi - in 2026",
        "description": "At Cyberk, we've been closely monitoring yield markets for DeFi build & investments.",
        "author": "Jon Ren",
        "date": "February 27, 2026",
        "readTime": "9 min read",
        "category": "Industry Insights & Research",
        "coverImg": f"{CDN}/Banner_11_14a5077bde.png",
    },
]


def fetch_html(url):
    """Fetch raw HTML from URL."""
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"  ERROR fetching {url}: {e}")
        return None


def extract_article_content(raw_html):
    """Extract the article/prose content from the Next.js rendered page."""
    cleaned = re.sub(r"<script[^>]*>.*?</script>", "", raw_html, flags=re.DOTALL)
    cleaned = re.sub(r"<style[^>]*>.*?</style>", "", cleaned, flags=re.DOTALL)

    # Target the prose div which contains the markdown-rendered content
    prose_match = re.search(
        r'<div[^>]*class="[^"]*prose[^"]*"[^>]*>(.*)',
        cleaned,
        re.DOTALL,
    )
    if prose_match:
        content = prose_match.group(1)
        # Find where the prose content ends (before "Content" heading or "Similar Posts")
        end_match = re.search(
            r'<h[23][^>]*>\s*(?:Content|Similar Posts)',
            content,
        )
        if end_match:
            content = content[: end_match.start()]

        # Strip the markdown-content wrapper div if present
        content = re.sub(r'^<div[^>]*class="markdown-content"[^>]*>', '', content.strip())

        # Remove trailing </div> tags
        content = re.sub(r'(</div>\s*)+$', '', content.strip())

        return content.strip()

    return None


def clean_content(content):
    """Clean extracted HTML content for static output."""
    if not content:
        return ""

    # Fix Next.js image URLs to use direct CDN URLs
    content = re.sub(
        r'src="[^"]*/_next/image\?url=([^&"]+)[^"]*"',
        lambda m: f'src="{urllib.request.unquote(m.group(1))}"',
        content,
    )

    # Remove Next.js specific attributes
    content = re.sub(r'\s+data-nimg="[^"]*"', "", content)
    content = re.sub(r'\s+fetchpriority="[^"]*"', "", content)
    content = re.sub(r'\s+decoding="[^"]*"', "", content)
    content = re.sub(r'\s+srcset="[^"]*"', "", content)
    content = re.sub(r'\s+sizes="[^"]*"', "", content)
    content = re.sub(r'\s+style="[^"]*color:\s*transparent[^"]*"', "", content)

    # Remove Next.js class attributes (Tailwind)
    content = re.sub(r'\s+class="[^"]*(?:prose|markdown|next|tailwind|dark:)[^"]*"', "", content)

    # Fix internal links to use static site paths
    content = re.sub(r'href="https://cyberk\.io/blog/([^"]+)"', r'href="\1.html"', content)
    content = re.sub(r'href="https://cyberk\.io/services/([^"]+)"', r'href="../../services/\1.html"', content)
    content = re.sub(r'href="https://cyberk\.io/about-us"', r'href="../../about-us.html"', content)
    content = re.sub(r'href="https://cyberk\.io/?"', r'href="../../index.html"', content)
    content = re.sub(r'href="https://cyberk\.io"', r'href="../../index.html"', content)

    # Remove empty style attributes
    content = re.sub(r'\s+style="\s*"', "", content)

    # Add loading="lazy" to images that don't have it
    content = re.sub(r"<img(?!\s+loading)", '<img loading="lazy"', content)

    # Clean up excessive whitespace
    content = re.sub(r"\n{3,}", "\n\n", content)

    return content


def generate_post_html(blog):
    """Generate the full HTML page for a blog post."""
    title_escaped = html_module.escape(blog["title"])
    desc_escaped = html_module.escape(blog["description"])
    content = blog.get("content", "<p>Content coming soon.</p>")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title_escaped} | Cyberk Blog</title>
  <meta name="description" content="{desc_escaped}">
  <link rel="canonical" href="https://cyberk.io/blog/{blog['slug']}">
  <meta property="og:title" content="{title_escaped} | Cyberk Blog">
  <meta property="og:description" content="{desc_escaped}">
  <meta property="og:image" content="{blog['coverImg']}">
  <meta property="og:url" content="https://cyberk.io/blog/{blog['slug']}">
  <meta property="og:type" content="article">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title_escaped}">
  <meta name="twitter:description" content="{desc_escaped}">
  <meta name="twitter:image" content="{blog['coverImg']}">
  <link rel="icon" href="../../assets/images/favicon.png">
  <link rel="stylesheet" href="../../css/design-system.css">
  <link rel="stylesheet" href="../../css/layout.css">
  <link rel="stylesheet" href="../../css/components.css">
  <style>
    .blog-post-hero {{ padding: 8rem 0 2rem; background: var(--color-bg-gray); }}
    .blog-post-meta {{ display: flex; align-items: center; gap: 1rem; margin-bottom: 1.5rem; font-size: 0.875rem; color: var(--color-text-muted); font-weight: var(--fw-light); }}
    .blog-post-meta img {{ width: 40px; height: 40px; border-radius: 50%; object-fit: cover; }}
    .blog-post-cover {{ width: 100%; max-height: 480px; object-fit: cover; border-radius: var(--radius-lg); margin-bottom: 2rem; }}
    .blog-content {{ max-width: 800px; margin: 0 auto; }}
    .blog-content h1 {{ font-size: clamp(1.5rem, 3vw, 2.25rem); margin: 2rem 0 1rem; }}
    .blog-content h2 {{ font-size: clamp(1.25rem, 2.5vw, 1.75rem); margin: 2rem 0 1rem; font-weight: var(--fw-semibold); }}
    .blog-content h3 {{ font-size: clamp(1.1rem, 2vw, 1.375rem); margin: 1.5rem 0 0.75rem; font-weight: var(--fw-medium); }}
    .blog-content p {{ font-size: 1rem; line-height: 1.8; margin-bottom: 1.25rem; font-weight: var(--fw-light); color: var(--color-text-secondary); }}
    .blog-content ul, .blog-content ol {{ margin: 1rem 0 1.25rem 1.5rem; }}
    .blog-content li {{ font-size: 1rem; line-height: 1.8; margin-bottom: 0.5rem; font-weight: var(--fw-light); color: var(--color-text-secondary); }}
    .blog-content img {{ max-width: 100%; height: auto; border-radius: var(--radius-md); margin: 1.5rem 0; }}
    .blog-content a {{ color: var(--red-2); text-decoration: underline; }}
    .blog-content blockquote {{ border-left: 4px solid var(--red-2); padding: 1rem 1.5rem; margin: 1.5rem 0; background: var(--color-bg-gray); border-radius: 0 var(--radius-md) var(--radius-md) 0; }}
    .blog-content blockquote p {{ margin-bottom: 0.5rem; }}
    .blog-content pre {{ background: #1a1a1a; color: #f0f0f0; padding: 1.25rem; border-radius: var(--radius-md); overflow-x: auto; margin: 1.5rem 0; font-size: 0.875rem; line-height: 1.6; }}
    .blog-content code {{ font-family: 'SF Mono', 'Fira Code', monospace; font-size: 0.875em; }}
    .blog-content :not(pre) > code {{ background: var(--color-bg-gray); padding: 0.15em 0.4em; border-radius: 4px; color: var(--red-2); }}
    .blog-content table {{ width: 100%; border-collapse: collapse; margin: 1.5rem 0; font-size: 0.9rem; }}
    .blog-content th, .blog-content td {{ border: 1px solid #e0e0e0; padding: 0.75rem 1rem; text-align: left; }}
    .blog-content th {{ background: var(--color-bg-gray); font-weight: var(--fw-medium); }}
    .blog-content strong {{ font-weight: var(--fw-semibold); color: var(--color-text-primary); }}
    .blog-back {{ display: inline-flex; align-items: center; gap: 0.5rem; font-size: 0.875rem; font-weight: var(--fw-medium); color: var(--red-2); text-decoration: none; margin-bottom: 2rem; }}
    .blog-back:hover {{ text-decoration: underline; }}
  </style>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-K8ZNFPQZPN"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-K8ZNFPQZPN');
  </script>
</head>
<body>

  <!-- Header -->
  <header class="site-header" id="site-header">
    <div class="container container-wide header-inner">
      <a href="../../index.html" class="logo" aria-label="Cyberk Home">
        <img src="../../assets/icons/cyberk-logo.svg" alt="Cyberk" width="160" height="30">
      </a>
      <input type="checkbox" id="nav-toggle" class="nav-toggle" hidden>
      <label for="nav-toggle" class="nav-toggle-label" aria-label="Toggle navigation menu">
        <span></span><span></span><span></span>
      </label>
      <nav class="nav-menu" id="nav-menu">
        <a href="../../index.html">Home</a>
        <div class="nav-dropdown">
          <a href="../../services/index.html">Service &#9662;</a>
          <div class="nav-dropdown-content">
            <a href="../../services/mvp-development.html">MVP Development</a>
            <a href="../../services/smart-contract-development.html">Smart Contract Development</a>
            <a href="../../services/dedicated-lab.html">Dedicated Lab</a>
            <a href="../../services/mvp-agent-development.html">MVP Agent Development</a>
          </div>
        </div>
        <a href="../../about-us.html">About Us</a>
        <a href="../index.html" class="active">Blog</a>
      </nav>
      <a href="https://t.me/cyberk_anderson" target="_blank" rel="noopener" class="btn btn-primary header-cta">CONTACT US <span class="arrow">&rarr;</span></a>
    </div>
  </header>

  <main>
    <section class="blog-post-hero">
      <div class="container blog-content">
        <a href="../index.html" class="blog-back">&larr; Back to blog</a>
        <h1>{title_escaped}</h1>
        <div class="blog-post-meta">
          <span>{blog['author']}</span>
          <span>&middot;</span>
          <span>{blog['date']}</span>
          <span>&middot;</span>
          <span>{blog['readTime']}</span>
        </div>
        <img src="{blog['coverImg']}" alt="{title_escaped}" class="blog-post-cover" loading="lazy">
      </div>
    </section>

    <section class="section" style="background:#fff;padding-top:2rem;">
      <div class="container blog-content">
        {content}
      </div>
    </section>
  </main>

  <!-- Footer -->
  <footer class="site-footer">
    <div class="container container-wide">
      <div class="footer-grid">
        <div class="footer-cta">
          <div class="footer-cta-row">
            <h2>Ready To<br>Get Started?</h2>
            <a href="https://t.me/cyberk_anderson" target="_blank" rel="noopener" class="btn btn-primary" style="padding:0.5rem 2rem;font-size:0.875rem;">CONTACT US <span class="arrow">&rarr;</span></a>
          </div>
        </div>
        <div class="footer-links">
          <div>
            <h3>COMPANY</h3>
            <ul>
              <li><a href="../../about-us.html">About us</a></li>
              <li><a href="../../services/index.html">Service</a></li>
              <li><a href="../index.html">Blog</a></li>
            </ul>
          </div>
          <div>
            <h3>SERVICES</h3>
            <ul>
              <li><a href="../../services/mvp-development.html">MVP Development</a></li>
              <li><a href="../../services/smart-contract-development.html">Smart Contract Development</a></li>
              <li><a href="../../services/dedicated-lab.html">Dedicated Lab</a></li>
              <li><a href="../../services/mvp-agent-development.html">MVP Agent Development</a></li>
            </ul>
          </div>
          <div>
            <h3>CONTACT</h3>
            <ul>
              <li><a href="https://www.linkedin.com/company/cyberk-io/" target="_blank" rel="noopener">Linkedin</a></li>
              <li><a href="https://www.facebook.com/Cyberk.io" target="_blank" rel="noopener">Facebook</a></li>
              <li><a href="https://t.me/cyberk_anderson" target="_blank" rel="noopener">Telegram</a></li>
              <li><a href="mailto:anderson@cyberk.io">anderson@cyberk.io</a></li>
            </ul>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <div>All copyrights reserved by Cyberk &copy; 2025</div>
        <div class="footer-bottom-right">HaNoi, VietNam GMT+7</div>
      </div>
    </div>
  </footer>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    "headline": "{title_escaped}",
    "description": "{desc_escaped}",
    "image": "{blog['coverImg']}",
    "author": {{
      "@type": "Person",
      "name": "{blog['author']}"
    }},
    "publisher": {{
      "@type": "Organization",
      "name": "Cyberk",
      "logo": {{ "@type": "ImageObject", "url": "https://cyberk.io/assets/icons/cyberk-logo.svg" }}
    }},
    "datePublished": "{blog['date']}",
    "url": "https://cyberk.io/blog/{blog['slug']}"
  }}
  </script>

  <script src="../../js/main.js" defer></script>
</body>
</html>"""


def generate_listing_html(blogs):
    """Generate the blog listing page."""
    cards = []
    for b in blogs:
        title_escaped = html_module.escape(b["title"])
        desc_escaped = html_module.escape(b["description"])
        cards.append(f"""            <a href="posts/{b['slug']}.html" class="blog-card">
              <img src="{b['coverImg']}" alt="{title_escaped}" class="blog-card-image" loading="lazy">
              <div class="blog-card-body">
                <span class="blog-card-tag">{html_module.escape(b['category'])}</span>
                <h2 class="blog-card-title">{title_escaped}</h2>
                <p class="blog-card-excerpt">{desc_escaped}</p>
                <p class="blog-card-meta">{b['date']} &middot; {b['readTime']}</p>
              </div>
            </a>""")

    cards_html = "\n".join(cards)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Blog | Cyberk - Blockchain Development Insights</title>
  <meta name="description" content="Read the latest insights on blockchain development, Web3 trends, smart contracts, and startup MVPs from the Cyberk team.">
  <link rel="canonical" href="https://cyberk.io/blog/">
  <meta property="og:title" content="Blog | Cyberk - Blockchain Development Insights">
  <meta property="og:description" content="Read the latest insights on blockchain development, Web3 trends, smart contracts, and startup MVPs from the Cyberk team.">
  <meta property="og:image" content="https://cyberk.io/assets/images/thumbnail-banner.png">
  <meta property="og:url" content="https://cyberk.io/blog/">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Blog | Cyberk - Blockchain Development Insights">
  <meta name="twitter:description" content="Read the latest insights on blockchain development, Web3 trends, and startup MVPs.">
  <meta name="twitter:image" content="https://cyberk.io/assets/images/thumbnail-banner.png">
  <link rel="icon" href="../assets/images/favicon.png">
  <link rel="stylesheet" href="../css/design-system.css">
  <link rel="stylesheet" href="../css/layout.css">
  <link rel="stylesheet" href="../css/components.css">
  <style>
    .blog-hero {{ padding: 8rem 0 3rem; background: var(--color-bg-gray); text-align: center; }}
    .blog-grid {{ display: grid; grid-template-columns: 1fr; gap: 2rem; }}
    @media (min-width: 768px) {{ .blog-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
    @media (min-width: 1024px) {{ .blog-grid {{ grid-template-columns: repeat(3, 1fr); }} }}
    .blog-card {{ background: #fff; border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-soft); transition: transform 0.3s, box-shadow 0.3s; display: flex; flex-direction: column; text-decoration: none; color: inherit; }}
    .blog-card:hover {{ transform: translateY(-4px); box-shadow: var(--shadow-card); }}
    .blog-card-image {{ width: 100%; height: 200px; object-fit: cover; }}
    .blog-card-body {{ padding: 1.5rem; flex: 1; display: flex; flex-direction: column; }}
    .blog-card-tag {{ display: inline-block; font-size: 0.75rem; font-weight: var(--fw-medium); color: var(--red-2); background: var(--color-bg-pink-2); padding: 0.25rem 0.75rem; border-radius: 999px; margin-bottom: 0.75rem; width: fit-content; }}
    .blog-card-title {{ font-size: 1.125rem; font-weight: var(--fw-medium); margin-bottom: 0.75rem; line-height: 1.4; }}
    .blog-card-excerpt {{ font-size: 0.875rem; font-weight: var(--fw-light); color: var(--color-text-muted); line-height: 1.6; flex: 1; }}
    .blog-card-meta {{ margin-top: 1rem; font-size: 0.75rem; color: var(--color-text-light); font-weight: var(--fw-extralight); }}
  </style>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-K8ZNFPQZPN"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-K8ZNFPQZPN');
  </script>
</head>
<body>

  <!-- Header -->
  <header class="site-header" id="site-header">
    <div class="container container-wide header-inner">
      <a href="../index.html" class="logo" aria-label="Cyberk Home">
        <img src="../assets/icons/cyberk-logo.svg" alt="Cyberk" width="160" height="30">
      </a>
      <input type="checkbox" id="nav-toggle" class="nav-toggle" hidden>
      <label for="nav-toggle" class="nav-toggle-label" aria-label="Toggle navigation menu">
        <span></span><span></span><span></span>
      </label>
      <nav class="nav-menu" id="nav-menu">
        <a href="../index.html">Home</a>
        <div class="nav-dropdown">
          <a href="../services/index.html">Service &#9662;</a>
          <div class="nav-dropdown-content">
            <a href="../services/mvp-development.html">MVP Development</a>
            <a href="../services/smart-contract-development.html">Smart Contract Development</a>
            <a href="../services/dedicated-lab.html">Dedicated Lab</a>
            <a href="../services/mvp-agent-development.html">MVP Agent Development</a>
          </div>
        </div>
        <a href="../about-us.html">About Us</a>
        <a href="../blog/index.html" class="active">Blog</a>
      </nav>
      <a href="https://t.me/cyberk_anderson" target="_blank" rel="noopener" class="btn btn-primary header-cta">CONTACT US <span class="arrow">&rarr;</span></a>
    </div>
  </header>

  <main>
    <section class="blog-hero">
      <div class="container">
        <h1 style="margin-bottom:1rem;">Blog</h1>
        <p style="font-size:clamp(0.875rem,1.5vw,1.25rem);font-weight:300;max-width:600px;margin:0 auto;color:var(--color-text-secondary);">
          Insights on blockchain development, Web3 trends, and building successful startups from the Cyberk team.
        </p>
      </div>
    </section>

    <section class="section" style="background:#fff;">
      <div class="container">
        <div class="blog-grid">
{cards_html}
        </div>
      </div>
    </section>
  </main>

  <!-- Footer -->
  <footer class="site-footer">
    <div class="container container-wide">
      <div class="footer-grid">
        <div class="footer-cta">
          <div class="footer-cta-row">
            <h2>Ready To<br>Get Started?</h2>
            <a href="https://t.me/cyberk_anderson" target="_blank" rel="noopener" class="btn btn-primary" style="padding:0.5rem 2rem;font-size:0.875rem;">CONTACT US <span class="arrow">&rarr;</span></a>
          </div>
        </div>
        <div class="footer-links">
          <div>
            <h3>COMPANY</h3>
            <ul>
              <li><a href="../about-us.html">About us</a></li>
              <li><a href="../services/index.html">Service</a></li>
              <li><a href="../blog/index.html">Blog</a></li>
            </ul>
          </div>
          <div>
            <h3>SERVICES</h3>
            <ul>
              <li><a href="../services/mvp-development.html">MVP Development</a></li>
              <li><a href="../services/smart-contract-development.html">Smart Contract Development</a></li>
              <li><a href="../services/dedicated-lab.html">Dedicated Lab</a></li>
              <li><a href="../services/mvp-agent-development.html">MVP Agent Development</a></li>
            </ul>
          </div>
          <div>
            <h3>CONTACT</h3>
            <ul>
              <li><a href="https://www.linkedin.com/company/cyberk-io/" target="_blank" rel="noopener">Linkedin</a></li>
              <li><a href="https://www.facebook.com/Cyberk.io" target="_blank" rel="noopener">Facebook</a></li>
              <li><a href="https://t.me/cyberk_anderson" target="_blank" rel="noopener">Telegram</a></li>
              <li><a href="mailto:anderson@cyberk.io">anderson@cyberk.io</a></li>
            </ul>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <div>All copyrights reserved by Cyberk &copy; 2025</div>
        <div class="footer-bottom-right">HaNoi, VietNam GMT+7</div>
      </div>
    </div>
  </footer>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "Organization",
        "name": "Cyberk",
        "url": "https://cyberk.io",
        "logo": "https://cyberk.io/assets/icons/cyberk-logo.svg"
      }},
      {{
        "@type": "WebSite",
        "name": "Cyberk",
        "url": "https://cyberk.io"
      }},
      {{
        "@type": "CollectionPage",
        "name": "Cyberk Blog",
        "description": "Insights on blockchain development, Web3 trends, and building successful startups",
        "url": "https://cyberk.io/blog/"
      }}
    ]
  }}
  </script>

  <script src="../js/main.js" defer></script>
</body>
</html>"""


def main():
    os.makedirs(POSTS_DIR, exist_ok=True)

    print(f"Generating {len(BLOGS)} blog posts...\n")

    for i, blog in enumerate(BLOGS):
        slug = blog["slug"]
        url = f"https://cyberk.io/blog/{slug}"
        print(f"[{i+1}/{len(BLOGS)}] Fetching: {blog['title'][:60]}...")

        raw_html = fetch_html(url)
        if raw_html:
            content = extract_article_content(raw_html)
            if content:
                content = clean_content(content)
                print(f"  -> Extracted {len(content)} chars of content")
            else:
                print(f"  -> WARNING: Could not extract content, using fallback")
                content = f"<p>{html_module.escape(blog['description'])}</p><p>Read the full article at <a href='{url}'>{url}</a></p>"
        else:
            content = f"<p>{html_module.escape(blog['description'])}</p><p>Read the full article at <a href='{url}'>{url}</a></p>"

        blog["content"] = content

        post_html = generate_post_html(blog)
        post_path = os.path.join(POSTS_DIR, f"{slug}.html")
        with open(post_path, "w", encoding="utf-8") as f:
            f.write(post_html)
        print(f"  -> Saved: {post_path}")

        if i < len(BLOGS) - 1:
            time.sleep(0.5)

    # Generate listing page
    print(f"\nGenerating blog listing page...")
    listing_html = generate_listing_html(BLOGS)
    listing_path = os.path.join(BLOG_DIR, "index.html")
    with open(listing_path, "w", encoding="utf-8") as f:
        f.write(listing_html)
    print(f"Saved: {listing_path}")

    print(f"\nDone! Generated {len(BLOGS)} blog posts + 1 listing page.")


if __name__ == "__main__":
    main()
