---
name: "check-google-rating"
description: "Audit a web page, site, or draft against Google's current helpful-content and generative-AI guidance and recent ranking updates; returns a risk rating with evidence."
---

# Check Google Rating

Assess how content is likely to be judged by Google's quality systems and search quality raters. The output is a risk assessment with evidence, not a ranking prediction. Google states rater data is not used directly in ranking.

## Inputs

Accept any of:
- One or more URLs
- A domain (audit a sample of pages)
- A draft (pasted text, attached file, or local Markdown/HTML) before publishing
- Optional: a date when traffic dropped

If the input is unclear, ask once which of these it is. Otherwise start.

## Step 1: Load the current guidance live

Google updates these pages often. Always fetch them at run time and note each page's "Last updated" date:
- https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- https://developers.google.com/search/docs/fundamentals/using-gen-ai-content
- https://developers.google.com/search/docs/essentials/spam-policies (scaled content abuse section)

If a page has new criteria not covered in the checklist below, add them to this run's assessment and mention them in the report.

## Step 2: Check recent ranking updates

Fetch https://status.search.google.com/summary (or https://status.search.google.com/incidents.json for exact start and end times).
- List core, spam, and other ranking updates from the last 90 days, with start date and duration.
- Flag any update still rolling out.
- If the user gave a traffic-drop date, state which update window it falls into, if any. Correlation only; do not claim causation.

## Step 3: Collect the content

- URL: fetch with WebFetch. If blocked or JavaScript-rendered, use the browser, or ask the user to paste the content.
- Domain: sample up to 8 pages: home, About, one author page, and 4 to 5 representative content pages (newest and highest-traffic if known). Check for templated or near-duplicate pages.
- Draft: read the file or pasted text directly.

Also capture metadata: title element, meta description, structured data (JSON-LD), image alt texts, byline, published and modified dates.

## Step 4: Assess

Rate each criterion as Pass, Risk, or Fail, with one line of concrete evidence (a short quote under 15 words, or a description).

**Main content quality**
- Effort: visible human work, original analysis, custom tools or media. Fail if text looks bulk-generated without curation.
- Originality: information or perspective not available elsewhere. Fail if it mainly rewrites other sources.
- Skill: clear writing, good production, working tools.
- Accuracy: spot-check 3 to 5 factual claims with web search. Report any errors found. Apply stricter scrutiny to YMYL topics (health, money, safety, legal).

**Who, How, Why**
- Who: byline where expected, author page with real background. Fail on fabricated personas, AI headshots, or false credentials.
- How: disclosure of AI or automation use where a reader would reasonably ask how it was made.
- Why: written for an audience, not to capture search traffic.

**Search-engine-first red flags**
- Many topics outside the site's focus
- Content chasing trends without audience fit
- Padding toward a word count
- Answers to questions that have no answer (unconfirmed release dates and similar)
- Dates changed without substantive edits
- Summaries of others with no added value

**Trust signals (E-E-A-T)**
- Sources cited, About page, contact information, first-hand experience shown

**Generative AI specifics**
- Signs of unreviewed AI output: hallucinated facts, generic phrasing, inconsistent details
- Metadata (title, description, structured data, alt text) accurate and matching the page
- For ecommerce: AI images carry IPTC DigitalSourceType TrainedAlgorithmicMedia; AI product data labeled

**Page experience**
- Note obvious issues only (intrusive interstitials, broken layout on mobile). Suggest PageSpeed Insights for Core Web Vitals rather than guessing values.

## Step 5: Report

Structure:
1. Overall verdict: Low, Medium, or High risk, with a two-sentence reason.
2. Ranking update context from Step 2.
3. Findings table: criterion, rating, evidence.
4. Top fixes, ordered by impact, each one concrete and actionable.
5. Guidance versions used (page names and last-updated dates).
6. Sources list.

For a single page or draft, give the report in the reply. For a domain audit or when the user wants to share it, publish it as a document.

## Rules

- Never invent metrics (traffic, rankings, Core Web Vitals scores). Say what would be needed to measure them.
- Keep quotes from any source under 15 words, one per source; paraphrase the rest.
- Distinguish clearly between what Google's documents say and your own judgment.
- Do not promise ranking outcomes.