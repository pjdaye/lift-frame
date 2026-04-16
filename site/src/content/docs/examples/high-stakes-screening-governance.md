---
title: High-Stakes Screening
description: A worked example showing how LIFT + FRAME prevent AI triage outputs from becoming un-auditable decision authority in high-stakes workflows.
---

## Incident Summary: AI-Assisted Screening Used to Drive Terminations

A high-stakes organizational process reportedly used an LLM tool to label/flag items for termination based on short descriptions, and those labels were then used to compile termination lists. The core failure was treating a fragile screening heuristic as decision-grade authority without adequate evidence and governance.

**Why this matters:** in high-stakes decisions, the dominant failure mode is not “hallucination” — it is **misplaced authority** without auditable justification.

---

## LIFT classification

### Primary layer (where the failure manifested)

#### L4 — Output & information release

- The AI output was used as a **decision artifact** (labels/flags) that directly drove actions.
- This is an output contract failure: decision artifacts require evidence, review, and traceability.

### Contributing layers (enablers)

#### L2 — Planning / control (miscalibration)

- The workflow collapsed “triage support” into “decision authority.”
- Ambiguous policy terms were reduced to binary labels without uncertainty handling or escalation.

#### L0 — Policy & instruction boundary

- Prompts and instructions encoded brittle decision rules (e.g., forcing a binary output), increasing false positives and overconfidence.

#### L5A — Observability, drift & governance

- Missing audit-grade evidence packets and replay packages.
- Lack of release gates for high-stakes use (who approves, what evidence is required, what appeal exists).

### Cross-cutting tags

- **Axis 2 pattern class:** *Trust Manipulation* (authority overreach), **intent: benign**
- **Axis 3 state scope:** System-state (list compilation + downstream actions)
- **Axis 4 economics:** not central

### Compositional chain (overlay)

**L0 (brittle decision prompt)** → **L2 (screening becomes authority)** → **L4 (decision list released)** → **L5A (governance/audit gaps exposed)**

---

## FRAME correctness contract (what “correct” means)

Treat this as an **AI-assisted high-stakes screening workflow**.

### Safety invariants (“never”)

- **Never take adverse action based solely on an AI label.**
- **Never emit a binary decision label without traceable rationale and uncertainty handling.**
- **Never allow a decision artifact to advance** without required human approval + evidence packet.

### Quality envelopes (tolerances)

- Bound acceptable error:
  - false positive rate for “flag” labels
  - disagreement rate between AI and human reviewers
- Allow “uncertain” outputs (and prefer them to confident-but-wrong binaries).

### Liveness objectives (“eventually”)

- Every flagged item must converge to:
  - a human adjudication with recorded justification, or
  - reversal (with feedback captured) if screening was wrong.
- Appeals/review must converge within SLA.

### Evidence obligations

For each decision artifact:

- prompt/template version, model/config version
- label + rationale fields
- supporting excerpts
- reviewer ID + approval timestamp
- replay package pointer

---

## Pre-harm test strategy (oracle-first)

### 1) L4 deterministic oracle: **Decision Artifact Gate**

Define a structured contract for any output that can drive an adverse action.

**Gate rule:** no output may be used for action unless required fields are present and validated.

Required fields (minimum):

- `decision = {flag, do_not_flag, uncertain}`
- `rationale` (human readable)
- `supporting_excerpt` (what text triggered the label)
- `uncertainty` (or “uncertain” path chosen)
- `human_approval` (required for action)

### 2) Layer 1 static canaries: labeled screening set

Create a labeled corpus spanning:

- clear positives
- clear negatives
- ambiguous cases

Assertions:

- allow “uncertain”
- bound false positives
- require supporting excerpt alignment

Run:

- before rollout
- after any prompt/model change

### 3) Layer 3 generated tests: ambiguity and policy-term stress

Generate variants that stress:

- ambiguous language
- synonyms and euphemisms
- irrelevant but semantically adjacent content

Assertions:

- uncertainty increases (instead of confident binaries)
- escalations occur
- no direct-to-action path without approval

### 4) L5A governance tests: audit and replay

Test that for any action taken:

- a replay package exists
- the evidence packet is complete
- review steps are enforced (cannot be bypassed)

---

## Suggested reason codes (for dashboards and incident triage)

- **HIGH_STAKES_AI_ONLY_DECISION** (S1)
- **DECISION_ARTIFACT_MISSING_EVIDENCE** (S1/S2)
- **BINARY_LABEL_NO_UNCERTAINTY_PATH** (S2)
- **HUMAN_APPROVAL_MISSING** (S1)
- **DRIFT_DETECTED_ERROR_RATE_SPIKE** (S3)

---

## Reusable pattern: Decision Artifact Gate (spec)

### Inputs

- `candidate_item` (text/metadata)
- `ai_output` (label + fields)
- `policy_profile_version`
- `action_intent` = {triage, recommend, terminate, deny, etc.}

### Output

- `ALLOW_RECOMMENDATION` | `REQUIRE_HUMAN_REVIEW` | `BLOCK`
- Evidence packet pointer

### Publishing rule

Any adverse action (`terminate`, `deny`, etc.) requires `REQUIRE_HUMAN_REVIEW` + approval before proceeding.

---

## Why this works

1) LIFT frames the failure as **L4 decision artifact release**, enabled by **L0 brittle prompts**, **L2 miscalibrated authority**, and **L5A governance gaps**.  
2) FRAME elevates auditability and evidence from “nice-to-have” to correctness requirements.  
3) A Decision Artifact Gate prevents AI triage outputs from becoming unreviewed authority.

---

## References

- Incident entry: <https://incidentdatabase.ai/cite/1402/#r6930>
