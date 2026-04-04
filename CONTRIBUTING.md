# Contributing

Thanks for your interest in improving **LIFT + FRAME**.

## How to contribute

1. Open an issue describing the proposed change.
2. Submit a PR that:
   - Updates the relevant docs in `docs/`
   - Updates the taxonomy source in `taxonomy/` if applicable
   - Updates `CHANGELOG.md` when appropriate

## Style guidelines

- Prefer **clear, testable language**.
- Keep “rules” in **invariants / envelopes / liveness / evidence** form.
- When adding new taxonomy items, include:
  - Scope
  - Failure classes
  - Evidence obligations
  - Example test ideas (optional)

## Development

Run locally:

```bash
pip install -r requirements.txt
mkdocs serve
```
