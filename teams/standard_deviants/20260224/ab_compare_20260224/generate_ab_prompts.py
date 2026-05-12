import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
AUDIENCE_PATH = Path('/Users/saanviaima/Documents/GitHub/standard_deviants/synthetic-user-testing/trk2121_synthetic/audience.json')
SCHEMA_PATH = BASE / 'eval_schema_common.json'
COPY_A_PATH = Path('/Users/saanviaima/Documents/GitHub/standard_deviants/synthetic-user-testing/trk2121_synthetic/copy_v3.md')
COPY_B_PATH = Path('/Users/saanviaima/Documents/GitHub/standard_deviants/sa4166/20260224.01_product-v1/copy_v2.md')
OUT_A = BASE / 'A_prompts.jsonl'
OUT_B = BASE / 'B_prompts.jsonl'

PROMPT_TEMPLATE = """You are roleplaying as a real person evaluating a landing page. You must fully embody the persona below and respond ONLY as that person would. Do not break character.

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
"""


def write_prompts(copy_path: Path, out_path: Path):
    audience = json.loads(AUDIENCE_PATH.read_text())
    copy_text = copy_path.read_text().strip()
    schema_text = SCHEMA_PATH.read_text().strip()

    with out_path.open('w') as out:
        for persona in audience:
            prompt = PROMPT_TEMPLATE.format(
                PERSONA=json.dumps(persona, indent=2),
                COPY=copy_text,
                SCHEMA=schema_text,
            )
            out.write(json.dumps({
                'person_id': persona['person_id'],
                'bucket': persona['bucket'],
                'prompt': prompt,
            }) + '\n')
    print(f'Wrote {len(audience)} prompts to {out_path}')


if __name__ == '__main__':
    write_prompts(COPY_A_PATH, OUT_A)
    write_prompts(COPY_B_PATH, OUT_B)
