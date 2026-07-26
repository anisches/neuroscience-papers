# Zero-Shot Neural Priors for Generalizable Cross-Subject and Cross-Task EEG Decoding

**arXiv:** [2606.23706](https://arxiv.org/abs/2606.23706)
**DOI:** 10.48550/arXiv.2606.23706
**Authors:** Baimam Boukar Jean Jacques, Brandone Fonya, Nchofon Tagha Ghogomu, Pauline Nyaboe, Kipngeno Koech
**Date:** 2026-07-26 (v2, revised from 2026-06-12)

## Abstract

The development of generalizable electroencephalography (EEG) decoding models is essential for robust brain-computer interfaces (BCI) and objective neural biomarkers in mental health. Conventional approaches have been hindered by poor cross-subject and cross-task generalization, owing to high inter-subject variability and non-stationary neural signals. We address this challenge with a zero-shot cross-subject decoding framework on the large-scale Healthy Brain Network dataset, benchmarking a convolutional neural network baseline, a hybrid LSTM, and a Transformer-based foundation model. To adapt the Transformer for regression while averting catastrophic forgetting, we propose a novel progressive unfreezing strategy. The baseline yielded an nRMSE of 0.9991, whereas our fine-tuned Transformer achieved 0.9799 on unseen subjects. This work advances scalable, calibration-free EEG decoding for computational psychiatry and behavioral prediction.

## Key Findings

1. **The "mean-barrier" in cross-subject EEG**: Standard CNN architectures (EEGNetv4, EEGNeX) fail to generalize across unseen subjects, converging to mean prediction (nRMSE ≈ 1.0) — quantitatively demonstrating that the domain shift between subjects in large-scale EEG is severe enough to render standard convolutions useless.

2. **BENDR breaks the barrier**: The BENDR Transformer-based foundation model, fine-tuned with progressive unfreezing, achieved nRMSE = 0.9799 — the first model in the study to break the "mean-barrier" (nRMSE < 1.0), demonstrating that self-attention mechanisms capture subject-invariant neural representations.

3. **Progressive unfreezing prevents catastrophic forgetting**: A principled three-phase fine-tuning schedule (head-only → contextualizer → full model) with differential learning rates (head:contextualizer:encoder = 100:10:1) preserves pretrained representations while enabling task-specific adaptation.

4. **Zero-shot cross-task transfer**: Models trained on passive visual stimulation (Surround Suppression, SuS) and evaluated on active Contrast Change Detection (CCD) demonstrate task-invariant "neural efficiency" markers.

## Architecture

BENDR consists of three components:
- **ConvEncoderBENDR**: Multiple 1D convolution blocks with batch norm and GELU activations, extracting 512-dimensional latent features from (128+1) channel EEG
- **BENDRContextualizer**: 8-layer Transformer encoder with 8 attention heads for long-range temporal dependencies
- **Regression Head**: Multi-head attention pooling with CLS token + feedforward network (512→256→128→1) with layer norm and dropout (p=0.4)

## Dataset

**Healthy Brain Network (HBN)** — 3,000+ subjects aged 5–21, 128-channel EEG. Subject-disjoint splitting: Releases 1–11 (excluding Release 5) for training, Release 5 for validation, Release 12 for held-out test. Preprocessing: 0.5–50 Hz bandpass filter, downsampled to 100 Hz.

## Limitations

- Restricted to 5–21 age range; not tested on older adults
- Single 128-channel montage; robustness to lower channel counts or clinical hardware not quantified
- Cross-task transfer tested only for passive→active visual paradigms (not memory, language, or motor)

## Relevant Tags

`computation` `eeg` `foundation-models` `bci` `zero-shot` `transformers` `computational-psychiatry`
