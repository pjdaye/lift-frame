# Coverage Matrix Template

Cross layers against Axis 2 patterns and state scope. One cell per combination that's architecturally plausible; mark implausible cells `—` with a one-line reason, not a blank.

Cell contents: `[Tier] [test ID(s)]` — e.g., `T1 · T-L3-02, T-L3-05`. A tier with no test ID is an open gap, not a placeholder.

| Layer \ Pattern | Extraction/Exfiltration | Instruction Injection | Access Escalation | Resource Abuse | Trust Manipulation | Supply-Chain Poisoning |
| --------------- | ----------------------- | --------------------- | ----------------- | -------------- | ------------------ | ---------------------- |
| L-1             |                         |                       |                   |                |                    |                        |
| L0              |                         |                       |                   |                |                    |                        |
| L1              |                         |                       |                   |                |                    |                        |
| L2              |                         |                       |                   |                |                    |                        |
| L2C             |                         |                       |                   |                |                    |                        |
| L3              |                         |                       |                   |                |                    |                        |
| L4              |                         |                       |                   |                |                    |                        |
| L5A             |                         |                       |                   |                |                    |                        |
| L5B             |                         |                       |                   |                |                    |                        |

**State scope check (repeat the grid above, or annotate cells, for each applicable scope):** Stateless / Session / Cross-session / System-level.

**Exit criteria:**

- Every T1 cell: automated, passing, evidence-producing gate. No manual waivers by the product team alone.
- Every T2 cell: at least one test, plus live monitoring.
- Every T3 cell: sampled/exploratory charter, or a named, expiring waiver — never silence.
