# Q-SpiRL: Quantum Spiking Reinforcement Learning for Adaptive Robot Navigation

**arXiv:** [2605.20801](https://arxiv.org/abs/2605.20801)
**DOI:** 10.48550/arXiv.2605.20801
**Authors:** Mohamed Khair Altrabulsi, Nouhaila Innan, Alberto Marchisio, Muhammad Kashif, Muhammad Shafique (NYU Abu Dhabi)
**Published:** 2026-05-20 (v2: 2026-07-23)
**Venue:** IEEE International Conference on Quantum Computing and Engineering (QCE), 2026
**License:** CC BY 4.0

## Abstract

Adaptive robot navigation in dynamic environments requires policies that can reach the target reliably while producing efficient and stable trajectories. This paper presents Q-SpiRL, a quantum spiking reinforcement learning framework for obstacle-aware robot navigation. The framework develops and evaluates five agent families: tabular Q-learning, classical MLP, classical SNN, quantum-enhanced MLP (QMLP), and quantum-enhanced spiking neural network (QSNN). While all models are implemented under a unified training and evaluation pipeline, the QSNN is the central architecture of interest, as it combines spike-based temporal processing with variational quantum feature transformation. Experiments are conducted across three grid-world environments of increasing size, namely 20x20, 30x30, and 40x40, with both static and dynamic obstacles. Performance is assessed using success rate, success-weighted path length, path length, and turn rate under deterministic inference. Results show that QSNN achieves the strongest overall trade-off between task completion, trajectory efficiency, and motion smoothness, reaching up to 99% success rate while maintaining high path efficiency in the most challenging setting. Execution on IBM quantum hardware further demonstrates the feasibility of deploying the proposed hybrid policy under real-device conditions.

## Key Findings

1. **QSNN achieves best overall trade-off**: Across all three environment scales, the quantum-enhanced spiking architecture (QSNN) yields the strongest combination of success rate, path efficiency, and motion smoothness, reaching up to 99% success rate in the 40x40 setting.

2. **Spiking > dense at scale**: Classical SNN consistently outperforms classical MLP, with the gap widening as environment complexity increases (MLP drops to 77% success in 40x40 vs SNN's 98%).

3. **Quantum layer provides consistent gains over classical SNN**: QSNN improves upon SNN across every metric at every environment scale — not just success rate but also path length and turn rate — with no apparent trade-off.

4. **Quantum enhancement more effective with spiking than dense**: QSNN shows uniform gains over SNN; QMLP improves over MLP less uniformly, sometimes at the cost of task completion (e.g., 89% vs 94% success rate in 20x20).

5. **Feasibility on real quantum hardware**: A single QSNN episode executed on IBM ibm_fez (IBM Quantum) reached the target successfully, albeit with reduced efficiency (SPL 0.819 vs 0.893 simulated; turn rate 0.692 vs 0.228 simulated) consistent with shot noise and device error.

## Architecture

The QSNN integrates three processing stages:
- **Pre-quantum spiking encoding**: One-hot state → Poisson spike train → LIF layers (spike-based temporal processing)
- **Firing-rate aggregation**: Temporal mean pooling across simulation timesteps → continuous firing-rate vector ∈ [0,1]⁸
- **Variational quantum circuit**: 8-qubit, 3-layer parameterized circuit (Hadamard + trainable controlled rotations + entangling operations) → Pauli-Z expectation values → post-quantum dense layers → 5 Q-values

All neural policies are converted to explicit Q-tables (2560 states × 5 actions) for deterministic evaluation, enabling apples-to-apples comparison.

## Limitations

- Single hardware execution (N=1 episode on ibm_fez); not statistically matched to simulation
- Discrete grid-world environments; real-world continuous navigation not tested
- Q-table conversion limits deployment to discrete state spaces
- Quantum circuit size (8 qubits, 3 layers) may limit expressivity at larger scales
- No ablation study isolating which component of the quantum circuit contributes most

## Relevant Tags

`computation` `quantum-machine-learning` `reinforcement-learning` `spiking-neural-networks` `robot-navigation` `hybrid-quantum-classical` `neural-networks`
