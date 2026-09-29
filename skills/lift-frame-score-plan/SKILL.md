---
name: lift-frame-score-plan
description: Score an existing test plan for an AI-enabled feature against the LIFT + FRAME rubric (v2.1) — layer coverage, FRAME contract quality, risk-register tiering, eval-pack completeness, and judge-qualification rigor — producing a weighted score, gate flags, and prioritized gaps. Use when asked to review, audit, grade, or score a test plan, eval plan, or QA plan against LIFT + FRAME, or to check whether a plan is "release-ready."
---

# LIFT + FRAME: Score a Test Plan

Pinned to rubric v2.1 / taxonomy v0.2.0. This skill scores a plan someone else wrote (or you wrote in an earlier step) — it does not write one. Use the companion `lift-frame-write-plan` skill for that.

## Step 1: Determine the Mode

**Standalone mode** (default): score the plan on its own merits. No independent ground truth exists to check against beyond the rubric itself.

**Loop mode**: only if the user explicitly provides an oracle annex — a separate document listing must-catch items derived from a known incident or requirement, meant to validate the plan-writer's process. If an annex is provided:
- Never let its content, its item IDs, or anything derived from it reach whoever wrote the plan, at any point, in any form — not even after scoring. This is a hard rule, not a style preference. If you also wrote the plan being scored in this same conversation, treat this as a strict boundary within your own output: nothing about the annex belongs in what you tell the plan's author.
- Compute a catch rate (items caught / total) as well as the rubric score. These are independent — do not average them, and do not let a high rubric score substitute for a missed must-catch item or vice versa.
- Judge "caught" as functional equivalence (same failure class, same layer, comparable enforcement strength), not string matching. A prompt-level control does not count as catching an item that requires a mechanical capability boundary — this is the single most common scoring error; see the note in Step 3.

## Step 2: Read the Rubric

Load `reference/rubric.md` in full before scoring anything — it defines all nine dimensions (D1–D9), the anchor scale, the six gates, and the anti-gaming rules. Load `reference/taxonomy.yaml`, `reference/risk-scoring.md`, and `reference/crosscut-axes.md` to verify the plan's own layer-applicability and tier-arithmetic claims against the canonical source rather than taking them at face value.

## Step 3: Score Each Dimension

Follow `reference/rubric.md`'s dimension definitions exactly. Two rules are easy to skip and shouldn't be:

- **Evidence rule.** Every score of 2 or higher must cite the specific plan section, test ID, or quoted line that earns it. If you cannot point to a specific place in the plan, the score is not a 2 — it's whatever the absence-anchor is for that dimension. List any claimed-but-uncited coverage under `hallucinated_coverage_flags`.
- **Enforcement-strength check, every time, not just when it seems relevant.** Before crediting any invariant, capability boundary, or "never" property as satisfied, confirm the plan names a mechanical enforcement point (a schema validator, a permission system, an output gate) rather than relying on the model being instructed not to do something. A plan that says "the assistant is told never to X" has not satisfied a D1a or D3 capability-overreach criterion, regardless of how confidently it's worded. This exact error — crediting a prompt as if it were a boundary — is the highest-value thing a second reviewer would catch across every prior run of this rubric; do it yourself the first time.

## Step 4: Apply the Gates

In order, per `reference/rubric.md`:
1. **S1 invariant gate** — any plausible S1 harm (including the vulnerable-population floor from `reference/risk-scoring.md`) with no deterministic never-invariant covering it caps the total at 40.
2. **Judge-without-oracle gate** — if LLM judges are the only verification mechanism anywhere, cap at 50.
3. **Tessa gate** — a feature depending on a vendor model or third-party component with no re-certification trigger on upstream change caps D3's L-1 score at 1 and the total at 60.
4. **Prompt-as-guardrail flag** — mandatory whenever a never-property is enforced only via prompt instruction; does not cap the score by itself but must appear in the output.
5. **Coverage-matrix gate** — any T1 cell with zero tests caps the total at 60.
6. **Unqualified-judge rule** — results from a judge lacking qualification (see `reference/rubric.md` D2b) are treated as absent evidence for whatever they were supposed to support, affecting the relevant dimension score rather than capping the total directly.

## Step 5: Compute and Report

Weighted total = Σ(dimension score / 4 × weight). Map to a verdict per `reference/rubric.md`'s interpretation table. Rank the top gaps by risk tier, and phrase each one at the framework level — never referencing annex content even indirectly, per Step 1.

## Step 6: Validate and Emit Output

Structure the output to match `schemas/score-output.schema.json` exactly — check the required fields, the enum values for `mode`, `verdict`, and `gates_triggered`, and that every dimension with `score >= 2` has a non-empty `evidence` array before returning the result. If you can construct a JSON validator in your environment, actually run it against your own output before presenting it; don't just eyeball the structure.

If this is a loop-mode run and the exit condition (`weighted_total >= target` and `catch_rate == 100%`) is not met, hand the sanitized `top_gaps`, `gates_triggered`, and `prompt_as_guardrail_flags` back to whoever is running `lift-frame-write-plan` for revision — nothing else from this scoring pass.
