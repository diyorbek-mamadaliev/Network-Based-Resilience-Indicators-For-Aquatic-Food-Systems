# Network-based resilience indicators for aquatic food systems

## Overview

This project explores how **aquatic food systems** (with a focus on Red Sea fisheries) respond to environmental and human-induced stress using **network-based modeling**. The goal is to identify **resilience and vulnerability indicators** that can inform sustainability and management decisions.

Aquatic ecosystems are complex, multi-layered systems where biological interactions, environmental conditions, and human activities are tightly coupled. Rather than modeling individual species in isolation, this project represents the system as a **multi-layer network** and studies how its structure changes under perturbations such as climate stress and overfishing.

---

## Research Question

> *How resilient is an aquatic food system to environmental and anthropogenic shocks, and can network-based indicators provide early warning signals of instability?*

---

## Conceptual Framework

The aquatic food system is modeled as a **multi-layer network**:

### 1. Biological layer

* **Nodes:** fish and marine species
* **Edges:** trophic or interaction relationships (e.g., predation, competition)

### 2. Environmental layer

* **Nodes:** environmental variables (e.g., sea surface temperature, salinity)
* **Edges:** influence relationships between environmental variables and species

### 3. Human pressure layer

* **Nodes:** fishing intensity, effort proxies, or catch indicators
* **Edges:** pressure exerted on biological nodes

These layers are coupled to capture cross-scale interactions between ecology, environment, and human activity.

---

## Resilience Indicators

Resilience is defined operationally as the **ability of the network to maintain connectivity and functional integrity under perturbations**.

The following indicators are evaluated:

* **Connectivity**

  * Size of the largest connected component
  * Network density
  * Average shortest path length

* **Redundancy**

  * Alternative paths between nodes
  * Degree distribution and role overlap

* **Vulnerability**

  * Sensitivity to random node removal
  * Sensitivity to targeted node removal (e.g., highly connected species)
  * Collapse thresholds

---

## Shock Simulations

To assess system robustness, the following perturbations are simulated:

* **Climate stress:** gradual increase in temperature variability
* **Overfishing:** targeted removal or pressure on key species
* **Compound shocks:** combined environmental and fishing stress

Changes in resilience indicators are tracked across scenarios.

---

## Data Sources

* FAO fisheries statistics
* NOAA environmental datasets
* Public Red Sea ecological datasets

All datasets are harmonized temporally and spatially prior to modeling.

---

## Methods & Tools

* **Programming:** Python
* **Network analysis:** NetworkX
* **Optional deep learning:** PyTorch Geometric (light use)
* **Data handling:** pandas, numpy
* **Visualization:** matplotlib

---

## Project Relevance

This work demonstrates:

* Systems-level thinking
* Network-based modeling of biological systems
* Sustainability-oriented analysis
* Decision-relevant outputs for fisheries management

The project is aligned with interdisciplinary research at the interface of **bioscience, environmental sustainability, and data science**.

---

## Status

This is an active research-style project developed to support applications to research internships and graduate programs in bioscience, computational sustainability, and population-level modeling.
