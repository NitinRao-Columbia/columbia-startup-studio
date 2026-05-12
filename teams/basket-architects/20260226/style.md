# STYLE_GUIDE.md — Vouch

**Purpose:** Define the visual identity for Vouch so that every page, screen, and asset feels cohesive. This document is also an AI onboarding doc: when you hand it to a code agent alongside your BRAND_POSITION.md, the agent generates consistent, on-brand output.

---

## 1. Visual Tone

**Overall feel:** Warm editorial confidence. A curator's magazine, not a growth hacker's landing page. Feels like a tasteful friend recommended it — not like it was served by an algorithm.

**What it is:** Intentional, warm, quietly confident

**What it is not:** Not hype-y, not cold/tech-minimalist, not playful/gamified

---

## 2. Color Palette

Generated via the landing page build and tested across all sections for contrast and cohesion. Warm earth tones anchored by terracotta as the primary accent.

| Name | Hex | Role |
|------|-----|------|
| **Terracotta** | #c2653a | Primary accent — buttons, links, key actions, CTAs, emphasis |
| **Amber** | #d4943a | Supporting accent — badges, rating mid-range, gradient partner |
| **Sage** | #7a8c72 | Selective emphasis — success states, checkmarks, positive signals |
| **Cream** | #faf7f2 | Page canvas — primary background |
| **Charcoal** | #1a1714 | Body text, headings, primary button fill, dark sections |
| **Text Body** | #4a4541 | Body copy — warm dark gray |
| **Text Muted** | #8a8480 | Captions, labels, helper text, secondary info |
| **Terracotta Light** | #e8a882 | Accent on dark backgrounds, hover glow, testimonial attribution |
| **Cream Deep** | #f3ede4 | Section alternation background, feature cards |
| **Warm White** | #fefcf9 | Card surfaces, elevated surfaces, phone screen |
| **Sage Light** | #e8ede5 | Trust sections, cold-start callout background |
| **Stone** | #d6cfc5 | Borders, dividers, secondary button outlines |
| **Stone Light** | #eae6df | Card borders, step number color, light separators |

### Color Rules

- Never use pure black (`#000000`) for text — `#1a1714` (Charcoal) is the darkest
- Terracotta is the only accent that appears on buttons and primary CTAs
- Sage and Amber are supporting — they never compete with Terracotta for attention
- Dark sections use `#1a1714` or `#2d2926` as background with Cream/Stone text
- Gradient accents: always Terracotta → Amber → Sage (warm to cool) for decorative lines
- WCAG AA contrast: all body text meets 4.5:1 ratio against its background

---

## 3. Typography

**Heading font:** Libre Baskerville (Google Fonts) — editorial serif, warm authority
**Body font:** Outfit (Google Fonts) — clean geometric sans, highly readable

**Why this pairing:** The serif/sans contrast signals "curated taste" without being stuffy. Libre Baskerville carries the brand voice (a magazine editor); Outfit keeps the UI crisp and modern. This pairing was tested across the full landing page build and works at every scale.

### Type Scale

| Style | Size | Weight | Usage |
|-------|------|--------|-------|
| H1 | clamp(2.4rem, 5.5vw, 4rem) | 400 (Regular) | Hero headline only |
| H2 | clamp(1.5rem, 3vw, 2.2rem) | 400 (Regular) | Section titles |
| H3 | clamp(1.1rem, 2vw, 1.4rem) | 400 (Regular) | Subsection headers |
| Body | clamp(0.95rem, 1.8vw, 1.08rem) | 400 | Paragraph text |
| Label | 0.72rem | 600 | Section labels, tags — uppercase, 0.14em tracking, Terracotta |
| Small | 0.82–0.85rem | 400 | Captions, card metadata, helper text |

### Typography Rules

- Headings are always Regular weight (400) — bold serif looks heavy and generic
- Labels are always uppercase Outfit with wide letter-spacing (0.14em) in Terracotta
- Body copy max-width: 640px — prevents eye fatigue on wide screens
- Italics in Libre Baskerville are used for key emotional phrases (e.g., "ranked." in hero)
- Italic + Terracotta color = the highest emphasis combination (use very sparingly)
- Never bold a heading — the serif weight carries enough authority at 400

---

## 4. Component Patterns

### Buttons

| Type | Style | Usage |
|------|-------|-------|
| **Primary CTA** | Charcoal (#1a1714) fill, Cream text, 50px border-radius (pill), 14px 28px padding | Main action: "Get Early Access" |
| **Primary Hover** | Terracotta (#c2653a) fill, translateY(-2px), shadow-lg | Hover reveals brand accent |
| **Secondary** | Transparent, 1.5px Stone (#d6cfc5) border, Charcoal text, 50px radius | Alternative actions: "See How It Works" |
| **Secondary Hover** | Border darkens to Charcoal, translateY(-2px) | Subtle lift |

### Cards

- Background: Warm White (#fefcf9) or Cream (#faf7f2)
- Border: 1px Stone Light (#eae6df), or 1.5px Terracotta for featured
- Border radius: 14px standard, 20px for large/featured cards
- Padding: 24–32px (generous)
- Hover: translateY(-4px) + shadow-md (`0 4px 20px rgba(26,23,20,0.08)`)

### Rating Cards (Product-Specific)

- Dark background: `rgba(255,255,255,0.06)` with 1px `rgba(255,255,255,0.08)` border
- Rating number: 2.2rem, Outfit 700, color-coded:
  - High (7–10): Sage/green `#6ee7b7`
  - Mid (5–6): Amber `#d4943a`
  - Low (1–4): Terracotta Light `#e8a882`
- Tags: pill-shaped, matching color at 12% opacity background

### Form Inputs (Email Capture)

- Background: Warm White (#fefcf9)
- Border: 1.5px Stone, 50px border-radius (pill, matching buttons)
- Focus state: border transitions to Terracotta
- Placeholder: Text Muted (#8a8480), Outfit 400
- Height: matches adjacent button for inline layout on desktop
- Mobile: stacks vertically, button goes full-width

---

## 5. Imagery & Icons

**Icon style:** Emoji for inline icons (phone mockup categories, scenario cards). Simple and universal — no custom icon set needed at this stage.

**Phone Mockup:** The hero features a mock phone UI showing the actual product interface. This addresses the #1 user-testing objection ("need to see the interface"). Uses Charcoal frame, Warm White screen, real-looking data (place names, ratings, dates, neighborhoods), and floating cards showing analytics + friend activity.

**Photography/illustration style:** Not needed at launch. The phone mockup and rating cards provide visual interest. When photography is introduced: warm natural lighting, real urban environments, casual social settings. Never staged.

**What to avoid:** Stock photos of people using phones. Gradient blob backgrounds. Abstract 3D illustrations. Anything that says "generic SaaS."

---

## 6. Motion & Atmosphere

### Animations

| Effect | Implementation | Timing |
|--------|---------------|--------|
| Scroll reveal | Elements enter from 24px below with opacity fade | 0.7s, cubic-bezier(0.23, 1, 0.32, 1) |
| Stagger | Sequential elements use 0.1s / 0.2s / 0.3s delay classes | Same easing |
| Card hover | translateY(-4px) + shadow-md | 0.3s ease |
| Button hover | translateY(-2px) + color change + shadow-lg | 0.3s cubic-bezier |
| Nav glass | Background + blur appears on scroll >60px | 0.4s ease |

### Texture

- Film grain overlay: SVG fractalNoise at 2.5% opacity, fixed position, pointer-events: none
- Subtle radial gradients at section level (brand colors at 4–8% opacity) for depth

---

## Implementation Notes

- **CSS framework:** Vanilla CSS with CSS custom properties (no Tailwind — the design relies on precise custom values that would fight utility classes)
- **Font loading:** Google Fonts with `preconnect` to `fonts.googleapis.com` and `fonts.gstatic.com`
- **Responsive:** Mobile-first. Primary breakpoint at 768px. Hero grid collapses to single column. Phone mockup scales down, floating cards hide on mobile. Email form stacks vertically.
- **Performance:** Single HTML file with inline CSS. No external dependencies except Google Fonts. JS limited to nav scroll, IntersectionObserver, smooth scroll, and form handling.
- **Deployment:** Any static host (Vercel, Netlify, Cloudflare Pages). Zero build step.