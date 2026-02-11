# Finer-139 Optimization Study

## Overview

This repository contains a research + production hybrid workflow for optimization experiments on the FINER-139 dataset. The current setup supports the following method families:

- MIPROv2
- ACE + GT (Offline)
- ACE + GT (Online)
- GEPA (Basic Prompt)
- GEPA (Instruction Optimized)

The repository is organized so each method has isolated configs, logs, results, and notebooks while shared logic lives in `src/`.

## Repository Structure

```text
Finer-139/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/
│   ├── processed/
│   └── splits/
├── experiments/
│   ├── miprov2/
│   │   ├── configs/
│   │   ├── logs/
│   │   ├── results/
│   │   └── notebook/
│   ├── ace_offline/
│   │   ├── configs/
│   │   ├── logs/
│   │   ├── results/
│   │   └── notebook/
│   ├── ace_online/
│   │   ├── configs/
│   │   ├── logs/
│   │   ├── results/
│   │   └── notebook/
│   ├── gepa/
│   │   ├── basic_prompt/
│   │   │   ├── configs/
│   │   │   ├── logs/
│   │   │   ├── results/
│   │   │   └── notebook/
│   │   ├── instruction_optimized/
│   │   │   ├── configs/
│   │   │   ├── logs/
│   │   │   ├── results/
│   │   │   └── notebook/
│   │   └── analysis/
│   └── comparison/
│       ├── summary_tables/
│       └── plots/
├── src/
│   ├── data_loader.py
│   ├── evaluation.py
│   ├── utils.py
│   └── metrics.py
└── docs/
    ├── methodology.md
    └── experimental_notes.md
```

## Dataset

- Dataset: FINER-139
- Subset sizes: 100 and 500
- Evaluation style: multi-pass (3 passes)

## Methods

### 1. MIPROv2
Structured prompt/program optimization baseline.

### 2. ACE Offline
ACE optimization with pre-generated trajectories/feedback.

### 3. ACE Online
ACE optimization with online interaction and iterative updates.

### 4. GEPA
- Basic Prompt
- Instruction Optimization

## Results

| Experiment | P1 (100) | P2 (100) | P3 (100) | Avg (100) | P1 (500) | P2 (500) |
|---|---:|---:|---:|---:|---:|---:|
| MIPROv2 | 84 | 95 | 92 | 90.33 | 59 | 37 |
| ACE + GT + Offline | 75 | 100 | 90 | 88.33 | 83 | 67 |
| ACE + GT + Online | 87 | 95 | 85 | 89.00 | 42 | 54 |
| ACE + no GT + Offline | 1 | 1 | 1 | 1.00 | -- | -- |
| ACE + no GT + Online | 1 | 1 | 1 | 1.00 | -- | -- |
| GEPA | 38 | 35 | 1 | 24.67 | -- | -- |

### LaTeX Table

```latex
\begin{table}[h]
\centering
\caption{FINER-139 Experimental Results}
\begin{tabular}{lcccccc}
\hline
\textbf{Experiment} & \textbf{P1 (100)} & \textbf{P2 (100)} & \textbf{P3 (100)} & \textbf{Avg (100)} & \textbf{P1 (500)} & \textbf{P2 (500)} \\
\hline
MIPROv2 & 84 & 95 & 92 & 90.33 & 59 & 37 \\
ACE + GT + Offline & 75 & 100 & 90 & 88.33 & 83 & 67 \\
ACE + GT + Online & 87 & 95 & 85 & 89.00 & 42 & 54 \\
ACE + no GT + Offline & 1 & 1 & 1 & 1.00 & -- & -- \\
ACE + no GT + Online & 1 & 1 & 1 & 1.00 & -- & -- \\
GEPA & 38 & 35 & 1 & 24.67 & -- & -- \\
\hline
\end{tabular}
\end{table}
```

## Notebook Organization

To keep the repo reviewable, each method should keep notebook assets under its own `notebook/` directory using a consistent naming convention:

- `01_data_loading.ipynb`
- `02_training_pass1.ipynb`
- `03_training_pass2.ipynb`
- `04_evaluation.ipynb`

Alternative for publication handoff:

- Keep one final pipeline notebook (e.g., `miprov2_pipeline.ipynb`)
- Move exploratory drafts to `archive_notebooks/` within each method folder.

## Reproducibility

Fill these fields before final publication:

- Model:
- Temperature:
- Seed:
- Metric:
- Hardware:

## Critical Analysis Checklist (Before Release)

- Explain GEPA pass-3 collapse.
- Explain performance degradation at subset size 500.
- Define metric precisely (e.g., precision/F1/exact match).
- Add std-dev and seed-level statistics for research rigor.

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

