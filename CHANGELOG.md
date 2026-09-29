# Changelog

All notable changes to **LIFT + FRAME** will be documented in this file.

The format is based on *Keep a Changelog* and adheres to *Semantic Versioning*.

## [0.2.0] - Unreleased

### Added

- **L-1 (Model & Data Supply)** lifecycle layer, covering vendor/model identity, fine-tune lineage, third-party component supply, and eval-set contamination — closes a gap where upstream capability changes had no home in the taxonomy.
- **Axis 5 (Harm Domain & Affected Population)**, including a vulnerable-population severity floor and an explicit affected-population definition that extends beyond direct users to anyone materially affected by the system's actions.
- **The Method** (`/method/`): practitioner guidance for writing a LIFT + FRAME test plan, plus four fully worked example test plans, synthesized from an independent validation exercise applying the taxonomy to four architecturally distinct AI features.
- The Method's "Before You Start" branch point, distinguishing prospective test-plan design (Section 1 onward) from an inductive error-discovery pass recommended for features that already have production traffic.
- TPR/TNR reporting requirement for judge qualification (Method §7.4), alongside the existing kappa-based agreement threshold.
- New Reading List section, "Practitioner evals methodology (agent-executed)," citing Hamel Husain and Shreya Shankar's evals-skills work.
- **`/lift/risk-scoring/`**: the Severity × Likelihood × Detectability → Tier formula (PRD E1), previously specified only in internal QCoE documents despite being listed as a publication target — closes that gap.
- **Skills** (`skills/lift-frame-write-plan/`, `skills/lift-frame-score-plan/`): agent-executable packaging of the Method and Rubric v2.1, installable the same way as `ai-evals-course/evals-skills`.
- `tools/check_skill_sync.py` + `tools/skill_sync_manifest.yaml`: CI-gating check that fails the build if a skill's bundled reference file drifts from its canonical source in `taxonomy/` or `site/`.

### Changed

- `taxonomy/schemas/lift.schema.json`: added `harm_domains` as a recognized (optional) field under `axes`.

### Fixed

- `CONTRIBUTING.md` still described the pre-migration MkDocs setup (`mkdocs serve`, root-level `requirements.txt`). Updated to the actual Astro/Starlight commands (`site/`, `npm run dev`, `npm run build`) and the correct taxonomy-validator path (`tools/requirements.txt`).

## [0.1.0] - 2026-03-29

### Added

- Initial repository structure
- MkDocs Material site scaffold
- LIFT taxonomy scaffold (YAML) + docs pages
- CI validation workflow + GitHub Pages deploy workflow
