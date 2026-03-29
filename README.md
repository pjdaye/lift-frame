# LIFT + FRAME

**LIFT** is a lifecycle-anchored fault & threat taxonomy for AI-enabled systems.  
**FRAME** is the correctness lens that motivates the approach: **bounded correctness** (invariants, envelopes, liveness, evidence).

This repository is designed to:
- Host the **canonical taxonomy** in a diffable format (`taxonomy/lift.yaml`)
- Publish a **readable documentation site** via GitHub Pages (`docs/`) using MkDocs Material
- Support **semantic versioning** and release snapshots

## Licensing (dual)
- **Documentation & taxonomy content** (Markdown in `docs/`, diagrams, and taxonomy text) are licensed under **CC BY 4.0** — see `docs/LICENSE`.
- **Code** (scripts, workflows) is licensed under **Apache-2.0** — see `LICENSE`.

## Quick start (local)
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Open: http://127.0.0.1:8000/

## GitHub Pages
This repo ships with a GitHub Actions workflow to build and deploy the MkDocs site to GitHub Pages.

1) In GitHub: **Settings → Pages**  
2) Set **Source** to **GitHub Actions**  
3) Push to `main` (or run the workflow manually)

> Tip: If you want to “hide until release,” keep the repo private while drafting and flip it public at launch.

## Semantic versioning
- Development: `v0.x.y`
- Public releases: `v1.0.0`, `v1.1.0`, etc.
See `CHANGELOG.md`.

## Repo URL placeholders
Update `mkdocs.yml` `repo_url` and `repo_name` with your GitHub username.
