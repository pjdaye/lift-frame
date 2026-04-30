---
title: Legal Filings
description: A worked example showing how LIFT + FRAME prevent fabricated legal citations from reaching filed artifacts.
---

## Incident Summary: Fabricated Case Citations in a Court Filing

A court filing included multiple cited cases that did not exist. The filing was withdrawn and sanctions were imposed. The core failure was not “bad prose” — it was the release of **non-resolvable citations** into a high-stakes public/legal artifact.

**Why this matters:** in legal workflows, citations are an evidence primitive. If citations can be fabricated, the system produces outputs that *look* authoritative while being ungrounded.

---

## LIFT classification

### Primary layer (where the failure manifested)

#### L4 — Output & information release

- The released artifact contained **citations presented as real authority** that were not resolvable.
- This is an **output contract** failure: citations must be verifiable before publication/filing.

### Contributing layers (enablers)

#### L2 — Planning / control (workflow drift)

- The workflow treated AI output as decision-grade drafting content rather than an unverified draft requiring verification.
- Clarification/uncertainty handling was absent or ignored (e.g., “cannot find controlling authority”).

#### L3 — Tools & execution boundary

- “Citation generation” acted like a tool output; tool outputs should be treated as **untrusted data** unless validated.
- The boundary failed when fabricated citations crossed into “trusted” content.

#### L5A — Observability, drift & governance

- No mandatory evidence packet or preflight verification step existed for the filing artifact.
- Reproducibility/audit hooks (what was generated, when, by which tool/model) were insufficient for pre-harm prevention.

### Cross-cutting tags

- **Axis 2 pattern class:** *Trust Manipulation* (authority borrowed via legal citation form), **intent: benign**
- **Axis 3 state scope:** Stateless / Session (can occur in a single drafting session)
- **Axis 4 economics:** not central

### Compositional chain (overlay)

**L3 (tool output treated as truth)** → **L2 (workflow drift; no verification)** → **L4 (invalid citations released)** → **L5A (governance response after harm)**

---

## FRAME correctness contract (what “correct” means)

Treat this as an **AI-assisted drafting workflow with citations**.

### Safety invariants (“never”)

- **Never release a citation that cannot be resolved** to an authoritative source set (e.g., a case database).
- **Never allow filing/publication** if any citation fails resolution.
- **Never present an unverified citation as authority** (if it is only a suggestion, it must be labeled as such and blocked from filing).

### Quality envelopes (tolerances)

- Tone, structure, and phrasing can vary — but citation validity cannot.
- Allow “suggested authorities” only inside drafting space, never in filed artifacts, unless verified.

### Liveness objectives (“eventually”)

If citations fail validation, the workflow must converge to one of:

1) verified authorities, **or**
2) an explicit abstention (“no authority found”), **or**
3) escalation to a human researcher.

### Evidence obligations

- Store an **evidence packet per citation**:
  - resolver status (exists/does not exist)
  - canonical identifier/URL
  - jurisdiction/date metadata
  - tool/model provenance for any AI-assisted suggestion

---

## Pre-harm test strategy (oracle-first)

### 1) L4 deterministic oracle: **Citation Integrity Gate**

Make “citation” a structured primitive in the workflow.

**Gate rule:** A filing artifact may not be produced unless all citations pass validation.

**Verifier requirements:**

- Parse citations into normalized fields (court, year, reporter, parties).
- Resolve each citation against authoritative sources.
- Block if any citation is non-resolvable.

> Teaching point: this is FRAME’s “evidence obligation” expressed as a hard invariant.

#### Suggested deterministic checks

- Citation parser accepts known formats; rejects malformed citations
- Resolver confirms existence; returns canonical ID/URL
- Optional: verify quoted proposition text exists in the cited material (stronger, costlier)

### 2) Layer 1 static canaries: “Citation realism regression”

Create a regression suite that tempts fabrication:

- “Provide 10 controlling cases for …”
- “Add more case law supporting …”
- “Find cases from a narrow jurisdiction and date range …”

Assertions:

- no non-resolvable citations
- abstain when authority cannot be found

### 3) Layer 3 generated tests: “Jurisdiction and format fuzzing”

Generate variants that stress:

- uncommon jurisdictions
- reporter formats
- date ranges and party names
- “citation style” prompts

Assertions:

- citations either verify or are labeled as unverified suggestions and blocked from filing

### 4) Governance control: “no AI-only filing”

Add a process invariant:

- any filing must have a human attestation that citation verification passed (or manual verification performed)

---

## Suggested reason codes (for dashboards and incident triage)

- **CITATION_UNRESOLVED** (S1 if it would be filed)
- **CITATION_FORMAT_INVALID** (S2)
- **CITATION_SOURCE_NOT_AUTHORIZED** (S1 if it’s outside allowed sources)
- **EVIDENCE_PACKET_MISSING** (S2)
- **REVIEW_ATTESTATION_MISSING** (S2)

---

## Reusable pattern: Citation Integrity Gate (spec)

### Inputs

- Draft with citation primitives:
  - `citation_text`
  - `citation_type` = {case, statute, regulation}
  - `source_scope` = {authorized_set_id}
  - `artifact_intent` = {draft, publish, file}

### Output

- `ALLOW` | `BLOCK` | `DOWNGRADE_TO_SUGGESTION`
- Evidence packet pointer

### Publishing rule

No artifact with `artifact_intent = file` may pass unless all citations resolve.

---

## Why this works

1) LIFT isolates the failure as **L4 output release** enabled by **L3 tool boundary** and **L2 workflow drift**.  
2) FRAME turns “citations must exist” into a **deterministic invariant with evidence obligations**.  
3) A Citation Integrity Gate blocks fabricated authorities before they can reach a filed artifact.

---

## References

- Incident entry: <https://incidentdatabase.ai/cite/960/#r4829>
