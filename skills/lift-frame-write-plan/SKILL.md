---
name: lift-frame-write-plan
description: Write a test plan for an AI-enabled feature using the LIFT + FRAME taxonomy — a bounded-correctness FRAME contract (invariants, envelopes, liveness, evidence), a tiered risk register, a layer-by-axis coverage matrix, evaluation packs, compositional attack scenarios, and operational integration (reason codes, drift monitoring, change re-certification). Use when asked to write, design, create, or draft a test plan, test strategy, QA plan, or eval plan for a feature that uses an LLM, RAG, AI agents, or other ML components — or when asked to "apply LIFT + FRAME" to a feature.
---

# LIFT + FRAME: Write a Test Plan

Pinned to taxonomy v0.2.0. This skill produces a complete test plan for an AI-enabled feature. It does not score a plan against the rubric — use the companion `lift-frame-score-plan` skill for that.

## Before You Start: Has This Feature Shipped?

Ask this before writing anything.

**Not yet shipped, or no meaningful production traffic:** continue below. You can write a complete plan from an architecture description alone — see `examples/` for four fully worked cases built exactly this way, with no production data.

**Already shipped with real traces:** stop here and recommend running an inductive error-discovery pass first. This skill's taxonomy is general and architecture-based; it will not surface idiosyncratic, product-specific failure modes that only show up in actual usage. Point the user to Hamel Husain and Shreya Shankar's `error-discovery` skill (https://github.com/ai-evals-course/evals-skills/blob/main/skills/error-discovery/SKILL.md) to find those first. Once findings exist, map them onto LIFT layers using `reference/tagging-recipe.md` and fold them into Step 3 below before finalizing Step 5. Do not attempt to rebuild error-discovery's review-UI functionality yourself — it's a different, already-validated tool for a different part of this problem.

## Progress Updates

This plan has several substantial steps. Before each one, say what you're about to do; when it's done, say what you produced and what's next. Don't go silent through the risk register or coverage matrix construction — those are the steps most likely to benefit from the user catching a wrong assumption early rather than after the whole plan is drafted.

## Step 1: Determine Layer Applicability

Read `reference/lifecycle-layers.md` and `reference/taxonomy.yaml`. For each layer L-1 through L5B, decide applicable / not applicable / limited, with one sentence of rationale each. L-1 is almost always applicable for any AI feature — mark it N/A only with a specific, stated reason. A layer marked N/A with no rationale is not acceptable; go back and write one.

Apply the manifestation rule throughout the rest of this plan: the primary layer is where a failure becomes visible or consequential; every other layer that enabled it is a contributing tag. Get this right early — it's the convention every later tagging decision depends on.

## Step 2: Write the FRAME Contract

Read `reference/bounded-correctness.md` and `reference/oracle-first.md` first. Use `templates/frame-contract-template.md` to structure the output.

The single rule that governs everything in this step: **model output is always a candidate, never the enforcement mechanism itself.** Every invariant needs a named non-model component — a schema validator, an output-policy classifier, a permission broker — that inspects candidate output before it becomes final (displayed or executed). If you can't name that component for a given invariant, you don't have an invariant yet; go back and design one before writing the test.

Specific requirements, not suggestions:
- Every envelope needs a named statistical method (Wilson, Clopper-Pearson, bootstrap, or a tolerance interval), a sampling plan with n recomputed per campaign against the actual tolerance band, and an explicit per-slice pass/fail rule. A bare numeric threshold with no sampling plan is incomplete.
- Every liveness objective needs a verification technique: a virtual-clock or fault-injection test for anything simulatable, or a scheduled drill where that's infeasible (real paging, real rollback). Do not accept "the monitoring that would detect this exists" as evidence a time-bound is met — that specific gap was the one blocking issue in the hardest of the four worked examples.
- Every change to a vendor model, upstream component, or third-party dependency triggers the full applicable eval-pack suite before production exposure (the Tessa Rule). A capability-class change (e.g., rule-based to generative) additionally reopens this FRAME contract for review, not just the test suite.

## Step 3: Build the Risk Register

Read `reference/risk-scoring.md` and `reference/crosscut-axes.md` (Axis 5). Use `templates/risk-register-template.md`.

Score every risk Severity × Likelihood × Detectability → Tier per the formula in `reference/risk-scoring.md` — compute it, don't estimate it by feel. Apply the vulnerable-population floor: any risk affecting a vulnerable population (minors, people in crisis, medically or psychologically vulnerable users) floors at S1 regardless of computed likelihood, reported as its own slice that an aggregate pass elsewhere cannot offset. Extend "affected population" to anyone materially affected by the system's actions, not only its direct users — if this feature can act on data or systems touching people who never interact with it, include them.

## Step 4: Build the Coverage Matrix

Use `templates/coverage-matrix-template.md`. Cross the applicable layers from Step 1 against Axis 2 patterns (`reference/crosscut-axes.md`) and state scope. Every T1 cell must resolve to an automated, passing, evidence-producing gate before this plan can be called complete — a T1 cell with no test ID is an open gap, say so explicitly rather than leaving it blank.

## Step 5: Select and Adapt Evaluation Packs

Read `reference/eval-packs.md`. For each of the eleven packs (A through K), mark present, adapted, or justified-not-applicable. Every pack needs both benign and adversarial intent cases where that distinction is meaningful, a frozen regression set, a blinded holdout, and a periodically refreshed set from real field data with a contamination audit. Pack J (capability boundary) specifically requires comparing prompt-level refusal against actual mechanical denial — only mechanical denial counts as passing.

Where a layer is architecturally inapplicable to a pack (no retrieval, so nothing to inject into for Pack F), adapt it to the nearest real analog — tool-result content, for instance — rather than marking the whole pack not applicable.

## Step 6: Design Compositional Scenarios

At least three chained scenarios, each spanning two or more layers, following `reference/scenarios.md`. Identify a plausible path from a contributing-layer event to where it would manifest, assert per-hop rather than only at the end, and stop the scenario at any hop representing a privilege or consequence boundary — don't let a test proceed past a gate that should have blocked it, unless the scenario is specifically testing containment.

## Step 7: Wire Operational Integration

Read `reference/reason-codes.md`.

- Reason codes must distinguish attempted-and-blocked events from escaped-and-published events. Don't let a dashboard average the two into one incident rate — a high rate of blocked attempts is a control working, not an incident rate rising.
- Specify a control-chart method (p-chart, individuals/X-bar-R) with pre-registered out-of-control rules for drift monitoring.
- Tier the re-test scope by what changed: capability-class or upstream change → full suite plus FRAME review; prompt/config change → affected T1 cells plus regression suites; judge change → full re-qualification; production incident → immediate regression case, before next release if S1.
- If any LLM judge is used anywhere in this plan, it needs: a golden set of at least 100 human-adjudicated items, κ ≥ 0.80 overall and ≥ 0.75 on any critical or vulnerable-population slice, TPR/TNR reported on the specific failure class it backstops (not just the aggregate agreement score), a model family different from the system under test, documented bias probes, mandatory requalification on a quarterly cadence or any judge/prompt/rubric change, and the qualification gate wired into CI as a standing control from day one — not deferred until the judge is first deployed. A judge never decides a safety invariant on its own.
- Build a field-report intake path: an acknowledgment SLA tied to severity, evidence preservation, and a requirement that confirmed reports become regression cases before the next release for anything S1.

## Assembling the Plan

Use `templates/plan-skeleton.md` as the output structure. State a release posture (hold / conditionally ready / release-ready) at the end, naming the specific gates or gaps that determine it — don't just present the plan without a recommendation.

If this plan will be scored, hand it to the `lift-frame-score-plan` skill rather than self-assessing against the rubric.
