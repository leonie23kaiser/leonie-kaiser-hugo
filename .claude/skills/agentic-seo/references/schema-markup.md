# Schema Markup (JSON-LD)

Ready-to-use structured data templates. Schema markup gives AI systems structured context and boosts AI visibility by 30-40%.

> **Detection note:** `web_fetch` and `curl` strip `<script>` tags. They cannot detect JSON-LD injected by JavaScript (e.g., via Yoast, RankMath, AIOSEO). Always verify schema using **Google Rich Results Test** or a browser tool — they render JavaScript.

---

## Schema Selection Guide

| Page Type | Schema to Use |
|-----------|---------------|
| Homepage / Company | `Organization` |
| Blog post / article | `Article` or `BlogPosting` |
| FAQ section | `FAQPage` |
| How-to guide / tutorial | `HowTo` |
| Product page | `Product` |
| Software / tool | `SoftwareApplication` |
| Service page | `Service` |
| All pages | `BreadcrumbList` |
| Voice/AI optimization | `SpeakableSpecification` |
| Local business | `LocalBusiness` |

For complex pages, combine schemas using `@graph`.

---

## 1. Organization

Best for: About pages, homepage, company pages.

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Leonie Kaiser",
  "url": "https://leoniekaiser.com",
  "logo": "https://leoniekaiser.com/images/logo.png",
  "description": "KI- und Digitalisierungs-Expertin für kleine Gesundheitspraxen im DACH-Raum. EU AI Act und DSGVO von Anfang an mitgedacht.",
  "foundingDate": "2020",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Niederösterreich",
    "addressRegion": "AT-3",
    "addressCountry": "AT"
  },
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "customer service",
    "email": "hello@leoniekaiser.com"
  },
  "sameAs": [
    "https://www.linkedin.com/in/leoniekaiser"
  ]
}
```

---

## 2. Article / BlogPosting

Best for: Blog posts, news articles, guides.

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "[Article Title — max 110 characters]",
  "description": "[Article summary]",
  "image": [
    "https://example.com/image-16x9.jpg",
    "https://example.com/image-4x3.jpg",
    "https://example.com/image-1x1.jpg"
  ],
  "datePublished": "2024-01-15T08:00:00+01:00",
  "dateModified": "2024-12-20T10:30:00+01:00",
  "author": {
    "@type": "Person",
    "name": "[Author Name]",
    "url": "https://example.com/team/author",
    "jobTitle": "[Job Title]",
    "worksFor": {
      "@type": "Organization",
      "name": "Leonie Kaiser"
    }
  },
  "publisher": {
    "@type": "Organization",
    "name": "Leonie Kaiser",
    "logo": {
      "@type": "ImageObject",
      "url": "https://leoniekaiser.com/images/logo.png",
      "width": 600,
      "height": 60
    }
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://example.com/blog/article-url"
  },
  "keywords": ["keyword1", "keyword2"],
  "articleSection": "[Category]",
  "wordCount": 2000
}
```

---

## 3. FAQPage (+40% AI Visibility)

Best for: FAQ sections, product pages with Q&A, knowledge base pages.

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is [Your Service/Product]?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Comprehensive answer. Include statistics where possible — e.g., 'According to X, 85% of businesses report Y benefit.']"
      }
    },
    {
      "@type": "Question",
      "name": "How does [Service/Product] work?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Step-by-step explanation. First... Then... Finally...]"
      }
    },
    {
      "@type": "Question",
      "name": "How long does [Service] take?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Specific answer with timeframes and context]"
      }
    }
  ]
}
```

---

## 4. HowTo

Best for: Tutorials, guides, step-by-step articles.

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to [Do Something]",
  "description": "[Brief description of what this guide covers]",
  "image": "https://example.com/how-to-image.jpg",
  "totalTime": "PT30M",
  "estimatedCost": {
    "@type": "MonetaryAmount",
    "currency": "EUR",
    "value": "0"
  },
  "tool": [
    { "@type": "HowToTool", "name": "[Required tool]" }
  ],
  "step": [
    {
      "@type": "HowToStep",
      "name": "Step 1: [Step Name]",
      "text": "[Detailed step instructions]",
      "image": "https://example.com/step-1.jpg",
      "url": "https://example.com/guide#step1"
    },
    {
      "@type": "HowToStep",
      "name": "Step 2: [Step Name]",
      "text": "[Detailed step instructions]",
      "url": "https://example.com/guide#step2"
    }
  ]
}
```

---

## 5. Product

Best for: E-commerce product pages, SaaS product pages.

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "[Product Name]",
  "description": "[Product description]",
  "image": ["https://example.com/product-image.jpg"],
  "brand": {
    "@type": "Brand",
    "name": "[Brand Name]"
  },
  "offers": {
    "@type": "Offer",
    "url": "https://example.com/product",
    "priceCurrency": "EUR",
    "price": "99.00",
    "availability": "https://schema.org/InStock",
    "seller": {
      "@type": "Organization",
      "name": "Leonie Kaiser"
    }
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "47"
  }
}
```

---

## 6. SoftwareApplication

Best for: Tools, apps, software products, SaaS platforms.

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "[App Name]",
  "description": "[App description]",
  "applicationCategory": "BusinessApplication",
  "operatingSystem": "Cross-platform",
  "url": "https://example.com",
  "featureList": [
    "Feature 1",
    "Feature 2",
    "Feature 3"
  ],
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "EUR",
    "availability": "https://schema.org/InStock"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.7",
    "ratingCount": "120",
    "bestRating": "5"
  }
}
```

---

## 7. BreadcrumbList

Best for: All pages with navigation hierarchy (add to every page).

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://leoniekaiser.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Agentic AI",
      "item": "https://leoniekaiser.com/leistungen/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "AI Integration Services",
      "item": "https://leoniekaiser.com/leistungen/leistung-termine-anfragen/"
    }
  ]
}
```

---

## 8. Service

Best for: Service pages (professional services, consulting, agency).

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "[Service Name]",
  "description": "[Service description]",
  "provider": {
    "@type": "Organization",
    "name": "Leonie Kaiser",
    "url": "https://leoniekaiser.com"
  },
  "areaServed": {
    "@type": "Country",
    "name": "Austria"
  },
  "serviceType": "[Type of service]",
  "offers": {
    "@type": "Offer",
    "description": "Custom pricing based on project scope"
  }
}
```

---

## 9. SpeakableSpecification (AI & Voice Optimization)

Best for: Pages targeting voice search or AI extraction. Marks which CSS selectors contain the most extractable content.

```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "[Page Title]",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": [
      "h1",
      ".summary",
      ".key-takeaways",
      ".faq-answer"
    ]
  }
}
```

---

## 10. LocalBusiness

Best for: Local business pages, location-specific service pages.

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "[Business Name]",
  "description": "[Description]",
  "url": "https://example.com",
  "telephone": "+43-[number]",
  "email": "contact@example.com",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[Street]",
    "addressLocality": "Niederösterreich",
    "addressRegion": "AT-3",
    "postalCode": "[ZIP]",
    "addressCountry": "AT"
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "09:00",
      "closes": "18:00"
    }
  ],
  "priceRange": "€€€"
}
```

---

## Combining Schemas (@graph)

For pages where multiple schemas apply, use `@graph` — more efficient and avoids conflicts.

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "name": "[Page Title]",
      "url": "https://example.com/page",
      "speakable": {
        "@type": "SpeakableSpecification",
        "cssSelector": ["h1", ".hero-text", ".faq-answer"]
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "[Question]?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "[Answer]"
          }
        }
      ]
    },
    {
      "@type": "Organization",
      "name": "Leonie Kaiser",
      "url": "https://leoniekaiser.com"
    }
  ]
}
```

---

## Hugo Implementation

In Hugo, add JSON-LD in `layouts/partials/head.html` or in page templates:

```html
{{- with .Params.schema }}
<script type="application/ld+json">
{{ . | jsonify (dict "indent" "  ") | safeJS }}
</script>
{{- end }}
```

Or embed directly in the layout partial for site-wide schemas (Organization, BreadcrumbList).

---

## Validation Tools

1. **Google Rich Results Test** — renders JavaScript, validates JSON-LD  
   `https://search.google.com/test/rich-results?url={your-url}`

2. **Schema.org Validator** — checks syntax  
   `https://validator.schema.org/?url={your-url}`

3. **Google Search Console** — check Enhancements tab for schema errors after deployment
