# LIFT + FRAME

**LIFT** is a lifecycle-anchored fault and threat taxonomy for AI-enabled systems.
**FRAME** is the correctness lens that motivates it: **bounded correctness** (invariants, envelopes, liveness, and evidence).

This repository is designed to:

- Host the canonical taxonomy in a diffable format (`taxonomy/lift.yaml`)
- Publish a readable documentation site with Astro + Starlight (`site/src/content/docs/`)
- Support semantic versioning and release snapshots

## Repository layout

- `taxonomy/`: canonical taxonomy (`lift.yaml`) and JSON Schema (`schemas/lift.schema.json`)
- `tools/`: taxonomy validation script and Python requirements
- `site/`: Astro + Starlight documentation site (published to GitHub Pages)

## Licensing (dual)

- Documentation and taxonomy content (Markdown in `site/src/content/docs/`, diagrams, and taxonomy text) are licensed under **CC BY 4.0**. See `site/src/content/docs/LICENSE`.
- Code (scripts, workflows) is licensed under **Apache-2.0**. See `LICENSE`.

## Quick start

### 1) Validate taxonomy

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
pip install -r tools/requirements.txt
python tools/validate_taxonomy.py
```

### 2) Run docs site locally

```bash
cd site
npm install
npm run dev
```

Open: <http://localhost:4321/>

## GitHub Pages deployment

The repository deploys the Starlight site to GitHub Pages using GitHub Actions.

1) In GitHub, go to **Settings -> Pages**
2) Set **Source** to **GitHub Actions**
3) Push to `main` (or run the deploy workflow manually)

The deploy workflow builds the site from `site/`.

## CI validation

CI installs dependencies from `tools/requirements.txt` and runs:

```bash
python tools/validate_taxonomy.py
```

## Semantic versioning

- Development: `v0.x.y`
- Public releases: `v1.0.0`, `v1.1.0`, etc.

See `CHANGELOG.md`.
