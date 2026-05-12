# Freeweight Style Guide

## Brand Identity

Freeweight is built for serious athletes and coaches. The visual language should feel precise, performance-oriented, and minimal. Nothing decorative. Every design choice should reduce cognitive load, not add to it.

---

## Colors

| Name | Hex | Usage |
|---|---|---|
| Base | `#1a1e22` | Primary background |
| Surface | `#22282e` | Cards, modals, elevated surfaces |
| Accent | `#c9f44e` | CTAs, highlights, active states, labels |
| White | `#ffffff` | Primary text on dark backgrounds |
| Muted | `#7a8a7e` | Secondary text, placeholders, disabled states |

### Rules
- Background is always Base (`#1a1e22`). Never white or light.
- Accent (`#c9f44e`) is used sparingly. It signals action or importance. Do not use it decoratively.
- Text on Base: White for primary, Muted for secondary.
- Never put Accent text on a white background.

---

## Typography

| Role | Font | Weight | Size (mobile) | Size (web) |
|---|---|---|---|---|
| Display / Hero | Arial Black | 900 | 32px | 48px |
| Heading 1 | Arial Black | 900 | 24px | 36px |
| Heading 2 | Arial Black | 900 | 18px | 24px |
| Body | Arial | 400 | 14px | 16px |
| Label / Overline | Arial | 700 | 10px | 11px |
| Caption | Arial | 400 | 12px | 13px |

### Rules
- Headings are always Arial Black. No exceptions.
- Body copy is Arial Regular.
- Labels and overlines (e.g. category tags above section headers) are Arial Bold, all caps, with tracked letter-spacing (3-4px).
- No serif fonts anywhere in the product.

---

## Spacing

Base unit: `8px`

| Token | Value |
|---|---|
| xs | 4px |
| sm | 8px |
| md | 16px |
| lg | 24px |
| xl | 32px |
| 2xl | 48px |
| 3xl | 64px |

All padding, margin, and gap values should be multiples of 8.

---

## Components

### Buttons

**Primary**
- Background: `#c9f44e`
- Text: `#1a1e22` (dark, not white)
- Font: Arial Bold
- Border radius: 6px
- Padding: 12px 24px

**Secondary**
- Background: transparent
- Border: 1px solid `#c9f44e`
- Text: `#c9f44e`
- Same radius and padding as primary

**Destructive**
- Background: transparent
- Border: 1px solid `#ff4f4f`
- Text: `#ff4f4f`

### Cards
- Background: `#22282e`
- Border radius: 8px
- Padding: 16px
- No drop shadows. Elevation is communicated through color contrast only.

### Input Fields
- Background: `#22282e`
- Border: 1px solid `#7a8a7e`
- Active border: `#c9f44e`
- Text: `#ffffff`
- Placeholder: `#7a8a7e`
- Border radius: 6px
- Padding: 12px 16px

### Tags / Labels
- All caps
- Arial Bold
- Font size: 10-11px
- Letter spacing: 3-4px
- Color: `#c9f44e`
- No background unless needed for contrast

---

## Iconography

- Use simple, single-weight line icons
- Icon color follows text color in context (white for primary, muted for secondary, accent for active)
- Do not mix icon styles

---

## Motion

- Keep animations fast: 150-200ms for micro-interactions, 250-300ms for transitions
- Easing: ease-out for entrances, ease-in for exits
- No decorative animations. Motion should only communicate state change.

---

## Voice and Tone

- Direct. No fluff.
- Written for athletes, not general consumers.
- Short labels, short CTAs. "Start workout" not "Begin your workout session."
- Error messages are plain and actionable. "Coach code not found. Check with your coach." not "An unexpected error has occurred."

---

## Do / Don't

| Do | Don't |
|---|---|
| Use accent color for one clear action per screen | Use accent on multiple competing elements |
| Keep workout execution UI to large tap targets | Add decorative elements in workout flow |
| Use muted color for secondary information | Use muted color for anything the user needs to act on |
| Write labels in all caps with tracking | Mix label styles |
| Keep backgrounds dark throughout | Introduce light mode inconsistencies |