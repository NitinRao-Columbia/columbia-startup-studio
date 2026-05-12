# Evaluation Schemas

## Full Schema (V1-V5)

Use for early rounds when maximum qualitative signal is needed.

```json
{
  "person_id": "<number from profile>",
  "bucket": "<bucket from profile>",
  "resonance": "<strongly_disagree|disagree|neutral|agree|strongly_agree>",
  "clarity_response": "<describe in one sentence what this product does>",
  "intent": "<strongly_disagree|disagree|neutral|agree|strongly_agree>",
  "conversion_confidence": "<strongly_disagree|disagree|neutral|agree|strongly_agree>",
  "price_perception": "<too_expensive|fair|good_deal>",
  "strongest_line": "<single line from the copy that resonated most>",
  "what_feels_off": "<anything generic, try-hard, or dishonest-feeling>",
  "objections": "<what's stopping you from signing up>",
  "dealbreaker": "<true|false>",
  "dealbreaker_reason": "<why, or null if dealbreaker is false>",
  "gut_reaction": "<1-2 sentences, first impression>",
  "unanswered_questions": "<what the page didn't answer>",
  "price_reaction": "<specific thoughts on pricing tiers>"
}
```

## Simplified Schema (V6+)

Acceptable for later rounds when the qualitative themes are established. Produces faster results with no loss of core signal.

```json
{
  "person_id": "<number from profile>",
  "bucket": "<bucket from profile>",
  "resonance": "<strongly_disagree|disagree|neutral|agree|strongly_agree>",
  "clarity_response": "<describe in one sentence what this product does>",
  "intent": "<strongly_disagree|disagree|neutral|agree|strongly_agree>",
  "conversion_confidence": "<strongly_disagree|disagree|neutral|agree|strongly_agree>",
  "price_perception": "<too_expensive|fair|good_deal>",
  "strongest_line": "<single line from the copy that resonated most>",
  "what_feels_off": "<anything generic, try-hard, or dishonest-feeling>",
  "objections": "<what's stopping you from signing up>",
  "dealbreaker": "<true|false>",
  "dealbreaker_reason": "<why, or null if dealbreaker is false>"
}
```

## Schema Rules

- **`clarity_response` is mandatory in ALL schemas.** V10 of the gratitude LP study dropped it from the simplified schema, which meant the clarity scoring pass had nothing to score and clarity data was lost for all 60 personas. Clarity is the only dimension that catches comprehension failures invisible to other metrics (high resonance + wrong understanding = false signal).
- Individual tests can **add** fields to either schema but should never **remove** `clarity_response`.
- `resonance`, `intent`, `conversion_confidence`: enum `"strongly_disagree"`, `"disagree"`, `"neutral"`, `"agree"`, `"strongly_agree"`
- `clarity_response`: free text (the synthetic person's description of the product)
- `clarity_score`: enum `"wrong"`, `"partial"`, `"nailed_it"` (scored separately via the clarity scoring prompt, not by eval agents)
- `price_perception`: enum `"too_expensive"`, `"fair"`, `"good_deal"`
- `dealbreaker`: boolean (`true` if any objection is a hard no)
- All qualitative fields: free text, 1-3 sentences max

---

## Narrative JSON Schema

The narrative is a JSON file that feeds into the report generator. Write one for each round from V6 onward. This is where the researcher's interpretation lives; it separates raw data from meaning.

**Critical formatting rules:**
- `findings`, `recommendations`, `qualitative_themes` must be **HTML strings** (not arrays)
- `bucket_deep_dives` must be a **dict keyed by bucket name** (not an array of objects)
- The report generator reads these directly as HTML

```json
{
  "version": "VN",
  "researchers_stance": "1-2 paragraph overall assessment",
  "exec_summary": "What was tested and what happened",
  "findings": "<ul><li><strong>Title</strong>: Detail</li>...</ul>",
  "recommendations": "<ol><li><strong>Action</strong>: Rationale</li>...</ol>",
  "qualitative_themes": "<ul><li><strong>Theme</strong> (N mentions): Quote</li>...</ul>",
  "clarity_notes": "Notes on clarity scoring (or 'unscored: N' if not run)",
  "invalidated_segments": [],
  "appendix_notes": "Caveats about audience changes, comparability, etc.",
  "bucket_deep_dives": {
    "bucket_name": "<h4>Headline</h4><p>Narrative</p><p><strong>Key personas:</strong> ...</p><p><strong>Risk:</strong> ...</p>"
  }
}
```

---

## Audience Persona Schema

Each person in the audience file follows this structure:

```json
{
  "person_id": 1,
  "name": "First Last",
  "age": 32,
  "gender": "female",
  "location": "City, ST",
  "bucket": "bucket_name",
  "occupation": "Job title",
  "life_stage": "Brief life context",
  "relevant_history": "What they've tried, how long it lasted, why it stopped",
  "emotional_baseline": "Current emotional state",
  "skepticism_level": 3,
  "price_sensitivity": 2,
  "referrer": "instagram_ad",
  "in_their_voice": "One sentence about why previous approaches didn't work"
}
```

**Field notes:**
- `skepticism_level`: 1 (trusting) to 5 (deeply skeptical)
- `price_sensitivity`: 1 (price insensitive) to 5 (very price conscious)
- `referrer`: How they found the page (instagram_ad, facebook_ad, google_search, word_of_mouth, direct, tiktok_ad, etc.)
- Names should be generated using Faker (Python or Ruby), not LLM-invented. AI-generated names are obvious and repetitive.
