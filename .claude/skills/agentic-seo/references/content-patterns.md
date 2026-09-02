# Content Patterns for AEO & GEO

Reusable content block templates optimized for answer engines (featured snippets, AI Overviews) and AI citation (ChatGPT, Perplexity, Claude, Gemini).

**AEO** = Answer Engine Optimization (featured snippets, voice, AI Overviews)  
**GEO** = Generative Engine Optimization (citation by AI assistants)

---

## Answer Engine Optimization (AEO) Patterns

### 1. Definition Block
**Use for:** "What is [X]?" queries

```markdown
## What is [Term]?

[Term] is [concise 1-sentence definition]. [Expanded 1-2 sentence explanation with key characteristics]. [Brief context on why it matters or how it's used].
```

**Example:**
```markdown
## What is API Integration?

API integration is the process of connecting two or more software applications so they can exchange data and functionality automatically. It eliminates manual data entry by enabling systems to communicate in real time via standardized interfaces. For businesses, this means CRMs, ERPs, and other tools stay synchronized without manual intervention.
```

---

### 2. Step-by-Step Block
**Use for:** "How to [X]" queries

```markdown
## How to [Action/Goal]

[1-sentence overview of the process and expected outcome]

1. **[Step Name]**: [Clear action description in 1-2 sentences]
2. **[Step Name]**: [Clear action description in 1-2 sentences]
3. **[Step Name]**: [Clear action description in 1-2 sentences]
4. **[Step Name]**: [Clear action description in 1-2 sentences]
5. **[Step Name]**: [Clear action description in 1-2 sentences]

[Optional: Expected outcome or timeframe]
```

---

### 3. Comparison Table Block
**Use for:** "[X] vs [Y]" queries — tables outperform prose for these

```markdown
## [Option A] vs [Option B]: [Brief Descriptor]

| Feature | [Option A] | [Option B] |
|---------|------------|------------|
| [Criteria 1] | [Value] | [Value] |
| [Criteria 2] | [Value] | [Value] |
| [Criteria 3] | [Value] | [Value] |
| Pricing | [Price] | [Price] |
| Best For | [Use case] | [Use case] |

**Bottom line**: [1-2 sentence recommendation based on different needs]
```

---

### 4. Pros and Cons Block
**Use for:** Evaluation queries — "Is [X] worth it?", "Should I use [X]?"

```markdown
## Pros and Cons of [Topic]

[1-sentence framing of the decision context]

### Pros
- **[Benefit category]**: [Specific explanation with data if available]
- **[Benefit category]**: [Specific explanation]
- **[Benefit category]**: [Specific explanation]

### Cons
- **[Drawback category]**: [Specific explanation]
- **[Drawback category]**: [Specific explanation]
- **[Drawback category]**: [Specific explanation]

**Verdict**: [1-2 sentence balanced conclusion with recommendation by use case]
```

---

### 5. FAQ Block
**Use for:** Topic pages with multiple common questions. Essential for FAQPage schema.

```markdown
## Frequently Asked Questions

### [Question phrased exactly as users search]?

[Direct answer in first sentence]. [Supporting context in 2-3 additional sentences. Stay under 100 words.]

### [Question phrased exactly as users search]?

[Direct answer in first sentence]. [Supporting context.]

### [Question phrased exactly as users search]?

[Direct answer in first sentence]. [Supporting context.]
```

**Tips for FAQ questions:**
- Use natural question phrasing ("How do I..." not "How does one...")
- Include question words: what, how, why, when, where, who, which
- Match "People Also Ask" boxes from Google results
- Keep answers 50-100 words

---

### 6. Listicle Block
**Use for:** "Best [X]", "Top [N] [items]", "[N] ways to [X]"

```markdown
## [Number] Best [Items] for [Goal]

[1-2 sentence intro establishing context and selection criteria]

### 1. [Item Name]

[Why it's recommended in 2-3 sentences with specific benefits or metrics]

### 2. [Item Name]

[Why it's recommended in 2-3 sentences]
```

---

## Generative Engine Optimization (GEO) Patterns

These patterns optimize content for citation by AI assistants. Research shows these combinations boost visibility most: **Fluency + Statistics** (maximum boost); **Citations + Quotations** (credibility).

### 7. Statistic Citation Block
**Use for:** Any factual claim — statistics boost AI citation by 15-30%

```markdown
[Claim statement]. According to [Source/Organization, Year], [specific statistic with number and unit]. [Context for why this matters or what it means for the reader].
```

**Example:**
```markdown
Software integration projects consistently reduce operational costs. According to Forrester Research (2024), companies that implement enterprise integration platforms report an average 34% reduction in manual data entry costs within 12 months. This makes integration a measurable ROI investment, not just a technical improvement.
```

---

### 8. Expert Quote Block
**Use for:** Adding authority to claims. Named expert attribution boosts AI citation.

```markdown
"[Direct quote from expert that makes a substantive claim]," says [Expert Name], [Title] at [Organization]. [1 sentence of context or implication].
```

---

### 9. Authoritative Claim Block
**Use for:** Establishing facts that AI systems should be able to extract and cite.

```markdown
[Topic] [is/has/requires] [clear, specific claim]. [Source] [confirms/reports/found] that [supporting evidence with specifics]. This [means/suggests/implies] [actionable implication].
```

---

### 10. Self-Contained Answer Block
**Use for:** Key definitions and answers that should work without surrounding context. AI systems extract these directly.

```markdown
**[Topic/Question]**: [Complete, self-contained answer that makes sense without additional context. Include specific details, numbers, or examples. Keep to 40-60 words for optimal extraction.]
```

**Example:**
```markdown
**Typical API integration timeline**: A standard B2B API integration between two enterprise systems takes 4-12 weeks depending on API quality, authentication complexity, and data transformation requirements. Simple REST integrations with good documentation can be completed in 2-3 weeks; legacy SOAP or EDI integrations typically require 6-16 weeks.
```

---

### 11. Evidence Sandwich Block
**Use for:** Claims that benefit from multiple data points — maximum credibility structure.

```markdown
[Opening claim statement].

Evidence supporting this includes:
- [Data point 1 with source and year]
- [Data point 2 with source and year]
- [Data point 3 with source and year]

[Concluding statement connecting evidence to actionable insight for the reader].
```
