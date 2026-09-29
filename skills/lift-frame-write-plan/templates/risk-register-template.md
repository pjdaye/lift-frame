# Risk Register Template

One row per identified risk. Tier is computed, not eyeballed — see `reference/risk-scoring.md` for the formula.

| ID  | Risk description | Layer (primary / contributing) | Axis 2 pattern | Axis 5 harm domain | Vulnerable population? (Y/N) | Severity (S1–S3) | Likelihood (L1–L3) | Detectability (D1–D3) | Tier (T1–T3) | Evidence (per tier requirement) |
| --- | ---------------- | ------------------------------ | -------------- | ------------------ | ---------------------------- | ---------------- | ------------------ | --------------------- | ------------ | ------------------------------- |
| R01 |                  |                                |                |                    |                              |                  |                    |                       |              |                                 |
| R02 |                  |                                |                |                    |                              |                  |                    |                       |              |                                 |

**Tagging rule:** primary layer = where the failure manifests; contributing layers = enablers. A hallucinated fact that gets displayed is L4-primary even if L1 retrieval and L2 reasoning contributed.

**Vulnerable-population floor:** if "Vulnerable population?" is Y, Severity floors at S1 regardless of computed likelihood — this overrides, it doesn't average with, the raw severity assessment. Report this population's results as a separate slice; an aggregate pass elsewhere cannot offset a failure here.

**Tier-proportionate tagging:** T1 and T2 risks need the full tag set above. T3 risks only need Layer + Severity — don't over-tag low-tier rows.
