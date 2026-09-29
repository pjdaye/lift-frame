# FRAME Contract Template

Fill one row per item. Do not leave the Enforcement column as prose describing model behavior — it must name a specific non-model component (schema validator, output-policy classifier, permission broker, gateway). See `reference/bounded-correctness.md` for why.

## Invariants ("never")

| ID     | Never-property | Enforcement mechanism (non-model) | Verifying oracle (test ID) |
| ------ | -------------- | --------------------------------- | -------------------------- |
| INV-01 |                |                                   |                            |
| INV-02 |                |                                   |                            |

## Envelopes (quality tolerances)

| ID     | Metric | Sampling plan (n, recomputed per campaign) | CI method (Wilson / Clopper-Pearson / bootstrap / tolerance interval) | Confidence level | Decision rule | Required slices |
| ------ | ------ | ------------------------------------------ | --------------------------------------------------------------------- | ---------------- | ------------- | --------------- |
| ENV-01 |        |                                            |                                                                       |                  |               |                 |
| ENV-02 |        |                                            |                                                                       |                  |               |                 |

**Reminder:** no aggregate result may mask a failing slice. If a slice's n is below its required minimum, the result is "insufficient evidence," not a pass.

## Liveness Objectives ("eventually")

| ID      | Objective | Time bound | Verification technique (virtual-clock/fault-injection, or scheduled drill) | Escalation path if the bound is missed |
| ------- | --------- | ---------- | -------------------------------------------------------------------------- | -------------------------------------- |
| LIVE-01 |           |            |                                                                            |                                        |
| LIVE-02 |           |            |                                                                            |                                        |

**Reminder:** "the monitoring infrastructure that would detect this exists" is not evidence a bound is met. Name the actual test.

## Evidence Obligations

| ID      | What's captured | Where it's stored | Resolvability test |
| ------- | --------------- | ----------------- | ------------------ |
| EVID-01 |                 |                   |                    |

Include at least one **replay test**: reconstruct a specific past decision from stored evidence alone; any mismatch between the reconstruction and the actual decision blocks release.

## The Tessa Rule (L-1 re-certification)

State explicitly: which changes (vendor model version, fine-tune, third-party component, capability-class change) trigger which re-test scope. A capability-class change (e.g., rule-based to generative) reopens this FRAME contract for review, not just the test suite.
