# STYLE_GUIDE.md — [Your Product Name]

**Purpose:** Define the visual identity for your product so that every page, screen, and asset feels cohesive. This document is also an AI onboarding doc: when you hand it to a code agent alongside your BRAND_POSITION.md, the agent generates consistent, on-brand output.

---

## 1. Visual Tone

<!-- One to two sentences that capture the overall feel of your brand.
     This is the single most important section. Everything else flows from this. -->

**Overall feel:** [e.g., "Clean and confident with subtle warmth. Modern but not cold."]

**What it is:** [2-3 descriptors, e.g., minimal, trustworthy, approachable]

**What it is not:** [2-3 anti-descriptors, e.g., not playful, not corporate, not edgy]

<!-- Examples:
     - "Intentional, grounded, quietly confident" (wellness app)
     - "Calm intelligence with professional warmth" (B2B SaaS)
     - "Warm, steady, clear — clinically grounded" (health tech)
-->

---

## 2. Color Palette

<!-- Use coolors.co to generate your palette. Lock your primary brand color
     and regenerate around it. Export hex codes and paste them here.

     You need at minimum:
     - 1 primary color (your brand color — buttons, links, key accents)
     - 1-2 secondary/accent colors (supporting colors for variety)
     - 1 background color (page canvas)
     - 1 text color (body copy — avoid pure black #000000)
     - 1 error/alert color (for form validation, warnings) -->

| Name | Hex | Role |
|------|-----|------|
| **[Primary]** | #______ | Primary accent — buttons, links, key actions |
| **[Secondary]** | #______ | Supporting accent — section highlights, hover states |
| **[Accent]** | #______ | Selective emphasis — badges, tags, small highlights |
| **[Background]** | #______ | Page canvas and card backgrounds |
| **[Text]** | #______ | Body text and headings |
| **[Error]** | #______ | Error states, alerts, destructive actions |

### Color Rules

- Avoid pure black (`#000000`) for text; use a dark gray instead
- Accent colors should not compete with primary for attention
- Ensure sufficient contrast between text and background (aim for WCAG AA: 4.5:1 ratio for body text)

---

## 3. Typography

<!-- Pick two fonts max. One for headings, one for body.
     Google Fonts (fonts.google.com) is the easiest source.
     Fontjoy (fontjoy.com) can suggest pairings.

     Common strong pairings:
     - Inter (body) + anything (it pairs with everything)
     - Poppins (headings) + Inter (body)
     - DM Sans (headings) + Inter (body)
     - Space Grotesk (headings) + Inter (body) -->

**Heading font:** [e.g., Inter, Poppins, DM Sans]
**Body font:** [e.g., Inter, system sans-serif]

### Type Scale

| Style | Size | Weight | Usage |
|-------|------|--------|-------|
| H1 | 2.25rem | Bold | Page title, hero headline |
| H2 | 1.75rem | Bold | Section titles |
| H3 | 1.375rem | Semibold | Subsection headers |
| Body | 1rem | Regular | Paragraph text |
| Small | 0.875rem | Regular | Captions, labels, helper text |

### Typography Rules

- Keep headings short and declarative
- Body copy should be highly readable; favor short paragraphs
- Use bold sparingly for structural emphasis, not decoration

---

## 4. Component Patterns

<!-- Light touch. Define just enough so your landing page looks consistent.
     You can expand this as you build more of the product. -->

### Buttons

| Type | Style | Usage |
|------|-------|-------|
| **Primary CTA** | Filled with [Primary color], white text, rounded corners | Main action: "Join Waitlist", "Get Early Access" |
| **Secondary** | Outlined with [Primary color], transparent background | Alternative actions |

### Cards (if used)

- Background: white or light variant of background color
- Border: subtle (1px, light gray) or shadow
- Border radius: [e.g., 8px, 12px, fully rounded]
- Padding: generous (at least 16px)

### Form Inputs

- Border radius: [e.g., 8px]
- Focus state: ring or border highlight in [Primary color]
- Placeholder text: muted gray

---

## 5. Imagery & Icons (Optional)

<!-- Skip this section if you don't have imagery needs yet.
     Fill it in when you start building real pages. -->

**Icon style:** [e.g., "Simple line icons, rounded strokes" or "Lucide icons" or "Heroicons"]

**Photography/illustration style:** [e.g., "Warm, natural lighting, real people" or "Clean product shots on white" or "Abstract/minimal illustrations"]

**What to avoid:** [e.g., "Stock photos that feel staged", "Overly polished lifestyle imagery"]

---

## Implementation Notes

<!-- Add any technical notes as you start building.
     These help AI code agents make better decisions. -->

- **CSS framework:** [e.g., Tailwind, vanilla CSS, Bootstrap]
- **Deployment:** [e.g., Vercel, Netlify, Carrd, Framer]
- **Responsive:** mobile-first design; test at 375px width minimum

---

<!--
GETTING STARTED (delete this section when you're done):

1. Fill in Visual Tone first — this guides everything else
2. Generate colors on coolors.co, paste hex codes into the Color Palette table
3. Pick fonts on Google Fonts, update the Typography section
4. Define your primary button style at minimum
5. Hand this file + BRAND_POSITION.md to your code agent when building your landing page

This should take ~15 minutes. Don't overthink it.
You can always iterate as you build.
-->
