# IsoSci: A Benchmark of Isomorphic Cross-Domain Science Problems for Evaluating Reasoning versus Knowledge Retrieval in LLMs

- **Authors:** Samir Abdaljalil, Erchin Serpedin, Hasan Kurban
- **ArXiv ID:** [2607.01431](https://arxiv.org/abs/2607.01431)
- **Date:** 2026-07-01
- **Category:** Computation and Language / AI Evaluation

## Abstract
We introduce ISOSCI, a benchmark of isomorphic cross-domain science problem pairs that separates reasoning ability from domain knowledge retrieval in LLM evaluation. Each pair shares identical logical structure but requires different domain-specific knowledge, enabling controlled attribution of reasoning-mode gains. Across five model pairs spanning four model families, we find that 91.3% of reasoning-mode gains are knowledge-dependent rather than structure-invariant (63/69 gains; Wilson 95% CI [82.3%, 96.0%]), directly challenging the assumption that chain-of-thought reasoning improves short-horizon procedural scientific problem-solving. Reasoning toggles on highly capable models provide less than 5 percentage points accuracy gain across all domains, and a reasoning-specialized model (o3-mini) that outperforms its standard counterpart on GPQA Diamond (+19.2 percentage points) underperforms on ISOSCI (-24.7 percentage points), showing that benchmark choice determines conclusions about reasoning utility.

## Key Findings
* **Knowledge Dependency:** Over 91% of "reasoning" gains in LLMs are actually dependent on domain knowledge rather than purely structural reasoning.
* **Isomorphic Benchmarking:** By using problems with identical logical structures but different domain content, the authors isolate reasoning from retrieval.
* **Performance Discrepancies:** Models like o3-mini show significant performance drops when knowledge retrieval is decoupled from reasoning structure, suggesting current "reasoning" modes are heavily optimized for specific knowledge-rich benchmarks.
* **CoT Utility:** The study challenges the belief that Chain-of-Thought (CoT) universally improves scientific problem solving, especially for short-horizon procedural tasks.
