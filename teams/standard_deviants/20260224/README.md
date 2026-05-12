# Synthetic User Testing

Test landing page copy against AI-generated personas before spending money on real traffic. Each team member runs their own test with their own point of view / assumptions. We then compare across tests to find audience segments we might not have in mind ourselves.

## How It Works

You use an LLM to orchestrate the full lifecycle. The process:
1. **Brief** — what you're testing, who sees it, persona buckets, evaluation criteria
2. **Audience** — 60 AI personas across your chosen segments (12 per bucket x 5 buckets)
3. **Copy** — write or provide your landing page copy
4. **Evaluation** — 60 isolated LLM calls, one per persona, scoring your copy
5. **Analysis** — stats, charts, qualitative themes, recommendations
6. **Iteration** — revise copy based on feedback, re-run, repeat

Each round takes ~10 minutes for the evaluation calls plus analysis time.

### If using Claude Code

There's a bundled skill (`synthetic-user-testing`) that automates the entire workflow. Tell Claude: "Let's do synthetic user testing" or "/synthetic-user-testing" and it will walk you through each phase. Works best with Opus as the orchestrator model.

### If using another LLM

You can run this manually with any capable LLM. The key files are:
- `references/prompt-templates.md` — the exact prompts to send (copy them verbatim)
- `references/evaluation-schemas.md` — the JSON schemas personas respond with
- `references/best-practices.md` — analytical guidance

The workflow: generate personas, send each persona + your copy + the evaluation prompt as a separate LLM call, collect the JSON responses into a single `results_vN.json`, then run `scripts/synthetic_eval.py` for stats and charts. See the **Manual Workflow** section below for details.

## Setup

### Prerequisites
- **An LLM** — any model capable of sustained roleplay and structured JSON output (GPT-4o, Claude, Gemini, etc.). Use a strong model for orchestration/analysis and a mid-tier model for the 60 evaluation calls.
- **Python 3** — stdlib only, no pip installs needed
- A web browser to view the HTML charts and reports

### Shared Resources (do not modify)

| File | Purpose |
|------|---------|
| `product_brief.md` | What the product does, who it's for, interview evidence |
| `brand_position.md` | Brand voice, canonical language, language to avoid |
| `product_direction.md` | Product strategy and wedge thesis |
| `references/prompt-templates.md` | Canonical evaluation prompts — used verbatim |
| `references/evaluation-schemas.md` | JSON response schemas for personas and evaluations |
| `references/best-practices.md` | Analytical patterns and decision guidance |
| `scripts/synthetic_eval.py` | Stats, charts, reports, extraction utilities |

Feed the product brief and brand position to your LLM at the start of your session — they make the personas and evaluations sharper.

## Your Test Directory

Create your directory here using the naming convention:

```
synthetic-user-testing/
  trk2121_synthetic/     <-- example (already done)
  youruni_synthetic/    <-- your directory
```

Your LLM (or you) will populate it with:
```
youruni_synthetic/
  01_brief_*.md          # your test brief
  audience.json          # your 60 personas
  copy_v1.md             # your landing page copy
  results_v1.json        # evaluation results
  summary_v1.md          # human-readable analysis
  charts_v1.html         # visual charts (open in browser)
  copy_v2.md             # revised copy (v2+)
  copy_v2_changes.md     # what changed and why (v2+)
  ...                    # more rounds as you iterate
```

## What to Keep Consistent

- **Prompt templates** — use the canonical prompts from `references/prompt-templates.md` verbatim. Do not paraphrase or "improve" them. If prompts vary between tests, cross-comparison breaks.
- **Evaluation schema** — use the same JSON response fields so results are aggregable across team members.
- **Shared context docs** — feed `product_brief.md` and `brand_position.md` to your LLM so it understands the product.

## What Should Be Different

- **Your audience buckets** — this is the whole point. Who do YOU think the customer is? Design your own 4-6 persona archetypes. The disagreements between team members' audiences are where the insight lives.
- **Your copy** — write your own version or take a different angle on the landing page. Different framings, different emphasis, different structure.
- **Your iteration choices** — follow the feedback where it leads you.

## Manual Workflow (for non-Claude setups)

If you're not using the Claude Code skill, here's how to run the process manually:

### 1. Create your brief
Write `01_brief_yourtest.md` covering: what you're testing, persona bucket definitions (4-6 archetypes with names and descriptions), product description (1-2 sentences for clarity scoring), and evaluation schema choice.

### 2. Generate personas
Create `audience.json` — an array of 60 persona objects. See `references/evaluation-schemas.md` for the persona schema. Each persona needs: `person_id`, `bucket`, `name`, `age`, `gender`, `occupation`, `relevant_history`, `emotional_baseline`, `skepticism_level`, `price_sensitivity`, `in_their_voice` (a quote in their voice). You can have your LLM generate these given your bucket definitions.

### 3. Run evaluation calls
For each of the 60 personas, send a separate LLM call using the evaluation prompt template from `references/prompt-templates.md`. Swap in:
- `{PERSONA}` — the single persona's JSON object
- `{COPY}` — your full landing page copy
- `{SCHEMA}` — the response schema from `references/evaluation-schemas.md`

**Critical: one persona per call.** Do not batch multiple personas into one call. LLMs flatten within-group diversity and lose character fidelity when roleplaying multiple personas simultaneously.

Collect all 60 JSON responses into a single array and save as `results_v1.json`.

### 4. Run clarity scoring
Send a single LLM call (a smaller/cheaper model is fine) using the clarity scoring prompt from `references/prompt-templates.md`. This scores whether each persona correctly understood what the product does. Merge the scores back into `results_v1.json`.

### 5. Generate stats and charts
```bash
# Stats (with comparison to previous round if v2+)
python3 scripts/synthetic_eval.py stats results_v1.json

# Charts
python3 scripts/synthetic_eval.py charts V1 results_v1.json charts_v1.html

# With cross-version history (v2+)
python3 scripts/synthetic_eval.py charts V2 results_v2.json charts_v2.html \
    --history V1:results_v1.json V2:results_v2.json
```

### 6. Analyze and iterate
Review the stats and charts. Write `summary_v1.md` with your analysis. Revise the copy, save as `copy_v2.md`, document changes in `copy_v2_changes.md`, and repeat from step 3.

## Known Issues and Workarounds

These are gotchas discovered during the first test run (trk2121). They apply broadly to any LLM-based evaluation workflow, not just Claude.

### 1. Sub-agents / tool-use agents can't read files

**Problem:** If your LLM setup uses sub-agents (e.g., Claude Code's Task tool, or any agent framework that spawns child processes), those sub-agents often run in isolated sandboxes and cannot read files from `/tmp/`, the project directory, or anywhere else on disk.

**Workaround:** Embed the full prompt content (persona JSON, copy text, schema) directly inline in each sub-agent's instructions. Don't write prompt files and ask agents to read them. If you see the orchestrator writing temporary prompt files, that approach will fail — tell it to inline the content instead.

**What it looks like when it goes wrong:** All agents complete but return errors like "permission denied" or "file not found." Results extraction finds 0 valid responses.

### 2. Clarity response compliance drift with batched personas

**Problem:** When multiple personas are batched into a single LLM call (e.g., 6 personas per call), the model sometimes loses schema compliance for the `clarity_response` field. Instead of writing a product description ("A platform that..."), personas write narrative reactions about the copy ("The copy is clear but..."). This typically gets worse for later personas in the batch.

**Impact:** Clarity scoring marks these as "wrong" even though the persona understood the product fine — they just answered the wrong question. Makes clarity scores unreliable for cross-version comparison.

**Workaround:** Accept noise in clarity scores when batching, or run one persona per call for clean results. The reliable signal is typically in the first few personas of each batch.

### 3. Dealbreaker field normalization

**Problem:** LLMs sometimes return `"dealbreaker": "yes"` or `"dealbreaker": "No dealbreaker"` instead of a clean boolean `true`/`false`. The stats script expects booleans.

**Workaround:** Normalize dealbreakers to booleans during result compilation before running stats. Check your raw JSON for string values if stats throw errors.

### 4. Messy JSON output from evaluation calls

**Problem:** LLMs sometimes return JSON wrapped in markdown code fences, with extra commentary before/after, or with trailing commas and other syntax issues. Some agent frameworks write results to files instead of returning them inline.

**Workaround:** Strip markdown fences, parse leniently, and check for stray result files in your directory. Merge everything by `person_id` into a single clean `results_vN.json`.

### 5. Context window overflow on long sessions

**Problem:** A full synthetic test with 3+ rounds can exhaust the LLM's context window, especially with 60 personas per round. When this happens, the session loses track of state.

**Workaround:** All state lives in the files. Start a new session and point it at your test directory. Say: "Continue synthetic testing in `yourname_synthetic/`. We finished V2 evaluation. Pick up from analysis." The LLM can read the existing files and resume.

## Cross-Comparison (After Everyone Finishes)

Once all team members have completed at least 2-3 rounds each, we'll do a cross-team comparison to map:

1. **Overlapping segments** — audiences everyone identified (likely the core customer)
2. **Unique segments** — audiences only one person thought of (potential blind spots or insights)
3. **Implied segments** — audiences nobody explicitly modeled but that the qualitative feedback keeps hinting at (the real discovery)
4. **Copy themes that win everywhere** — messaging that resonates regardless of audience framing
5. **Copy themes that win nowhere** — messaging we should drop

Then we'll build a unified audience and iterate together.

## Reference: trk2121 Test Summary

The first completed test (`trk2121_synthetic/`) ran 3 rounds (V1-V3) with 60 personas across 5 segments:

| Segment | Description | V3 Conversion |
|---------|-------------|---------------|
| thesis_dreader | PhD/grad students drowning in data they can't analyze | 17% |
| duct_tape_analyst | Professionals duct-taping Excel, R, ChatGPT together | 25% |
| ai_loop_prisoner | People stuck pasting errors into ChatGPT in a loop | 33% |
| budget_gatekeeper | Institutional buyers (compliance, procurement, teams) | 8% |
| skeptical_methodologist | Stats professors and methodological purists | 0% |

Key findings: transparency/auditability is the strongest resonance driver. The "paste cycle" problem description has visceral recognition. Remaining blockers are mostly product-level (missing advanced methods, missing compliance certs), not copy-level. See `trk2121_synthetic/summary_v3.md` for the full analysis.
