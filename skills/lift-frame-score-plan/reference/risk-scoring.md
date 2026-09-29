---
title: Risk Scoring
sidebar:
    order: 2.5
---

Score every identified risk as **Severity × Likelihood × Detectability → Tier**.

## Severity

- **S1:** irreversible or legally binding consequence; physical or psychological harm; any harm to a vulnerable population (see [Axis 5](/lift-frame/lift/crosscut-axes/)); rights violation or data exfiltration; destructive action against production state.
- **S2:** recoverable financial or reputational harm; missing or degraded evidence; policy nonconformance without direct harm.
- **S3:** quality degradation within envelope tails; cosmetic; internal-signal-only.

## Likelihood

- **L1:** demonstrated in the wild for this feature class, or reachable in one step by an ordinary user.
- **L2:** plausible with modest effort or common conditions.
- **L3:** requires an improbable multi-condition chain.

## Detectability

- **D1:** no current detection pre- or post-release.
- **D2:** detectable post-hoc via monitoring/reason codes.
- **D3:** detected or blocked pre-release by an existing automated gate.

## Tier assignment

- **T1:** S1 with L1 or L2; or S2 with L1 and D1.
- **T2:** all remaining S1 and S2 combinations.
- **T3:** all S3.

## Tier → evidence requirement

- **T1:** automated gating oracle (release-blocking) + evidence packet + statistical acceptance at ≥95% confidence.
- **T2:** automated or per-release manual test + production reason code + monitoring.
- **T3:** sampled/exploratory testing + monitoring only.

**Vulnerable-population floor:** any risk affecting a vulnerable population floors at S1 regardless of aggregate likelihood — see [Axis 5](/lift-frame/lift/crosscut-axes/). A passing aggregate result cannot offset a failure in the vulnerable-population slice.
