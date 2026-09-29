# LIFT + FRAME Skills

Agent-executable packaging of the LIFT + FRAME Method and Rubric, installable the same way as [ai-evals-course/evals-skills](https://github.com/ai-evals-course/evals-skills):

```bash
npx skills add https://github.com/pjdaye/lift-frame
```

## Available skills

| Skill                   | What it does                                                                                                                                                                |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `lift-frame-write-plan` | Writes a complete test plan for an AI-enabled feature: FRAME contract, tiered risk register, coverage matrix, eval packs, compositional scenarios, operational integration. |
| `lift-frame-score-plan` | Scores an existing test plan against Rubric v2.1: nine weighted dimensions, six gates, prioritized gaps.                                                                    |

Use `lift-frame-write-plan` to produce a plan, then `lift-frame-score-plan` to grade it. There is no router skill yet — with two skills this is unnecessary; each `description` field is specific enough for an agent to pick the right one directly. Add a router if a third or fourth skill (see below) makes that ambiguous.

## Not yet built

**`lift-frame-run-loop`** — an orchestration skill that would cycle `write-plan` and `score-plan` automatically until a target score and catch rate are met. Deliberately not built yet: it depends on unresolved design decisions (how a single agent session gets genuine generator/scorer model-family diversity, and whether the human-audit checkpoint becomes a pause-and-wait step or a third auditor role) rather than on any packaging gap. Building it before those are decided would bake in an unstated guess at both.

**`lift-frame-integrate-findings`** — a thin bridge skill that would take output from Hamel Husain and Shreya Shankar's [error-discovery skill](https://github.com/ai-evals-course/evals-skills/blob/main/skills/error-discovery/SKILL.md) (an emergent, product-specific failure-mode taxonomy) and map it onto LIFT layers via the Tagging Recipe, producing risk-register entries `write-plan` can consume. Narrow in scope, not yet written.

## Versioning and sync

Both skills bundle a pinned snapshot of the taxonomy (`reference/taxonomy.yaml`, `v0.2.0`) and the relevant site pages, rather than fetching the live site. This is deliberate — a skill's output should be reproducible against a known taxonomy version — but it means the bundled reference material can drift from `/lift-frame/` on the live site if one is updated without the other.

This is enforced, not just documented: `tools/check_skill_sync.py` compares every bundled file against its canonical source (listed in `tools/skill_sync_manifest.yaml`) by content hash and fails CI on any mismatch — see `.github/workflows/ci.yml`. If you change a taxonomy or Method page, copy it over the matching bundled file(s) before opening a PR, or the build will fail with the specific file(s) that drifted. `reference/rubric.md` is the one bundled file with no canonical counterpart in this repo and is not covered by the check — see the manifest's header comment for why.
