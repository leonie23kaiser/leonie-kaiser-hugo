# On-Page SEO

Title tags, meta descriptions, heading structure, content quality, E-E-A-T, image optimization, and internal linking.

---

## Title Tags

```html
<!-- ❌ Generic or missing -->
<title>Page</title>
<title>Home</title>

<!-- ✅ Descriptive with keyword -->
<title>Software Integration Services | integrations.at</title>
```

**Rules:**
- 50-60 characters (Google truncates at ~60)
- Primary keyword near the beginning
- Unique for every page
- Brand name at end (except homepage)
- Action-oriented where appropriate
- No keyword stuffing

**Common issues:** Duplicate titles, too long/short, keyword stuffing, missing entirely

---

## Meta Descriptions

```html
<!-- ✅ Compelling and unique -->
<meta name="description" content="Expert software integration services for Austrian businesses. Connect your systems with Microsoft, SAP, and custom APIs. Free consultation.">
```

**Rules:**
- 150-160 characters
- Include primary keyword naturally
- Clear value proposition and call to action
- Unique for every page
- Matches the actual page content

**Note:** Google rewrites ~60% of meta descriptions. Even rewritten ones benefit from keyword presence — Google bolts matching terms.

---

## Heading Structure

```html
<!-- ✅ Proper hierarchy -->
<h1>Software Integration Services in Austria</h1>
  <h2>Our Integration Approach</h2>
    <h3>Discovery Phase</h3>
    <h3>Implementation</h3>
  <h2>Integration Technologies</h2>
  <h2>Pricing & Engagement</h2>

<!-- ❌ Poor structure -->
<h2>Welcome</h2>
<h4>Services</h4>
<h1>Contact Us</h1>
```

**Rules:**
- Single `<h1>` per page — the main topic
- Logical hierarchy, no skipped levels (H1 → H2 → H3, not H1 → H3)
- H1 contains primary keyword
- Headings describe content, not styled decoration
- H2/H3 headings should match how users phrase queries (boosts AI snippet extraction)

---

## Content Optimization

### Keyword Placement

- Keyword in first 100 words
- Primary keyword in H1 and ideally one H2
- Related/semantic keywords used naturally throughout
- Keyword in URL (naturally)
- No keyword stuffing — AI systems penalize it (-10% visibility)

### Content Depth

- Answers the full search intent (informational, commercial, navigational, transactional)
- Sufficient length for the topic — not a target word count, but comprehensive coverage
- Better than what currently ranks: more specific, more accurate, more actionable
- Updated and current — show publish/update date

### Thin Content to Fix

- Pages with little unique content
- Tag/category pages with no editorial value
- Near-duplicate pages targeting the same keyword
- Marketing fluff without substance ("We're the best solution for...")

---

## E-E-A-T (Experience, Expertise, Authoritativeness, Trust)

Google's quality signal for content — especially important for YMYL topics (finance, health, legal, safety).

| Signal | What It Looks Like |
|--------|--------------------|
| **Experience** | First-hand accounts, original case studies, real examples, "we've seen", "in our projects" |
| **Expertise** | Named authors with credentials, accurate technical detail, proper sourcing |
| **Authoritativeness** | Industry recognition, citations by others, thought leadership, press mentions |
| **Trust** | HTTPS, contact info visible, privacy policy, accurate information, transparent about company |

**Practical actions:**
- Add author bio with name, role, and relevant credentials to blog/article content
- Show "Last updated: [date]" on time-sensitive content
- Cite original sources (not summaries of summaries)
- Include real contact details and company information
- Original data, original research, original case studies outperform recycled content

---

## Image SEO

```html
<!-- ❌ Poor -->
<img src="IMG_12345.jpg">

<!-- ✅ Optimized -->
<img src="software-integration-diagram.webp"
     alt="Software integration architecture showing ERP connected to CRM via middleware"
     width="800"
     height="600"
     loading="lazy">
```

**Rules:**
- Descriptive, keyword-relevant filenames (hyphens, not underscores)
- Alt text describes the image content — don't stuff keywords, describe what's shown
- Set explicit `width` and `height` to prevent layout shift (CLS)
- Compress: WebP/AVIF with fallback
- Lazy load below-fold images (`loading="lazy"`)
- Responsive images with `srcset` for different screen sizes

---

## Internal Linking

For audits in this repository, apply these rules only to public URLs discoverable from visible navigation, `sitemap.xml`, `robots.txt`, and public in-content links. Hidden Hugo sections or intentionally non-public collection routes are out of scope unless they leak into public runtime output.

```html
<!-- ❌ Non-descriptive -->
<a href="/services">Click here</a>
<a href="/blog">Read more</a>

<!-- ✅ Descriptive anchor text -->
<a href="/services/sap-integration">SAP integration services</a>
<a href="/blog/microsoft-365-integration-guide">how to integrate Microsoft 365</a>
```

**Rules:**
- Descriptive anchor text with relevant keywords
- Link important pages from high-authority pages
- No orphan pages — every page reachable from navigation or in-content links
- Reasonable link count per page (no excessive footer/sidebar links)
- Fix broken internal links promptly
- Use breadcrumbs with schema for hierarchy

**Strategy for service sites:**
- Homepage → Area pages → Service pages (3-click max)
- Blog posts → Related service pages (convert informational traffic to commercial)
- Service pages → Related service pages (cross-sell within topical clusters)

---

## Keyword Targeting Strategy

### Per Page

- One clear primary keyword target per page
- Title, H1, URL, and meta all aligned to same keyword
- Content satisfies the dominant search intent for that keyword
- Not competing with other pages on same site (keyword cannibalization)

### Cannibalization Check

If two pages target the same keyword:
1. Identify which one ranks better in Search Console
2. Either merge them (301 redirect weaker to stronger)
3. Or differentiate them clearly by intent (informational vs. commercial)

### Topical Clusters (for service sites)

```
Hub: /agentic-ai/  (area page — broad topic)
  Spoke: /agentic-ai/automation-agents/
  Spoke: /agentic-ai/ai-integration/
  Spoke: /agentic-ai/agent-orchestration/
```

- Hub page targets broad keyword with highest volume
- Spoke pages target specific long-tail variations
- All spokes link back to hub; hub links to all spokes
- Internal linking reinforces topical authority
