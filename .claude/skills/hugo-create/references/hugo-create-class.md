# hugo-create-class

Create a new training class with curriculum modules, duration, level, and learning outcomes.

## Triggers
"create class", "new training class", "add class", "course page", "class curriculum"

## When to Use
- Adding a class to `/classes/` section
- Multi-module curriculum with learning objectives
- Class must appear in listings and have a detail page with Angular Element

## Front Matter Schema

```yaml
---
title: "Class Title"
date: 'YYYY-MM-DD'
lastmod: 'YYYY-MM-DD'
layout: "class-detail-layout"
type: "classes"
url: "/classes/class-slug/"
tags: ['Tag1', 'Tag2']
level: 'Intermediate'               # Beginner | Intermediate | Advanced
banner:
  image: "/images/class-pictures/class-slug.svg"
duration: "3 Days"
summary: "140–165 char summary for SEO and listings"
customer: "open"                    # open | enterprise | internal
showInList: false
---

Intro paragraph...

## Module 1: Title
- Learning objective
```

## File Location
`content/classes/[class-slug]-page.md`

## Step Flow
1. Gather: title, level, customer segment, duration, tags, summary
2. Per module: number, title, 5–10 learning objectives
3. Create `.md` file with front matter + module content
4. Image: auto-generate with `hugo-create-image` or update with `hugo-update-class-image`
5. Verify at `localhost:1313/classes/[slug]/` and in listings

## Key Notes
- `showInList: false` hides from listings until explicitly enabled
- `customer: "open"` = public; `"enterprise"` = filtered audience
- Class images: `static/images/class-pictures/[slug].svg` or `.png` (420×420 square)
- The `class-detail` template loads the `skills-list` Angular Element when `elementDemo.enabled: true`
- Docs reference: `docs/classes.md`
