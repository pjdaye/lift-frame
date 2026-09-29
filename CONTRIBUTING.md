# Contributing

Thanks for your interest in improving **LIFT + FRAME**.

## How to contribute

1. Open an issue describing the proposed change.
2. Submit a PR that:
   - Updates the relevant docs in `site/src/content/docs/`
   - Updates the taxonomy source in `taxonomy/lift.yaml` if applicable (validate with `tools/validate_taxonomy.py`)
   - Updates the bundled reference material in `skills/*/reference/` (and `skills/lift-frame-write-plan/examples/`) if the taxonomy or Method changed — `tools/check_skill_sync.py` enforces this in CI and will fail the build with the specific file(s) that drifted (see `skills/README.md`)
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

The site is built with [Astro](https://astro.build) and [Starlight](https://starlight.astro.build), under `site/`.

Run the site locally:

```bash
cd site
npm install
npm run dev
```

Build the static site (do this before opening a PR that touches `site/`):

```bash
cd site
npm run build
```

If your change touches `taxonomy/lift.yaml`, validate it against the schema before opening a PR:

```bash
pip install -r tools/requirements.txt
python3 tools/validate_taxonomy.py
```

If your change touches any file listed in `tools/skill_sync_manifest.yaml` (a taxonomy page, the Method, or a worked example), check the skill bundles are still in sync:

```bash
python3 tools/check_skill_sync.py
```
