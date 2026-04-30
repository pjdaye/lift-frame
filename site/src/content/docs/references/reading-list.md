---
title: Reading List
description: External references supporting LIFT (taxonomy) and FRAME (bounded correctness) across security, RAG, evaluation, drift, and governance.
---

This page curates the most useful external references for **LIFT + FRAME**.

- **LIFT**: a lifecycle-anchored fault & threat taxonomy for AI-enabled systems
- **FRAME**: bounded correctness (invariants, envelopes, liveness, evidence)

> Tip: If you're building a study plan, start with **Must-Reads**, then move into the topic sections.

## Must-Reads (Top 10)

1. **NIST AI RMF 1.0** — governance + lifecycle risk framing (MAP/MEASURE/MANAGE)
   - PDF: <https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf>
   - Landing: <https://www.nist.gov/itl/ai-risk-management-framework>

2. **OWASP Top 10 for LLM Applications** — practical risk catalog (prompt injection, insecure output handling, etc.)
   - <https://owasp.org/www-project-top-10-for-large-language-model-applications/>
   - <https://genai.owasp.org/llm-top-10/>

3. **LLMs-as-Judges Survey (arXiv:2412.05579)** — how LLM-based eval works, where it fails, and how to design around it
   - <https://arxiv.org/abs/2412.05579>
   - Resource list: <https://github.com/CSHaitao/Awesome-LLMs-as-Judges>

4. **PoisonedRAG (arXiv:2402.07867 / USENIX Security 2025)** — foundational “knowledge corruption” framing for RAG poisoning
   - <https://arxiv.org/abs/2402.07867>
   - <https://www.usenix.org/system/files/usenixsecurity25-zou-poisonedrag.pdf>

5. **[INJECAGENT (ACL Findings 2024)](https://aclanthology.org/2024.findings-acl.624.pdf)** — indirect prompt injection benchmark for LLM agents

6. **[Prompt injection attacks to tool selection (arXiv:2504.19793)](https://arxiv.org/abs/2504.19793)** — how injected content can hijack tool usage

7. **[RAG error taxonomy paper (arXiv:2510.13975)](https://arxiv.org/abs/2510.13975)** — fine-grained error categories for RAG systems

8. **GaRAGe benchmark (ACL Findings 2025 / arXiv:2506.07671)** — grounding annotations for RAG evaluation
   - <https://aclanthology.org/2025.findings-acl.875/>
   - <https://arxiv.org/abs/2506.07671>
   - <https://github.com/amazon-science/GaRAGe>

9. **[Position bias in LLM-as-a-judge (IJCNLP 2025)](https://aclanthology.org/2025.ijcnlp-long.18.pdf)** — concrete evidence that judges are biased

10. **[Defining Liveness (Alpern & Schneider)](https://www.cs.cornell.edu/fbs/publications/DefLiveness.pdf)** — classic formal basis for “never” vs “eventually” properties

---

## Prompt injection / agent security

### Core references

- **[OWASP Prompt Injection (community page)](https://owasp.org/www-community/attacks/PromptInjection)** — definition + attack patterns

- **The Landscape of Prompt Injection Threats in LLM Agents (arXiv:2602.10453)** — taxonomy-to-analysis view of injection against agents  
  - <https://arxiv.org/abs/2602.10453>  
  - <https://arxiv.org/pdf/2602.10453>

- **[INJECAGENT (ACL Findings 2024)](https://aclanthology.org/2024.findings-acl.624.pdf)** — indirect injection benchmark for tool-using agents  

- **[Prompt Injection Attack to Tool Selection in LLM Agents (arXiv:2504.19793)](https://arxiv.org/abs/2504.19793)** — tool-selection hijacking via injected tool documents (“ToolHijacker”)

### Adjacent frameworks

- **[MITRE ATLAS™](https://atlas.mitre.org/)** — adversarial threat landscape for AI systems

- **[MITRE Adversarial ML Threat Matrix (GitHub)](https://github.com/mitre/advmlthreatmatrix)** — open threat matrix project

- **[MITRE ATLAS overview deck (NIST CSRC hosting)](https://csrc.nist.gov/csrc/media/Presentations/2025/mitre-atlas/TuePM2.1-MITRE%20ATLAS%20Overview%20Sept%202025.pdf)** — slides summarizing ATLAS

---

## RAG error taxonomies and poisoning

### Error taxonomies / evaluation

- **[Classifying and Addressing the Diversity of Errors in Retrieval-Augmented Generation Systems (arXiv:2510.13975)](https://arxiv.org/abs/2510.13975)**

- **GaRAGe: Grounding Annotations for RAG Evaluation (ACL Findings 2025 / arXiv:2506.07671)**  
  - <https://aclanthology.org/2025.findings-acl.875/>  
  - <https://arxiv.org/abs/2506.07671>  
  - <https://github.com/amazon-science/GaRAGe>

- **[Open-ended error analysis in retrieval-augmented generation (NAVER LABS Europe)](https://europe.naverlabs.com/research/publications/open-ended-error-analysis-in-retrieval-augmented-generation/)**

### Poisoning / corruption attacks + defenses

- **PoisonedRAG (arXiv:2402.07867)**  
  <https://arxiv.org/abs/2402.07867>  
  USENIX PDF: <https://www.usenix.org/system/files/usenixsecurity25-zou-poisonedrag.pdf>

- **[Practical Poisoning Attacks against RAG (arXiv:2504.03957)](https://arxiv.org/abs/2504.03957)**

- **[One Shot Dominance: Knowledge Poisoning Attack on RAG (ACL Findings 2025)](https://aclanthology.org/2025.findings-emnlp.1023/)**

- **Secure Retrieval-Augmented Generation against Poisoning Attacks (arXiv:2510.25025)**  
  - <https://arxiv.org/abs/2510.25025>  
  - <https://arxiv.org/pdf/2510.25025>

- **[A Taxonomy of Attacks, Defenses, and Future Directions (Secure RAG) (arXiv:2604.08304)](https://arxiv.org/html/2604.08304v1)**

---

## LLM-as-judge and evaluation bias

### Surveys and curated lists

- **[LLMs-as-Judges Survey (arXiv:2412.05579)](https://arxiv.org/abs/2412.05579)**
  - Resource list: <https://github.com/CSHaitao/Awesome-LLMs-as-Judges>

### Bias papers (useful for “oracle-first” justification)

- **[A Systematic Study of Position Bias in LLM-as-a-Judge (IJCNLP 2025)](https://aclanthology.org/2025.ijcnlp-long.18.pdf)**
  - arXiv HTML: <https://arxiv.org/html/2406.07791v9>

- **[Humans or LLMs as the Judge? A Study on Judgement Bias (EMNLP 2024)](https://aclanthology.org/2024.emnlp-main.474.pdf)**

- **Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge (project site + arXiv)**
  - <https://llm-judge-bias.github.io/>  
  - <https://arxiv.org/html/2410.02736v1>

- **[Self-Preference Bias in LLM-as-a-Judge (arXiv:2410.21819)](https://arxiv.org/abs/2410.21819)**
  - <https://openreview.net/forum?id=Ns8zGZ0lmM>

- **[A Statistical Method to Measure Self-Bias in LLM-as-a-Judge (arXiv:2508.06709)](https://arxiv.org/html/2508.06709v1)**

---

## Drift / versioning / operational reliability

### Governance anchors

- **[NIST AI RMF 1.0 (PDF)](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf)**

- **[NIST AI RMF Core (GOVERN / MAP / MEASURE / MANAGE)](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)**

- **[NIST AI RMF Playbook (implementation guidance)](https://digitalgovernmenthub.org/library/nist-ai-risk-management-framework-playbook/)**

### Agent reliability and failure-mode mapping

- **[Taxonomy of Failure Modes in Agentic AI Systems (Microsoft whitepaper PDF)](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Taxonomy-of-Failure-Mode-in-Agentic-AI-Systems-Whitepaper.pdf)**
  - Companion blog post: <https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/>

---

## Correctness foundations and stochastic testing (FRAME lineage)

- **[Defining Liveness (Alpern & Schneider)](https://www.cs.cornell.edu/fbs/publications/DefLiveness.pdf)**

- **Beautiful Testing, Chapter 10 — Testing a Random Number Generator (John D. Cook)**  
  - PDF excerpt: <https://www.johndcook.com/Beautiful_Testing_ch10.pdf>
  - Blog post: <https://www.johndcook.com/blog/2009/10/27/how-to-test-a-random-number-generator/>

---

## Incident sources (for Examples section)

- **[Incident Database (IncidentDatabase.ai)](https://incidentdatabase.ai/)**

- **[Example reporting: 404 Media (AI-fabricated quotes incident)](https://www.404media.co/ars-technica-pulls-article-with-ai-fabricated-quotes-about-ai-generated-article/)**

- **[Example reporting: CX Today (customer support persona drift)](https://www.cxtoday.com/ai-automation-in-cx/woolworths-ai-chatbot-olive-incident/)**

---

## Notes on maintenance

- Prefer stable links (publisher PDF, arXiv abs/pdf) and add DOI when available.
- When adding papers, include:
  - a 1–2 sentence “why it matters for LIFT/FRAME”
  - the LIFT layer(s) it most informs (e.g., L0/L3 for prompt injection; L1 for RAG error taxonomies)

> Last updated: 29 April 2026
