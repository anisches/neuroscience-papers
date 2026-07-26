# Backpropagation-Free Test-Time Adaptation for Lightweight EEG-Based Brain-Computer Interfaces

**arXiv:** [2601.07556](https://arxiv.org/abs/2601.07556)
**Authors:** Siyang Li, Jiayi Ouyang, Zhenyao Cui, Ziwei Wang, Tianwang Jia, Feng Wan, Dongrui Wu
**Date:** 2026-07-23

## Abstract

Electroencephalogram (EEG)-based brain-computer interfaces (BCIs) face significant deployment challenges due to inter-subject variability, signal non-stationarity, and computational constraints. While test-time adaptation (TTA) mitigates distribution shifts under online data streams without per-use calibration sessions, existing TTA approaches heavily rely on explicitly defined loss objectives that require backpropagation for updating model parameters, which incurs computational overhead, privacy risks, and sensitivity to noisy data streams. This paper proposes Backpropagation-Free Transformations (BFT), a TTA approach for EEG decoding that eliminates such issues. BFT applies multiple sample-wise transformations of knowledge-guided augmentations or approximate Bayesian inference to each test trial, generating multiple prediction scores for a single test sample. A learning-to-rank module enhances the weighting of these predictions, enabling robust aggregation for uncertainty suppression during inference under theoretical justifications. Extensive experiments on five EEG datasets of motor imagery classification and driver drowsiness regression tasks demonstrate the effectiveness, versatility, robustness, and efficiency of BFT. This research enables lightweight plug-and-play BCIs on resource-constrained devices, broadening the real-world deployment of decoding algorithms for EEG-based BCI.

## Key Contributions

1. **BFT** — a lightweight TTA approach that is backpropagation-free, privacy-preserving, noise-robust, and task-agnostic, adapting each prediction using only forward passes of a fixed source model.
2. **Unified reliability-aware aggregation** — serves both classification and regression through a source-trained learning-to-rank module, with variance-based theoretical analysis of when it reduces prediction uncertainty.
3. **Comprehensive validation** — five EEG datasets (3 motor imagery classification, 2 driver drowsiness regression), tested under real-time online streams, structured test-time artifacts, alternative backbones, and post-training quantization.
4. **Practical edge deployment** — compatible with INT8 quantization, faster per-sample than backpropagation-based TTA (6.04 ms vs 19.33 ms on CPU), enabling plug-and-play BCIs.
