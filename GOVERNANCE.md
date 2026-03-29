# Governance

This repository maintains two artifacts:

- **LIFT** (the taxonomy): lifecycle layers + cross-cutting axes + compositional scenario overlay
- **FRAME** (the correctness lens): bounded correctness (invariants, envelopes, liveness, evidence)

## Decision making
- Small editorial changes: direct commit to `main`
- Substantive taxonomy changes (new layers/axes, renames, breaking tags):
  - Open an issue describing the change + rationale
  - Submit a PR referencing the issue
  - Update `CHANGELOG.md`
  - If breaking: bump major version

## Releases
- Tag releases using SemVer: `vMAJOR.MINOR.PATCH`
- Each release should update:
  - `CHANGELOG.md`
  - `taxonomy/lift.yaml` version field
  - `docs/releases/` snapshot (optional but recommended)

## Contact
- Maintainer: <YOUR NAME / HANDLE>
