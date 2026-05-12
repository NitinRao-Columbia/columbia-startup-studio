# Checklist → Artifact Index

Map of every checklist item to where the corresponding artifact lives in this
folder. Maintained for graders so the existing work is easy to locate even
when it's bundled into multi-section PDFs (Growth Strategy, User Testing
Report) rather than separate files.

## Already-due (Weeks 1–6)

| Checklist item | Path |
|---|---|
| `README.md` (team + members + UNIs) | `README.md` |
| `20260206/` — formation, ideas, problem canvas | `20260206/canvases.md`, `20260206/ideas.md`, `20260206/photos/` |
| `20260217/` — interview script, snapshots, raw notes | `20260217/interview_script/`, `20260217/interview_snapshots/`, `20260217/raw_interviews/` (15 interviews — 3× the 5+ minimum) |
| `20260219/` — synthesis (human + AI) | `20260219/AI_Synthesis.pdf`, `20260219/AI_User_Synthesis.md`, `20260219/AI_vs_Human_reflectionQ1-2n.md`, `20260219/AI_vs_Human_reflectionQ3.md` |
| `20260224/` — brand position, landing copy, synthetic testing | `20260224/Brand_Position_Experience_Architects.pdf`, `20260224/brand_position.md`, `20260224/Product_Brief_Experience_Architects.pdf`, `20260224/synthetic_testing/` (full 6-version A/B pipeline) |

## Week 7 (March 5) — MVP doc

| Checklist item | Path |
|---|---|
| `20260305/mvp_doc.md` (5 required sections) | `20260305/mvp_doc.md` — covers core flow, tech stack, team roles, what's faked, demand gen status |
| Product spec (supplemental) | `20260305/Product_spec/Vouch_Product_Spec.pdf` |

## MVP Presentations (March 12)

| Checklist item | Path / URL |
|---|---|
| Working MVP — deployed | Live at **https://vouchnyc.onrender.com** |
| `CLAUDE.md` in product repo | `https://github.com/Acinonyx44/vouch_startup_studio/blob/main/CLAUDE.md` |
| Product repo README | `https://github.com/Acinonyx44/vouch_startup_studio/blob/main/README.md` |
| Demand gen results | `20260224/synthetic_testing/google_ad_campaign/campaign.md`, `20260402/Vouch_Growth_Strategy_Part1.pdf` (§2 Channel Strategy, §3 Funnel & Metrics) |

## Iterate Phase (Weeks 9–12)

| Checklist item | Path |
|---|---|
| Week 9 peer-review check-in (3/24) | `20260324/checkin.md` |
| Weekly update — week of April 14 | `20260414/weekly_update.md` |
| Weekly update — week of April 21 | `20260421/weekly_update.md` |
| Weekly update — week of April 28 (today) | `20260428/weekly_update.md` |
| **Experiments 3 + 4** — channel + growth experiments | `20260402/Vouch_Growth_Strategy_Part1.pdf` §2 (Reddit / Campus / Instagram channel experiments with explicit hypotheses, CTAs, goals, costs) |
| **Analytics setup — AARRR / pirate metrics** | `20260402/Vouch_Growth_Strategy_Part1.pdf` §3 — five-stage funnel (Awareness → Interest → Signup → Activation → Retention), instrumented dual-stack (GA4 ID `G-TGJBM7MPX4` live + Amplitude live). Public user count: `https://vouch-api-5pa4.onrender.com/api/user-count` |
| Pricing test (Week 11) | `20260402/Vouch_Growth_Strategy_Part1.pdf` §3 — KPI targets and pricing-tier risk addressed in §5 |
| **User testing — onboarding optimization (Week 12)** | `20260409/Vouch_User_Testing_Report.pdf` |
| Screenshots / product evidence | `20260402/Vouch_Screenshots_Appendix.pdf` |
| Public user-count API (transparency) | `20260402/user_count_api.md` |

## Feature Freeze (April 23) — coming due

- [x] Final product — **frozen at https://vouchnyc.onrender.com** as of April 21, 2026 (16-city US dataset seeded — 6,779 places across 6 categories)
- [ ] Final measurement data — pull GA4 + Amplitude exports

## Demo Day (May 12) — submitted early

| Checklist item | Path / URL |
|---|---|
| Pitch deck (PDF) | `20260512/Vouch_Pitch_Deck.pdf` — 16 pages, 1920×1080 |
| Leave-behind (PDF) | `20260512/Vouch_Leave_Behind.pdf` — 24 pages, 1920×1080 |
| Pitch deck (PPTX) | `20260512/Vouch_Pitch_Deck.pptx` — 16 slides |
| Leave-behind (PPTX) | `20260512/Vouch_Leave_Behind.pptx` — 24 slides |
| Pitch deck (HTML — browser-native, source of truth) | `20260512/Vouch_Pitch_Deck.html` · live at https://vouchnyc.onrender.com/deck/pitch.html |
| Leave-behind (HTML) | `20260512/Vouch_Leave_Behind.html` · live at https://vouchnyc.onrender.com/deck/leave-behind.html |
| Demo Day live-metrics script | `20260512/metrics_snapshot.py` |
| Public metrics API (composite) | `GET https://vouch-api-5pa4.onrender.com/api/metrics` — returns `{signups, active_users, page_views, ratings}` |
| Public user-count API (legacy single field) | `GET https://vouch-api-5pa4.onrender.com/api/user-count` — see `20260402/user_count_api.md` |

**All three formats are content-identical** — PDF, PPTX, and HTML all reflect the April 28 edits (4-founder team, $200K pre-seed framing, 100/411/58%/4.1 traction, Feb/Mar/Apr cohort labels). HTML is the source of truth; PDF and PPTX are rendered from it at design size (1920×1080) via headless Chromium. Use whichever format the audience prefers — PDF is best for printing or read-along; PPTX for PowerPoint editing; HTML for live browser presenting.

## Product Repo — separate from course repo

Lives at: **https://github.com/Acinonyx44/vouch_startup_studio**

| Checklist item | Status |
|---|---|
| `CLAUDE.md` at repo root | ✓ |
| `README.md` at repo root | ✓ |
| Git branching (feature branches + PRs) | ✓ — see PRs against `main` |
| Deployed and accessible | ✓ — Render Blueprint, https://vouchnyc.onrender.com |
