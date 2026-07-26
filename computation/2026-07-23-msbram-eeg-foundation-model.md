# MSBraM: A Multi-scale Self-supervised Brain Foundation Model for Hierarchical EEG Dynamics Learning

**arXiv:** [2607.21402](https://arxiv.org/abs/2607.21402) · **Authors:** Tao Zhou, Jing Han, Lingyu Shu, Zixing Zhang · **Date:** 2026-07-23

Self-supervised foundation models have recently shown strong potential for EEG-based analysis, but existing approaches struggle to capture the multi-scale temporal structure of EEG signals. MSBraM proposes a two-stage pretraining framework: first, a multi-scale neural tokenizer discretizes raw EEG into semantic codes at different temporal resolutions via vector-quantized reconstruction; second, the model is pretrained to predict masked codes using a curriculum multi-scale masking strategy. Pretrained on 2,400+ hours of EEG data and evaluated across 10 downstream tasks on 12 public datasets, MSBraM achieves superior performance over existing pretrained models.
