# Best Practices

Hard-won patterns from running synthetic user testing at scale. Follow them.

---

## Audience Design

- **Equal bucket sizes.** Unequal groups make per-bucket charts misleading and comparisons harder. Default to equal sizes (12 per bucket with 5 buckets = 60 total) unless there's a strong reason not to.
- **Deterministic skeletons.** LLMs cannot reliably generate audiences that meet exact distribution constraints (bucket size, gender ratio, age band counts). Generate a Python skeleton first using `synthetic_eval.py skeleton`, then have the LLM fill in qualitative profile fields.
- **60 > 50.** 60 personas (12 per bucket) is more reliable than 50. The extra 2 per bucket reduces small-sample noise.
- **Pivot when the data says to.** If a bucket shows 0% conversion across 3+ versions with high dealbreakers, it's a structural mismatch (the product doesn't serve them). Replace it with a reachable segment. Don't optimize for people who won't buy.
- **Match the audience to the campaign.** When testing for ad campaigns, the audience should mirror ad targeting (gender skew, age range, interests). Broad-spectrum audiences are fine for early exploration but waste evaluation capacity later.
- **Audience versioning.** When replacing a dead bucket, create a new audience file (`audience_v4.json`) rather than modifying the existing one. This preserves comparability for returning segments while documenting the evolution.
- **Names via Faker.** Generate names using the Faker library (Python or Ruby), not LLM-invented. AI-generated names tend to be obvious and repetitive. Generate more than needed and cherry-pick the ones that sound like real people.

## Evaluation

- **Baseline is mandatory.** Without a deliberately flat baseline, there's no way to tell if V1 gains are real or just generous AI grading. The baseline calibrates the floor. Use a mediocre or generic version of the copy (e.g., a competitor's landing page, or a flat product description with no persuasive copy).
- **One persona per call, always Sonnet.** Each persona gets its own isolated LLM call. When multiple personas share a single prompt, the model flattens within-group diversity and loses character fidelity (the same reasons real actors don't play two roles in the same scene). Use Sonnet for eval calls (richer qualitative responses than Haiku at reasonable cost). Use `run_in_background: true` and batch parallel calls in groups of 10 for throughput.
- **Separate changelogs.** Keep `copy_vN_changes.md` as separate files from the copy itself. Evaluators should never see the changelog; it contaminates their responses by priming them to look for specific changes.
- **Freeze the prompt within a round.** The evaluation prompt template is canonical. Only `{PERSONA}` changes between calls. If the AI paraphrases or reorders the instructions between calls, a confounding variable has been introduced. See prompt-templates.md.
- **Always keep `clarity_response` in the schema.** If you drop it from the schema, the clarity scoring pass has nothing to score and clarity data is lost for the entire round. Clarity is the only dimension that catches comprehension failures invisible to other metrics (high resonance + wrong understanding = false signal).
- **Anti-sycophancy phrasing matters.** "Lean NEGATIVE to counter AI sycophancy bias" in the prompt header is more effective than longer calibration blocks. Both work, but the short version produces more naturally negative responses.
- **Confirm before launching.** Always ask before kicking off a round. Rounds are expensive and you may still be editing.
- **Check for stray files.** AI agents occasionally write their JSON to a file in the working directory instead of outputting it inline. Always check for stray `evaluation_persons_*.json` files and merge them into the results. Clean up afterward.

## Analysis

- **Lead with findings, not tables.** Reports should lead with what was proved and what to change next, not with distribution tables. Tables belong in the appendix.
- **Framing is the highest-leverage variable.** The single biggest metric swings come from changing the emotional framing of a section, not from structural changes (adding sections, testimonials, pricing). Structural changes produce 3-8pp shifts. Framing changes can produce 20-45pp shifts. Test framing first.
- **Resonance-conversion gap is a real pattern.** High resonance + low conversion often means the copy names the pain perfectly but doesn't build enough trust to act. This is different from low resonance (wrong audience/framing). Watch for segments where resonance is high but conversion is near zero; the barrier is usually trust, not copy quality.
- **Dealbreaker collapse is as valuable as conversion gain.** Reducing dealbreakers from 45% to 13% means moving 32% of the audience from "never" to "maybe." These people are now reachable through follow-up touchpoints (retargeting, email, social proof). This is sometimes more valuable than a small conversion lift.
- **Dealbreaker qualitative cross-reference.** A rising dealbreaker rate isn't always bad. Cross-reference themes: structural dealbreakers (price, format) vs. copy dealbreakers require different responses. Don't panic about the number without reading the reasons.
- **Track specific claims.** When copy makes factual claims, flag them for verification early. Incorrect claims that slip through erode trust with real users.

## Process

- **Use the `report` command.** The HTML report with inline charts, narrative, persona cards, and cross-version trends is dramatically more useful than separate files.
- **Cross-version comparison is essential.** Per-round charts are useful; cross-version trend lines are where the real insights live. Always include full history in the `--history` flag.
- **New audience = caveat, not new baseline.** When the audience changes (bucket swap), per-bucket deltas for returning segments remain valid. Overall deltas are directionally valid but need a caveat in the narrative. A full new baseline is only needed if >50% of the audience changed.
- **Narrative JSON is the analysis layer.** The narrative file is where the researcher's interpretation lives. It separates raw data (results JSON) from meaning (narrative JSON). Always write a narrative; the report without one is just charts with no story.
- **Priority list before cutting.** When trimming copy, make a priority list of what to keep before removing anything. Cutting aggressively without a priority list can destroy conversion. List what's working, rank it, then cut from the bottom.
- **Document changes before running eval.** Write `copy_vN_changes.md` before running the eval, not after. This forces articulation of why each change was made and what signal it's responding to. It also creates the decision log for future reference.
- **Minimum 5 rounds.** Never stop after one round regardless of scores. A lucky V1 needs validation, and meaningful iteration typically requires at least 5 cycles.

---

## Limitations

These are inherent to synthetic testing. Know them, communicate them, and don't overfit to synthetic data.

- **Synthetic users are not real users.** They can identify obvious problems but may miss subtle emotional responses. Use this to get from rough to solid; real user behavior is the final arbiter.
- **AI personas tend toward articulate, rational feedback.** Real users are messier, more emotional, and less able to articulate why something feels off. Synthetic feedback skews toward "marketing reviewer" and away from "gut-level consumer."
- **This tests copy, not design.** Visual design, load speed, layout, and interactive elements are not evaluated. A page that tests well here can still fail if the design undermines the copy.
- **Price sensitivity is directional, not precise.** Synthetic personas have no real wallets. "Too expensive" vs "fair" ratings indicate relative perception, not willingness-to-pay curves.
- **Thin buckets are noisy.** With 60 people and 5 buckets (12 each), per-bucket stats are more reliable than with 50/5 (10 each). But niche sub-segments within a bucket can still be driven by 1-2 outliers. Treat per-bucket stats for groups under 10 as directional, not conclusive.
- **No cross-round persona memory.** Each evaluation is a fresh context. The same persona may respond differently to similar copy across rounds. This is a feature (independent evaluation) but means you can't track individual persona consistency across versions.
