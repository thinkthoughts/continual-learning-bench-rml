# RML Extension

This folder contains **Residue Manifold Learning (RML)** extensions for **CL-BENCH**, exploring how continual learning systems discover, reuse, adapt, and discard context over time.

CL-BENCH demonstrates that continual learning is not equivalent to long-term memory alone. The benchmark introduces realistic tasks containing **shared latent structure** that can only be exploited through sequential experience. Surprisingly, simple in-context learning (ICL) often outperforms dedicated memory systems.

The goal of the RML extension is to provide an **interpretable layer** for these learning trajectories.

Rather than asking only:

> *Did the agent improve?*

we additionally ask:

> *What context was reused?*
> *When did accumulated experience become stale?*
> *Which forms of adaptation contributed to gain?*
> *How do stability and plasticity interact across task variants?*

The extension follows the **lab-report-init** notebook style:

```
0 → Context

{1, 7, 11, 13, 17, 19, 23, 29}
```

where each notebook investigates a distinct aspect of continual learning under shared latent structure.

---

## Notebooks

| Notebook | Description |
|-----------|-------------|
| [00_context.ipynb](notebooks/00_context.ipynb) | Introduces CL-BENCH, reproduces the continual-learning framing, explores reward vs. gain, and generates initial artifacts comparing stateful and stateless systems. |
| 01_gain_signal.ipynb | *(planned)* Investigates gain as a measurable advantage derived from sequential experience. |
| 07_latent_structure.ipynb | *(planned)* Maps the hidden structures agents must discover across tasks. |
| 11_state_vs_stateless.ipynb | *(planned)* Compares performance trajectories between stateful and stateless systems. |
| 13_stability.ipynb | *(planned)* Examines retention across task variants. |
| 17_plasticity.ipynb | *(planned)* Studies adaptation to new information. |
| 19_stale_context.ipynb | *(planned)* Investigates when accumulated experience becomes harmful. |
| 23_drift_adaptation.ipynb | *(planned)* Explores concept drift and belief revision. |
| 29_failure_modes.ipynb | *(planned)* Develops a taxonomy of continual-learning failures. |
---

### Notebook 00 — Context

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](
https://colab.research.google.com/github/thinkthoughts/continual-learning-bench-rml/blob/main/rml/notebooks/00_context.ipynb
)

Introduces the CL-BENCH continual-learning framework and establishes the baseline analyses used throughout the RML extension.

Objectives:

1. Define reward and gain.
2. Compare stateful and stateless trajectories.
3. Generate reproducible artifacts.
4. Establish a common context for subsequent notebooks.

Outputs:

- `results/00_context_gain.csv`
- `figures/00_context_gain.png`
- `results/00_context_artifacts.zip`

---

### 01_gain_signal.ipynb

Investigates gain as a measurable advantage derived from prior experience.

Questions:

* Where does gain emerge?
* Which tasks exhibit the strongest learning effects?

---

### 07_latent_structure.ipynb

Maps the hidden structures agents must discover.

Examples include:

* database schemas,
* codebase organization,
* RF transmitter configurations,
* opponent strategies,
* forecasting dynamics.

---

### 11_state_vs_stateless.ipynb

Compares performance trajectories between stateful and stateless systems.

Questions:

* When does accumulated context help?
* When does it hinder?

---

### 13_stability.ipynb

Explores retention across changing task variants.

Questions:

* Which systems preserve useful structure?
* Which systems forget too aggressively?

---

### 17_plasticity.ipynb

Studies adaptation to new information.

Questions:

* How rapidly do systems incorporate feedback?
* Does rapid adaptation come at the cost of forgetting?

---

### 19_stale_context.ipynb

Examines when prior experience becomes harmful.

Questions:

* Can systems detect outdated assumptions?
* What patterns precede negative gain?

---

### 23_drift_adaptation.ipynb

Investigates concept drift.

Questions:

* Can systems revise beliefs when environments change?
* Which architectures adapt most effectively?

---

### 29_failure_modes.ipynb

Develops a taxonomy of continual-learning failures.

Examples include:

* over-reliance on recent observations,
* stale memory reuse,
* failure to transfer latent structure,
* spurious generalization.

---

## Perspective

The RML extension treats continual learning as **learning in context**.

Memory alone is insufficient.

Learning requires:

* **headroom** for improvement,
* **shared latent structure** across experiences,
* **mechanisms for adaptation** through feedback.

The aim of these notebooks is not to replace CL-BENCH's metrics, but to complement them with analyses that make continual-learning trajectories more interpretable and reproducible.

---

**Continual Learning in Context**

*Lab reports identify reproducible structure before analytic explanation.*
