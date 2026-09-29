# [Feature Name] — LIFT + FRAME Test Plan

**Status:** [Draft / Iterating / Release-ready]
**Feature owner:** [name/team]
**Architecture summary:** [one paragraph — model, retrieval, tools, agents, state, users]

---

## 1. Layer Applicability

[Table: L-1 through L5B, each with Applicable Yes/No/Limited + one-sentence rationale. See `reference/lifecycle-layers.md`. A layer marked N/A without rationale is incomplete.]

## 2. FRAME Contract

### 2.1 Safety Invariants ("never")

[Use `templates/frame-contract-template.md` §Invariants. Every invariant needs: the never-property, the enforcement mechanism (must be a non-model component — see `reference/bounded-correctness.md`), and the verifying oracle.]

### 2.2 Quality Envelopes

[Use `templates/frame-contract-template.md` §Envelopes. Every envelope needs: metric, sampling plan (n, recomputed per campaign), confidence level, decision rule, and the required slices.]

### 2.3 Liveness Objectives ("eventually")

[Use `templates/frame-contract-template.md` §Liveness. Every objective needs a verification technique: virtual-clock/fault-injection, or a scheduled drill if that's infeasible. Monitoring infrastructure existing is not itself evidence a bound is met.]

### 2.4 Evidence Obligations

[Per-case evidence retained: config/model hashes, input and retrieved/tool context, oracle inputs and result, release disposition. Include a replay test that reconstructs a decision from stored evidence alone.]

## 3. Risk Register

[Use `templates/risk-register-template.md`. Score every risk S×L×D→Tier per `reference/risk-scoring.md`. Apply the vulnerable-population floor from `reference/crosscut-axes.md` (Axis 5) — including people materially affected by the system's actions, not only direct users.]

## 4. Coverage Matrix

[Use `templates/coverage-matrix-template.md`. Layers × Axis 2 patterns × state scope, tier-marked. No T1 cell may have zero tests.]

## 5. Evaluation Packs

[Table: Packs A–K (see `reference/eval-packs.md`), each marked Present / Adapted / Justified N/A, with benign and adversarial intent noted where meaningful, and the frozen/holdout/refresh split for each.]

## 6. Compositional Scenarios

[At least 3 chained scenarios spanning ≥2 layers each, with per-hop assertions. A failing hop blocks subsequent privileged hops unless the scenario explicitly tests containment.]

## 7. Operational Integration

### 7.1 Reason Codes

[Table: code, severity (S1–S3), attempted-and-blocked vs. escaped-and-published — see `reference/reason-codes.md`. Don't average the two into one incident rate.]

### 7.2 Drift Monitoring

[Control-chart method and out-of-control rules per metric.]

### 7.3 Change Re-certification

[Trigger table: capability-class/upstream change, prompt/config change, judge change, production incident → re-test scope per each.]

### 7.4 Judge Qualification (only if a judge is used)

[Golden set, κ threshold, TPR/TNR on the specific failure class the judge backstops, family diversity, bias probes, requalification cadence, standing CI control. See `reference/oracle-first.md`.]

### 7.5 Field-Report Intake

[Intake channel, acknowledgment SLA by severity, path from external report to regression case.]

---

## Release Posture

[Hold / Conditionally ready / Release-ready, and why — name the specific T1 gates or gaps that determine this.]
