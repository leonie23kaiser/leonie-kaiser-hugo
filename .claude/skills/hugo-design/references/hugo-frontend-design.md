# hugo-frontend-design

Create production-grade frontend UI with strong aesthetic direction and WCAG 2.2 compliance.

## When to Use

- The request needs design system guidance beyond CSS variable swaps.
- Building a new UI component with typography, color, layout, and spacing decisions.
- Designing or refining a visual interface with clear aesthetic intent.
- Accessibility-first frontend design reasoning is needed alongside implementation.

## Design Direction

Before coding, establish the visual goal clearly:

- Define the interface purpose and the user goal.
- Choose an intentional aesthetic direction instead of defaulting to a generic layout.
- Document constraints such as framework, performance, accessibility, and device targets.
- Identify what should make the design memorable.

Strong design directions can include minimalist, editorial, brutalist, retro-futuristic, organic, luxury, playful, industrial, or geometric styles.

## Core Design Rules

### Typography

- Choose distinctive typography instead of default-looking stacks.
- Pair a characterful display style with a readable body style.
- Keep contrast at or above WCAG 2.2 AA thresholds.

### Color and Theme

- Define CSS variables for colors and use them consistently.
- Build a clear palette with strong hierarchy instead of evenly-muted tones.
- Test interactive states for contrast and clarity.
- Support forced colors mode with system colors where needed.

### Motion and Animation

- Use motion deliberately, not decoratively.
- Prefer a few high-impact transitions over scattered micro-motion.
- Avoid motion that distracts or causes discomfort.

### Layout and Composition

- Use visual hierarchy intentionally.
- Allow asymmetry or unusual composition when it improves the design.
- Keep the layout responsive and usable down to a 320px viewport.
- Avoid horizontal scrolling for ordinary text and controls.

### Accessibility

- Use semantic HTML first.
- Ensure keyboard operability and visible focus.
- Do not rely on color alone for meaning.
- Use ARIA only where native semantics are insufficient.
- Support high contrast and forced colors mode.

## Implementation Guidance

- Use the repository's `docs/` for project-specific design tokens, layout conventions, and UI patterns.
- Use project-approved component or styling systems when they exist.
- Keep frontend design guidance reusable across frameworks unless the request is explicitly framework-specific.

## Avoid Generic Output

- Avoid interchangeable SaaS-style layouts.
- Avoid overused color patterns and safe default typography.
- Avoid treating accessibility as a post-processing step.
- Design with a clear point of view.

## Final Verification

- Clear aesthetic direction is visible in the result.
- Typography and color choices are intentional and accessible.
- Layout reflows at small viewports.
- Interactive elements are keyboard operable with visible focus.
- Forced-colors mode and contrast needs are covered.