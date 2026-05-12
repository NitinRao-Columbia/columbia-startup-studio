# Slide Component Library

A reference guide for all available slide types and reusable components. Use these semantic classes to create beautiful, consistent slides without inline styles.

---

## Slide Types

### Title Slide
Opening hero slide with course metadata.

```markdown
<!-- .slide: class="title-slide" -->
<p class="meta">c5w3 · Thursday, February 5, 2026</p>
<h1>Slide Title</h1>
<p class="subtitle">Subtitle or description</p>
```

### Section Slide
Dark divider slide between major sections. Optionally add time/duration.

```markdown
<!-- .slide: class="section-slide" -->
## Section Title
<p class="section-subtitle">Until 2:05</p>
```

### Content Slide
Standard slide with orange accent bar on heading. Use `data-theme="rose"` for pink accent.

```markdown
<!-- .slide: class="content-slide" -->
## Content Title

- Bullet points
- More content
```

```markdown
<!-- .slide: class="content-slide" data-theme="rose" -->
## Warning Topic

This slide has a pink accent bar.
```

### Emphasis Slide
Big statement slide for key takeaways. Add `style="justify-content: center;"` to vertically center.

```markdown
<!-- .slide: class="emphasis-slide" -->
## This is a big idea that needs to stand out.

<p class="mt-1" style="font-style: italic;">Optional follow-up text.</p>
```

```markdown
<!-- .slide: class="emphasis-slide" style="justify-content: center;" -->
## Centered emphasis for maximum impact.
```

### Split Slide
Two-column layout with dark left, light right. Great for comparisons.

```markdown
<!-- .slide: class="split-slide" -->
<div class="left">
<h3>Category Label</h3>
<h2 class="track-label">Yes</h2>
<ul>
<li><strong>Bold item</strong> — detail</li>
</ul>
</div>
<div class="right">
<h3>Category Label</h3>
<h2 class="track-label">No</h2>
<ul>
<li><strong>Bold item</strong> — detail</li>
</ul>
</div>
```

### End Slide
Dark closing slide.

```markdown
<!-- .slide: class="end-slide" -->
<div style="text-align: center;">
<h2 style="margin-bottom: 0;">End of Class 5</h2>
<p style="color: #666; margin-top: 0.5em;">Next: Topic Preview</p>
</div>
```

---

## Cards

### Basic Card
White card with shadow and hover effect.

```html
<div class="card">
<h4>Card Title</h4>
<p>Card description.</p>
</div>
```

### Colored Border Cards
Add color accent with border-top. Available: `card-accent` (orange), `card-indigo`, `card-emerald`, `card-rose`.

```html
<div class="card card-accent">...</div>
<div class="card card-indigo">...</div>
<div class="card card-emerald">...</div>
<div class="card card-rose">...</div>
```

### Dark Card
Dark background for emphasis, prompts, or code.

```html
<div class="card card-dark">
<p style="color: white;">Content on dark background.</p>
</div>
```

### Compact Card
Tighter padding for dense layouts. Add `card-compact` or use inside `.grid-compact`.

```html
<div class="card card-compact card-indigo">
<h4>Compact Title</h4>
<ul>
<li>Item one</li>
<li>Item two</li>
</ul>
</div>
```

### Icon Card (Centered)
Card with large icon, centered title, and description.

```html
<div class="card card-icon card-indigo">
<span class="icon-lg">👤</span>
<h4>Join a Pitcher</h4>
<p>Talk to them. Stand with them.</p>
</div>
```

### Compare Cards (Pro/Con Pattern)
For "Good/Bad", "Yes/No", "Do/Don't" comparisons.

```html
<div class="grid-2 grid-compact mt-1">
<div class="card card-compact card-indigo">
<h4><i data-lucide="check-circle" style="color: #10b981;"></i> Good Fit</h4>
<ul>
<li>Item one</li>
<li>Item two</li>
</ul>
</div>
<div class="card card-compact card-rose">
<h4><i data-lucide="x-circle" style="color: #ef4444;"></i> Doesn't Fit</h4>
<ul>
<li>Item one</li>
<li>Item two</li>
</ul>
</div>
</div>
```

### Prompt Card (Dark with Code)
For AI prompts, formulas, or code snippets.

```html
<div class="card card-dark" style="padding: 1.2em;">
<pre style="margin: 0; white-space: pre-wrap; color: #e5e5e5;">
Create a Lean Startup Canvas for this concept:

[PROBLEM]: [describe the problem]
[SOLUTION]: [describe the solution concept]
</pre>
</div>
```

### Formula Card
For showing combinations with colored variables.

```html
<div class="card card-dark mt-2" style="padding: 1.5em;">
<p style="color: white; font-size: 1.3em; margin: 0;">
<span class="clr-emerald">[Persona]</span> +
<span class="clr-indigo">[Device]</span> +
<span class="clr-accent">[Environment]</span> +
<span class="clr-pink">[Activity]</span>
</p>
</div>
```

---

## Grids

### Two-Column Grid
```html
<div class="grid-2">
<div class="card">Left</div>
<div class="card">Right</div>
</div>
```

### Three-Column Grid
```html
<div class="grid-3">
<div class="card">One</div>
<div class="card">Two</div>
<div class="card">Three</div>
</div>
```

### Four-Column Grid
```html
<div class="grid-4">
<div class="card">1</div>
<div class="card">2</div>
<div class="card">3</div>
<div class="card">4</div>
</div>
```

### Compact Grid
Tighter spacing for dense content. Also makes child cards compact.

```html
<div class="grid-2 grid-compact">
<div class="card card-indigo">...</div>
<div class="card card-rose">...</div>
</div>
```

---

## Steps (Process Flows)

### Standard Steps
For 2-4 step processes. Shows numbered circles with connecting lines.

```html
<div class="steps-container">
<div class="step">
<div class="step-number">1</div>
<div class="step-content">
<h4>First Step</h4>
<p>Description of what happens.</p>
</div>
</div>
<div class="step">
<div class="step-number">2</div>
<div class="step-content">
<h4>Second Step</h4>
<p>Description of what happens.</p>
</div>
</div>
<div class="step">
<div class="step-number">3</div>
<div class="step-content">
<h4>Third Step</h4>
<p>Description of what happens.</p>
</div>
</div>
</div>
```

### Compact Steps
For slides with more content. Add `steps-compact` class.

```html
<div class="steps-container steps-compact">
...
</div>
```

---

## Stats

### Stat Boxes
For displaying key numbers/metrics.

```html
<div class="stats-container mt-1">
<div class="stat-box">
<div class="stat-value accent">10</div>
<div class="stat-label">For validation</div>
</div>
<div class="stat-box">
<div class="stat-value clr-indigo">100</div>
<div class="stat-label">For MVP testing</div>
</div>
<div class="stat-box">
<div class="stat-value clr-emerald">~1,000</div>
<div class="stat-label">Scale target</div>
</div>
</div>
```

### Stat with Description
Add a `<p>` for extra context below the label.

```html
<div class="stat-box">
<div class="stat-value accent" style="font-size: 2em;">A</div>
<div class="stat-label">Access</div>
<p>How easily can we reach users?</p>
</div>
```

### Compact Stats
For slides with more content.

```html
<div class="stats-container stats-compact">
...
</div>
```

---

## Callouts

### Info Callout (Blue)
For tips, hints, and helpful information.

```html
<div class="callout callout-info">
<span class="callout-icon">💡</span>
<p>This is helpful information.</p>
</div>
```

### Warning Callout (Yellow)
For important notices and cautions.

```html
<div class="callout callout-warning">
<span class="callout-icon">⚠️</span>
<p>This is an important warning.</p>
</div>
```

### Success Callout (Green)
For confirmations and positive messages.

```html
<div class="callout callout-success">
<span class="callout-icon">✅</span>
<p>This is a success message.</p>
</div>
```

### Compact Callout
For tight slides. Add `callout-compact`.

```html
<div class="callout callout-info callout-compact">
<span class="callout-icon">💡</span>
<p>Compact callout text.</p>
</div>
```

---

## Badges

### Colored Badges
For labels, tags, and categories.

```html
<span class="badge">Default</span>
<span class="badge badge-accent">Accent</span>
<span class="badge badge-indigo">Indigo</span>
<span class="badge badge-emerald">Emerald</span>
```

### Reference Badge
Mark reference/optional slides.

```html
<span class="badge badge-accent">Reference Slide</span>
<span class="badge badge-indigo">Reference Slide</span>
```

---

## Icons (Lucide)

Use Lucide icons with `<i data-lucide="icon-name">`. Browse at [lucide.dev/icons](https://lucide.dev/icons).

### Icon Colors
Use color classes instead of inline styles.

```html
<i data-lucide="rocket" class="icon-accent"></i>
<i data-lucide="users" class="icon-indigo"></i>
<i data-lucide="check-circle" class="icon-emerald"></i>
<i data-lucide="target" class="icon-rose"></i>
<i data-lucide="heart" class="icon-pink"></i>
<i data-lucide="cloud" class="icon-sky"></i>
```

**Semantic colors** for common patterns:
```html
<i data-lucide="check-circle" class="icon-success"></i>  <!-- green check -->
<i data-lucide="x-circle" class="icon-error"></i>        <!-- red x -->
```

### In Card Headers
Icons auto-size to match h4 text. Use icon color classes.

```html
<h4><i data-lucide="check-circle" class="icon-success"></i> Good Fit</h4>
<h4><i data-lucide="x-circle" class="icon-error"></i> Doesn't Fit</h4>
```

### Size Classes

| Class | Size | Use For |
|-------|------|---------|
| `.icon-inline` | 1em | Icons in running text |
| `.icon-sm` | 40px | Small accents |
| `.icon-md` | 48px | Icon cards, grids |
| (default) | 72px | Standalone display |
| `.icon-lg` | 96px | Hero icons |

```html
<i data-lucide="info" class="icon-inline icon-indigo"></i>  <!-- in text -->
<i data-lucide="rocket" class="icon-md icon-accent"></i>    <!-- icon card -->
<i data-lucide="target" class="icon-lg icon-rose"></i>      <!-- hero -->
```

---

## Color Utilities

### Text Colors
```html
<span class="clr-accent">Orange text</span>
<span class="clr-indigo">Indigo text</span>
<span class="clr-emerald">Emerald text</span>
<span class="clr-rose">Rose text</span>
<span class="clr-pink">Pink text</span>
<span class="gray">Gray text</span>
```

### Gradient Text
```html
<span class="gradient-text">Gradient orange-pink text</span>
```

### Background Colors
```html
<div class="bg-dark">...</div>
<div class="bg-faint">...</div>
<div class="bg-gradient">...</div>
```

---

## Typography Utilities

### Text Size
```html
<p class="text-small">Smaller text (0.85em)</p>
<p class="text-large">Larger text (1.2em)</p>
```

### Text Alignment
```html
<p class="text-center">Centered text</p>
```

---

## Spacing Utilities

### Margin Top
```html
<div class="mt-1">1em margin-top</div>
<div class="mt-2">2em margin-top</div>
<div class="mt-3">3em margin-top</div>
```

### Margin Bottom
```html
<div class="mb-1">1em margin-bottom</div>
<div class="mb-2">2em margin-bottom</div>
```

---

## Common Patterns

### Exercise Slide with Timer
```markdown
<!-- .slide: class="section-slide" -->
## Exercise 1: Exquisite Corpse
<p class="section-subtitle">Until 1:53</p>
```

### Summary Slide (Keep on Screen)
```markdown
<!-- .slide: class="emphasis-slide" style="padding-top: 40px; font-size: 0.9em;" -->
## Exercise Summary
<p class="section-subtitle">Until 1:53</p>

<div class="grid-2 grid-compact mt-1">
...
</div>
```

### Questions Slide
```markdown
<!-- .slide: class="emphasis-slide" style="justify-content: center;" -->
## <i data-lucide="help-circle" style="color: #6366f1;"></i> Questions?
```

### Image with Caption
```html
<div style="text-align: center; margin-top: 0.5em;">
<img src="assets/image.png" alt="Description" style="max-width: 90%; height: auto;">
</div>
<p class="mt-1" style="text-align: center; font-size: 0.55em; font-style: italic; color: #999;">
Source: <a href="https://example.com" style="color: #999;">Attribution</a>
</p>
```

---

## CSS Variables Reference

```css
/* Colors */
--black: #0f0f0f;
--dark: #1a1a1a;
--gray: #525252;
--light: #a3a3a3;
--faint: #f5f5f5;
--white: #ffffff;

/* Accent Palette */
--accent: #f97316;      /* Orange */
--indigo: #6366f1;      /* Indigo */
--emerald: #10b981;     /* Green */
--rose: #f43f5e;        /* Red/Rose */
--sky: #0ea5e9;         /* Blue */
--pink: #ec4899;        /* Pink */

/* Gradients */
--gradient-warm: linear-gradient(135deg, #f97316 0%, #ec4899 100%);
--gradient-cool: linear-gradient(135deg, #6366f1 0%, #06b6d4 100%);
--gradient-dark: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
```
