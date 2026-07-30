# Active dendrites enable robust spiking computations despite timing jitter

**DOI:** [10.7554/eLife.89629](https://doi.org/10.7554/eLife.89629) · **Authors:** Thomas SJ Burger, Michael E Rule, Timothy O'Leary · **Date:** 2026-07-27 (eLife)

**Tags:** `dendrites` `NMDA spikes` `plateau potentials` `spike timing jitter` `LIH model` `leaky-integrate-and-hold` `spiking neural networks` `binary neural networks` `asynchronous integration` `neuromorphic` `computational neuroscience` `dendritic computation`

Dendritic plateau potentials outlive axonal spikes by ~10x, which seems at odds with rapid computation. Burger et al. propose this slow timescale actually *enables* reliable computation by serving as a resettable temporal buffer for asynchronous inputs. They develop a "Leaky-Integrate-and-Hold" (LIH) model that abstracts NMDA spike dynamics (threshold + plateau hold + decay) and show it reproduces detailed biophysical simulations of Layer 5 pyramidal neurons. In a spiking network solving a 3-class association/discrimination task, LIH dendrites maintain 100% classification accuracy even when input jitter exceeds the membrane time constant by 10x, while networks without plateaus degrade to chance performance. This provides a principled resolution to the paradox of slow dendrites enabling fast computation, plus a design principle for neuromorphic SNN hardware.

**Key contribution:** Demonstrates that the extended duration of dendritic plateau potentials is not a computational liability but a feature — a biologically grounded mechanism for tolerance to spike timing jitter that enables sparse, reliable spiking computations without requiring precisely synchronised inputs.

→ Full literature note: [[2026-07-28-091500-burger-active-dendrites-robust-spiking-lit]]
