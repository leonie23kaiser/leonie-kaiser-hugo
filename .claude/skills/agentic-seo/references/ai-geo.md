# AI SEO (GEO — Generative Engine Optimization)

Optimizing content to be cited by AI search engines: Google AI Overviews, ChatGPT, Perplexity, Microsoft Copilot, and Claude.

---

## Key Difference from Traditional SEO

Traditional SEO gets you **ranked**. AI SEO gets you **cited**.

AI systems extract passages and cite sources — they don't just show ranked links. A well-structured page can be cited even if it doesn't rank on page 1. Conversely, a page that ranks #1 but has poor structure may not get cited at all.

**Critical stats:**
- AI Overviews appear in ~45% of Google searches and reduce clicks by up to 58%
- Brands are 6.5x more likely to be cited via third-party sources than their own domains
- Optimized content gets cited 3x more often than non-optimized
- Adding statistics and citations boosts AI visibility by 37-40%
- Keyword stuffing **hurts** AI visibility by 10% (Princeton GEO study, KDD 2024)

---

## Three Pillars

```
1. Structure  — make content extractable
2. Authority  — make content citable
3. Presence   — be where AI looks
```

---

## Pillar 1: Structure — Extractable Content

AI systems pull passages, not pages. Every key claim should work as a standalone statement.

**Structural rules:**
- Lead every section with a direct answer (don't bury it)
- Keep key answer passages to 40-60 words (optimal extraction length)
- Use H2/H3 headings that match how people phrase queries
- Tables beat prose for comparison content
- Numbered lists beat paragraphs for process content
- Each paragraph should convey one clear idea

**Content block patterns** (see seo-content-patterns.md for full templates):
- **Definition blocks** for "What is X?" queries
- **Step-by-step blocks** for "How to X" queries
- **Comparison tables** for "X vs Y" queries
- **FAQ blocks** for common questions
- **Statistic blocks** with cited sources

---

## Pillar 2: Authority — Citable Content

### The 9 Princeton GEO Methods (ranked by impact)

| Method | Visibility Boost | How to Apply |
|--------|:---------------:|--------------|
| **Cite sources** | +40% | Add authoritative references with links |
| **Add statistics** | +37% | Include specific numbers with named sources |
| **Add quotations** | +30% | Expert quotes with name and title |
| **Authoritative tone** | +25% | Write with demonstrated expertise |
| **Improve clarity** | +20% | Simplify complex concepts |
| **Technical terms** | +18% | Use domain-specific terminology accurately |
| **Unique vocabulary** | +15% | Increase word diversity |
| **Fluency optimization** | +15-30% | Improve readability and flow |
| ~~Keyword stuffing~~ | **-10%** | Actively hurts — avoid |

**Best combination:** Fluency + Statistics = maximum boost. Low-ranking sites benefit even more — up to 115% visibility increase.

### Freshness

- Show "Last updated: [date]" prominently
- Refresh competitive content at minimum quarterly
- Include current-year references and recent statistics
- Remove or update outdated claims

### E-E-A-T for AI Citation

- Named authors with credentials (not "Staff" or "Admin")
- Expert quotes with name, title, organization
- "According to [Source]" framing for claims
- Original data beats aggregated data
- First-hand experience demonstrated in content

---

## Pillar 3: Presence — Where AI Looks

AI systems cite where you appear, not just your own domain.

**Third-party sources matter more:**
- Wikipedia mentions (7.8% of all ChatGPT citations)
- Reddit discussions (1.8% of ChatGPT citations)
- Industry publications and guest posts
- Review sites (G2, Capterra, TrustRadius for B2B SaaS)
- YouTube (frequently cited by Google AI Overviews)

**Actions:**
- Ensure your Wikipedia page is accurate and current (if you have one)
- Participate authentically in relevant Reddit communities
- Get featured in industry roundups and comparison articles
- Maintain updated profiles on relevant review platforms
- Answer Quora questions with substantive depth

### Machine-Readable Files for AI Agents

AI agents evaluating tools on behalf of buyers need parseable information. If your pricing is behind "contact sales" or JavaScript rendering, agents skip you.

**`/pricing.md` or `/pricing.txt`:**
```markdown
# Pricing — [Your Product Name]

## Starter
- Price: $0/month
- Limits: 100 items/month, 1 user
- Features: Basic API access, standard support

## Pro
- Price: $29/month (annual) | $35/month (monthly)
- Limits: 10,000 items/month, 5 users
- Features: Custom domains, analytics, priority support

## Enterprise
- Price: Custom — contact sales@example.com
- Features: SSO, SLA, dedicated account manager
```

**`/llms.txt`:** A Markdown index of your site's important pages for AI context. Low-cost to add. No major AI vendor has confirmed they read it (as of 2026, ~0.015% adoption), but it signals intent and costs nothing. See [llmstxt.org](https://llmstxt.org).

---

## AI Bot Access (robots.txt)

Blocking an AI bot means that platform cannot cite you.

```
User-agent: GPTBot           # ChatGPT search
Allow: /

User-agent: ChatGPT-User     # ChatGPT browsing
Allow: /

User-agent: PerplexityBot    # Perplexity
Allow: /

User-agent: ClaudeBot        # Claude (Anthropic)
Allow: /

User-agent: anthropic-ai     # Claude (alternate)
Allow: /

User-agent: Google-Extended  # Gemini + AI Overviews
Allow: /

User-agent: Bingbot          # Copilot (via Bing)
Allow: /

# Safe to block — only used for training, not search citation:
User-agent: CCBot
Disallow: /
```

---

## Platform-Specific Optimization

### Google AI Overviews

Appear in ~45% of Google searches. Only ~15% of AI Overview sources overlap with traditional Top 10 — pages that don't crack page 1 can still get cited.

**Key signals:**
- Schema markup is the single biggest lever (+30-40% visibility)
- Topical authority via content clusters with internal linking
- Named, sourced citations in content (+132% visibility)
- Author bios with real credentials
- Target "how to" and "what is" queries — these trigger AI Overviews most often

### ChatGPT

Uses Bing-based index. Authority + freshness are the top signals.

**Key signals:**
- Domain authority matters most (~40% of citation likelihood)
- Content updated within 30 days gets cited 3.2x more
- Content-answer fit: write the way ChatGPT formats its own answers (conversational, direct, organized)
- Clean heading hierarchy (H1 > H2 > H3)
- Verifiable statistics with named sources

### Perplexity

Always cites sources with links. Most research-oriented AI search engine.

**Key signals:**
- FAQ Schema (JSON-LD) — notably higher citation rate
- Publicly accessible PDFs (whitepapers, reports) are prioritized
- Publishing velocity matters more than keyword targeting
- Self-contained paragraphs that work as standalone answers
- Allow PerplexityBot in robots.txt

### Microsoft Copilot

Bing-only — if Bing hasn't indexed you, Copilot can't cite you.

**Key signals:**
- Submit to Bing Webmaster Tools + use IndexNow protocol
- Page speed < 2 seconds
- Clear entity definitions
- LinkedIn and GitHub presence (unique Copilot advantage)

### Claude

Uses Brave Search — not Google or Bing. Different index entirely.

**Key signals:**
- Verify visibility in Brave Search (search.brave.com for your brand + key terms)
- Allow ClaudeBot and anthropic-ai in robots.txt
- Maximize factual density: specific numbers, named sources, dated statistics
- Clear extractable structure — Claude is highly selective and rewards precision
- Be the most factually accurate source on your topic

---

## AI Visibility Audit

### Step 1: Test Your Key Queries

Pick 10-20 most important queries and test across platforms:

| Query | Google AI Overview | ChatGPT | Perplexity | You Cited? | Competitors? |
|-------|:-----------------:|:-------:|:----------:|:----------:|:------------:|
| "what is [service]" | | | | | |
| "best [category]" | | | | | |
| "[brand] vs [competitor]" | | | | | |

### Step 2: Content Extractability Check

Per priority page:
- [ ] Clear definition in first paragraph?
- [ ] Self-contained answer blocks?
- [ ] Statistics with named sources?
- [ ] Comparison tables for "[X] vs [Y]" queries?
- [ ] FAQ section with natural-language questions?
- [ ] Schema markup (FAQ, Article, Organization)?
- [ ] Expert attribution (author name + credentials)?
- [ ] Recently updated (within 6 months)?
- [ ] AI bots allowed in robots.txt?
- [ ] Heading structure matches query patterns?

### Step 3: Monitor

| Tool | Coverage | Best For |
|------|----------|----------|
| Otterly AI | ChatGPT, Perplexity, Google AI Overviews | Share of AI voice |
| Peec AI | ChatGPT, Gemini, Perplexity, Claude, Copilot | Multi-platform at scale |
| ZipTie | Google AI Overviews, ChatGPT, Perplexity | Brand mention + sentiment |
| LLMrefs | ChatGPT, Perplexity, AI Overviews, Gemini | SEO keyword → AI visibility |

**DIY (no tools):** Monthly manual check — pick top 20 queries, run through ChatGPT + Perplexity + Google, log who gets cited. Track month-over-month.

---

## Common Mistakes

- **Blocking AI bots** in robots.txt — removes you from that platform's citations
- **No freshness signals** — undated content loses to dated content
- **Keyword stuffing** — actively hurts AI visibility (-10%)
- **Gating content** — AI can't access it; keep authoritative content open
- **Opaque pricing** — AI agents skip you if pricing requires JavaScript or "contact sales"
- **Ignoring third-party presence** — a Wikipedia mention often outperforms your own blog
- **No structured data** — schema is the biggest single lever for AI Overviews
- **Generic content without data** — "we're the best" won't be cited; "customers see 3x improvement" will
