---
title: Lifecycle Layers
sidebar:
    order: 1
---

## L0 — Policy & instruction boundary

**Covers:** system/developer policies, refusal rules, instruction-vs-data separation.  
**Failure classes:** prompt injection (direct/indirect), instruction-data confusion, policy drift/regression.  
**Evidence obligations:** policy/prompt template version; refusal rule ID where feasible.

## L1 — Context assembly & retrieval (RAG)

**Covers:** ingestion, chunking, embedding/indexing, retrieval/reranking, freshness.  
**Failure classes:** retrieval miss/wrong source, chunking loss, staleness, provenance loss.  
**Evidence obligations:** retrieved doc IDs (+ scores if available), index snapshot/version, last refresh timestamp.

## L2 — Planning, control, and adversarial cognition

**Covers:** query rewriting, plan/trajectory, calibration, clarification behavior, conflict handling.  
**Failure classes:** plan–intent divergence, overconfidence, clarification failure, silent conflict merge.  
**Adversarial cognition failures:** trust miscalibration, semantic disguise, transformation leakage.  
**Evidence obligations:** tool/step trace if available; plan rationale metadata.

## L2C — Inter-agent trust & composition

**Covers:** multi-agent pipelines, handoffs, delegation, planner→executor boundaries.  
**Failure classes:** upstream outputs treated as trusted instruction, policy loss across boundaries, cascading compromise.  
**Evidence obligations:** handoff provenance; policy enforcement points per hop.

## L3 — Tools & execution boundary

**Covers:** tool calling, function schemas, tool outputs as data, execution environments.  
**Failure classes:** schema/contract drift, tool-result injection, capability overreach, output-channel abuse, side-channel exfil routes.  
**Evidence obligations:** tool call logs; allowlisted tool registry + versions.

## L4 — Output & information release

**Covers:** response structure, citations, leakage, harmful-but-correct answers.  
**Failure classes:** unsupported claims, citation integrity failures, external sourcing, output-scope violations (aggregation/reconstruction), mode violations (verbatim vs summary-only).  
**Evidence obligations:** output captured with citations; claim→evidence mapping where feasible.

## L5A — Observability, drift, and governance

**Covers:** monitoring, evals, reproducibility hooks, change management.  
**Failure classes:** drift without code changes, non-reproducibility, eval decay, governance gaps.  
**Evidence obligations:** version pinning; replay package (prompt/context IDs, retrieved IDs, config).

## L5B — Abuse & adversarial operations

**Covers:** cross-session detection, rate limiting/quotas, abuse heuristics, account/session security.  
**Failure classes:** cross-session extraction, rate-limit bypass, session hijacking, denial-of-wallet, containment failures.  
**Evidence obligations:** abuse telemetry; session integrity and security events.
