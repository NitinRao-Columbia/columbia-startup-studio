# Rekindled — Style Guide

**Team Name:** LLmao  
**Date:** March 2026  
**Version:** 2.0 (Redesign)

**Purpose:** This is the canonical visual and interaction reference for Rekindled. Every surface — landing page, app prototype, pitch deck, social assets — must conform to this guide. When something looks or feels off-brand, this document is the source of truth.

---

## Design Philosophy

Rekindled's visual identity mirrors its product promise: **warmth without hype, structure without rigidity, confidence without loudness.**

The aesthetic is dark, warm, and editorial — closer to a high-end magazine or boutique hospitality brand than a tech startup. It should feel like a calm room you'd actually want to walk into.

---

## Color Palette

### Core Colors

| Token         | Hex         | Role                                                    |
|---------------|-------------|---------------------------------------------------------|
| `--bg`        | `#0E0E0C`   | Primary background. Near-black with a warm undertone.   |
| `--surface`   | `#161614`   | Elevated surfaces: cards, nav (scrolled), alternating sections. |
| `--cream`     | `#F1F0EC`   | Primary text. Warm off-white — never pure `#FFFFFF`.    |
| `--muted`     | `#9B9B93`   | Secondary text, metadata, captions, footnotes.          |
| `--warm`      | `#C8B89A`   | Section labels, accents, left-border highlights, italic emphasis. |
| `--accent`    | `#E8A85C`   | CTAs, step numbers, featured card borders, primary action color. |

### Semantic / Vibe Colors

| Token              | Hex         | Usage                              |
|--------------------|-------------|------------------------------------|
| Chill vibe         | `#7EC8A0`   | "Chill" vibe tags on event cards   |
| Energetic vibe     | `#E89B6C`   | "Energetic" vibe tags              |
| Social vibe        | `#C8B89A`   | "Social" vibe tags (same as warm)  |

### Transparency & Border Colors

| Usage                        | Value                            |
|------------------------------|----------------------------------|
| Card borders (default)       | `rgba(255, 255, 255, 0.05–0.06)` |
| Card borders (hover)         | `rgba(200, 184, 154, 0.15–0.2)` |
| Section dividers             | `rgba(255, 255, 255, 0.05)`     |
| FAQ dividers                 | `rgba(255, 255, 255, 0.08)`     |
| Ghost button border          | `rgba(255, 255, 255, 0.12)`     |
| Ghost button border (hover)  | `rgba(255, 255, 255, 0.3)`      |
| Nav background (scrolled)    | `rgba(14, 14, 12, 0.92)`        |
| Featured card gradient       | `linear-gradient(135deg, rgba(232,168,92,0.08), rgba(200,184,154,0.05))` |
| Featured card border         | `rgba(232, 168, 92, 0.25)`      |
| Warm tint (transparency card bg) | `rgba(200, 184, 154, 0.03)` |

### Rules

- **Never use pure white (`#FFFFFF`) for text.** Always use `--cream` (`#F1F0EC`).
- **Never use pure black (`#000000`) for backgrounds.** Always use `--bg` (`#0E0E0C`).
- **Accent (`#E8A85C`) is reserved for actions and numbered markers.** Do not use it for body text or decorative fill.
- **Warm (`#C8B89A`) is the workhorse brand color.** Use it for labels, emphasis, left-borders, and light accents — but never for primary CTAs.

---

## Typography

### Font Stack

| Role          | Family                          | Fallback             |
|---------------|---------------------------------|----------------------|
| Display       | **Playfair Display**            | `serif`              |
| Body / UI     | **DM Sans**                     | `sans-serif`         |

**Load via Google Fonts:**
```
DM Sans: 400, 500, 600, 700 (normal + italic)
Playfair Display: 400, 500, 600, 700 (normal + italic)
```

### Type Scale

| Element              | Family            | Size                        | Weight | Line Height | Letter Spacing | Notes                    |
|----------------------|-------------------|-----------------------------|--------|-------------|----------------|--------------------------|
| Hero headline (h1)   | Playfair Display  | `clamp(42px, 6vw, 72px)`   | 500    | 1.1         | -1.5px         | Max-width 720px          |
| Section title (h2)   | Playfair Display  | `clamp(28px, 4vw, 40px)`   | 500    | 1.2         | -0.8px         |                          |
| Final CTA headline   | Playfair Display  | `clamp(32px, 5vw, 48px)`   | 500    | 1.15        | -1px           | Centered                 |
| Card heading (h3)    | DM Sans           | 20px                        | 600    | 1.3         | 0              |                          |
| Transparency heading (h4) | DM Sans      | 17px                        | 600    | —           | 0              |                          |
| Hero subhead         | DM Sans           | `clamp(17px, 2vw, 20px)`   | 400    | 1.65        | 0              | Color: `--muted`         |
| Body / paragraph     | DM Sans           | 17px                        | 400    | 1.75        | 0              | Color: `--muted`         |
| Card body            | DM Sans           | 15px                        | 400    | 1.65        | 0              | Color: `--muted`         |
| Section label        | DM Sans           | 13px                        | 600    | —           | 2.5px          | Uppercase, color: `--warm` |
| Step number          | DM Sans           | 13px                        | 700    | —           | 0              | Color: `--accent`        |
| Step label text      | DM Sans           | 11px                        | 600    | —           | 1.5px          | Uppercase, color: `--warm` |
| Metadata / captions  | DM Sans           | 13px                        | 500    | —           | 0              | Color: `--muted`         |
| Micro text           | DM Sans           | 13px                        | 500    | —           | 0.3px          | Color: `--muted`         |
| FAQ question         | DM Sans           | 17px                        | 500    | 1.4         | 0              | Color: `--cream`         |
| FAQ answer           | DM Sans           | 15px                        | 400    | 1.65        | 0              | Color: `--muted`         |
| Nav logo             | Playfair Display  | 22px                        | 600    | —           | -0.5px         | Color: `--cream`         |
| Nav CTA              | DM Sans           | 14px                        | 600    | —           | 0.2px          |                          |
| Pricing amount       | DM Sans           | 36px                        | 700    | —           | 0              | Color: `--cream`         |
| Pricing label        | DM Sans           | 13px                        | 600    | —           | 1px            | Uppercase, color: `--muted` |
| Testimonial quote    | Playfair Display  | 16px                        | 400    | 1.6         | 0              | Italic, color: `--cream` |
| Testimonial author   | DM Sans           | 13px                        | 500    | —           | 0              | Color: `--muted`         |
| Problem punchline    | Playfair Display  | 21px                        | 600    | —           | 0              | Italic, color: `--cream` |

### Typography Rules

- **Playfair Display is for impact.** Headlines, punchlines, quotes, and the logo. Never for body text or UI labels.
- **DM Sans is for everything else.** Body, buttons, metadata, cards, FAQ, navigation.
- **Italic Playfair** is used for emotional emphasis — the word "blind" in the hero, punchline statements, and testimonial quotes.
- **Never use Inter, Roboto, Arial, or system fonts.** These are explicitly off-brand.
- **Section labels are always:** uppercase, 13px, weight 600, letter-spacing 2.5px, color `--warm`.

---

## Spacing & Layout

### Container

| Property    | Value   |
|-------------|---------|
| Max width   | 1140px  |
| Side padding| 28px    |
| Centering   | `margin: 0 auto` |

### Section Padding

| Context            | Padding        |
|--------------------|----------------|
| Standard sections  | 100px top/bottom |
| Hero               | 140px top, 80px bottom |
| Final CTA          | 120px top/bottom |
| Mobile sections    | 72px top/bottom |
| Mobile hero        | 120px top, 60px bottom |
| Mobile final CTA   | 80px top/bottom |

### Content Max-Widths

| Section          | Max Width |
|------------------|-----------|
| Hero headline    | 720px     |
| Hero subhead     | 520px     |
| Problem section  | 680px     |
| How-it-works sub | 560px     |
| Transparency     | 780px     |
| FAQ              | 680px     |
| Final CTA        | 600px     |
| Pricing          | 800px (outer), 660px (card grid) |

### Grid Specifications

| Grid              | Columns                                      | Gap   |
|-------------------|----------------------------------------------|-------|
| Steps (How It Works)| `repeat(auto-fit, minmax(280px, 1fr))`      | 24px  |
| Hang cards        | `repeat(auto-fill, minmax(260px, 1fr))`      | 16px  |
| Testimonials      | `repeat(auto-fill, minmax(300px, 1fr))`      | 20px  |
| Pricing cards     | `repeat(auto-fit, minmax(200px, 1fr))`       | 20px  |
| Transparency      | `repeat(auto-fit, minmax(220px, 1fr))`       | 20px  |

### Mobile Breakpoint

At `max-width: 640px`, all grids collapse to single-column (`grid-template-columns: 1fr`).

---

## Components

### Buttons

**Primary (CTA)**

| Property       | Value                     |
|----------------|---------------------------|
| Background     | `--accent` (`#E8A85C`)    |
| Text color     | `--bg` (`#0E0E0C`)        |
| Font           | DM Sans, 16px, weight 600 |
| Padding        | 16px 32px                 |
| Border radius  | 8px                       |
| Hover          | `translateY(-1px)`, opacity 0.9 |

**Nav CTA (compact)**

| Property       | Value                     |
|----------------|---------------------------|
| Background     | `--accent`                |
| Text color     | `--bg`                    |
| Font           | DM Sans, 14px, weight 600 |
| Padding        | 10px 22px                 |
| Border radius  | 6px                       |
| Hover          | opacity 0.88              |

**Secondary (Ghost)**

| Property       | Value                           |
|----------------|---------------------------------|
| Background     | transparent                     |
| Text color     | `--cream`                       |
| Font           | DM Sans, 16px, weight 500       |
| Padding        | 16px 32px                       |
| Border         | 1px solid `rgba(255,255,255,0.12)` |
| Border radius  | 8px                             |
| Hover          | border-color `rgba(255,255,255,0.3)` |

### Cards

**Standard Card (hang cards, testimonials)**

| Property       | Value                             |
|----------------|-----------------------------------|
| Background     | `--surface` (`#161614`)           |
| Border radius  | 10px                              |
| Padding        | 24–28px                           |
| Border         | 1px solid `rgba(255,255,255,0.05)` |
| Hover          | `translateY(-3px)`, border warms to `rgba(200,184,154,0.15)` |

**Step Card (How It Works)**

| Property       | Value                             |
|----------------|-----------------------------------|
| Background     | `--bg` (`#0E0E0C`)               |
| Border radius  | 12px                              |
| Padding        | 36px 32px                         |
| Border         | 1px solid `rgba(255,255,255,0.06)` |
| Hover          | border warms to `rgba(200,184,154,0.2)` |

**Pricing Card**

| Property       | Value                             |
|----------------|-----------------------------------|
| Background     | `--bg`                            |
| Border radius  | 12px                              |
| Padding        | 36px 24px                         |
| Border         | 1px solid `rgba(255,255,255,0.06)` |
| Featured bg    | `linear-gradient(135deg, rgba(232,168,92,0.08), rgba(200,184,154,0.05))` |
| Featured border| `rgba(232,168,92,0.25)`           |

**Transparency Card**

| Property       | Value                              |
|----------------|------------------------------------|
| Background     | `rgba(200,184,154,0.03)`          |
| Left border    | 2px solid `--warm`                 |
| Border radius  | 0 8px 8px 0                       |
| Padding        | 28px 24px                          |

### Navigation

| Property              | Value                              |
|-----------------------|------------------------------------|
| Height                | 68px                               |
| Position              | Fixed, z-index 100                 |
| Default background    | transparent                        |
| Scrolled background   | `rgba(14,14,12,0.92)`             |
| Scrolled backdrop     | `blur(16px)`                       |
| Scrolled border       | 1px solid `rgba(255,255,255,0.05)` |
| Transition trigger    | `scrollY > 50`                     |

### Input Fields

| Property       | Value                              |
|----------------|------------------------------------|
| Background     | `--surface`                        |
| Border         | 1px solid `rgba(255,255,255,0.1)`  |
| Border (focus) | `rgba(200,184,154,0.3)`           |
| Border radius  | 8px                                |
| Padding        | 16px 20px                          |
| Font           | DM Sans, 16px                      |
| Text color     | `--cream`                          |
| Placeholder    | `rgba(155,155,147,0.6)`           |

### FAQ Accordion

| Property           | Value                              |
|--------------------|------------------------------------|
| Question font      | DM Sans, 17px, weight 500          |
| Question padding   | 22px 0                             |
| Answer font        | DM Sans, 15px, weight 400          |
| Divider            | 1px solid `rgba(255,255,255,0.08)` |
| Toggle icon        | `+` character, 22px, weight 300, color `--warm` |
| Toggle animation   | `rotate(45deg)` on open, 0.3s ease |
| Answer expand      | `max-height` 0 → 200px, 0.4s ease |

---

## Motion & Animation

### Scroll Reveal (Fade In)

| Property       | Value                    |
|----------------|--------------------------|
| Initial state  | `opacity: 0`, `translateY(28px)` |
| Visible state  | `opacity: 1`, `translateY(0)`    |
| Duration       | 0.7s ease                |
| Trigger        | IntersectionObserver, threshold 0.12 |
| Stagger delays | 0–0.45s depending on element order |

### Hover Transitions

| Element          | Effect                              | Duration   |
|------------------|-------------------------------------|------------|
| Primary button   | `translateY(-1px)`, opacity 0.9     | 0.2s       |
| Ghost button     | Border color brightens              | 0.2s       |
| Nav CTA          | opacity 0.88                        | 0.2s       |
| Step cards       | Border color warms                  | 0.3s       |
| Hang cards       | `translateY(-3px)`, border warms    | 0.25s ease |
| FAQ icon         | `rotate(45deg)`                     | 0.3s ease  |

### Nav Transition

| Property         | Duration | Trigger        |
|------------------|----------|----------------|
| Background       | 0.3s ease| scrollY > 50px |
| Backdrop filter   | 0.3s ease| scrollY > 50px |
| Border color     | 0.3s ease| scrollY > 50px |

---

## Visual Effects & Texture

### Grain Overlay (Hero)

Applied as an SVG noise filter via `::before` pseudo-element on the hero section, at `opacity: 0.03`. Creates subtle texture that prevents the dark background from feeling flat.

### Warm Glow (Hero + Final CTA)

A radial gradient positioned off-canvas (top-right for hero, centered for final CTA) using `rgba(232,168,92,0.03–0.025)`. Adds atmospheric warmth without being visible as a discrete element.

### Section Alternation

Sections alternate between `--bg` and `--surface` backgrounds. Dividers between `--bg` sections use a 1px line at `rgba(255,255,255,0.05)`.

---

## Responsive Behavior

### Breakpoint: 640px

| Change                          | Desktop                    | Mobile            |
|---------------------------------|----------------------------|-------------------|
| Section padding                 | 100px 0                   | 72px 0            |
| Hero padding                    | 140px top, 80px bottom    | 120px top, 60px bottom |
| Final CTA padding               | 120px 0                   | 80px 0            |
| All grids                       | Multi-column              | Single column     |
| Pricing grid max-width          | 660px                     | 320px             |
| Email form                      | Row (flex)                | Column (stacked)  |
| Email input min-width           | 260px                     | Full width        |

### Fluid Typography

Headlines use `clamp()` for smooth scaling between mobile and desktop — no abrupt size jumps at breakpoints.

---

## Anti-Patterns (Do Not)

- **Do not** use pure white or pure black anywhere.
- **Do not** use Inter, Roboto, Arial, or system-default fonts.
- **Do not** use Playfair Display for body text, buttons, or UI labels.
- **Do not** use the accent color (`#E8A85C`) for anything other than CTAs and numbered markers.
- **Do not** use bright saturated colors. The palette is muted and warm.
- **Do not** use sharp box shadows. Use border-based elevation with low-opacity warm tones.
- **Do not** use abrupt transitions. All state changes should animate at 0.2–0.7s.
- **Do not** center body text. Only headlines and the final CTA section use centered alignment.
- **Do not** exceed content max-widths. Respect the per-section constraints listed above.

---

*This document is the visual source of truth for Rekindled. When any surface conflicts with this guide, the guide wins.*
