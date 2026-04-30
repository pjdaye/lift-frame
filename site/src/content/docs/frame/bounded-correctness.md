---
title: Bounded Correctness
---

A useful unifying frame is **bounded correctness**:

> A system is correct if it produces an outcome that lies within an allowed set under stated constraints and can provide evidence that the constraints were met.

## Correctness patterns by system type

### Safety invariants (“never” properties)

- No data leakage
- No prohibited actions
- No policy overrides

### Quality envelopes (ranges/tolerances)

- Latency SLOs
- Relevance thresholds
- Coverage levels

### Liveness objectives (“eventually” properties)

- Eventual convergence
- Eventual retry success
- Recovery to a safe state

### Evidence obligations

- Citations
- Provenance and traceability
- Audit trails and reproducibility hooks
