# Methodology

This document captures the intended methodology for FINER-139 experiments.

## Core principles

1. Keep method-specific artifacts isolated in `experiments/<method>/`.
2. Keep all shared logic in `src/`.
3. Record configuration, seed, and model version for each run.
4. Retain evaluation outputs in machine-readable formats (`.json`, `.csv`).

## Experimental flow

1. Prepare splits under `data/splits/`.
2. Run method-specific optimization.
3. Store logs/results in each method folder.
4. Aggregate cross-method comparisons under `experiments/comparison/`.
