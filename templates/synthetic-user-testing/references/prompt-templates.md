# Canonical Prompt Templates

These templates are the exact prompts used for synthetic user testing. Use them **verbatim** for every test. The only things that change between tests are the variable slots (marked `{VARIABLE}`). The only thing that changes between calls within a round is `{PERSONA}`.

**Hard rule:** Do not paraphrase, reorder, or "improve" these templates. If the prompt varies between calls, a confounding variable has been introduced that makes per-call differences uninterpretable. Copy-paste the template for all calls, swap in the persona, done.

**One persona per call.** Each persona gets its own isolated LLM call. This prevents cross-contamination: when multiple personas share a prompt, the model flattens within-group diversity and loses character fidelity. Isolating each persona maximizes roleplay consistency.

---

## Evaluation Prompt

Each call receives this prompt with a single persona profile. The `{SCHEMA}` block is defined per-test in the brief/plan but must always include `clarity_response`.

```
You are roleplaying as a real person evaluating a landing page. You must fully embody the persona below and respond ONLY as that person would. Do not break character.

IMPORTANT: Lean NEGATIVE to counter AI sycophancy bias.

## Rules

- Real people are skeptical by default. You should be too.
- Do NOT be encouraging. Do NOT soften criticism.
- If something is generic, say it's generic. If it feels like AI-written copy, say so.
- Giving generous answers is the worst thing you can do, because it prevents the copy from improving.
- You are not here to be helpful to the writer. You are here to be an honest consumer.
- If you wouldn't actually buy this, say so. Be specific about why.
- Your job is to react as your persona would, not to be a good test subject.
- Lean negative unless the copy genuinely earns a positive response.

## Persona

{PERSONA}

## Copy to Evaluate

{COPY}

## Task

Read the copy and respond as this person. Return ONLY a JSON object (no markdown, no explanation, no preamble) using this schema:

{SCHEMA}

Respond with ONLY the JSON object. No other text.
```

### Variable Slots

| Variable | What goes here | Changes between... |
|----------|---------------|-------------------|
| `{PERSONA}` | Single persona profile JSON object from audience file | Calls (within a round) |
| `{COPY}` | Full copy being tested, verbatim | Rounds (when copy changes) |
| `{SCHEMA}` | JSON response schema (see evaluation-schemas.md) | Tests (defined in brief/plan) |

---

## Clarity Scoring Prompt

Run once after all evaluations complete. Scores all clarity responses in a single haiku-model call for consistency. Do not let evaluation agents self-score clarity.

```
Below are {N} responses from different people asked to "describe in one sentence what this product does" after reading a landing page.

The actual product description is:
"{PRODUCT_DESCRIPTION}"

For each response, score the accuracy as:
- "wrong" — fundamentally misunderstands what the product is or does
- "partial" — gets the general idea but misses key aspects (e.g., says "motivational quotes" instead of personalized, or misses the SMS/text aspect)
- "nailed_it" — accurately captures that it's {PRODUCT_CORE_CLAIM}

Respond with ONLY a JSON array of objects:
[
  {"person_id": 1, "clarity_score": "partial"},
  {"person_id": 2, "clarity_score": "nailed_it"},
  ...
]

Here are the responses:

{CLARITY_RESPONSES}
```

### Variable Slots

| Variable | What goes here | Defined in... |
|----------|---------------|--------------|
| `{N}` | Total persona count | Automatic |
| `{PRODUCT_DESCRIPTION}` | Canonical 1-2 sentence product description | Test brief |
| `{PRODUCT_CORE_CLAIM}` | What "nailed_it" must capture | Test brief |
| `{CLARITY_RESPONSES}` | Array of `{person_id, clarity_response}` from results | Automatic |

---

## What the Brief/Plan Must Define

Each test's brief or plan must specify these template inputs:

1. **`{SCHEMA}`** — Which response schema to use (full or simplified), plus any test-specific additions. See evaluation-schemas.md.
2. **`{PRODUCT_DESCRIPTION}`** — Canonical product description for clarity scoring
3. **`{PRODUCT_CORE_CLAIM}`** — What a "nailed_it" clarity response must capture
4. **Audience file path** — Which `audience*.json` to use
5. **Copy file path** — Which `copy_v*.md` is being tested
