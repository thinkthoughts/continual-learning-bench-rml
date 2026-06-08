# Continual-Learning-Bench-RML

Residue Manifold Learning (RML) extensions for CL-BENCH: interpretable
analyses of gain, stability, plasticity, drift adaptation, and failure
modes in continual learning.

**Paper:** `paper/continual_learning_in_context.md`\
**Notebooks:** `rml/notebooks/`

------------------------------------------------------------------------

## Abstract

CL-BENCH demonstrates that continual learning depends on shared latent
structure rather than long-term memory alone.

The RML extension complements CL-BENCH through a sequence of
reproducible analyses that investigate how agents:

-   accumulate gain through sequential experience,
-   preserve useful structure,
-   adapt under changing conditions,
-   detect stale context,
-   revise beliefs under drift, and
-   fail when revision mechanisms break down.

The goal is not to replace CL-BENCH metrics, but to provide
interpretable perspectives on continual-learning trajectories.

------------------------------------------------------------------------

## RML Notebook Arc

``` text
0 → Context

{1, 7, 11, 13, 17, 19, 23, 29}

gain
→ latent structure
→ state
→ stability
→ plasticity
→ stale context
→ drift adaptation
→ failure modes
```

------------------------------------------------------------------------

## Quick Start

Clone the repository:

``` bash
git clone https://github.com/thinkthoughts/continual-learning-bench-rml.git
cd continual-learning-bench-rml
```

Install dependencies:

``` bash
pip install -r requirements.txt
```

Launch notebooks locally:

``` bash
jupyter lab
```

Or open directly in Google Colab using the links below.

------------------------------------------------------------------------

## Notebook Overview

  Notebook   Theme              Question
  ---------- ------------------ -----------------------------------
  00         Context            What is CL-BENCH?
  01         Gain               When does experience help?
  07         Latent Structure   What transfers?
  11         State              When does context matter?
  13         Stability          What persists?
  17         Plasticity         What adapts?
  19         Stale Context      When does memory become harmful?
  23         Drift Adaptation   Can beliefs revise?
  29         Failure Modes      What happens when revision fails?

------------------------------------------------------------------------

## Colab Links
## Colab Links

| Notebook | Code | Colab |
|---|---|---|
| 00 | [`rml/notebooks/00_context.ipynb`](rml/notebooks/00_context.ipynb) | [Open](https://colab.research.google.com/github/thinkthoughts/continual-learning-bench-rml/blob/main/rml/notebooks/00_context.ipynb) |
| 01 | [`rml/notebooks/01_gain_signal.ipynb`](rml/notebooks/01_gain_signal.ipynb) | [Open](https://colab.research.google.com/github/thinkthoughts/continual-learning-bench-rml/blob/main/rml/notebooks/01_gain_signal.ipynb) |
| 07 | [`rml/notebooks/07_latent_structure.ipynb`](rml/notebooks/07_latent_structure.ipynb) | [Open](https://colab.research.google.com/github/thinkthoughts/continual-learning-bench-rml/blob/main/rml/notebooks/07_latent_structure.ipynb) |
| 11 | [`rml/notebooks/11_state_vs_stateless.ipynb`](rml/notebooks/11_state_vs_stateless.ipynb) | [Open](https://colab.research.google.com/github/thinkthoughts/continual-learning-bench-rml/blob/main/rml/notebooks/11_state_vs_stateless.ipynb) |
| 13 | [`rml/notebooks/13_stability.ipynb`](rml/notebooks/13_stability.ipynb) | [Open](https://colab.research.google.com/github/thinkthoughts/continual-learning-bench-rml/blob/main/rml/notebooks/13_stability.ipynb) |
| 17 | [`rml/notebooks/17_plasticity.ipynb`](rml/notebooks/17_plasticity.ipynb) | [Open](https://colab.research.google.com/github/thinkthoughts/continual-learning-bench-rml/blob/main/rml/notebooks/17_plasticity.ipynb) |
| 19 | [`rml/notebooks/19_stale_context.ipynb`](rml/notebooks/19_stale_context.ipynb) | [Open](https://colab.research.google.com/github/thinkthoughts/continual-learning-bench-rml/blob/main/rml/notebooks/19_stale_context.ipynb) |
| 23 | [`rml/notebooks/23_drift_adaptation.ipynb`](rml/notebooks/23_drift_adaptation.ipynb) | [Open](https://colab.research.google.com/github/thinkthoughts/continual-learning-bench-rml/blob/main/rml/notebooks/23_drift_adaptation.ipynb) |
| 29 | [`rml/notebooks/29_failure_modes.ipynb`](rml/notebooks/29_failure_modes.ipynb) | [Open](https://colab.research.google.com/github/thinkthoughts/continual-learning-bench-rml/blob/main/rml/notebooks/29_failure_modes.ipynb) |

## Repository Structure

``` text
continual-learning-bench-rml/

├── paper/
├── figures/
├── rml/
│   ├── notebooks/
│   ├── results/
│   └── figures/
├── requirements.txt
├── LICENSE
└── README.md
```

------------------------------------------------------------------------

## Reproducibility

Each notebook produces:

-   figures,
-   CSV summaries,
-   JSON artifacts,

stored under:

``` text
rml/results/
rml/figures/
```

All analyses are deterministic given the included benchmark outputs.

------------------------------------------------------------------------

## Paper

The accompanying manuscript is available here:

-   `paper/continual_learning_in_context.md`

The paper follows the same progression as the notebook arc.

------------------------------------------------------------------------

## Citation

``` bibtex
@misc{hawkley2026clbenchrml,
  title={Continual Learning in Context: An RML Extension for CL-BENCH},
  author={Dan Hawkley},
  year={2026},
  url={https://github.com/thinkthoughts/continual-learning-bench-rml}
}
```

------------------------------------------------------------------------

## Perspective

Continual learning is learning in context.

Memory alone is insufficient.

Effective continual-learning systems require:

-   opportunities for gain,
-   shared latent structure,
-   mechanisms for adaptation,
-   protection against stale context,
-   revision processes that remain stable under drift.

*Lab reports identify reproducible structure before analytic
explanation.*
