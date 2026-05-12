# Copy Changelog: V1 → V2
**Test run:** 20260224.01 | **Eval date:** 2026-02-24 | **n=60**

Each change below is linked to a specific finding from `summary_v1.md`.

---

## P0 Changes (blocking — applied before V2 eval)

### 1. Hero headline rewritten to lead with "Receipt"
**Before:** "Stop the manual grind. Start finding the answers."  
**After:** "Every change has a 'Receipt.' Every decision has a trail."

**Evidence:** "Receipt" line selected by 15 of 60 personas as the strongest line in the copy — 2.5x more than the second-ranked line. The current H1 was flagged as generic startup-speak by ai_loop_prisoner and ai_weary_old_school_analyst. Moving the highest-resonance line to the H1 position is the highest-confidence change available.

---

### 2. Sub-headline rewritten — removed "indestructible timeline of logic"
**Before:** "Data work shouldn't feel like a house of cards. CleanSheet turns scattered spreadsheets and legacy scripts into a single, indestructible timeline of logic."  
**After:** "Data work breaks when key people leave. CleanSheet turns your scattered spreadsheets, inherited scripts, and ad-hoc analyses into a single workspace with a permanent, auditable history — so anyone can pick it up, and no one has to start from scratch."

**Changes made:**
- "indestructible timeline of logic" → "permanent, auditable history" — The old phrase was cited by ~40 personas as overwrought or AI-sounding
- "house of cards" → "breaks when key people leave" — More specific, maps to the tribal-knowledge pain that all buckets recognized
- Added **"Works with Excel, Google Sheets, Python, R, MATLAB, and SQL."** — This line directly addresses the #1 unanswered question from duct_tape_analyst (all 10 personas): "Does this work with Excel?" Without an explicit mention in the hero section, this bucket soft-exits before reading further.

---

### 3. "Polyglot Logic Engine" section renamed and rewritten
**Before:** Section heading "The Polyglot Logic Engine" with "Paste your Python, MATLAB, or R scripts directly into the flow. We deconstruct complex code into visual 'Logic Blocks'..."  
**After:** "Step 2: Connect your logic into a visual workspace." with plain-language description of what happens.

**Evidence:** "Polyglot Logic Engine" was flagged by approximately 55 of 60 personas across all buckets as the primary jargon failure. Verbatim: "sounds like AI invented these terms yesterday," "marketing trying too hard to sound technical," "not how anyone talks." The rename is also aligned with canonical brand language ("One workspace for any language or logic") from brand-positioning.md.

**Also changed:**
- "deconstruct complex code into visual Logic Blocks" → "maps them into a connected, visual flow" — "deconstruct" was repeatedly flagged as a red flag word for ai_weary_old_school_analyst ("that's a massive red flag — does it break my scripts?")
- Added: "No rewrites. No migrations. Bring your work as it is." — Directly addresses duct_tape_analyst's objection about migration burden

---

### 4. "Transparency Tax" phrase removed
**Before:** "We pay the 'Transparency Tax' for you by automatically generating the documentation and explanations for your methods as you work."  
**After:** "CleanSheet handles the documentation and logging so you don't have to."

**Evidence:** "Transparency Tax" cited alongside "Polyglot Logic Engine" as invented jargon with no audience recognition. 0 of 60 personas used this framing unprompted. The plain-language replacement preserves the actual product claim without the brand-invented vocabulary.

---

### 5. Testimonials replaced
**Before:** USC Brain and Music Lab (genomics/music research), Settlement Housing Fund (education-adjacent), Cancer Genetics researcher  
**After:** Operations Analyst (healthcare system), Data Analyst (growth startup), Research Director (public health nonprofit)

**Evidence:** 5 of 6 buckets flagged the testimonials as wrong-audience signals. Verbatim from duct_tape_analyst: "I work in operations, not a research lab." Social_science_thesis: "I saw 'genomic research' and that was it." Budget_gatekeeper: "The testimonials are from institutions that have nothing to do with program evaluation and impact reporting."

New testimonials are written to match the three highest-volume objection clusters:
- Persona 1 → duct_tape_analyst pain (inherited multi-person workbooks)
- Persona 2 → ai_loop_prisoner pain (validating AI-generated code)
- Persona 3 → budget_gatekeeper pain (grant committee auditability + institutional pricing justification)

---

## P1 Changes (high-impact, applied in V2)

### 6. Free trial added to pricing and CTA
**Before:** Individual tier with no trial mentioned. CTA: "Join the waitlist."  
**After:** "14-day free trial" added to Individual tier. CTA offers both "Start Free Trial" and "Join the Waitlist."

**Evidence:** Free trial was the most consistently requested item across all buckets that didn't cite it as a dealbreaker (ai_loop_prisoner, ai_weary, budget_gatekeeper all listed "no trial option" in objections). Duct_tape_analyst: "$29 steep when I don't know if it handles my use case — I'd need a free trial." The waitlist-only CTA was a soft-close blocker for every bucket below skeptical conviction.

---

### 7. Institutional pricing clarified
**Before:** "Institutional — $2,500/year" (no further detail)  
**After:** "Institutional — $2,500/year — Unlimited users, priority support, compliant audit exports, academic licensing"

**Evidence:** Budget_gatekeeper consistently flagged the institutional tier as confusing. The jump from $149/month team to $2,500/year institutional prompted questions about seat limits, support quality, and whether this was actually cheaper per month. "Is that unlimited seats or a fixed number? What's the SLA? What's included?" — cited by 7 of 10 budget_gatekeeper personas.

---

### 8. CTA rewritten
**Before:** "Close the gap between 'now' and 'results.' Stop managing files and start managing insights."  
**After:** "Stop managing files. Start defending results."

**Evidence:** "Managing insights" was flagged as vague by multiple buckets. "Defending results" maps directly to the brand's core value proposition (auditability, receipts, methodological credibility) and is actionable language that connects to the transparency_trust finding (mean: 1.9/5 — showing that V1 did not establish product credibility).

---

## What Was Not Changed

- The three-tier pricing structure — price point is not broken; credibility is
- The "How It Works" three-step structure — the format is right; the labels and language needed updating
- The objection handling section structure — the three objections being addressed are the right ones; the responses needed rewriting
- Pain framing in sub-headline — tribal knowledge / "breaks when key people leave" is the strongest observed pain framing

---

### 9. Zip upload + legacy codebase sense-making added (user-directed, V2 amendment)
**Added to:** Hero sub-headline (last line) and Step 2 section  
**Content added:**
- Hero: "Upload a zip file and we'll make sense of it" — makes the onboarding mechanic concrete in the first section
- Step 2 rewritten to lead with the zip/multi-file upload as the primary interaction, explicitly naming mixed-language and multi-author legacy codebases as the target input

**Rationale:** Addresses duct_tape_analyst and ai_weary_old_school_analyst objections about migration friction. The recurring unanswered question "How do I get my existing files into this?" is now answered before the objection section. Also materially differentiates from git-based alternatives — ai_weary personas asked "what does this do that Git + Jupyter don't?" — parsing a messy zip of inherited files is something git does not do.

---

## What Was Deferred to V3

- Product screenshot or UI demo (P1) — requires design asset; flagged as #1 "show don't tell" request by ai_weary_old_school_analyst
- Technical documentation link for skeptical_quant_methodologist (P2) — needs a dedicated methods/whitepaper page
- Student pricing tier for social_science_thesis_dreader (P2) — pricing policy decision required
- Data security / compliance section for budget_gatekeeper (P2) — requires legal/compliance review
- "If you can use a search bar" language — removed in spirit through full objection section rewrite; flagged as condescending but the rewrite addresses root cause

---

*V1 copy preserved at: `copy_v1.md`*  
*V2 copy: `copy_v2.md`*  
*Eval results that drove these decisions: `results_v1.json`, `summary_v1.md`*
