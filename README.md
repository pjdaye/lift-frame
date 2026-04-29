# LIFT + FRAME

LIFT + FRAME is a taxonomy and documentation project for AI-enabled systems.

- **LIFT**: a lifecycle-anchored fault and threat taxonomy.
- **FRAME**: the correctness lens behind the taxonomy, centered on bounded correctness (invariants, envelopes, liveness, and evidence).

## Repository purpose

This repository is the canonical source for:

- The taxonomy data model and content in YAML.
- Human-readable documentation and examples.
- Schema validation and CI checks.
- Versioned releases and changelog history.

## Repository layout

- `taxonomy/lift.yaml`: canonical LIFT taxonomy.
- `taxonomy/schemas/lift.schema.json`: JSON Schema for taxonomy validation.
- `tools/validate_taxonomy.py`: local and CI taxonomy validator.
- `tools/requirements.txt`: Python dependencies for validation tooling.
- `site/`: Astro + Starlight documentation site.
- `site/src/content/docs/`: docs content (FRAME, LIFT, examples, references).

## Prerequisites

- Python 3.12 (matches CI) or a compatible Python 3.x runtime.
- Node.js (for the docs site in `site/`).

## Quick start

### 1) Validate the taxonomy

From the repository root:

```bash
python -m venv .venv
# Windows (PowerShell): .venv\Scripts\Activate.ps1
# Linux/macOS: source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r tools/requirements.txt
python tools/validate_taxonomy.py
```

Expected output:

- `LIFT taxonomy validation passed.`

### 2) Run docs locally

```bash
cd site
npm install
npm run dev
```

Local URL: <http://localhost:4321/lift-frame/> (base path configured in `site/astro.config.mjs`).

## Build docs for production

```bash
cd site
npm run build
npm run preview
```

## CI and deployment

- **Validation CI** (`.github/workflows/ci.yml`): runs on push to `main` and on pull requests; installs `tools/requirements.txt` and executes `python tools/validate_taxonomy.py`.
- **GitHub Pages deploy** (`.github/workflows/deploy.yml`): builds `site/` with Astro and deploys to Pages on push to `main` or manual dispatch.

To enable Pages deployment in a fork/repo:

1. Go to GitHub Settings -> Pages.
2. Set Source to GitHub Actions.

## Versioning

- Taxonomy version is stored in `taxonomy/lift.yaml`.
- Repository release history is tracked in `CHANGELOG.md`.
- Semantic versioning is used for releases.

## Licensing

Dual licensing is used:

- Documentation and taxonomy content are licensed under CC BY 4.0. See `site/src/content/docs/LICENSE`.
- Code (scripts, workflows, tooling) is licensed under Apache-2.0. See `LICENSE`.
